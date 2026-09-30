"""
Configuración de servidores MCP a los que se conectará el host.

Cada entrada define cómo lanzar un servidor MCP como subproceso (transporte stdio).
Agrega aquí tantos servidores como necesites: el host abre una ClientSession por
cada uno al arrancar y combina sus catálogos de tools en un solo agente.

IMPORTANTE: las rutas en "args" son relativas al directorio desde donde ejecutes
uvicorn (ver README.md).
"""
import sys
from pathlib import Path

SERVERS_DIR = Path(__file__).resolve().parent.parent / "servers"

MCP_SERVERS = [
    {
        "name": "recetas", 
        "command": sys.executable,
        "args": [str(SERVERS_DIR / "server_recetas.py")]
        },
    {
        "name": "reservaciones",
        "command": sys.executable,
        "args": [str(SERVERS_DIR / "server_reservacion.py")]
        },
]