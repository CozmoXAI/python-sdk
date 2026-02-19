# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["BulkImportResponse", "SkippedRow"]


class SkippedRow(BaseModel):
    phone: Optional[str] = None

    reason: Optional[str] = None

    row: Optional[int] = None


class BulkImportResponse(BaseModel):
    list_id: Optional[str] = None

    list_name: Optional[str] = None

    prospect_ids: Optional[List[str]] = None

    skipped_rows: Optional[List[SkippedRow]] = None

    total_imported: Optional[int] = None

    total_rows: Optional[int] = None

    total_skipped: Optional[int] = None

    total_updated: Optional[int] = None
