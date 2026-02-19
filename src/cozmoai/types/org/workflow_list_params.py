# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkflowListParams"]


class WorkflowListParams(TypedDict, total=False):
    is_active: bool
    """Filter by active status"""

    page: int
    """Page number"""

    search: str
    """Search in workflow name and description"""

    size: int
    """Page size"""

    trigger_type: str
    """Filter by trigger type"""
