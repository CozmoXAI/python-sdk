# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OrgListVoicesResponse", "Meta", "Voice"]


class Meta(BaseModel):
    has_more: Optional[bool] = None

    next_page: Optional[str] = None
    """Cursor for next page (cartesia, elevenlabs)"""

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None
    """May not be available with cursor pagination"""

    total_pages: Optional[int] = None
    """May not be available with cursor pagination"""


class Voice(BaseModel):
    id: Optional[str] = None

    accent: Optional[str] = None

    age: Optional[str] = None

    category: Optional[str] = None

    description: Optional[str] = None

    gender: Optional[str] = None

    language: Optional[str] = None

    model: Optional[str] = None

    name: Optional[str] = None

    preview_url: Optional[str] = None

    provider: Optional[str] = None
    """\"elevenlabs", "cartesia", "openai", "cambai", "sarvam", "inworld", "minimax" """

    use_case: Optional[str] = None


class OrgListVoicesResponse(BaseModel):
    meta: Optional[Meta] = None

    voices: Optional[List[Voice]] = None
