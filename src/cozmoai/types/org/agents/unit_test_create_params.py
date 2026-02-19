# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UnitTestCreateParams"]


class UnitTestCreateParams(TypedDict, total=False):
    org_id: Required[str]

    answer_prompt: Required[str]

    question_prompt: Required[str]

    question_variance: Required[Literal["low", "med", "high"]]

    function_tool_assertion: str

    title: str

    yaml_config: str
