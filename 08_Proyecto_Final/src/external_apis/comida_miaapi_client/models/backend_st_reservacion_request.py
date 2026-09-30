from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackendStReservacionRequest")


@_attrs_define
class BackendStReservacionRequest:
    """
    Attributes:
        reservacion_fecha (datetime.date | Unset): Reservacion Fecha
        reservacion_hora_inicio (datetime.datetime | Unset): Reservacion Hora Inicio
        cliente_telefono (str | Unset): Cliente Telefono
        cliente_nombre (str | Unset): Cliente Nombre
        cliente_correo (str | Unset): Cliente Correo
        mesa_codigo (str | Unset): Mesa Codigo
        reservacion_adultos (int | Unset): Reservacion Adultos
        reservacion_ninos (int | Unset): Reservacion Ninos
        reservacion_token (str | Unset): Reservacion Token
    """

    reservacion_fecha: datetime.date | Unset = UNSET
    reservacion_hora_inicio: datetime.datetime | Unset = UNSET
    cliente_telefono: str | Unset = UNSET
    cliente_nombre: str | Unset = UNSET
    cliente_correo: str | Unset = UNSET
    mesa_codigo: str | Unset = UNSET
    reservacion_adultos: int | Unset = UNSET
    reservacion_ninos: int | Unset = UNSET
    reservacion_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reservacion_fecha: str | Unset = UNSET
        if not isinstance(self.reservacion_fecha, Unset):
            reservacion_fecha = self.reservacion_fecha.isoformat()

        reservacion_hora_inicio: str | Unset = UNSET
        if not isinstance(self.reservacion_hora_inicio, Unset):
            reservacion_hora_inicio = self.reservacion_hora_inicio.isoformat()

        cliente_telefono = self.cliente_telefono

        cliente_nombre = self.cliente_nombre

        cliente_correo = self.cliente_correo

        mesa_codigo = self.mesa_codigo

        reservacion_adultos = self.reservacion_adultos

        reservacion_ninos = self.reservacion_ninos

        reservacion_token = self.reservacion_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reservacion_fecha is not UNSET:
            field_dict["ReservacionFecha"] = reservacion_fecha
        if reservacion_hora_inicio is not UNSET:
            field_dict["ReservacionHoraInicio"] = reservacion_hora_inicio
        if cliente_telefono is not UNSET:
            field_dict["ClienteTelefono"] = cliente_telefono
        if cliente_nombre is not UNSET:
            field_dict["ClienteNombre"] = cliente_nombre
        if cliente_correo is not UNSET:
            field_dict["ClienteCorreo"] = cliente_correo
        if mesa_codigo is not UNSET:
            field_dict["MesaCodigo"] = mesa_codigo
        if reservacion_adultos is not UNSET:
            field_dict["ReservacionAdultos"] = reservacion_adultos
        if reservacion_ninos is not UNSET:
            field_dict["ReservacionNinos"] = reservacion_ninos
        if reservacion_token is not UNSET:
            field_dict["ReservacionToken"] = reservacion_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        cliente_correo = d.pop("ClienteCorreo", UNSET)

        mesa_codigo = d.pop("MesaCodigo", UNSET)

        reservacion_adultos = d.pop("ReservacionAdultos", UNSET)

        reservacion_ninos = d.pop("ReservacionNinos", UNSET)

        reservacion_token = d.pop("ReservacionToken", UNSET)

        backend_st_reservacion_request = cls(
            reservacion_fecha=reservacion_fecha,
            reservacion_hora_inicio=reservacion_hora_inicio,
            cliente_telefono=cliente_telefono,
            cliente_nombre=cliente_nombre,
            cliente_correo=cliente_correo,
            mesa_codigo=mesa_codigo,
            reservacion_adultos=reservacion_adultos,
            reservacion_ninos=reservacion_ninos,
            reservacion_token=reservacion_token,
        )

        backend_st_reservacion_request.additional_properties = d
        return backend_st_reservacion_request

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
