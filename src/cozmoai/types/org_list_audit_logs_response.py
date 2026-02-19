# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OrgListAuditLogsResponse", "Data", "Meta"]


class Data(BaseModel):
    action: Optional[str] = None

    created_at: Optional[str] = None

    organization_id: Optional[str] = None

    resource_id: Optional[str] = None

    resource_type: Optional[str] = None

    user_id: Optional[str] = None


class Meta(BaseModel):
    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class OrgListAuditLogsResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
