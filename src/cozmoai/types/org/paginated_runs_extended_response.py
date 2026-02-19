# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .prospect_info import ProspectInfo
from .pagination_meta_workflow_batches import PaginationMetaWorkflowBatches

__all__ = ["PaginatedRunsExtendedResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    batch_id: Optional[str] = None

    batch_name: Optional[str] = None

    current_step_id: Optional[str] = None

    ended_at: Optional[str] = None

    prospect: Optional[ProspectInfo] = None

    prospect_id: Optional[str] = None

    started_at: Optional[str] = None

    status: Optional[str] = None

    workflow_id: Optional[str] = None

    workflow_name: Optional[str] = None

    workflow_version_id: Optional[str] = None


class PaginatedRunsExtendedResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[PaginationMetaWorkflowBatches] = None
