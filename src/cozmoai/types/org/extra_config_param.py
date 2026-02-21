# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtraConfigParam"]


class ExtraConfigParam(TypedDict, total=False):
    allow_interruptions: bool

    interruption_sensitivity: float

    min_words: int

    turn_detector_enabled: bool

    turn_detector_is_multilingual: bool

    turn_detector_model_type: str
