# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["IntegrationConnectParams"]


class IntegrationConnectParams(TypedDict, total=False):
    slug: Required[str]

    credentials: Iterable[int]

    settings: Iterable[int]
