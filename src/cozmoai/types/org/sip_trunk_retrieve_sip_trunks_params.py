# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SipTrunkRetrieveSipTrunksParams"]


class SipTrunkRetrieveSipTrunksParams(TypedDict, total=False):
    is_active: bool
    """Filter by active status"""

    page: int
    """Page number"""

    provider: str
    """Filter by provider (TWILIO, TELNYX, VONAGE, GENERIC)"""

    size: int
    """Page size"""
