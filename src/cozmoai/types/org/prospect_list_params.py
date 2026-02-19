# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProspectListParams"]


class ProspectListParams(TypedDict, total=False):
    country: str
    """Filter by country code"""

    list_id: str
    """Filter by prospect list ID"""

    no_list: bool
    """Filter prospects without a list"""

    page: int
    """Page number"""

    search: str
    """Search in name, phone, email"""

    size: int
    """Page size"""

    status: str
    """Filter by status"""

    tag_id: str
    """Filter by tag ID"""
