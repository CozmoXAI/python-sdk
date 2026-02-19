# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["PaginationMetaUnitTests"]


class PaginationMetaUnitTests(BaseModel):
    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None
