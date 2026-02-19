# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .tag_response_tag import TagResponseTag

__all__ = ["TagListResponse"]


class TagListResponse(BaseModel):
    data: Optional[List[TagResponseTag]] = None
