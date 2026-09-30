from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackendStDisponibilidadRequest")


@_attrs_define
class BackendStDisponibilidadRequest:
    """
    Attributes:
        fecha (datetime.date | Unset): Fecha
        hora (datetime.datetime | Unset): Hora
    """

    fecha: datetime.date | Unset = UNSET
    hora: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fecha: str | Unset = UNSET
        if not isinstance(self.fecha, Unset):
            fecha = self.fecha.isoformat()

        hora: str | Unset = UNSET
        if not isinstance(self.hora, Unset):
            hora = self.hora.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fecha is not UNSET:
            field_dict["Fecha"] = fecha
        if hora is not UNSET:
            field_dict["Hora"] = hora

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _fecha = d.pop("Fecha", UNSET)
        fecha: datetime.date | Unset
        if isinstance(_fecha, Unset):
            fecha = UNSET
        else:
            fecha = datetime.date.fromisoformat(_fecha)

        _hora = d.pop("Hora", UNSET)
        hora: datetime.datetime | Unset
        if isinstance(_hora, Unset):
            hora = UNSET
        else:
            hora = datetime.datetime.fromisoformat(_hora)

        backend_st_disponibilidad_request = cls(
            fecha=fecha,
            hora=hora,
        )

        backend_st_disponibilidad_request.additional_properties = d
        return backend_st_disponibilidad_request

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
