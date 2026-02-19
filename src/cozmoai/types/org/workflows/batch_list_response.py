# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ..batch_response import BatchResponse
from ..pagination_meta_workflow_batches import PaginationMetaWorkflowBatches

__all__ = ["BatchListResponse"]


class BatchListResponse(BaseModel):
    data: Optional[List[BatchResponse]] = None

    pagination: Optional[PaginationMetaWorkflowBatches] = None
