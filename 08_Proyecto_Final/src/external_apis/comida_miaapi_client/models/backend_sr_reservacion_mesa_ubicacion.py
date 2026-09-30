from typing import Literal

BackendSrReservacionMesaUbicacion = Literal["SalonPrincipal", "Terraza", "Ventana"]

BACKEND_SR_RESERVACION_MESA_UBICACION_VALUES: set[BackendSrReservacionMesaUbicacion] = {
    "SalonPrincipal",
    "Terraza",
    "Ventana",
}


def check_backend_sr_reservacion_mesa_ubicacion(value: str) -> BackendSrReservacionMesaUbicacion:
    if value in BACKEND_SR_RESERVACION_MESA_UBICACION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKEND_SR_RESERVACION_MESA_UBICACION_VALUES!r}")
