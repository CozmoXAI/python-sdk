# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .list_response import ListResponse

__all__ = ["ListListResponse", "Meta"]


class Meta(BaseModel):
    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class ListListResponse(BaseModel):
    data: Optional[List[ListResponse]] = None

    meta: Optional[Meta] = None
