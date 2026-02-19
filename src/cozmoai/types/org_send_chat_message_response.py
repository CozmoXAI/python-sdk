# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OrgSendChatMessageResponse"]


class OrgSendChatMessageResponse(BaseModel):
    data: Optional[object] = None

    event: Optional[str] = None
