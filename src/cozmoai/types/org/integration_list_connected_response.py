# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .connected_integration_response import ConnectedIntegrationResponse

__all__ = ["IntegrationListConnectedResponse"]


class IntegrationListConnectedResponse(BaseModel):
    data: Optional[List[ConnectedIntegrationResponse]] = None
