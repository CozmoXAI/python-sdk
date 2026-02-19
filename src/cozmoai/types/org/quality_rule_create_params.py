# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QualityRuleCreateParams"]


class QualityRuleCreateParams(TypedDict, total=False):
    key: Required[str]

    penalty: Required[int]

    prompt: Required[str]

    is_active: bool
