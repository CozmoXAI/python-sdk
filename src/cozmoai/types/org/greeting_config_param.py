# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GreetingConfigParam"]


class GreetingConfigParam(TypedDict, total=False):
    agent_speaks_first: bool

    greeting: str

    pause_before_first_message: int

    voice_mail_message: str

    welcome_message_is_generated: bool
