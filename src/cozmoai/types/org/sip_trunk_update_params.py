# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SipTrunkUpdateParams"]


class SipTrunkUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    is_active: bool

    max_concurrency: int

    name: str
