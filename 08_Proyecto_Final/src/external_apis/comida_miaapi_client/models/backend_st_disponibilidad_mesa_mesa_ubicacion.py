from typing import Literal

BackendStDisponibilidadMesaMesaUbicacion = Literal["SalonPrincipal", "Terraza", "Ventana"]

BACKEND_ST_DISPONIBILIDAD_MESA_MESA_UBICACION_VALUES: set[BackendStDisponibilidadMesaMesaUbicacion] = {
    "SalonPrincipal",
    "Terraza",
    "Ventana",
}


def check_backend_st_disponibilidad_mesa_mesa_ubicacion(value: str) -> BackendStDisponibilidadMesaMesaUbicacion:
    if value in BACKEND_ST_DISPONIBILIDAD_MESA_MESA_UBICACION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BACKEND_ST_DISPONIBILIDAD_MESA_MESA_UBICACION_VALUES!r}"
    )
