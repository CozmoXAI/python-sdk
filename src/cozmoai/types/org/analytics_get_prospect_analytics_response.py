# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .analytics_period import AnalyticsPeriod

__all__ = ["AnalyticsGetProspectAnalyticsResponse", "ByCountry", "Growth", "StatusDistribution"]


class ByCountry(BaseModel):
    count: Optional[int] = None

    country: Optional[str] = None


class Growth(BaseModel):
    date: Optional[str] = None

    new_prospects: Optional[int] = None


class StatusDistribution(BaseModel):
    count: Optional[int] = None

    percentage: Optional[float] = None

    status: Optional[str] = None


class AnalyticsGetProspectAnalyticsResponse(BaseModel):
    by_country: Optional[List[ByCountry]] = None

    growth: Optional[List[Growth]] = None

    period: Optional[AnalyticsPeriod] = None

    status_distribution: Optional[List[StatusDistribution]] = None
