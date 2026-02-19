# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OutcomeDefinition"]


class OutcomeDefinition(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    display_name: Optional[str] = None

    is_unique_per_call: Optional[bool] = None

    key: Optional[str] = None

    organization_id: Optional[str] = None

    value_type: Optional[str] = None
