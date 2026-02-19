# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SipTrunkSipTrunksParams"]


class SipTrunkSipTrunksParams(TypedDict, total=False):
    address: Required[str]

    name: Required[str]

    phone_numbers: Required[SequenceNotStr[str]]

    provider: Required[Literal["twilio", "telnyx", "custom", "did-logic", "vonage", "other"]]

    auth_password: str

    auth_username: str

    max_concurrency: int
