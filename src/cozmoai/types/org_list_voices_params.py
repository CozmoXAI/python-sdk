# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrgListVoicesParams"]


class OrgListVoicesParams(TypedDict, total=False):
    provider: Required[Literal["elevenlabs", "cartesia", "openai", "cambai", "sarvam", "inworld", "minimax"]]
    """Voice provider"""

    model: str
    """Filter by model (e.g., bulbul:v2, bulbul:v3-beta) - only for sarvam provider"""

    next_page: str
    """Cursor for next page - used for native pagination (cartesia, elevenlabs)"""

    page: int
    """Page number (default: 1) - used for offset pagination"""

    size: int
    """Page size (default: 50, max: 100)"""
