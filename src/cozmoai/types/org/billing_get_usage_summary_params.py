# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BillingGetUsageSummaryParams"]


class BillingGetUsageSummaryParams(TypedDict, total=False):
    end_date: str
    """Filter by end date (ISO 8601)"""

    start_date: str
    """Filter by start date (ISO 8601)"""
