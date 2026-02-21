# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AgentListResponse", "Data", "Meta"]


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    name: Optional[str] = None

    type: Optional[str] = None

    updated_at: Optional[str] = None


class Meta(BaseModel):
    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class AgentListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
