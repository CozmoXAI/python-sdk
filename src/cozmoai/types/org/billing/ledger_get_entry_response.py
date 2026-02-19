# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..numeric import Numeric
from ...._models import BaseModel

__all__ = ["LedgerGetEntryResponse", "UsageBreakdown"]


class UsageBreakdown(BaseModel):
    id: Optional[str] = None

    applied_unit_price: Optional[Numeric] = None

    created_at: Optional[str] = None

    product_name: Optional[str] = None

    product_type: Optional[str] = None

    quantity: Optional[Numeric] = None

    total_cost: Optional[Numeric] = None

    unit_type: Optional[str] = None


class LedgerGetEntryResponse(BaseModel):
    id: Optional[str] = None

    amount: Optional[Numeric] = None

    balance_after: Optional[Numeric] = None

    call_id: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    event_type: Optional[str] = None

    external_provider: Optional[str] = None

    external_transaction_id: Optional[str] = None

    idempotency_key: Optional[str] = None

    is_reversal: Optional[bool] = None

    last_sync_error: Optional[str] = None

    payment_provider_id: Optional[str] = None

    reversal_of_id: Optional[str] = None

    sync_status: Optional[str] = None

    synced_at: Optional[str] = None

    usage_breakdown: Optional[List[UsageBreakdown]] = None
