# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .sip_trunk_response import SipTrunkResponse
from .pagination_meta_telephony import PaginationMetaTelephony

__all__ = ["SipTrunkRetrieveSipTrunksResponse"]


class SipTrunkRetrieveSipTrunksResponse(BaseModel):
    data: Optional[List[SipTrunkResponse]] = None

    meta: Optional[PaginationMetaTelephony] = None
