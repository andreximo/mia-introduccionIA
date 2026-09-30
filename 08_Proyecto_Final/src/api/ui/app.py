"""
Interfaz de chat (Streamlit) para interactuar con el agente MCP.

Es un cliente más de la API REST del host: no importa nada de host/ ni habla
con los servidores MCP. Solo llama a:
  POST /agent/query      -> ciclo ReAct completo (respuesta + traza de tools)
  GET  /agent/tools      -> catálogo combinado de tools (para la barra lateral)
  GET  /mcp/servidores   -> servidores MCP conectados

Como las llamadas las hace el servidor de Streamlit (Python), no el navegador,
no hace falta configurar CORS en FastAPI.

Ejecución (desde la raíz del proyecto, con el host ya corriendo):
    streamlit run ui/app.py

URL del host configurable con la variable de entorno AGENT_API_URL
(por defecto http://localhost:8000).
"""

import os
from typing import Any

import httpx
import streamlit as st

API_URL = os.environ.get("AGENT_API_URL", "http://localhost:8050").rstrip("/")

# El ciclo ReAct puede tardar (varias llamadas al LLM + tools): timeout generoso.
TIMEOUT_AGENTE = httpx.Timeout(120.0, connect=5.0)

st.set_page_config(page_title="Agente MCP", page_icon="🤖", layout="wide")


# ---------------------------------------------------------------------------
# Acceso a la API del host
# ---------------------------------------------------------------------------

@st.cache_data(ttl=30, show_spinner=False)
def cargar_info_host(api_url: str) -> dict[str, Any]:
    """Servidores y tools del host. Se cachea 30 s para no consultarlo en cada rerun."""
    with httpx.Client(base_url=api_url, timeout=5.0) as c:
        servidores = c.get("/mcp/servidores")
        servidores.raise_for_status()
        tools = c.get("/agent/tools")
        tools.raise_for_status()
    return {"servidores": servidores.json(), "tools": tools.json()}


def consultar_agente(
    query: str, historial: list[dict[str, str]]
) -> tuple[dict[str, Any] | None, str | None]:
    """Devuelve (respuesta_json, None) si todo salió bien, o (None, mensaje_de_error)."""
    try:
        r = httpx.post(
            f"{API_URL}/agent/query",
            json={"query": query, "historial": historial},
            timeout=TIMEOUT_AGENTE,
        )
        r.raise_for_status()
        return r.json(), None
    except httpx.ConnectError:
        return None, f"No se pudo conectar con el host en {API_URL}. ¿Está corriendo uvicorn?"
    except httpx.TimeoutException:
        return None, "El agente tardó demasiado en responder (timeout)."
    except httpx.HTTPStatusError as e:
        try:
            detalle = e.response.json().get("detail", e.response.text)
        except ValueError:
            detalle = e.response.text
        return None, f"El host respondió {e.response.status_code}: {detalle}"


# ---------------------------------------------------------------------------
# Componentes de UI
# ---------------------------------------------------------------------------

def mostrar_pasos(pasos: list[dict[str, Any]]) -> None:
    """Muestra la traza del ciclo ReAct: qué tools invocó el agente y con qué."""
    if not pasos:
        return
    with st.expander(f"🔧 Herramientas usadas ({len(pasos)})"):
        for i, paso in enumerate(pasos, start=1):
            st.markdown(f"**{i}. `{paso['herramienta']}`**")
            st.json(paso["argumentos"])
            st.code(paso["resultado"], language="json")


def mostrar_mensaje(mensaje: dict[str, Any]) -> None:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])
        mostrar_pasos(mensaje.get("pasos", []))


def barra_lateral() -> None:
    with st.sidebar:
        st.header("Host MCP")
        st.caption(API_URL)

        try:
            info = cargar_info_host(API_URL)
            st.success(f"Conectado · {len(info['servidores'])} servidor(es) MCP")
            st.write(", ".join(f"`{s}`" for s in info["servidores"]))
            with st.expander(f"Tools disponibles ({len(info['tools'])})"):
                for tool in info["tools"]:
                    funcion = tool["function"]
                    st.markdown(f"**`{funcion['name']}`**")
                    st.caption(funcion.get("description", ""))
        except httpx.HTTPError:
            st.error("No se pudo consultar el host. ¿Está corriendo `uvicorn host.main:app`?")

        if st.button("🗑️ Nueva conversación"):
            st.session_state.mensajes = []
            st.rerun()


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

st.title("🤖 Agente Comida-MIA")
st.caption("Ciclo ReAct sobre herramientas expuestas por servidores MCP")

st.session_state.setdefault("mensajes", [])
barra_lateral()

for m in st.session_state.mensajes:
    mostrar_mensaje(m)

if prompt := st.chat_input("Escribe tu consulta..."):
    # El historial son los turnos ANTERIORES (solo texto), sin el mensaje actual.
    historial = [
        {"role": m["role"], "content": m["content"]} for m in st.session_state.mensajes
    ]

    mensaje_usuario = {"role": "user", "content": prompt}
    st.session_state.mensajes.append(mensaje_usuario)
    mostrar_mensaje(mensaje_usuario)

    with st.chat_message("assistant"):
        with st.spinner("El agente está razonando..."):
            data, error = consultar_agente(prompt, historial)

        if error:
            st.error(error)
        else:
            st.markdown(data["respuesta"])
            mostrar_pasos(data["pasos"])
            st.session_state.mensajes.append({
                "role": "assistant",
                "content": data["respuesta"],
                "pasos": data["pasos"],
            })