# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailTemplateCreateParams"]


class EmailTemplateCreateParams(TypedDict, total=False):
    body_html: Required[str]

    name: Required[str]

    subject: Required[str]

    body_text: str
