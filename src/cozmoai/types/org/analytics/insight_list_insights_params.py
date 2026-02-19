# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InsightListInsightsParams"]


class InsightListInsightsParams(TypedDict, total=False):
    end_date: str
    """Filter by period end date (YYYY-MM-DD)"""

    limit: int
    """Number of items per page"""

    offset: int
    """Number of items to skip"""

    start_date: str
    """Filter by period start date (YYYY-MM-DD)"""
