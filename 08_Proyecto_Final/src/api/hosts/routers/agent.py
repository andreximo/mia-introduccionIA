"""
Router del agente: ejecuta el ciclo ReAct combinando TODAS las tools de
TODOS los servidores MCP conectados, usando openai/gpt-oss-20b.

Groq expone una API compatible con OpenAI (chat.completions), por lo que el
formato de mensajes y de tool calling es:
  - El system prompt es un mensaje más, con role "system".
  - El modelo pide tools en `message.tool_calls`; los argumentos llegan como
    string JSON (hay que hacer json.loads).
  - Cada observation va en su propio mensaje con role "tool" y el
    `tool_call_id` correspondiente.
  - El ciclo termina cuando el mensaje del modelo ya no trae tool_calls

Rutas (bajo el prefijo /agent):
  POST /agent/query  -> corre el ciclo ReAct completo. Acepta un `historial`
                        opcional (turnos previos de la conversación) y devuelve
                        la respuesta final más la traza de tools usadas (`pasos`).
  GET  /agent/tools  -> catálogo combinado de tools que ve el LLM
"""

import json
import os
from typing import Any, Literal

import groq
from fastapi import APIRouter, HTTPException, Request
from groq import AsyncGroq
from pydantic import BaseModel, Field

from ..state import AppState

router = APIRouter(prefix="/agent", tags=["agente"])

MODEL = "openai/gpt-oss-20b"

# Tope de vueltas del ciclo ReAct. Los modelos abiertos pueden entrar en
# bucles de tool calls repetidas; sin este límite el request no terminaría.
MAX_ITERACIONES = 8

SYSTEM_PROMPT = (
    "Eres un asistente del restaurante comida-MIA que puede usar herramientas externas (vía MCP) para "
    "responder con precisión. Tienes una herramienta para consultar la disponibilidad de las mesas y hacer reservaciones; "
    "y otra para obtener información de de las recetas que forman parte del menú, cuando consultes la información de las recestas no inventes información."
    "Usa una herramienta cuando la necesites; si ya tienes suficiente información, responde directamente con texto. "
    "Responde siempre en el idioma del usuario."
)

# AsyncGroq: no bloquea el event loop de FastAPI mientras espera al LLM.
groq_client = AsyncGroq(api_key=os.environ["GROQ_API_KEY"])


class Mensaje(BaseModel):
    """Un turno previo de la conversación (solo texto)."""
    role: Literal["user", "assistant"]
    content: str


class PasoTool(BaseModel):
    """Traza de una invocación de tool: qué pidió el LLM y qué devolvió MCP."""
    herramienta: str
    argumentos: dict[str, Any]
    resultado: str


class QueryRequest(BaseModel):
    query: str
    historial: list[Mensaje] = Field(default_factory=list)


class QueryResponse(BaseModel):
    respuesta: str
    pasos: list[PasoTool] = Field(default_factory=list)


async def _ejecutar_tool(tool_call, state: AppState) -> tuple[dict[str, Any], str]:
    """
    Despacha un tool_call del LLM a la sesión MCP que sirve esa tool.
    Devuelve (argumentos, texto_de_la_observation).
    """
    nombre = tool_call.function.name

    try:
        argumentos = json.loads(tool_call.function.arguments or "{}")
    except json.JSONDecodeError as e:
        return {}, f"Error: los argumentos no son un JSON válido ({e}). Reintenta la llamada."
    if not isinstance(argumentos, dict):
        return {}, "Error: los argumentos deben ser un objeto JSON."

    session = state.tool_to_session.get(nombre)
    if session is None:
        return argumentos, f"Error: herramienta '{nombre}' no encontrada."

    try:
        # === Aquí ocurre la invocación real cliente MCP -> servidor MCP ===
        resultado = await session.call_tool(nombre, argumentos)
    except Exception as e:
        return argumentos, f"Error al ejecutar la herramienta '{nombre}': {e}"

    texto = "\n".join(
        bloque.text for bloque in resultado.content if getattr(bloque, "text", None)
    )
    return argumentos, texto


async def ejecutar_ciclo_react(
    query_usuario: str,
    state: AppState,
    historial: list[Mensaje] | None = None,
) -> tuple[str, list[PasoTool]]:
    messages: list[dict[str, Any]] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *[m.model_dump() for m in (historial or [])],
        {"role": "user", "content": query_usuario},
    ]
    pasos: list[PasoTool] = []

    for _ in range(MAX_ITERACIONES):
        response = await groq_client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=state.tools_catalog,
            tool_choice="auto",
            temperature=0,  # más determinista = tool calls más fiables
            max_completion_tokens=1024,
        )
        mensaje = response.choices[0].message

        if not mensaje.tool_calls:
            # El modelo ya no pidió herramientas -> respuesta final
            return mensaje.content or "", pasos

        # Se reinyecta el turno del assistant tal como lo emitió el modelo
        messages.append({
            "role": "assistant",
            "content": mensaje.content or "",
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in mensaje.tool_calls
            ],
        })

        # Una observation (mensaje role "tool") por cada tool_call
        for tc in mensaje.tool_calls:
            argumentos, resultado_texto = await _ejecutar_tool(tc, state)
            pasos.append(PasoTool(
                herramienta=tc.function.name,
                argumentos=argumentos,
                resultado=resultado_texto,
            ))
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": resultado_texto,
            })

    return (
        "No pude completar la solicitud: el agente alcanzó el máximo de iteraciones.",
        pasos,
    )


@router.post("/query", response_model=QueryResponse)
async def query_endpoint(body: QueryRequest, request: Request) -> QueryResponse:
    try:
        respuesta, pasos = await ejecutar_ciclo_react(
            body.query, request.app.state.mcp, body.historial
        )
    except groq.APIError as e:
        # Incluye rate limits (429), errores de auth (401) y tool calls mal formadas (400)
        raise HTTPException(status_code=502, detail=f"Error del proveedor LLM (Groq): {e}")
    return QueryResponse(respuesta=respuesta, pasos=pasos)


@router.get("/tools")
async def listar_catalogo(request: Request) -> list[dict[str, Any]]:
    return request.app.state.mcp.tools_catalog