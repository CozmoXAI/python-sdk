# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .numeric import Numeric
from ..._models import BaseModel

__all__ = ["BillingGetBalanceResponse"]


class BillingGetBalanceResponse(BaseModel):
    billing_tier_id: Optional[str] = None

    credits_balance: Optional[Numeric] = None
