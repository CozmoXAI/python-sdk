# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VoiceConfigParam"]


class VoiceConfigParam(TypedDict, total=False):
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
