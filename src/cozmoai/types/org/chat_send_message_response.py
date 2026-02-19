# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ChatSendMessageResponse"]


class ChatSendMessageResponse(BaseModel):
    conversation_id: Optional[str] = None

    message_id: Optional[str] = None

    response: Optional[str] = None

    tools_used: Optional[List[str]] = None
