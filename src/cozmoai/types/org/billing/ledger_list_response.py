# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..numeric import Numeric
from ...._models import BaseModel
from .pagination_meta_billing import PaginationMetaBilling

__all__ = ["LedgerListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    amount: Optional[Numeric] = None

    balance_after: Optional[Numeric] = None

    call_id: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    event_type: Optional[str] = None

    external_provider: Optional[str] = None

    is_reversal: Optional[bool] = None

    reversal_of_id: Optional[str] = None

    sync_status: Optional[str] = None


class LedgerListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaBilling] = None
