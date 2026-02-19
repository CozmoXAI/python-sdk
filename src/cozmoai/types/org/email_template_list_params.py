# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmailTemplateListParams"]


class EmailTemplateListParams(TypedDict, total=False):
    page: int
    """Page number (default: 1)"""

    search: str
    """Search in template name"""

    size: int
    """Page size (default: 20, max: 100)"""
