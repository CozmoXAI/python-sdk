# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .unit_test import UnitTest
from ...._models import BaseModel
from .pagination_meta_unit_tests import PaginationMetaUnitTests

__all__ = ["UnitTestListResponse"]


class UnitTestListResponse(BaseModel):
    data: Optional[List[UnitTest]] = None

    meta: Optional[PaginationMetaUnitTests] = None
