from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentSessionCreateParams", "NewProspect"]


class AgentSessionCreateParams(TypedDict, total=False):
    prospect_id: str
    """UUID of an existing prospect to associate with the session. Mutually exclusive with new_prospect."""

    new_prospect: NewProspect
    """Inline prospect to create and associate with the session. Mutually exclusive with prospect_id."""

    root_agent_id: str
    """UUID of the agent to run in this session."""

    title: str
    """Title for the session."""

    channel: str
    """Communication channel."""

    entrypoint: str
    """Entry point description."""

    workflow_run_id: str
    """UUID of an associated workflow run."""

    call_id: str
    """UUID of an associated call."""


class NewProspect(TypedDict, total=False):
    phone: Required[str]
    """Phone number in E.164 format."""

    first_name: str

    last_name: str

    email: str

    external_id: str
