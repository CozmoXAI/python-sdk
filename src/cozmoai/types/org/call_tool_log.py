# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CallToolLog"]


class CallToolLog(BaseModel):
    id: Optional[str] = None

    arguments: Optional[List[int]] = None

    created_at: Optional[str] = None

    error_message: Optional[str] = None

    result: Optional[List[int]] = None

    status: Optional[str] = None

    tool_name: Optional[str] = None
