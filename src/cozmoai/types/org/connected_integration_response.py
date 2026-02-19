# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ConnectedIntegrationResponse"]


class ConnectedIntegrationResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    is_active: Optional[bool] = None

    last_sync_at: Optional[str] = None

    last_sync_error: Optional[str] = None

    last_sync_status: Optional[str] = None

    name: Optional[str] = None

    schema_config: Optional[List[int]] = None

    settings: Optional[List[int]] = None

    slug: Optional[str] = None
