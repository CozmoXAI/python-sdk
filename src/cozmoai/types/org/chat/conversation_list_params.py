# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    limit: int
    """Number of items per page"""

    offset: int
    """Number of items to skip"""
