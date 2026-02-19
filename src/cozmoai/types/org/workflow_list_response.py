# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .pagination_meta_workflows import PaginationMetaWorkflows

__all__ = ["WorkflowListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    is_active: Optional[bool] = None

    name: Optional[str] = None

    published_at: Optional[str] = None

    trigger_type: Optional[str] = None

    updated_at: Optional[str] = None

    version: Optional[int] = None


class WorkflowListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaWorkflows] = None
