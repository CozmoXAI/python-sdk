# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemberUpdateRoleParams"]


class MemberUpdateRoleParams(TypedDict, total=False):
    org_id: Required[str]

    role: Required[Literal["OWNER", "ADMIN", "MANAGER", "MEMBER"]]
