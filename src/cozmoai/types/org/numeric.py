# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Numeric"]


class Numeric(BaseModel):
    exp: Optional[int] = None

    infinity_modifier: Optional[Literal[1, 0, -1]] = FieldInfo(alias="infinityModifier", default=None)

    int: Optional[object] = None

    na_n: Optional[bool] = FieldInfo(alias="naN", default=None)

    valid: Optional[bool] = None
