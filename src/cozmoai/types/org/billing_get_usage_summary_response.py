# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .numeric import Numeric
from ..._models import BaseModel

__all__ = ["BillingGetUsageSummaryResponse", "Data"]


class Data(BaseModel):
    product_name: Optional[str] = None

    product_type: Optional[str] = None

    total_cost: Optional[Numeric] = None

    total_quantity: Optional[Numeric] = None

    unit_type: Optional[str] = None


class BillingGetUsageSummaryResponse(BaseModel):
    data: Optional[List[Data]] = None

    end_date: Optional[str] = None

    start_date: Optional[str] = None
