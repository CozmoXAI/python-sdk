# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ..analytics_period import AnalyticsPeriod

__all__ = ["WorkflowListWorkflowsResponse", "Workflow"]


class Workflow(BaseModel):
    completed: Optional[int] = None

    completion_rate_pct: Optional[float] = None

    failed: Optional[int] = None

    pending: Optional[int] = None

    running: Optional[int] = None

    total_runs: Optional[int] = None

    workflow_id: Optional[str] = None

    workflow_name: Optional[str] = None


class WorkflowListWorkflowsResponse(BaseModel):
    period: Optional[AnalyticsPeriod] = None

    workflows: Optional[List[Workflow]] = None
