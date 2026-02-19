# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["CallListCallsByHourResponse", "CallListCallsByHourResponseItem"]


class CallListCallsByHourResponseItem(BaseModel):
    avg_duration: Optional[float] = None

    call_count: Optional[int] = None

    hour_utc: Optional[int] = None


CallListCallsByHourResponse: TypeAlias = List[CallListCallsByHourResponseItem]
