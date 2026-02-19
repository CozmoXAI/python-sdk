# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["MeListOrganizationsResponse", "MeListOrganizationsResponseItem"]


class MeListOrganizationsResponseItem(BaseModel):
    id: Optional[str] = None

    joined_at: Optional[str] = None

    name: Optional[str] = None

    role: Optional[str] = None

    slug: Optional[str] = None


MeListOrganizationsResponse: TypeAlias = List[MeListOrganizationsResponseItem]
