# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.org import batch_list_workflow_runs_params, batch_update_batch_status_params
from ..._base_client import make_request_options
from ...types.org.batch_response import BatchResponse
from ...types.org.batch_list_workflow_runs_response import BatchListWorkflowRunsResponse

__all__ = ["BatchesResource", "AsyncBatchesResource"]


class BatchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return BatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return BatchesResourceWithStreamingResponse(self)

    def get_workflow_batch(
        self,
        batch_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """
        Get a single workflow batch with run statistics

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            f"/org/{org_id}/batches/{batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    def list_workflow_runs(
        self,
        batch_id: str,
        *,
        org_id: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListWorkflowRunsResponse:
        """
        List all workflow runs in a batch with pagination

        Args:
          limit: Items per page

          page: Page number

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            f"/org/{org_id}/batches/{batch_id}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    batch_list_workflow_runs_params.BatchListWorkflowRunsParams,
                ),
            ),
            cast_to=BatchListWorkflowRunsResponse,
        )

    def update_batch_status(
        self,
        batch_id: str,
        *,
        org_id: str,
        status: Literal["PENDING", "PAUSED", "CANCELLED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """
        Update batch status and cascade to all runs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._patch(
            f"/org/{org_id}/batches/{batch_id}",
            body=maybe_transform({"status": status}, batch_update_batch_status_params.BatchUpdateBatchStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )


class AsyncBatchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncBatchesResourceWithStreamingResponse(self)

    async def get_workflow_batch(
        self,
        batch_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """
        Get a single workflow batch with run statistics

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            f"/org/{org_id}/batches/{batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )

    async def list_workflow_runs(
        self,
        batch_id: str,
        *,
        org_id: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListWorkflowRunsResponse:
        """
        List all workflow runs in a batch with pagination

        Args:
          limit: Items per page

          page: Page number

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            f"/org/{org_id}/batches/{batch_id}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "status": status,
                    },
                    batch_list_workflow_runs_params.BatchListWorkflowRunsParams,
                ),
            ),
            cast_to=BatchListWorkflowRunsResponse,
        )

    async def update_batch_status(
        self,
        batch_id: str,
        *,
        org_id: str,
        status: Literal["PENDING", "PAUSED", "CANCELLED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponse:
        """
        Update batch status and cascade to all runs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._patch(
            f"/org/{org_id}/batches/{batch_id}",
            body=await async_maybe_transform(
                {"status": status}, batch_update_batch_status_params.BatchUpdateBatchStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponse,
        )


class BatchesResourceWithRawResponse:
    def __init__(self, batches: BatchesResource) -> None:
        self._batches = batches

        self.get_workflow_batch = to_raw_response_wrapper(
            batches.get_workflow_batch,
        )
        self.list_workflow_runs = to_raw_response_wrapper(
            batches.list_workflow_runs,
        )
        self.update_batch_status = to_raw_response_wrapper(
            batches.update_batch_status,
        )


class AsyncBatchesResourceWithRawResponse:
    def __init__(self, batches: AsyncBatchesResource) -> None:
        self._batches = batches

        self.get_workflow_batch = async_to_raw_response_wrapper(
            batches.get_workflow_batch,
        )
        self.list_workflow_runs = async_to_raw_response_wrapper(
            batches.list_workflow_runs,
        )
        self.update_batch_status = async_to_raw_response_wrapper(
            batches.update_batch_status,
        )


class BatchesResourceWithStreamingResponse:
    def __init__(self, batches: BatchesResource) -> None:
        self._batches = batches

        self.get_workflow_batch = to_streamed_response_wrapper(
            batches.get_workflow_batch,
        )
        self.list_workflow_runs = to_streamed_response_wrapper(
            batches.list_workflow_runs,
        )
        self.update_batch_status = to_streamed_response_wrapper(
            batches.update_batch_status,
        )


class AsyncBatchesResourceWithStreamingResponse:
    def __init__(self, batches: AsyncBatchesResource) -> None:
        self._batches = batches

        self.get_workflow_batch = async_to_streamed_response_wrapper(
            batches.get_workflow_batch,
        )
        self.list_workflow_runs = async_to_streamed_response_wrapper(
            batches.list_workflow_runs,
        )
        self.update_batch_status = async_to_streamed_response_wrapper(
            batches.update_batch_status,
        )
