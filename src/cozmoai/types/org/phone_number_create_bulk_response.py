# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .phone_number_response import PhoneNumberResponse

__all__ = ["PhoneNumberCreateBulkResponse"]


class PhoneNumberCreateBulkResponse(BaseModel):
    count: Optional[int] = None

    created: Optional[List[PhoneNumberResponse]] = None
