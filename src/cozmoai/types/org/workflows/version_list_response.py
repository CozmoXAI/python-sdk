# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ..pagination_meta_workflows import PaginationMetaWorkflows

__all__ = ["VersionListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    created_by: Optional[str] = None

    version: Optional[int] = None


class VersionListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaWorkflows] = None
