# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .phone_number_response import PhoneNumberResponse
from .pagination_meta_telephony import PaginationMetaTelephony

__all__ = ["PhoneNumberListResponse"]


class PhoneNumberListResponse(BaseModel):
    data: Optional[List[PhoneNumberResponse]] = None

    meta: Optional[PaginationMetaTelephony] = None
