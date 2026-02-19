# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DeleteListResponse"]


class DeleteListResponse(BaseModel):
    message: Optional[str] = None

    prospects_deleted_count: Optional[int] = None

    status: Optional[str] = None
