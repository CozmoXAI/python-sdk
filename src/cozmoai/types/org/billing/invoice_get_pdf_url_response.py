# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["InvoiceGetPdfURLResponse"]


class InvoiceGetPdfURLResponse(BaseModel):
    invoice_id: Optional[str] = None

    pdf_url: Optional[str] = None
