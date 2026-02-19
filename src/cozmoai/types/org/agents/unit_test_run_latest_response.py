# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .pagination_meta_unit_tests import PaginationMetaUnitTests

__all__ = ["UnitTestRunLatestResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    agent_id: Optional[str] = None

    answer_prompt: Optional[str] = None

    batch_id: Optional[str] = None

    created_at: Optional[str] = None

    details: Optional[str] = None

    is_success: Optional[bool] = None

    organization_id: Optional[str] = None

    question_prompt: Optional[str] = None

    run_at: Optional[str] = None

    test_title: Optional[str] = None

    title: Optional[str] = None

    unit_test_id: Optional[str] = None


class UnitTestRunLatestResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaUnitTests] = None
