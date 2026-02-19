# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TagResponseTag"]


class TagResponseTag(BaseModel):
    id: Optional[str] = None

    color: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    prospect_count: Optional[int] = None
