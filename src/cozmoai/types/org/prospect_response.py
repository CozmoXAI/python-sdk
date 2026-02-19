# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .tag_response_prospect import TagResponseProspect

__all__ = ["ProspectResponse"]


class ProspectResponse(BaseModel):
    id: Optional[str] = None

    country: Optional[str] = None

    created_at: Optional[str] = None

    custom_data: Optional[Dict[str, object]] = None

    email: Optional[str] = None

    external_id: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    list_id: Optional[str] = None

    phone: Optional[str] = None

    status: Optional[str] = None

    tags: Optional[List[TagResponseProspect]] = None

    timezone: Optional[str] = None

    updated_at: Optional[str] = None
