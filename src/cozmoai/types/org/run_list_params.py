# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    batch_id: str
    """Filter by batch ID"""

    end_date: str
    """Filter runs started before this date (RFC3339 format)"""

    limit: int
    """Items per page"""

    page: int
    """Page number"""

    prospect_id: str
    """Filter by prospect ID"""

    sort: str
    """
    Sort order (started_asc, started_desc, status_asc, status_desc, workflow_asc,
    workflow_desc)
    """

    start_date: str
    """Filter runs started after this date (RFC3339 format)"""

    status: str
    """Filter by status (PENDING, IN_PROGRESS, PAUSED, FINISHED, CANCELLED, FAILED)"""

    workflow_id: str
    """Filter by workflow ID"""

    workflow_version_id: str
    """Filter by workflow version ID"""
