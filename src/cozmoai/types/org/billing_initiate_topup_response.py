# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BillingInitiateTopupResponse"]


class BillingInitiateTopupResponse(BaseModel):
    redirect_url: Optional[str] = None
