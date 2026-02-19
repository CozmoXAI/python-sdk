# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["Eval"]


class Eval(BaseModel):
    id: Optional[int] = None

    agent_id: Optional[str] = None

    category: Optional[str] = None

    created_at: Optional[str] = None

    org_id: Optional[str] = None

    prompt: Optional[str] = None

    score: Optional[int] = None

    title: Optional[str] = None
