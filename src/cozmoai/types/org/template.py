# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Template"]


class Template(BaseModel):
    id: Optional[str] = None

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    created_at: Optional[str] = None

    name: Optional[str] = None

    subject: Optional[str] = None

    updated_at: Optional[str] = None
