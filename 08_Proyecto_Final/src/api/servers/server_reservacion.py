"""
Servidor MCP: consulta de disponibilidad y reservación de mesas (ComidaMIA).

Adaptado de api_restauran_client.py. Es un ADAPTADOR: el agente solo ve dos
tools con parámetros simples; los detalles de la API REST (cliente generado,
URL, token de seguridad, modelos de request) quedan encapsulados aquí.

Diferencias respecto al script original:
  - counsultar_disponibilidad() -> tool consultar_disponibilidad_mesas(fecha, hora).
    El armado del JSON {"Fecha", "Hora"} lo hace el servidor, no el LLM.
  - hacer_reservacion() -> tool reservar_mesa(...). Ya no recibe un objeto
    BackendStReservacionRequest: los datos llegan como parámetros simples y
    el servidor construye el modelo.
  - reservacion_token NO es un parámetro de la tool: es una credencial y se
    lee de la variable de entorno RESERVACION_TOKEN. El LLM nunca la ve.
  - Los errores se devuelven como {"error": ...} (observations que el LLM
    puede leer), en vez de dejar que la excepción tumbe el proceso.
  - Los logs van a stderr: en transporte stdio, stdout es el canal del
    protocolo MCP y no debe usarse con print().

Requisito: el paquete generado `comida_miaapi_client` debe ser importable.
Colócalo en la raíz del proyecto (junto a host/ y servers/) o instálalo
con pip (pip install -e ruta/al/cliente).
"""

import json
import os
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from mcp.server.mcpserver import MCPServer


PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# El SDK de MCP no propaga todas las variables de entorno del host a los
# subprocesos stdio, así que este servidor carga el .env por su cuenta.
load_dotenv(PROJECT_ROOT / ".env")

#from ...external_apis.comida_miaapi_client import Client  # noqa: E402
from src.external_apis.comida_miaapi_client import Client
from src.external_apis.comida_miaapi_client.api.interfaz_comidamiaapi import (  # noqa: E402
    interfaz_comida_miaapi_consultar_diponibilidad_mesas,
    interfaz_comida_miaapi_reservar_mesa,
)

from src.external_apis.comida_miaapi_client.models import (  # noqa: E402
    BackendStReservacionRequest,
    ReservarMesaInput,
)

BASE_URL = os.environ.get(
    "COMIDAMIA_API_URL",
    "https://sandbox10.gxapps.cloud/Id439a4e252e200e443e3dc87d04884cfd/Interfaz/comidaMIAAPI",
)
RESERVACION_TOKEN = os.environ.get("RESERVACION_TOKEN")

mcp = MCPServer("servidor-reservacion")
client = Client(base_url=BASE_URL)


def _serializar(respuesta: Any) -> Any:
    """Convierte la respuesta del cliente generado (modelos attrs) a algo serializable."""
    if respuesta is None:
        return None
    if hasattr(respuesta, "to_dict"):
        return respuesta.to_dict()
    return str(respuesta)


def _parse_datetime(valor: str) -> datetime:
    """Acepta ISO 8601 con sufijo 'Z' (fromisoformat no lo soporta antes de Python 3.11)."""
    return datetime.fromisoformat(valor.replace("Z", "+00:00"))


@mcp.tool()
def consultar_disponibilidad_mesas(fecha: str, hora: str) -> dict:
    """
    Consulta qué mesas del restaurante están disponibles para una fecha y hora.
    Úsala antes de reservar, para obtener el código de una mesa libre (mesa_codigo).

    Args:
        fecha: Fecha de la consulta en formato YYYY-MM-DD (ej. "2026-10-15").
        hora: Fecha y hora de inicio en ISO 8601 UTC (ej. "2026-10-15T19:30:00Z").
    """
    try:
        payload = json.dumps({"Fecha": fecha, "Hora": hora})
        respuesta = interfaz_comida_miaapi_consultar_diponibilidad_mesas.sync(
            client=client, stdisponibilidadrequest=payload
        )
        if respuesta is None:
            return {"error": "La API no devolvió una respuesta válida."}
        return {"disponibilidad": _serializar(respuesta)}
    except Exception as e:
        return {"error": f"No se pudo consultar la disponibilidad: {e}"}


@mcp.tool()
def reservar_mesa(
    reservacion_fecha: str,
    reservacion_hora_inicio: str,
    cliente_nombre: str,
    cliente_telefono: str,
    cliente_correo: str,
    mesa_codigo: str,
    reservacion_adultos: int,
    reservacion_ninos: int = 0,
) -> dict:
    """
    Crea una reservación REAL de mesa en el restaurante. Es una acción con
    efectos: antes de llamarla, confirma con el usuario todos los datos y
    verifica con consultar_disponibilidad_mesas que la mesa esté libre y obtener el código de la mesa(mesa_codigo).

    Args:
        reservacion_fecha: Fecha de la reservación, YYYY-MM-DD.
        reservacion_hora_inicio: Fecha y hora de inicio en ISO 8601 UTC
            (ej. "2026-09-27T19:30:00Z").
        cliente_nombre: Nombre completo del cliente.
        cliente_telefono: Teléfono con lada internacional (ej. "+525512345678").
        cliente_correo: Correo electrónico del cliente.
        mesa_codigo: Código de la mesa a reservar (ej. "S01").
        reservacion_adultos: Número de adultos.
        reservacion_ninos: Número de niños (0 si no hay).
    """
    if not RESERVACION_TOKEN:
        return {"error": "Servidor mal configurado: falta RESERVACION_TOKEN en el entorno."}

    try:
        datos = BackendStReservacionRequest(
            reservacion_fecha=date.fromisoformat(reservacion_fecha),
            reservacion_hora_inicio=_parse_datetime(reservacion_hora_inicio),
            cliente_telefono=cliente_telefono,
            cliente_nombre=cliente_nombre,
            cliente_correo=cliente_correo,
            mesa_codigo=mesa_codigo,
            reservacion_adultos=reservacion_adultos,
            reservacion_ninos=reservacion_ninos,
            reservacion_token=RESERVACION_TOKEN,
        )
        cuerpo = ReservarMesaInput(st_reservacion_request=datos)
        respuesta = interfaz_comida_miaapi_reservar_mesa.sync(client=client, body=cuerpo)

        if respuesta is None:
            return {"error": "La API no devolvió una respuesta válida."}
        return {"reservacion": _serializar(respuesta)}
    except ValueError as e:
        return {"error": f"Formato de fecha/hora inválido: {e}"}
    except Exception as e:
        return {"error": f"No se pudo crear la reservación: {e}"}


if __name__ == "__main__":
    mcp.run(transport="stdio")