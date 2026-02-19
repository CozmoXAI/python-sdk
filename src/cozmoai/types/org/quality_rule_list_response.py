# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .quality_rule_response import QualityRuleResponse

__all__ = ["QualityRuleListResponse", "Meta"]


class Meta(BaseModel):
    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class QualityRuleListResponse(BaseModel):
    data: Optional[List[QualityRuleResponse]] = None

    meta: Optional[Meta] = None
