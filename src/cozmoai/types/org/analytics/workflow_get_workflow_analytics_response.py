# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ..analytics_period import AnalyticsPeriod

__all__ = ["WorkflowGetWorkflowAnalyticsResponse"]


class WorkflowGetWorkflowAnalyticsResponse(BaseModel):
    avg_duration_seconds: Optional[float] = None

    completed: Optional[int] = None

    completion_rate_pct: Optional[float] = None

    failed: Optional[int] = None

    pending: Optional[int] = None

    period: Optional[AnalyticsPeriod] = None

    running: Optional[int] = None

    total_runs: Optional[int] = None

    workflow_id: Optional[str] = None

    workflow_name: Optional[str] = None
