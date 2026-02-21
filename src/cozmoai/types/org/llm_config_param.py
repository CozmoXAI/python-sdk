# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LlmConfigParam"]


class LlmConfigParam(TypedDict, total=False):
    model: Required[str]

    provider: Required[Literal["openai", "anthropic"]]
    """Core (All Providers)"""

    frequency_penalty: float

    max_tokens: int

    parallel_tool_calls: bool

    presence_penalty: float
    """OpenAI Only"""

    system_prompt: str

    temperature: float
    """Sampling Parameters (All Providers)"""

    top_k: int
    """Anthropic Only"""

    top_p: float
