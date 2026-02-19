# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .template import Template
from ..._models import BaseModel

__all__ = ["EmailTemplateListResponse", "Meta"]


class Meta(BaseModel):
    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class EmailTemplateListResponse(BaseModel):
    data: Optional[List[Template]] = None

    meta: Optional[Meta] = None
