# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExportGetCsvParams"]


class ExportGetCsvParams(TypedDict, total=False):
    agent_id: str
    """Filter by agent ID"""

    direction: str
    """Filter by direction"""

    end_date: str
    """Filter by end date (ISO 8601)"""

    min_duration: int
    """Filter by minimum duration in seconds"""

    phone: str
    """Search by phone number"""

    prospect_external_id: str
    """Filter by prospect external ID"""

    prospect_id: str
    """Filter by prospect ID"""

    start_date: str
    """Filter by start date (ISO 8601)"""

    status: str
    """Filter by status"""

    workflow_id: str
    """Filter by workflow ID"""
