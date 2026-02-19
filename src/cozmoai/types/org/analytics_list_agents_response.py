# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .analytics_period import AnalyticsPeriod

__all__ = ["AnalyticsListAgentsResponse", "Agent", "OutcomeRate"]


class Agent(BaseModel):
    agent_id: Optional[str] = None

    agent_name: Optional[str] = None

    avg_duration_seconds: Optional[float] = None

    completed_calls: Optional[int] = None

    total_calls: Optional[int] = None

    total_cost_usd: Optional[float] = None


class OutcomeRate(BaseModel):
    agent_id: Optional[str] = None

    agent_name: Optional[str] = None

    outcome_key: Optional[str] = None

    positive: Optional[int] = None

    positive_rate_pct: Optional[float] = None

    total: Optional[int] = None


class AnalyticsListAgentsResponse(BaseModel):
    agents: Optional[List[Agent]] = None

    outcome_rates: Optional[List[OutcomeRate]] = None

    period: Optional[AnalyticsPeriod] = None
