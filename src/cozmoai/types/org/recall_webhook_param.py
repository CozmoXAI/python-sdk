# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RecallWebhookParam"]


class RecallWebhookParam(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "PATCH"]]

    url: Required[str]

    body_template: Dict[str, object]

    headers: Dict[str, str]

    timeout_seconds: int
