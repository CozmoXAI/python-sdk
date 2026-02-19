# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["APIKeyUpdateAPIKeyScopesParams"]


class APIKeyUpdateAPIKeyScopesParams(TypedDict, total=False):
    org_id: Required[str]

    scopes: Required[SequenceNotStr[str]]
