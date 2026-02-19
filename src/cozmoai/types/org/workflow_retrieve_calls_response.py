# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["WorkflowRetrieveCallsResponse", "WorkflowRetrieveCallsResponseItem"]


class WorkflowRetrieveCallsResponseItem(BaseModel):
    id: Optional[str] = None

    duration_seconds: Optional[int] = None

    ended_at: Optional[str] = None

    prospect_id: Optional[str] = None

    started_at: Optional[str] = None

    status: Optional[str] = None

    workflow_run_id: Optional[str] = None


WorkflowRetrieveCallsResponse: TypeAlias = List[WorkflowRetrieveCallsResponseItem]
