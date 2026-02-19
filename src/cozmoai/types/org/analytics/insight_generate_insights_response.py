# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["InsightGenerateInsightsResponse", "Issue", "IssueExample", "Recommendation"]


class IssueExample(BaseModel):
    customer_name: Optional[str] = None

    incident_cause: Optional[str] = None

    quote: Optional[str] = None

    recommendation: Optional[str] = None

    reference_id: Optional[str] = None


class Issue(BaseModel):
    count: Optional[int] = None

    description: Optional[str] = None

    examples: Optional[List[IssueExample]] = None

    name: Optional[str] = None

    percentage: Optional[float] = None

    rank: Optional[int] = None

    recommendation: Optional[str] = None


class Recommendation(BaseModel):
    description: Optional[str] = None

    priority: Optional[str] = None
    """HIGH, MEDIUM, LOW"""

    title: Optional[str] = None


class InsightGenerateInsightsResponse(BaseModel):
    cached: Optional[bool] = None

    executive_summary: Optional[str] = None

    generated_at: Optional[str] = None

    issue_rate: Optional[float] = None

    issues: Optional[List[Issue]] = None

    issues_identified: Optional[int] = None

    organization_id: Optional[str] = None

    organization_name: Optional[str] = None

    period: Optional[str] = None

    recommendations: Optional[List[Recommendation]] = None

    routine_rate: Optional[float] = None

    success_factors: Optional[List[str]] = None

    total_calls: Optional[int] = None
