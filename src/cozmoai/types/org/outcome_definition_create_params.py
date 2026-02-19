# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OutcomeDefinitionCreateParams"]


class OutcomeDefinitionCreateParams(TypedDict, total=False):
    display_name: Required[str]

    key: Required[str]

    value_type: Required[Literal["BOOLEAN", "TEXT", "NUMBER", "DATE", "JSON"]]

    description: str

    is_unique_per_call: bool
