# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OrgCreateWorkflowRunResponse"]


class OrgCreateWorkflowRunResponse(BaseModel):
    external_id: Optional[str] = None

    workflow_run_id: Optional[str] = None
