# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PhoneNumberResponse"]


class PhoneNumberResponse(BaseModel):
    id: Optional[str] = None

    is_verified: Optional[bool] = None

    label: Optional[str] = None

    number: Optional[str] = None

    provider: Optional[str] = None

    sip_trunk_id: Optional[str] = None

    trunk_name: Optional[str] = None
