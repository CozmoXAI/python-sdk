# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RoomDurationConfigParam"]


class RoomDurationConfigParam(TypedDict, total=False):
    close_room_message: str

    duration_warning_message: str

    max_duration_min: int

    max_silence_sec: int

    silence_message: str

    wait_for_message_sec: int
