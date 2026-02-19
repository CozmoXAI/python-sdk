# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import FileTypes

__all__ = ["BulkImportParams"]


class BulkImportParams(TypedDict, total=False):
    file: Required[FileTypes]
    """CSV file (max 2MB)"""

    list_name: Required[str]
    """Name for the prospect list"""
