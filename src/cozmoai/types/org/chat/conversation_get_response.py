# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ConversationGetResponse", "Message"]


class Message(BaseModel):
    id: Optional[str] = None

    content: Optional[str] = None

    created_at: Optional[str] = None

    role: Optional[str] = None


class ConversationGetResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    messages: Optional[List[Message]] = None

    title: Optional[str] = None

    updated_at: Optional[str] = None
