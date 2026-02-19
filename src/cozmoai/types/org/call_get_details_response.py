# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .call_tool_log import CallToolLog
from .call_evaluation import CallEvaluation

__all__ = ["CallGetDetailsResponse"]


class CallGetDetailsResponse(BaseModel):
    id: Optional[str] = None

    agent_name: Optional[str] = None

    cost_usd: Optional[str] = None

    detected_intents: Optional[List[str]] = None

    direction: Optional[str] = None

    duration_seconds: Optional[int] = None

    ended_at: Optional[str] = None

    evaluations: Optional[List[CallEvaluation]] = None
    """Related data"""

    from_number: Optional[str] = None

    initial_agent_id: Optional[str] = None

    organization_id: Optional[str] = None

    participating_agent_ids: Optional[List[str]] = None

    prospect_email: Optional[str] = None

    prospect_external_id: Optional[str] = None

    prospect_first_name: Optional[str] = None

    prospect_id: Optional[str] = None

    prospect_last_name: Optional[str] = None

    prospect_phone: Optional[str] = None

    recording_analysis: Optional[List[int]] = None

    recording_slug: Optional[str] = None

    recording_url: Optional[str] = None

    scheduled_at: Optional[str] = None

    selected_outbound_number_id: Optional[str] = None

    sip_trunk_id: Optional[str] = None

    started_at: Optional[str] = None

    status: Optional[str] = None

    stt_duration_seconds: Optional[int] = None

    telephony_code: Optional[int] = None

    to_number: Optional[str] = None

    tokens_input: Optional[int] = None

    tokens_output: Optional[int] = None

    tool_logs: Optional[List[CallToolLog]] = None

    transcript_text: Optional[str] = None
    """Transcript summary (null if call has no transcript yet)"""

    tts_characters: Optional[int] = None

    workflow_node_id: Optional[str] = None

    workflow_run_id: Optional[str] = None

    workflow_version_id: Optional[str] = None
