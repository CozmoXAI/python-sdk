# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ConversationListResponse", "Conversation"]


class Conversation(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    title: Optional[str] = None

    updated_at: Optional[str] = None


class ConversationListResponse(BaseModel):
    conversations: Optional[List[Conversation]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None
