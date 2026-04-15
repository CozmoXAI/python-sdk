from __future__ import annotations

from typing import Any, Optional

from .._models import BaseModel

__all__ = ["AgentSessionResponse"]


class AgentSessionResponse(BaseModel):
    id: Optional[str] = None

    organization_id: Optional[str] = None

    root_agent_id: Optional[str] = None

    prospect_id: Optional[str] = None

    workflow_run_id: Optional[str] = None

    call_id: Optional[str] = None

    case_id: Optional[str] = None
    """Auto-generated 6-character alphanumeric case identifier (e.g. 'ABC123')."""

    title: Optional[str] = None

    channel: Optional[str] = None

    entrypoint: Optional[str] = None

    status: Optional[str] = None

    agent_binding: Optional[Any] = None

    bootstrap: Optional[Any] = None

    external_refs: Optional[Any] = None

    metadata: Optional[Any] = None

    last_event_sequence: Optional[int] = None

    last_journal_sequence: Optional[int] = None

    last_handle_version: Optional[int] = None

    last_event_at: Optional[str] = None

    last_activity_at: Optional[str] = None

    started_at: Optional[str] = None

    ended_at: Optional[str] = None

    created_by: Optional[str] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None
