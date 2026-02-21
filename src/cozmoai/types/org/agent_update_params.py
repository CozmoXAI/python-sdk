# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .goodbye_config_param import GoodbyeConfigParam
from .recall_webhook_param import RecallWebhookParam
from .background_sound_config_param import BackgroundSoundConfigParam

__all__ = [
    "AgentUpdateParams",
    "ExtraConfig",
    "GreetingConfig",
    "LlmConfig",
    "RoomDurationConfig",
    "TranscriberConfig",
    "VadConfig",
    "VoiceConfig",
]


class AgentUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    allowed_sip_trunks: SequenceNotStr[str]

    background_sound: BackgroundSoundConfigParam

    extra_config: ExtraConfig

    goodbye_config: GoodbyeConfigParam

    greeting_config: GreetingConfig

    llm_config: LlmConfig

    name: str

    plugins: Iterable[object]

    precall_webhook: RecallWebhookParam

    prompt_template: str

    room_duration_config: RoomDurationConfig

    transcriber_config: TranscriberConfig

    type: Literal["voice", "chat", "video"]

    vad_config: VadConfig

    voice_config: VoiceConfig


class ExtraConfig(TypedDict, total=False):
    allow_interruptions: bool

    interruption_sensitivity: float

    min_words: int

    turn_detector_enabled: bool

    turn_detector_is_multilingual: bool

    turn_detector_model_type: str


class GreetingConfig(TypedDict, total=False):
    agent_speaks_first: bool

    greeting: str

    pause_before_first_message: int

    voice_mail_message: str

    welcome_message_is_generated: bool


class LlmConfig(TypedDict, total=False):
    model: Required[str]

    provider: Required[Literal["openai", "anthropic"]]
    """Core (All Providers)"""

    frequency_penalty: float

    max_tokens: int

    parallel_tool_calls: bool

    presence_penalty: float
    """OpenAI Only"""

    system_prompt: str

    temperature: float
    """Sampling Parameters (All Providers)"""

    top_k: int
    """Anthropic Only"""

    top_p: float


class RoomDurationConfig(TypedDict, total=False):
    close_room_message: str

    duration_warning_message: str

    max_duration_min: int

    max_silence_sec: int

    silence_message: str

    wait_for_message_sec: int


class TranscriberConfig(TypedDict, total=False):
    provider: Required[Literal["deepgram", "elevenlabs", "speechmatics"]]
    """Core fields (All Providers)"""

    commit_strategy: Literal["manual", "vad"]
    """ElevenLabs Only"""

    detect_language: bool

    eager_eot_threshold: float
    """Unified EOT/VAD Fields"""

    enable_logging: bool

    endpointing: int

    endpointing_ms: int

    energy_filter: bool

    eot_threshold: float

    eot_timeout_ms: int

    filler_words: bool

    include_language_detection: bool

    include_timestamps: bool

    interim_results: bool
    """Deepgram V1 Only"""

    keyterms: SequenceNotStr[str]
    """Deepgram Flux Only"""

    keywords: SequenceNotStr[str]

    language: str
    """Legacy fields (backward compatibility)"""

    language_code: str

    min_speech_duration_ms: int

    model: str

    no_delay: bool

    num_channels: int

    preemptive_generation: bool
    """Preemptive Generation (All Providers)"""

    preemptive_min_confidence: float

    profanity_filter: bool

    punctuate: bool

    sample_rate: int

    smart_format: bool

    vad_events: bool


class VadConfig(TypedDict, total=False):
    activation_threshold: float

    max_buffered_speech: int

    min_silence_duration: float

    min_speech_duration: float

    prefix_padding_duration: float

    sample_rate: int


class VoiceConfig(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    language: str

    sample_rate: int

    similarity_boost: float

    speed: float

    stability: float

    style: float

    use_speaker_boost: bool

    voice_id: str
