# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ToolResponse", "Parameter"]


class Parameter(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    position: Optional[int] = None

    required: Optional[bool] = None

    type: Optional[str] = None


class ToolResponse(BaseModel):
    id: Optional[str] = None

    body: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    filler_phrases: Optional[List[str]] = None

    headers: Optional[List[int]] = None

    method: Optional[str] = None

    name: Optional[str] = None

    parameters: Optional[List[Parameter]] = None

    updated_at: Optional[str] = None

    url: Optional[str] = None
