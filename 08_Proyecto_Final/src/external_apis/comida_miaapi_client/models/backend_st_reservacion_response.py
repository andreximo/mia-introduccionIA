from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backend_sr_reservacion import BackendSrReservacion


T = TypeVar("T", bound="BackendStReservacionResponse")


@_attrs_define
class BackendStReservacionResponse:
    """
    Attributes:
        error_code (str | Unset): Error Code
        error_description (str | Unset): Error Description
        reservacion (BackendSrReservacion | Unset):
    """

    error_code: str | Unset = UNSET
    error_description: str | Unset = UNSET
    reservacion: BackendSrReservacion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        error_description = self.error_description

        reservacion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reservacion, Unset):
            reservacion = self.reservacion.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code
        if error_description is not UNSET:
            field_dict["ErrorDescription"] = error_description
        if reservacion is not UNSET:
            field_dict["Reservacion"] = reservacion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backend_sr_reservacion import BackendSrReservacion  # noqa: PLC0415

        d = dict(src_dict)
        error_code = d.pop("ErrorCode", UNSET)

        error_description = d.pop("ErrorDescription", UNSET)

        _reservacion = d.pop("Reservacion", UNSET)
        reservacion: BackendSrReservacion | Unset
        if isinstance(_reservacion, Unset):
            reservacion = UNSET
        else:
            reservacion = BackendSrReservacion.from_dict(_reservacion)

        backend_st_reservacion_response = cls(
            error_code=error_code,
            error_description=error_description,
            reservacion=reservacion,
        )

        backend_st_reservacion_response.additional_properties = d
        return backend_st_reservacion_response

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
