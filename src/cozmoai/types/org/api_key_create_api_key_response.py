# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["APIKeyCreateAPIKeyResponse"]


class APIKeyCreateAPIKeyResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    expires_at: Optional[str] = None

    key: Optional[str] = None
    """Only returned once on creation"""

    name: Optional[str] = None

    scopes: Optional[List[str]] = None
