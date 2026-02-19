# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...._types import (
    Body,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    not_given,
)
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.org.prospects import bulk_delete_params, bulk_import_params, bulk_update_params
from ....types.org.prospects.bulk_import_response import BulkImportResponse
from ....types.org.prospects.bulk_operation_response_prospects import BulkOperationResponseProspects

__all__ = ["BulkResource", "AsyncBulkResource"]


class BulkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return BulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return BulkResourceWithStreamingResponse(self)

    def update(
        self,
        org_id: str,
        *,
        prospect_ids: SequenceNotStr[str],
        updates: bulk_update_params.Updates,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkOperationResponseProspects:
        """Update multiple prospects with the same field values.

        At least one update field
        must be provided. Phone cannot be bulk updated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._patch(
            f"/org/{org_id}/prospects/bulk",
            body=maybe_transform(
                {
                    "prospect_ids": prospect_ids,
                    "updates": updates,
                },
                bulk_update_params.BulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperationResponseProspects,
        )

    def delete(
        self,
        org_id: str,
        *,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkOperationResponseProspects:
        """
        Soft delete multiple prospects at once

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._delete(
            f"/org/{org_id}/prospects/bulk",
            body=maybe_transform({"prospect_ids": prospect_ids}, bulk_delete_params.BulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperationResponseProspects,
        )

    def import_(
        self,
        org_id: str,
        *,
        file: FileTypes,
        list_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkImportResponse:
        """Import prospects from a CSV file.

        Creates a prospect list and upserts prospects.
        Auto-detects country/timezone from phone.

        Args:
          file: CSV file (max 2MB)

          list_name: Name for the prospect list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        body = deepcopy_minimal(
            {
                "file": file,
                "list_name": list_name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/org/{org_id}/prospects/bulk",
            body=maybe_transform(body, bulk_import_params.BulkImportParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkImportResponse,
        )


class AsyncBulkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncBulkResourceWithStreamingResponse(self)

    async def update(
        self,
        org_id: str,
        *,
        prospect_ids: SequenceNotStr[str],
        updates: bulk_update_params.Updates,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkOperationResponseProspects:
        """Update multiple prospects with the same field values.

        At least one update field
        must be provided. Phone cannot be bulk updated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._patch(
            f"/org/{org_id}/prospects/bulk",
            body=await async_maybe_transform(
                {
                    "prospect_ids": prospect_ids,
                    "updates": updates,
                },
                bulk_update_params.BulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperationResponseProspects,
        )

    async def delete(
        self,
        org_id: str,
        *,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkOperationResponseProspects:
        """
        Soft delete multiple prospects at once

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._delete(
            f"/org/{org_id}/prospects/bulk",
            body=await async_maybe_transform({"prospect_ids": prospect_ids}, bulk_delete_params.BulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperationResponseProspects,
        )

    async def import_(
        self,
        org_id: str,
        *,
        file: FileTypes,
        list_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkImportResponse:
        """Import prospects from a CSV file.

        Creates a prospect list and upserts prospects.
        Auto-detects country/timezone from phone.

        Args:
          file: CSV file (max 2MB)

          list_name: Name for the prospect list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        body = deepcopy_minimal(
            {
                "file": file,
                "list_name": list_name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/org/{org_id}/prospects/bulk",
            body=await async_maybe_transform(body, bulk_import_params.BulkImportParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkImportResponse,
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.update = to_raw_response_wrapper(
            bulk.update,
        )
        self.delete = to_raw_response_wrapper(
            bulk.delete,
        )
        self.import_ = to_raw_response_wrapper(
            bulk.import_,
        )


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.update = async_to_raw_response_wrapper(
            bulk.update,
        )
        self.delete = async_to_raw_response_wrapper(
            bulk.delete,
        )
        self.import_ = async_to_raw_response_wrapper(
            bulk.import_,
        )


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.update = to_streamed_response_wrapper(
            bulk.update,
        )
        self.delete = to_streamed_response_wrapper(
            bulk.delete,
        )
        self.import_ = to_streamed_response_wrapper(
            bulk.import_,
        )


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.update = async_to_streamed_response_wrapper(
            bulk.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            bulk.delete,
        )
        self.import_ = async_to_streamed_response_wrapper(
            bulk.import_,
        )
