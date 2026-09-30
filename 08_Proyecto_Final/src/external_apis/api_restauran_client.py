import json
from datetime import date, datetime
from comida_miaapi_client.api.interfaz_comidamiaapi import interfaz_comida_miaapi_consultar_diponibilidad_mesas
from comida_miaapi_client.api.interfaz_comidamiaapi import interfaz_comida_miaapi_reservar_mesa
from comida_miaapi_client.models import ReservarMesaInput, BackendStReservacionRequest
from comida_miaapi_client import Client

client = Client(base_url="https://sandbox10.gxapps.cloud/Id439a4e252e200e443e3dc87d04884cfd/Interfaz/comidaMIAAPI")

def counsultar_disponibilidad(payload_string):
    responseDisponibilidad = interfaz_comida_miaapi_consultar_diponibilidad_mesas.sync(
        client=client, stdisponibilidadrequest=payload_string
    )
    return responseDisponibilidad


def hacer_reservacion(datos_reservacion):
    
    cuerpo_peticion = ReservarMesaInput(st_reservacion_request=datos_reservacion)

    responseReservarMesa = interfaz_comida_miaapi_reservar_mesa.sync(
                client=client, body=cuerpo_peticion
            )

    return responseReservarMesa


def main():
    stdisponibilidadrequest = json.dumps(
            obj={"Fecha": "2026-10-15", "Hora": "2026-10-15T19:30:00Z"}
        )
    st_disponibilidad_response = counsultar_disponibilidad(payload_string=stdisponibilidadrequest)
    print(st_disponibilidad_response)

    datos_reservacion = BackendStReservacionRequest(
            reservacion_fecha=date(year=2026, month=9, day=27),
            reservacion_hora_inicio=datetime.fromisoformat("2026-09-27T19:30:00Z"),
            cliente_telefono="+525512345678",
            cliente_nombre="Andrés Pérez",
            cliente_correo="andres@correo.com",
            mesa_codigo="S01",
            reservacion_adultos=2,
            reservacion_ninos=1,
            reservacion_token="token_de_seguridad_xyz_xyz_01"
        )

    # El response ya vendrá parseado con las propiedades ErrorCode, ErrorDescription y Reservacion
    #st_reservacion_response = hacer_reservacion(datos_reservacion)
    #print(f"Código de Error: {st_reservacion_response.error_code}")
    #print(f"ID de Reservación creada: {st_reservacion_response.reservacion.reservacion_id}")
    


if __name__ == "__main__":
    main()
