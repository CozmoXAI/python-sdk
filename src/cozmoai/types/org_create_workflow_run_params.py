# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["OrgCreateWorkflowRunParams", "Prospect"]


class OrgCreateWorkflowRunParams(TypedDict, total=False):
    prospect: Required[Prospect]

    workflow_id: Required[str]

    scheduled_at: str


class Prospect(TypedDict, total=False):
    phone: Required[str]

    country: str

    custom_data: Dict[str, object]

    email: str

    external_id: str

    first_name: str

    last_name: str

    timezone: str
