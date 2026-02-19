# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MemberListResponse", "Member"]


class Member(BaseModel):
    email: Optional[str] = None

    joined_at: Optional[str] = None

    organization_id: Optional[str] = None

    role: Optional[str] = None

    user_id: Optional[str] = None


class MemberListResponse(BaseModel):
    members: Optional[List[Member]] = None
