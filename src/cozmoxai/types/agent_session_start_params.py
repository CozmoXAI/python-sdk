from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentSessionStartParams"]


class AgentSessionStartParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]
    """UUID of the agent to run. Required."""

    instruction: Required[str]
    """The user instruction / initial message to send to the agent. Required."""

    title: str
    """Title for the session. Defaults to the first 100 chars of instruction."""

    source: str
    """Source identifier. Defaults to 'command-center'."""

    prospect_id: Annotated[str, PropertyInfo(alias="prospectId")]
    """UUID of a prospect to associate with this session."""
