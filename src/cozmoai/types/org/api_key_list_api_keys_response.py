# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["APIKeyListAPIKeysResponse", "APIKeyListAPIKeysResponseItem"]


class APIKeyListAPIKeysResponseItem(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    expires_at: Optional[str] = None

    key_prefix: Optional[str] = None
    """e.g., "cozmo*live*\\**\\**\\**\\**" """

    last_used_at: Optional[str] = None

    name: Optional[str] = None

    scopes: Optional[List[str]] = None


APIKeyListAPIKeysResponse: TypeAlias = List[APIKeyListAPIKeysResponseItem]
