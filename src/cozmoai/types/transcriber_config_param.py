# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TranscriberConfigParam"]


class TranscriberConfigParam(TypedDict, total=False):
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
