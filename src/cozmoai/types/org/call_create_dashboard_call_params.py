# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["CallCreateDashboardCallParams"]


class CallCreateDashboardCallParams(TypedDict, total=False):
    agent_id: Required[str]

    from_number: Required[str]

    phone_number: Required[str]

    extras: Dict[str, str]
    """first_name, last_name, email, etc."""
