# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AnalyticsListBatchesParams"]


class AnalyticsListBatchesParams(TypedDict, total=False):
    end_date: str
    """End date (ISO 8601)"""

    start_date: str
    """Start date (ISO 8601)"""
