# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BulkOperationResponseProspects"]


class BulkOperationResponseProspects(BaseModel):
    affected_ids: Optional[List[str]] = None

    count: Optional[int] = None
