# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .pagination_meta_calls import PaginationMetaCalls

__all__ = ["ProspectListCallsResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    agent_name: Optional[str] = None

    direction: Optional[str] = None

    duration_seconds: Optional[int] = None

    ended_at: Optional[str] = None

    from_number: Optional[str] = None

    started_at: Optional[str] = None

    status: Optional[str] = None

    to_number: Optional[str] = None


class ProspectListCallsResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaCalls] = None
