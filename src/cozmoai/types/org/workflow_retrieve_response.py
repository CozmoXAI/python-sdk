# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["WorkflowRetrieveResponse"]


class WorkflowRetrieveResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    definition: Optional[List[int]] = None

    description: Optional[str] = None

    is_active: Optional[bool] = None

    name: Optional[str] = None

    published_at: Optional[str] = None

    trigger_type: Optional[str] = None

    updated_at: Optional[str] = None

    version: Optional[int] = None
