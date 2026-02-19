# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    end_date: str
    """Filter by end date (ISO 8601)"""

    invoice_status: SequenceNotStr[str]
    """Filter by invoice status (DRAFT, FINALIZED, VOIDED)"""

    page: int
    """Page number"""

    payment_status: SequenceNotStr[str]
    """Filter by payment status (INITIATED, PENDING, SUCCEEDED, etc.)"""

    per_page: int
    """Items per page"""

    start_date: str
    """Filter by start date (ISO 8601)"""
