# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["AgentTool", "Parameter"]


class Parameter(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    type: Optional[str] = None


class AgentTool(BaseModel):
    config_override: Optional[Dict[str, object]] = None

    description: Optional[str] = None

    is_enabled: Optional[bool] = None

    method: Optional[str] = None

    name: Optional[str] = None

    parameters: Optional[List[Parameter]] = None

    tool_id: Optional[str] = None

    url: Optional[str] = None
