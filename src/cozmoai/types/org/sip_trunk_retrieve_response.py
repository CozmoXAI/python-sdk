# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .phone_number_response import PhoneNumberResponse

__all__ = ["SipTrunkRetrieveResponse"]


class SipTrunkRetrieveResponse(BaseModel):
    id: Optional[str] = None

    is_active: Optional[bool] = None

    max_concurrency: Optional[int] = None

    name: Optional[str] = None

    phone_numbers: Optional[List[PhoneNumberResponse]] = None

    provider: Optional[str] = None

    type: Optional[str] = None
