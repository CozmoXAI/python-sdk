# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InsightGenerateInsightsParams"]


class InsightGenerateInsightsParams(TypedDict, total=False):
    end_date: Required[str]
    """End date (YYYY-MM-DD)"""

    start_date: Required[str]
    """Start date (YYYY-MM-DD)"""

    force_refresh: bool
    """Force regeneration (skip cache)"""
