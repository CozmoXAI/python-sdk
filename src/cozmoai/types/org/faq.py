# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Faq"]


class Faq(BaseModel):
    id: Optional[str] = None

    answer: Optional[str] = None

    created_at: Optional[str] = None

    instruction: Optional[str] = None

    logic: Optional[str] = None

    question: Optional[str] = None

    updated_at: Optional[str] = None
