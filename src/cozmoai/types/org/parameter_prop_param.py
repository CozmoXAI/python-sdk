# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ParameterPropParam"]


class ParameterPropParam(TypedDict, total=False):
    name: Required[str]

    type: Required[str]
    """string, number, boolean, object, array"""

    description: str

    required: bool
