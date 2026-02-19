# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CallEvaluation"]


class CallEvaluation(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    extracted_value: Optional[str] = None

    outcome_definition_id: Optional[str] = None

    outcome_key: Optional[str] = None

    reasoning: Optional[str] = None

    result_boolean: Optional[bool] = None
