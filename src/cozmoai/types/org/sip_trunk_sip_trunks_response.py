# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .sip_trunk_response import SipTrunkResponse
from .phone_number_response import PhoneNumberResponse

__all__ = ["SipTrunkSipTrunksResponse"]


class SipTrunkSipTrunksResponse(BaseModel):
    inbound_trunk: Optional[SipTrunkResponse] = None

    outbound_trunk: Optional[SipTrunkResponse] = None

    phone_numbers: Optional[List[PhoneNumberResponse]] = None
