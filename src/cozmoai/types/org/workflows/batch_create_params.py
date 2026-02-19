# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    org_id: Required[str]

    name: Required[str]

    prospect_ids: SequenceNotStr[str]

    prospect_list_id: str

    scheduled_at: str
