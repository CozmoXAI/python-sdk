# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LedgerListParams"]


class LedgerListParams(TypedDict, total=False):
    end_date: str
    """Filter by end date (ISO 8601)"""

    event_type: str
    """Filter by event type (TOPUP, CALL_USAGE, RENTAL)"""

    page: int
    """Page number"""

    size: int
    """Page size"""

    start_date: str
    """Filter by start date (ISO 8601)"""
