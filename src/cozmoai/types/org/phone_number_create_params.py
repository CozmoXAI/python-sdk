# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberCreateParams"]


class PhoneNumberCreateParams(TypedDict, total=False):
    number: Required[str]

    sip_trunk_id: Required[str]

    label: str
