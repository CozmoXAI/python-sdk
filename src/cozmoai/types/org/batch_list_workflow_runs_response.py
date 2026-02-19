# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .run_response import RunResponse
from .pagination_meta_workflow_batches import PaginationMetaWorkflowBatches

__all__ = ["BatchListWorkflowRunsResponse"]


class BatchListWorkflowRunsResponse(BaseModel):
    data: Optional[List[RunResponse]] = None

    pagination: Optional[PaginationMetaWorkflowBatches] = None
