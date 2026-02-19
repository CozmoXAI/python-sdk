# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .prospect_info import ProspectInfo

__all__ = ["RunResponse"]


class RunResponse(BaseModel):
    id: Optional[str] = None

    batch_id: Optional[str] = None

    current_step_id: Optional[str] = None

    ended_at: Optional[str] = None

    prospect: Optional[ProspectInfo] = None

    prospect_id: Optional[str] = None

    started_at: Optional[str] = None

    status: Optional[str] = None

    workflow_id: Optional[str] = None

    workflow_version_id: Optional[str] = None
