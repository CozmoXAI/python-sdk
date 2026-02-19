# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ListResponse"]


class ListResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    deleted_at: Optional[str] = None

    name: Optional[str] = None

    prospect_count: Optional[int] = None

    source: Optional[str] = None
