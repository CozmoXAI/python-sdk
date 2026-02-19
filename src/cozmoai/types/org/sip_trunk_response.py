# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SipTrunkResponse"]


class SipTrunkResponse(BaseModel):
    id: Optional[str] = None

    is_active: Optional[bool] = None

    max_concurrency: Optional[int] = None

    name: Optional[str] = None

    phone_count: Optional[int] = None

    provider: Optional[str] = None

    type: Optional[str] = None
