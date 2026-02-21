# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .llm_config_param import LlmConfigParam
from .vad_config_param import VadConfigParam
from .extra_config_param import ExtraConfigParam
from .voice_config_param import VoiceConfigParam
from .goodbye_config_param import GoodbyeConfigParam
from .greeting_config_param import GreetingConfigParam
from .transcriber_config_param import TranscriberConfigParam
from .room_duration_config_param import RoomDurationConfigParam
from .background_sound_config_param import BackgroundSoundConfigParam

__all__ = ["AgentUpdateParams", "PrecallWebhook"]


class AgentUpdateParams(TypedDict, total=False):
    allowed_sip_trunks: SequenceNotStr[str]

    background_sound: BackgroundSoundConfigParam

    extra_config: ExtraConfigParam

    goodbye_config: GoodbyeConfigParam

    greeting_config: GreetingConfigParam

    llm_config: LlmConfigParam

    name: str

    plugins: Iterable[object]

    precall_webhook: PrecallWebhook

    prompt_template: str

    room_duration_config: RoomDurationConfigParam

    transcriber_config: TranscriberConfigParam

    type: Literal["voice", "chat", "video"]

    vad_config: VadConfigParam

    voice_config: VoiceConfigParam


class PrecallWebhook(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "PATCH"]]

    url: Required[str]

    body_template: Dict[str, object]

    headers: Dict[str, str]

    timeout_seconds: int
