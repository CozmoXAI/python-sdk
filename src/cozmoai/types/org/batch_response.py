# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatchResponse", "Stats"]


class Stats(BaseModel):
    cancelled_count: Optional[int] = None

    failed_count: Optional[int] = None

    finished_count: Optional[int] = None

    in_progress_count: Optional[int] = None

    paused_count: Optional[int] = None

    pending_count: Optional[int] = None

    total_count: Optional[int] = None


class BatchResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    created_by: Optional[str] = None

    name: Optional[str] = None

    organization_id: Optional[str] = None

    scheduled_at: Optional[str] = None

    source_type: Optional[str] = None

    stats: Optional[Stats] = None

    status: Optional[str] = None

    total_prospects: Optional[int] = None

    updated_at: Optional[str] = None

    workflow_id: Optional[str] = None

    workflow_version_id: Optional[str] = None

    workflow_version_number: Optional[int] = None
