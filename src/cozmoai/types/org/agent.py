# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .agents.agent_tool import AgentTool

__all__ = ["Agent"]


class Agent(BaseModel):
    id: Optional[str] = None

    allowed_sip_trunks: Optional[List[str]] = None

    background_sound: Optional[List[int]] = None

    created_at: Optional[str] = None

    goodbye_config: Optional[List[int]] = None

    greeting_config: Optional[List[int]] = None

    llm_config: Optional[List[int]] = None

    name: Optional[str] = None

    organization_id: Optional[str] = None

    plugins: Optional[List[int]] = None

    precall_webhook: Optional[List[int]] = None

    prompt_template: Optional[str] = None

    tools: Optional[List[AgentTool]] = None

    transcriber_config: Optional[List[int]] = None

    type: Optional[str] = None

    updated_at: Optional[str] = None

    vad_config: Optional[List[int]] = None

    voice_config: Optional[List[int]] = None
