# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["AgentResponse", "Tool", "ToolParameter"]


class ToolParameter(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    type: Optional[str] = None


class Tool(BaseModel):
    config_override: Optional[Dict[str, object]] = None

    description: Optional[str] = None

    is_enabled: Optional[bool] = None

    method: Optional[str] = None

    name: Optional[str] = None

    parameters: Optional[List[ToolParameter]] = None

    tool_id: Optional[str] = None

    url: Optional[str] = None


class AgentResponse(BaseModel):
    id: Optional[str] = None

    allowed_sip_trunks: Optional[List[str]] = None

    background_sound: Optional[List[int]] = None

    created_at: Optional[str] = None

    extra_config: Optional[List[int]] = None

    goodbye_config: Optional[List[int]] = None

    greeting_config: Optional[List[int]] = None

    llm_config: Optional[List[int]] = None

    name: Optional[str] = None

    organization_id: Optional[str] = None

    plugins: Optional[List[int]] = None

    precall_webhook: Optional[List[int]] = None

    prompt_template: Optional[str] = None

    public_quota: Optional[int] = None

    room_duration_config: Optional[List[int]] = None

    tools: Optional[List[Tool]] = None

    transcriber_config: Optional[List[int]] = None

    type: Optional[str] = None

    updated_at: Optional[str] = None

    vad_config: Optional[List[int]] = None

    voice_config: Optional[List[int]] = None
