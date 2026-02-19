# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .call_tool_log import CallToolLog

__all__ = ["CallGetToolLogsResponse"]

CallGetToolLogsResponse: TypeAlias = List[CallToolLog]
