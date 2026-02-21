# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentsThinkingSoundParam"]


class AgentsThinkingSoundParam(TypedDict, total=False):
    sound: Required[str]

    probability: float

    volume: float
