from __future__ import annotations

from typing import Optional

import pydantic

from .._models import BaseModel

__all__ = ["AgentSessionStartResponse"]


class AgentSessionStartResponse(BaseModel):
    session_id: Optional[str] = pydantic.Field(None, alias="sessionId")
    """UUID of the started session."""
