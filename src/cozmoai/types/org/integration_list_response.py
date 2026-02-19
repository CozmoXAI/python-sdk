# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["IntegrationListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    connected_at: Optional[str] = None

    is_active: Optional[bool] = None

    is_connected: Optional[bool] = None

    name: Optional[str] = None

    organization_integration_id: Optional[str] = None

    schema_config: Optional[List[int]] = None

    slug: Optional[str] = None


class IntegrationListResponse(BaseModel):
    data: Optional[List[Data]] = None
