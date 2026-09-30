from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backend_st_reservacion_request import BackendStReservacionRequest


T = TypeVar("T", bound="ReservarMesaInput")


@_attrs_define
class ReservarMesaInput:
    """
    Attributes:
        st_reservacion_request (BackendStReservacionRequest | Unset):
    """

    st_reservacion_request: BackendStReservacionRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        st_reservacion_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.st_reservacion_request, Unset):
            st_reservacion_request = self.st_reservacion_request.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if st_reservacion_request is not UNSET:
            field_dict["stReservacionRequest"] = st_reservacion_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backend_st_reservacion_request import BackendStReservacionRequest  # noqa: PLC0415

        d = dict(src_dict)
        _st_reservacion_request = d.pop("stReservacionRequest", UNSET)
        st_reservacion_request: BackendStReservacionRequest | Unset
        if isinstance(_st_reservacion_request, Unset):
            st_reservacion_request = UNSET
        else:
            st_reservacion_request = BackendStReservacionRequest.from_dict(_st_reservacion_request)

        reservar_mesa_input = cls(
            st_reservacion_request=st_reservacion_request,
        )

        reservar_mesa_input.additional_properties = d
        return reservar_mesa_input

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
