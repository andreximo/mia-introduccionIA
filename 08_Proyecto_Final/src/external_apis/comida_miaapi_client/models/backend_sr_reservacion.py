from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backend_sr_reservacion_mesa_ubicacion import (
    BackendSrReservacionMesaUbicacion,
    check_backend_sr_reservacion_mesa_ubicacion,
)
from ..models.backend_sr_reservacion_reservacion_estatus import (
    BackendSrReservacionReservacionEstatus,
    check_backend_sr_reservacion_reservacion_estatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackendSrReservacion")


@_attrs_define
class BackendSrReservacion:
    """
    Attributes:
        reservacion_id (int | Unset): Reservacion Id
        reservacion_fecha (datetime.date | Unset): Reservacion Fecha
        reservacion_hora_inicio (datetime.datetime | Unset): Reservacion Hora Inicio
        cliente_telefono (str | Unset): Cliente Telefono
        cliente_nombre (str | Unset): Cliente Nombre
        reservacion_pax (int | Unset): Reservacion Pax
        mesa_codigo (str | Unset): Mesa Codigo
        mesa_ubicacion (BackendSrReservacionMesaUbicacion | Unset): Ubicacion
        reservacion_estatus (BackendSrReservacionReservacionEstatus | Unset): Reservacion Estatus
    """

    reservacion_id: int | Unset = UNSET
    reservacion_fecha: datetime.date | Unset = UNSET
    reservacion_hora_inicio: datetime.datetime | Unset = UNSET
    cliente_telefono: str | Unset = UNSET
    cliente_nombre: str | Unset = UNSET
    reservacion_pax: int | Unset = UNSET
    mesa_codigo: str | Unset = UNSET
    mesa_ubicacion: BackendSrReservacionMesaUbicacion | Unset = UNSET
    reservacion_estatus: BackendSrReservacionReservacionEstatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reservacion_id = self.reservacion_id

        reservacion_fecha: str | Unset = UNSET
        if not isinstance(self.reservacion_fecha, Unset):
            reservacion_fecha = self.reservacion_fecha.isoformat()

        reservacion_hora_inicio: str | Unset = UNSET
        if not isinstance(self.reservacion_hora_inicio, Unset):
            reservacion_hora_inicio = self.reservacion_hora_inicio.isoformat()

        cliente_telefono = self.cliente_telefono

        cliente_nombre = self.cliente_nombre

        reservacion_pax = self.reservacion_pax

        mesa_codigo = self.mesa_codigo

        mesa_ubicacion: str | Unset = UNSET
        if not isinstance(self.mesa_ubicacion, Unset):
            mesa_ubicacion = self.mesa_ubicacion

        reservacion_estatus: str | Unset = UNSET
        if not isinstance(self.reservacion_estatus, Unset):
            reservacion_estatus = self.reservacion_estatus

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reservacion_id is not UNSET:
            field_dict["ReservacionId"] = reservacion_id
        if reservacion_fecha is not UNSET:
            field_dict["ReservacionFecha"] = reservacion_fecha
        if reservacion_hora_inicio is not UNSET:
            field_dict["ReservacionHoraInicio"] = reservacion_hora_inicio
        if cliente_telefono is not UNSET:
            field_dict["ClienteTelefono"] = cliente_telefono
        if cliente_nombre is not UNSET:
            field_dict["ClienteNombre"] = cliente_nombre
        if reservacion_pax is not UNSET:
            field_dict["ReservacionPax"] = reservacion_pax
        if mesa_codigo is not UNSET:
            field_dict["MesaCodigo"] = mesa_codigo
        if mesa_ubicacion is not UNSET:
            field_dict["MesaUbicacion"] = mesa_ubicacion
        if reservacion_estatus is not UNSET:
            field_dict["ReservacionEstatus"] = reservacion_estatus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reservacion_id = d.pop("ReservacionId", UNSET)

        _reservacion_fecha = d.pop("ReservacionFecha", UNSET)
        reservacion_fecha: datetime.date | Unset
        if isinstance(_reservacion_fecha, Unset):
            reservacion_fecha = UNSET
        else:
            reservacion_fecha = datetime.date.fromisoformat(_reservacion_fecha)

        _reservacion_hora_inicio = d.pop("ReservacionHoraInicio", UNSET)
        reservacion_hora_inicio: datetime.datetime | Unset
        if isinstance(_reservacion_hora_inicio, Unset):
            reservacion_hora_inicio = UNSET
        else:
            reservacion_hora_inicio = datetime.datetime.fromisoformat(_reservacion_hora_inicio)

        cliente_telefono = d.pop("ClienteTelefono", UNSET)

        cliente_nombre = d.pop("ClienteNombre", UNSET)

        reservacion_pax = d.pop("ReservacionPax", UNSET)

        mesa_codigo = d.pop("MesaCodigo", UNSET)

        _mesa_ubicacion = d.pop("MesaUbicacion", UNSET)
        mesa_ubicacion: BackendSrReservacionMesaUbicacion | Unset
        if isinstance(_mesa_ubicacion, Unset):
            mesa_ubicacion = UNSET
        else:
            mesa_ubicacion = check_backend_sr_reservacion_mesa_ubicacion(_mesa_ubicacion)

        _reservacion_estatus = d.pop("ReservacionEstatus", UNSET)
        reservacion_estatus: BackendSrReservacionReservacionEstatus | Unset
        if isinstance(_reservacion_estatus, Unset):
            reservacion_estatus = UNSET
        else:
            reservacion_estatus = check_backend_sr_reservacion_reservacion_estatus(_reservacion_estatus)

        backend_sr_reservacion = cls(
            reservacion_id=reservacion_id,
            reservacion_fecha=reservacion_fecha,
            reservacion_hora_inicio=reservacion_hora_inicio,
            cliente_telefono=cliente_telefono,
            cliente_nombre=cliente_nombre,
            reservacion_pax=reservacion_pax,
            mesa_codigo=mesa_codigo,
            mesa_ubicacion=mesa_ubicacion,
            reservacion_estatus=reservacion_estatus,
        )

        backend_sr_reservacion.additional_properties = d
        return backend_sr_reservacion

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
