# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ..analytics_period import AnalyticsPeriod

__all__ = ["CallGetCallCostsResponse", "TimeSeries"]


class TimeSeries(BaseModel):
    avg_cost_per_call: Optional[float] = None

    date: Optional[str] = None

    total_calls: Optional[int] = None

    total_cost_usd: Optional[float] = None

    total_tokens: Optional[int] = None


class CallGetCallCostsResponse(BaseModel):
    period: Optional[AnalyticsPeriod] = None

    time_series: Optional[List[TimeSeries]] = None
