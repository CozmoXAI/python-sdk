# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .parameter_prop_param import ParameterPropParam

__all__ = ["ToolCreateParams"]


class ToolCreateParams(TypedDict, total=False):
    description: Required[str]

    method: Required[Literal["GET", "POST", "PUT", "PATCH", "DELETE"]]

    name: Required[str]

    url: Required[str]

    body: str
    """Request body template"""

    filler_phrases: SequenceNotStr[str]
    """Phrases to say while tool is executing"""

    headers: Iterable[int]
    """JSON object of headers"""

    parameters: Iterable[ParameterPropParam]
    """Tool parameters"""
