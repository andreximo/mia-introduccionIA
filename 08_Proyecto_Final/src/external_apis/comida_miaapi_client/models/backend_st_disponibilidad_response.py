from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backend_st_disponibilidad_mesa import BackendStDisponibilidadMesa


T = TypeVar("T", bound="BackendStDisponibilidadResponse")


@_attrs_define
class BackendStDisponibilidadResponse:
    """
    Attributes:
        error_code (str | Unset): Error Code
        error_description (str | Unset): Error Description
        st_disponibilidad_mesa (list[BackendStDisponibilidadMesa] | Unset): st Disponibilidad Mesa
    """

    error_code: str | Unset = UNSET
    error_description: str | Unset = UNSET
    st_disponibilidad_mesa: list[BackendStDisponibilidadMesa] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        error_description = self.error_description

        st_disponibilidad_mesa: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.st_disponibilidad_mesa, Unset):
            st_disponibilidad_mesa = []
            for st_disponibilidad_mesa_item_data in self.st_disponibilidad_mesa:
                st_disponibilidad_mesa_item = st_disponibilidad_mesa_item_data.to_dict()
                st_disponibilidad_mesa.append(st_disponibilidad_mesa_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code
        if error_description is not UNSET:
            field_dict["ErrorDescription"] = error_description
        if st_disponibilidad_mesa is not UNSET:
            field_dict["stDisponibilidadMesa"] = st_disponibilidad_mesa

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backend_st_disponibilidad_mesa import BackendStDisponibilidadMesa  # noqa: PLC0415

        d = dict(src_dict)
        error_code = d.pop("ErrorCode", UNSET)

        error_description = d.pop("ErrorDescription", UNSET)

        _st_disponibilidad_mesa = d.pop("stDisponibilidadMesa", UNSET)
        st_disponibilidad_mesa: list[BackendStDisponibilidadMesa] | Unset = UNSET
        if _st_disponibilidad_mesa is not UNSET:
            st_disponibilidad_mesa = []
            for st_disponibilidad_mesa_item_data in _st_disponibilidad_mesa:
                st_disponibilidad_mesa_item = BackendStDisponibilidadMesa.from_dict(st_disponibilidad_mesa_item_data)

                st_disponibilidad_mesa.append(st_disponibilidad_mesa_item)

        backend_st_disponibilidad_response = cls(
            error_code=error_code,
            error_description=error_description,
            st_disponibilidad_mesa=st_disponibilidad_mesa,
        )

        backend_st_disponibilidad_response.additional_properties = d
        return backend_st_disponibilidad_response

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
