# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvoiceGetPdfURLParams"]


class InvoiceGetPdfURLParams(TypedDict, total=False):
    invoice_id: Required[str]
    """Invoice ID"""

    url: str
    """Return URL (optional)"""
