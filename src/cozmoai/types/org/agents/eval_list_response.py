# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .eval import Eval
from ...._models import BaseModel
from ..pagination_meta_evals_postcall import PaginationMetaEvalsPostcall

__all__ = ["EvalListResponse"]


class EvalListResponse(BaseModel):
    data: Optional[List[Eval]] = None

    meta: Optional[PaginationMetaEvalsPostcall] = None
