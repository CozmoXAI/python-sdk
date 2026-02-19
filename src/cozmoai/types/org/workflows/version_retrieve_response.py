# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["VersionRetrieveResponse"]


class VersionRetrieveResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    created_by: Optional[str] = None

    definition: Optional[List[int]] = None

    version: Optional[int] = None

    workflow_id: Optional[str] = None
