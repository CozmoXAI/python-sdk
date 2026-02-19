# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailTemplateUpdateParams"]


class EmailTemplateUpdateParams(TypedDict, total=False):
    org_id: Required[str]

    body_html: str

    body_text: str

    name: str

    subject: str
