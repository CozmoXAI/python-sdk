# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ExportGetCountResponse"]


class ExportGetCountResponse(BaseModel):
    count: Optional[int] = None

    limited: Optional[bool] = None
    """true if count > 10000"""

    message: Optional[str] = None
