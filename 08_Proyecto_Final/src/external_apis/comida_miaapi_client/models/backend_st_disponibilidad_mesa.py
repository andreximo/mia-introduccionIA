from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backend_st_disponibilidad_mesa_mesa_ubicacion import (
    BackendStDisponibilidadMesaMesaUbicacion,
    check_backend_st_disponibilidad_mesa_mesa_ubicacion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackendStDisponibilidadMesa")


@_attrs_define
class BackendStDisponibilidadMesa:
    """
    Attributes:
        mesa_codigo (str | Unset): Mesa Codigo
        mesa_capacidad (int | Unset): Capacidad
        mesa_ubicacion (BackendStDisponibilidadMesaMesaUbicacion | Unset): Ubicacion
    """

    mesa_codigo: str | Unset = UNSET
    mesa_capacidad: int | Unset = UNSET
    mesa_ubicacion: BackendStDisponibilidadMesaMesaUbicacion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mesa_codigo = self.mesa_codigo

        mesa_capacidad = self.mesa_capacidad

        mesa_ubicacion: str | Unset = UNSET
        if not isinstance(self.mesa_ubicacion, Unset):
            mesa_ubicacion = self.mesa_ubicacion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mesa_codigo is not UNSET:
            field_dict["MesaCodigo"] = mesa_codigo
        if mesa_capacidad is not UNSET:
            field_dict["MesaCapacidad"] = mesa_capacidad
        if mesa_ubicacion is not UNSET:
            field_dict["MesaUbicacion"] = mesa_ubicacion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mesa_codigo = d.pop("MesaCodigo", UNSET)

        mesa_capacidad = d.pop("MesaCapacidad", UNSET)

        _mesa_ubicacion = d.pop("MesaUbicacion", UNSET)
        mesa_ubicacion: BackendStDisponibilidadMesaMesaUbicacion | Unset
        if isinstance(_mesa_ubicacion, Unset):
            mesa_ubicacion = UNSET
        else:
            mesa_ubicacion = check_backend_st_disponibilidad_mesa_mesa_ubicacion(_mesa_ubicacion)

        backend_st_disponibilidad_mesa = cls(
            mesa_codigo=mesa_codigo,
            mesa_capacidad=mesa_capacidad,
            mesa_ubicacion=mesa_ubicacion,
        )

        backend_st_disponibilidad_mesa.additional_properties = d
        return backend_st_disponibilidad_mesa

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
