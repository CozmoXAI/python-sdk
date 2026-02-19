# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ProspectUpdateParams"]


class ProspectUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    country: str

    custom_data: Dict[str, object]

    email: str

    external_id: str

    first_name: str

    last_name: str

    list_id: str

    phone: str

    status: str

    timezone: str
