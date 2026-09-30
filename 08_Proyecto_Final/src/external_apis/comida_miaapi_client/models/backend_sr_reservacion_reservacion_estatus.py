from typing import Literal

BackendSrReservacionReservacionEstatus = Literal["CANCELADA", "CONFIRMADA", "RESERVADA"]

BACKEND_SR_RESERVACION_RESERVACION_ESTATUS_VALUES: set[BackendSrReservacionReservacionEstatus] = {
    "CANCELADA",
    "CONFIRMADA",
    "RESERVADA",
}


def check_backend_sr_reservacion_reservacion_estatus(value: str) -> BackendSrReservacionReservacionEstatus:
    if value in BACKEND_SR_RESERVACION_RESERVACION_ESTATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BACKEND_SR_RESERVACION_RESERVACION_ESTATUS_VALUES!r}"
    )
