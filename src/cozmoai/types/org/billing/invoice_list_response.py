# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .pagination_meta_billing import PaginationMetaBilling

__all__ = ["InvoiceListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    amount: Optional[str] = None

    amount_due: Optional[str] = None

    amount_paid: Optional[str] = None

    amount_remaining: Optional[str] = None

    billing_period: Optional[str] = None

    billing_reason: Optional[str] = None

    created_at: Optional[str] = None

    currency: Optional[str] = None

    customer_id: Optional[str] = None

    description: Optional[str] = None

    due_date: Optional[str] = None

    finalized_at: Optional[str] = None

    invoice_number: Optional[str] = None

    invoice_pdf_url: Optional[str] = None

    line_items_count: Optional[int] = None
    """Summary fields"""

    paid_at: Optional[str] = None

    payment_status: Optional[str] = None

    period_end: Optional[str] = None

    period_start: Optional[str] = None

    status: Optional[str] = None

    subscription_id: Optional[str] = None

    subtotal: Optional[str] = None

    total: Optional[str] = None

    total_discount: Optional[str] = None

    total_tax: Optional[str] = None

    type: Optional[str] = None


class InvoiceListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaBilling] = None
