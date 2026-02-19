# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.org.analytics import call_list_calls_params, call_get_call_costs_params, call_list_calls_by_hour_params
from ....types.org.analytics.call_list_calls_response import CallListCallsResponse
from ....types.org.analytics.call_get_call_costs_response import CallGetCallCostsResponse
from ....types.org.analytics.call_list_calls_by_hour_response import CallListCallsByHourResponse

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def get_call_costs(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetCallCostsResponse:
        """
        Returns call cost breakdown by day

        Args:
          end_date: End date (ISO 8601)

          start_date: Start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/analytics/calls/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    call_get_call_costs_params.CallGetCallCostsParams,
                ),
            ),
            cast_to=CallGetCallCostsResponse,
        )

    def list_calls(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListCallsResponse:
        """
        Returns call volume, duration stats, and outcomes for the organization

        Args:
          end_date: End date (ISO 8601)

          start_date: Start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/analytics/calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    call_list_calls_params.CallListCallsParams,
                ),
            ),
            cast_to=CallListCallsResponse,
        )

    def list_calls_by_hour(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListCallsByHourResponse:
        """
        Returns call distribution by hour of day

        Args:
          end_date: End date (ISO 8601)

          start_date: Start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/analytics/calls/by-hour",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    call_list_calls_by_hour_params.CallListCallsByHourParams,
                ),
            ),
            cast_to=CallListCallsByHourResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def get_call_costs(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallGetCallCostsResponse:
        """
        Returns call cost breakdown by day

        Args:
          end_date: End date (ISO 8601)

          start_date: Start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/analytics/calls/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    call_get_call_costs_params.CallGetCallCostsParams,
                ),
            ),
            cast_to=CallGetCallCostsResponse,
        )

    async def list_calls(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListCallsResponse:
        """
        Returns call volume, duration stats, and outcomes for the organization

        Args:
          end_date: End date (ISO 8601)

          start_date: Start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/analytics/calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    call_list_calls_params.CallListCallsParams,
                ),
            ),
            cast_to=CallListCallsResponse,
        )

    async def list_calls_by_hour(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallListCallsByHourResponse:
        """
        Returns call distribution by hour of day

        Args:
          end_date: End date (ISO 8601)

          start_date: Start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/analytics/calls/by-hour",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    call_list_calls_by_hour_params.CallListCallsByHourParams,
                ),
            ),
            cast_to=CallListCallsByHourResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.get_call_costs = to_raw_response_wrapper(
            calls.get_call_costs,
        )
        self.list_calls = to_raw_response_wrapper(
            calls.list_calls,
        )
        self.list_calls_by_hour = to_raw_response_wrapper(
            calls.list_calls_by_hour,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.get_call_costs = async_to_raw_response_wrapper(
            calls.get_call_costs,
        )
        self.list_calls = async_to_raw_response_wrapper(
            calls.list_calls,
        )
        self.list_calls_by_hour = async_to_raw_response_wrapper(
            calls.list_calls_by_hour,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.get_call_costs = to_streamed_response_wrapper(
            calls.get_call_costs,
        )
        self.list_calls = to_streamed_response_wrapper(
            calls.list_calls,
        )
        self.list_calls_by_hour = to_streamed_response_wrapper(
            calls.list_calls_by_hour,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.get_call_costs = async_to_streamed_response_wrapper(
            calls.get_call_costs,
        )
        self.list_calls = async_to_streamed_response_wrapper(
            calls.list_calls,
        )
        self.list_calls_by_hour = async_to_streamed_response_wrapper(
            calls.list_calls_by_hour,
        )
