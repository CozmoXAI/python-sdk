# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UnitTestListParams"]


class UnitTestListParams(TypedDict, total=False):
    org_id: Required[str]

    page: int
    """Page number"""

    size: int
    """Page size"""
