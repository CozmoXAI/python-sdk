# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .agents_thinking_sound_param import AgentsThinkingSoundParam

__all__ = ["BackgroundSoundConfigParam"]


class BackgroundSoundConfigParam(TypedDict, total=False):
    file: Required[str]

    enabled: bool

    initial_volume: float

    thinking_sound: Iterable[AgentsThinkingSoundParam]

    volume: float
