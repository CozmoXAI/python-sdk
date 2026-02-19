# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ListListParams"]


class ListListParams(TypedDict, total=False):
    page: int
    """Page number"""

    search: str
    """Search in list name"""

    size: int
    """Page size"""

    sort: Literal["name_asc", "name_desc", "created_asc", "created_desc"]
    """Sort order"""

    source: Literal["CSV", "API", "MANUAL", "INTEGRATION"]
    """Filter by source"""
