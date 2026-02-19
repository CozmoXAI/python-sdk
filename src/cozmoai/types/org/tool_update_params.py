# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .parameter_prop_param import ParameterPropParam

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    body: str

    description: str

    filler_phrases: SequenceNotStr[str]

    headers: Iterable[int]

    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]

    name: str

    parameters: Iterable[ParameterPropParam]
    """If provided, replaces all existing parameters"""

    url: str
