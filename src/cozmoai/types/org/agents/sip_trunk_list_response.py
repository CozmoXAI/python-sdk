# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["SipTrunkListResponse", "SipTrunkListResponseItem"]


class SipTrunkListResponseItem(BaseModel):
    id: Optional[str] = None

    is_active: Optional[bool] = None

    name: Optional[str] = None

    provider: Optional[str] = None

    type: Optional[str] = None


SipTrunkListResponse: TypeAlias = List[SipTrunkListResponseItem]
