# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .pagination_meta_evals_postcall import PaginationMetaEvalsPostcall

__all__ = ["AgentListEvalRunsResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None

    agent_id: Optional[str] = None

    call_id: Optional[str] = None

    created_at: Optional[str] = None

    eval_id: Optional[int] = None

    eval_title: Optional[str] = None

    has_passed: Optional[bool] = None

    org_id: Optional[str] = None

    reasoning: Optional[str] = None


class AgentListEvalRunsResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaEvalsPostcall] = None
