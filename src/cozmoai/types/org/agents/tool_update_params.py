# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    agent_id: Required[str]

    config_override: Dict[str, object]

    is_enabled: bool
