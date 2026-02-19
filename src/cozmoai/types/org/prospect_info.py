# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProspectInfo"]


class ProspectInfo(BaseModel):
    email: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    phone: Optional[str] = None
