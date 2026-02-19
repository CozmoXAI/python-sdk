# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .agent_tool import AgentTool

__all__ = ["ToolListResponse"]

ToolListResponse: TypeAlias = List[AgentTool]
