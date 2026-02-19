# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["BulkUpdateParams", "Updates"]


class BulkUpdateParams(TypedDict, total=False):
    prospect_ids: Required[SequenceNotStr[str]]

    updates: Required[Updates]


class Updates(TypedDict, total=False):
    country: str

    custom_data: Dict[str, object]

    email: str

    external_id: str

    first_name: str

    last_name: str

    list_id: str

    remove_from_list: bool
    """Explicit flag to set list_id to NULL"""

    status: str

    timezone: str
