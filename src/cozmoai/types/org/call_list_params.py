# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CallListParams"]


class CallListParams(TypedDict, total=False):
    agent_id: str
    """Filter by agent ID"""

    direction: str
    """Filter by direction (INBOUND, OUTBOUND)"""

    end_date: str
    """Filter by end date (ISO 8601)"""

    min_duration: int
    """Filter by minimum duration in seconds"""

    page: int
    """Page number"""

    phone: str
    """Search by phone number"""

    prospect_external_id: str
    """Filter by prospect external ID"""

    prospect_id: str
    """Filter by prospect ID"""

    prospect_name: str
    """Filter by prospect name (first or last)"""

    size: int
    """Page size"""

    start_date: str
    """Filter by start date (ISO 8601)"""

    status: str
    """
    Filter by status (SCHEDULED, RINGING, IN_PROGRESS, completed, no-answer, failed,
    busy)
    """

    workflow_id: str
    """Filter by workflow ID"""
