# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ListProspectOperationResponse"]


class ListProspectOperationResponse(BaseModel):
    affected_count: Optional[int] = None

    message: Optional[str] = None

    status: Optional[str] = None
