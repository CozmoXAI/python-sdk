# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WorkflowListResponse", "Data", "Meta"]


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


class Meta(BaseModel):
    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class WorkflowListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
