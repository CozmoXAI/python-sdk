# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .numeric import Numeric
from ..._models import BaseModel

__all__ = ["BillingGetSummaryResponse", "DailyReport"]


class DailyReport(BaseModel):
    call_count: Optional[int] = None

    charges: Optional[Numeric] = None

    credits: Optional[Numeric] = None

    date: Optional[str] = None


class BillingGetSummaryResponse(BaseModel):
    credits_this_month: Optional[Numeric] = None

    current_balance: Optional[Numeric] = None

    daily_report: Optional[List[DailyReport]] = None

    usage_this_month: Optional[Numeric] = None
