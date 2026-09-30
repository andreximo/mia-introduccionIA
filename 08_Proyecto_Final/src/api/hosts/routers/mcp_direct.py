"""
Router de acceso DIRECTO a los servidores MCP, sin pasar por el ciclo ReAct
ni por el LLM. Sirve para depurar/probar tools individuales durante el
desarrollo, o para exponer un servidor MCP puntual como API normal.

Rutas (todas bajo el prefijo /mcp):
  GET  /mcp/servidores                    -> nombres de servidores conectados
  GET  /mcp/{servidor}/tools              -> tools que expone ESE servidor
  POST /mcp/{servidor}/tools/{tool_name}  -> invoca esa tool directamente
"""

from typing import Any

from fastapi import APIRouter, HTTPException, Request

router = APIRouter(prefix="/mcp", tags=["mcp-directo"])


def _obtener_sesion(servidor: str, request: Request):
    state = request.app.state.mcp
    if servidor not in state.mcp_sessions:
        raise HTTPException(
            status_code=404,
            detail=f"Servidor '{servidor}' no conectado. Conectados: {list(state.mcp_sessions)}",
        )
    return state.mcp_sessions[servidor]


@router.get("/servidores")
async def listar_servidores(request: Request) -> list[str]:
    return list(request.app.state.mcp.mcp_sessions.keys())


@router.get("/{servidor}/tools")
async def listar_tools_de_servidor(servidor: str, request: Request) -> list[dict[str, Any]]:
    session = _obtener_sesion(servidor, request)
    listado = await session.list_tools()
    return [{"name": t.name, "description": t.description} for t in listado.tools]


@router.post("/{servidor}/tools/{tool_name}")
async def invocar_tool_directa(
    servidor: str, tool_name: str, argumentos: dict[str, Any], request: Request
) -> dict[str, Any]:
    session = _obtener_sesion(servidor, request)
    resultado = await session.call_tool(tool_name, argumentos)
    return {"resultado": resultado.content[0].text}