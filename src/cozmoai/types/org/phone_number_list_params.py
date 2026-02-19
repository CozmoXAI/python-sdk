# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PhoneNumberListParams"]


class PhoneNumberListParams(TypedDict, total=False):
    direction: Literal["inbound", "outbound"]
    """Filter by SIP trunk type/direction"""

    is_verified: bool
    """Filter by verification status"""

    page: int
    """Page number"""

    search: str
    """Search by number or label"""

    sip_trunk_id: str
    """Filter by SIP trunk ID"""

    size: int
    """Page size"""
