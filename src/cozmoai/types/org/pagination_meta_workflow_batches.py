# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PaginationMetaWorkflowBatches"]


class PaginationMetaWorkflowBatches(BaseModel):
    limit: Optional[int] = None

    page: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None
