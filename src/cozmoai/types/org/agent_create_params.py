# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .goodbye_config_param import GoodbyeConfigParam
from .recall_webhook_param import RecallWebhookParam
from .background_sound_config_param import BackgroundSoundConfigParam

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    name: Required[str]

    prompt_template: Required[str]

    type: Required[Literal["voice", "chat", "video"]]

    allowed_sip_trunks: SequenceNotStr[str]

    background_sound: BackgroundSoundConfigParam

    goodbye_config: GoodbyeConfigParam

    greeting_config: Dict[str, object]

    llm_config: Dict[str, object]

    plugins: Iterable[object]

    precall_webhook: RecallWebhookParam

    transcriber_config: Dict[str, object]

    vad_config: Dict[str, object]

    voice_config: Dict[str, object]
