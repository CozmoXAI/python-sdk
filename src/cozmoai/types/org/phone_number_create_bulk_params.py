# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberCreateBulkParams", "Number"]


class PhoneNumberCreateBulkParams(TypedDict, total=False):
    numbers: Required[Iterable[Number]]

    sip_trunk_id: Required[str]


class Number(TypedDict, total=False):
    number: Required[str]

    label: str
