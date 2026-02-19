# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .goodbye_config_param import GoodbyeConfigParam
from .recall_webhook_param import RecallWebhookParam
from .background_sound_config_param import BackgroundSoundConfigParam

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    allowed_sip_trunks: SequenceNotStr[str]

    background_sound: BackgroundSoundConfigParam

    goodbye_config: GoodbyeConfigParam

    greeting_config: Dict[str, object]

    llm_config: Dict[str, object]

    name: str

    plugins: Iterable[object]

    precall_webhook: RecallWebhookParam

    prompt_template: str

    transcriber_config: Dict[str, object]

    type: Literal["voice", "chat", "video"]

    vad_config: Dict[str, object]

    voice_config: Dict[str, object]
