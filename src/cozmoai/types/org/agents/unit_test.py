# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["UnitTest"]


class UnitTest(BaseModel):
    id: Optional[str] = None

    agent_id: Optional[str] = None

    answer_prompt: Optional[str] = None

    created_at: Optional[str] = None

    function_tool_assertion: Optional[str] = None

    organization_id: Optional[str] = None

    question_prompt: Optional[str] = None

    question_variance: Optional[str] = None

    title: Optional[str] = None

    updated_at: Optional[str] = None

    yaml_config: Optional[str] = None
