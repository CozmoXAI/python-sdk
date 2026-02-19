# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ResponseError"]


class ResponseError(BaseModel):
    data: Optional[object] = None

    error: Optional[object] = None

    message: Optional[str] = None

    status: Optional[bool] = None
