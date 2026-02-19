# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["AnalyticsListBatchesResponse", "AnalyticsListBatchesResponseItem"]


class AnalyticsListBatchesResponseItem(BaseModel):
    batch_id: Optional[str] = None

    batch_name: Optional[str] = None

    completed: Optional[int] = None

    completion_rate_pct: Optional[float] = None

    created_at: Optional[str] = None

    failed: Optional[int] = None

    total_prospects: Optional[int] = None

    workflow_name: Optional[str] = None


AnalyticsListBatchesResponse: TypeAlias = List[AnalyticsListBatchesResponseItem]
