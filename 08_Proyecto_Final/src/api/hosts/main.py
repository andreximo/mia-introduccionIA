"""
Ensambla la app FastAPI:
  - Al arrancar (lifespan): abre las sesiones MCP de config.py y las guarda
    en app.state.mcp (una instancia de AppState).
  - Monta el router del agente (/agent/*) y el de acceso directo (/mcp/*).

Ejecución (desde la raíz del proyecto, para que las rutas relativas de
config.py encuentren servers/):
    uvicorn host.main:app --reload
"""
from pathlib import Path
from dotenv import load_dotenv

# Debe ir ANTES de importar los routers: agente.py lee GROQ_API_KEY al importarse
load_dotenv(Path(__file__).resolve().parents[3] / ".env")

from contextlib import AsyncExitStack, asynccontextmanager
from fastapi import FastAPI
from .mcp_manager import conectar_servidores_mcp
from .state import AppState
from .routers import agent, mcp_direct


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.mcp = AppState()
    app.state.mcp_exit_stack = AsyncExitStack()

    await conectar_servidores_mcp(app.state.mcp, app.state.mcp_exit_stack)

    yield

    await app.state.mcp_exit_stack.aclose()


app = FastAPI(title="Host MCP multi-servidor con ciclo ReAct", lifespan=lifespan)

app.include_router(agent.router)
app.include_router(mcp_direct.router)