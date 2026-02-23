# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VadConfigParam"]


class VadConfigParam(TypedDict, total=False):
    activation_threshold: float

    max_buffered_speech: int

    min_silence_duration: float

    min_speech_duration: float

    prefix_padding_duration: float

    sample_rate: int
