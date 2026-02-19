# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UnitTestUpdateParams"]


class UnitTestUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    agent_id: Required[str]

    answer_prompt: str

    function_tool_assertion: str

    question_prompt: str

    question_variance: Literal["low", "med", "high"]

    title: str

    yaml_config: str
