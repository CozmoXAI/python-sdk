# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .tag_response_prospect import TagResponseProspect

__all__ = ["ProspectListResponse", "Data", "Meta"]


class Data(BaseModel):
    id: Optional[str] = None

    country: Optional[str] = None

    created_at: Optional[str] = None

    email: Optional[str] = None

    external_id: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    list_id: Optional[str] = None

    phone: Optional[str] = None

    status: Optional[str] = None

    tags: Optional[List[TagResponseProspect]] = None

    timezone: Optional[str] = None


class Meta(BaseModel):
    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class ProspectListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
