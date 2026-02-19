# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EvalListParams"]


class EvalListParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]
    """Agent ID"""

    page: int
    """Page number"""

    size: int
    """Page size"""
