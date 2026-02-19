# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EvalCreateParams"]


class EvalCreateParams(TypedDict, total=False):
    agent_id: Required[str]

    category: Required[str]

    prompt: Required[str]

    score: Required[int]

    title: Required[str]
