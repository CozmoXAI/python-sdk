# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["InsightListInsightsResponse", "Insight"]


class Insight(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    executive_summary: Optional[str] = None

    issue_rate: Optional[float] = None

    issues_identified: Optional[int] = None

    period_end: Optional[str] = None

    period_start: Optional[str] = None

    total_calls: Optional[int] = None


class InsightListInsightsResponse(BaseModel):
    insights: Optional[List[Insight]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
