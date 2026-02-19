# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CallGetTranscriptResponse"]


class CallGetTranscriptResponse(BaseModel):
    id: Optional[str] = None

    cost_usd: Optional[str] = None

    duration_seconds: Optional[int] = None

    ended_at: Optional[str] = None

    messages: Optional[List[int]] = None

    started_at: Optional[str] = None

    status: Optional[str] = None

    stt_duration_seconds: Optional[int] = None

    tokens_input: Optional[int] = None

    tokens_output: Optional[int] = None

    transcript_text: Optional[str] = None

    tts_characters: Optional[int] = None
