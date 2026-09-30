"""
Apertura de las sesiones MCP configuradas en config.py, y armado del
catálogo combinado de tools (unión de todos los servidores).
"""

from contextlib import AsyncExitStack
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from .config import MCP_SERVERS
from .state import AppState


def mcp_tool_to_openai_schema(tool) -> dict[str, Any]:
    """
    Convierte el esquema de una tool MCP al formato de tool calling compatible
    con OpenAI, que es el que usa Groq: {"type": "function", "function": {...}}.
    (En Anthropic era {"name", "description", "input_schema"}).
    """
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description or "",
            "parameters": tool.input_schema ,
        },
    }


async def conectar_servidores_mcp(state: AppState, exit_stack: AsyncExitStack) -> None:
    """Abre una ClientSession por cada servidor en MCP_SERVERS y llena `state`."""
    for server in MCP_SERVERS:
        params = StdioServerParameters(command=server["command"], args=server["args"])

        read_stream, write_stream = await exit_stack.enter_async_context(
            stdio_client(params)
        )
        session = await exit_stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )
        await session.initialize()

        state.mcp_sessions[server["name"]] = session

        listado = await session.list_tools()
        for tool in listado.tools:
            if tool.name in state.tool_to_session:
                raise RuntimeError(
                    f"Nombre de tool duplicado entre servidores MCP: '{tool.name}'. "
                    "Los nombres deben ser únicos entre todos los servidores conectados."
                )
            state.tool_to_session[tool.name] = session
            state.tools_catalog.append(mcp_tool_to_openai_schema(tool))

    print(f"[MCP] Conectado a {len(state.mcp_sessions)} servidor(es): {list(state.mcp_sessions)}")
    print(f"[MCP] Tools disponibles: {[t['function']['name'] for t in state.tools_catalog]}")