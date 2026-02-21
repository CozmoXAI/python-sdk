# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .pagination_meta_calls import PaginationMetaCalls

__all__ = ["CallListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    agent_name: Optional[str] = None

    call_type: Optional[str] = None

    callback_for: Optional[str] = None

    direction: Optional[str] = None

    duration_seconds: Optional[int] = None

    ended_at: Optional[str] = None

    from_number: Optional[str] = None

    initial_agent_id: Optional[str] = None

    prospect_external_id: Optional[str] = None

    prospect_first_name: Optional[str] = None

    prospect_id: Optional[str] = None

    prospect_last_name: Optional[str] = None

    prospect_phone: Optional[str] = None

    scheduled_at: Optional[str] = None

    started_at: Optional[str] = None

    status: Optional[str] = None

    to_number: Optional[str] = None


class CallListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaCalls] = None
