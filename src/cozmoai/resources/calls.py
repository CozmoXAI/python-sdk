# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import call_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.call_list_response import CallListResponse
from ..types.call_retrieve_response import CallRetrieveResponse

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        call_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallRetrieveResponse:
        """
        Returns full details for a specific call including prospect and agent info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._get(
            f"/org/{org_id}/calls/{call_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    def list(
        self,
        org_id: str,
        *,
        agent_id: str | Omit = omit,
        direction: str | Omit = omit,
        end_date: str | Omit = omit,
        min_duration: int | Omit = omit,
        page: int | Omit = omit,
        phone: str | Omit = omit,
        prospect_external_id: str | Omit = omit,
        prospect_id: str | Omit = omit,
        prospect_name: str | Omit = omit,
        size: int | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListResponse:
        """
        Returns a paginated list of calls for the organization with optional filters

        Args:
          agent_id: Filter by agent ID

          direction: Filter by direction (INBOUND, OUTBOUND)

          end_date: Filter by end date (ISO 8601)

          min_duration: Filter by minimum duration in seconds

          page: Page number

          phone: Search by phone number

          prospect_external_id: Filter by prospect external ID

          prospect_id: Filter by prospect ID

          prospect_name: Filter by prospect name (first or last)

          size: Page size

          start_date: Filter by start date (ISO 8601)

          status: Filter by status (SCHEDULED, RINGING, IN_PROGRESS, completed, no-answer, failed,
              busy)

          workflow_id: Filter by workflow ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "direction": direction,
                        "end_date": end_date,
                        "min_duration": min_duration,
                        "page": page,
                        "phone": phone,
                        "prospect_external_id": prospect_external_id,
                        "prospect_id": prospect_id,
                        "prospect_name": prospect_name,
                        "size": size,
                        "start_date": start_date,
                        "status": status,
                        "workflow_id": workflow_id,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            cast_to=CallListResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        call_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallRetrieveResponse:
        """
        Returns full details for a specific call including prospect and agent info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._get(
            f"/org/{org_id}/calls/{call_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    async def list(
        self,
        org_id: str,
        *,
        agent_id: str | Omit = omit,
        direction: str | Omit = omit,
        end_date: str | Omit = omit,
        min_duration: int | Omit = omit,
        page: int | Omit = omit,
        phone: str | Omit = omit,
        prospect_external_id: str | Omit = omit,
        prospect_id: str | Omit = omit,
        prospect_name: str | Omit = omit,
        size: int | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListResponse:
        """
        Returns a paginated list of calls for the organization with optional filters

        Args:
          agent_id: Filter by agent ID

          direction: Filter by direction (INBOUND, OUTBOUND)

          end_date: Filter by end date (ISO 8601)

          min_duration: Filter by minimum duration in seconds

          page: Page number

          phone: Search by phone number

          prospect_external_id: Filter by prospect external ID

          prospect_id: Filter by prospect ID

          prospect_name: Filter by prospect name (first or last)

          size: Page size

          start_date: Filter by start date (ISO 8601)

          status: Filter by status (SCHEDULED, RINGING, IN_PROGRESS, completed, no-answer, failed,
              busy)

          workflow_id: Filter by workflow ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "direction": direction,
                        "end_date": end_date,
                        "min_duration": min_duration,
                        "page": page,
                        "phone": phone,
                        "prospect_external_id": prospect_external_id,
                        "prospect_id": prospect_id,
                        "prospect_name": prospect_name,
                        "size": size,
                        "start_date": start_date,
                        "status": status,
                        "workflow_id": workflow_id,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            cast_to=CallListResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.retrieve = to_raw_response_wrapper(
            calls.retrieve,
        )
        self.list = to_raw_response_wrapper(
            calls.list,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.retrieve = async_to_raw_response_wrapper(
            calls.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            calls.list,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.retrieve = to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            calls.list,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.retrieve = async_to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            calls.list,
        )
