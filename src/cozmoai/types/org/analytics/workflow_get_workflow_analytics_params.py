# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkflowGetWorkflowAnalyticsParams"]


class WorkflowGetWorkflowAnalyticsParams(TypedDict, total=False):
    org_id: Required[str]

    end_date: str
    """End date (ISO 8601)"""

    start_date: str
    """Start date (ISO 8601)"""
