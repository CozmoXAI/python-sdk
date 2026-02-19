# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .analytics_period import AnalyticsPeriod

__all__ = ["AnalyticsGetDashboardSummaryResponse"]


class AnalyticsGetDashboardSummaryResponse(BaseModel):
    active_workflows: Optional[int] = None

    calls_in_period: Optional[int] = None

    current_balance: Optional[str] = None

    period: Optional[AnalyticsPeriod] = None

    total_agents: Optional[int] = None

    total_call_minutes: Optional[int] = None

    total_prospects: Optional[int] = None
