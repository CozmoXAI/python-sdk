# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BackgroundSoundConfigParam", "ThinkingSound"]


class ThinkingSound(TypedDict, total=False):
    sound: Required[str]

    probability: float

    volume: float


class BackgroundSoundConfigParam(TypedDict, total=False):
    file: Required[str]

    enabled: bool

    initial_volume: float

    thinking_sound: Iterable[ThinkingSound]

    volume: float
