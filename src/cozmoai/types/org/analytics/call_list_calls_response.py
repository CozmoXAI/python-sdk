# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ..analytics_period import AnalyticsPeriod

__all__ = ["CallListCallsResponse", "Duration", "Outcome", "TimeSeries"]


class Duration(BaseModel):
    avg_duration_seconds: Optional[float] = None

    max_duration_seconds: Optional[int] = None

    total_calls: Optional[int] = None

    total_duration_seconds: Optional[int] = None


class Outcome(BaseModel):
    outcome_count: Optional[int] = None

    outcome_key: Optional[str] = None

    outcome_value: Optional[str] = None


class TimeSeries(BaseModel):
    busy: Optional[int] = None

    completed: Optional[int] = None

    date: Optional[str] = None

    failed: Optional[int] = None

    no_answer: Optional[int] = None

    total: Optional[int] = None


class CallListCallsResponse(BaseModel):
    duration: Optional[Duration] = None

    outcomes: Optional[List[Outcome]] = None

    period: Optional[AnalyticsPeriod] = None

    time_series: Optional[List[TimeSeries]] = None
