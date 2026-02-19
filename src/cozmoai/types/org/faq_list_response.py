# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .faq import Faq
from ..._models import BaseModel

__all__ = ["FaqListResponse", "Pagination"]


class Pagination(BaseModel):
    has_more: Optional[bool] = None

    next_cursor: Optional[str] = None


class FaqListResponse(BaseModel):
    data: Optional[List[Faq]] = None

    pagination: Optional[Pagination] = None
