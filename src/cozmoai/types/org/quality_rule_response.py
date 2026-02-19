# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["QualityRuleResponse"]


class QualityRuleResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    is_active: Optional[bool] = None

    is_global: Optional[bool] = None

    key: Optional[str] = None

    organization_id: Optional[str] = None

    penalty: Optional[int] = None

    prompt: Optional[str] = None

    updated_at: Optional[str] = None
