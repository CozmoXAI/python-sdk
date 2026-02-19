# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CallCreateDashboardCallResponse"]


class CallCreateDashboardCallResponse(BaseModel):
    call_id: Optional[str] = None

    created_at: Optional[str] = None

    from_number: Optional[str] = None

    prospect_id: Optional[str] = None

    status: Optional[str] = None

    to_number: Optional[str] = None
