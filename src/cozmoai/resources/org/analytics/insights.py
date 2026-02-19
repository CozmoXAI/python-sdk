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
from ....types.org.analytics import insight_list_insights_params, insight_generate_insights_params
from ....types.org.analytics.insight_list_insights_response import InsightListInsightsResponse
from ....types.org.analytics.insight_generate_insights_response import InsightGenerateInsightsResponse

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return InsightsResourceWithStreamingResponse(self)

    def generate_insights(
        self,
        org_id: str,
        *,
        end_date: str,
        start_date: str,
        force_refresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightGenerateInsightsResponse:
        """
        Generate comprehensive AI analysis of call performance for a given time period

        Args:
          end_date: End date (YYYY-MM-DD)

          start_date: Start date (YYYY-MM-DD)

          force_refresh: Force regeneration (skip cache)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/analytics/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "force_refresh": force_refresh,
                    },
                    insight_generate_insights_params.InsightGenerateInsightsParams,
                ),
            ),
            cast_to=InsightGenerateInsightsResponse,
        )

    def list_insights(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightListInsightsResponse:
        """
        Get a paginated list of previously generated insights

        Args:
          end_date: Filter by period end date (YYYY-MM-DD)

          limit: Number of items per page

          offset: Number of items to skip

          start_date: Filter by period start date (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/analytics/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "start_date": start_date,
                    },
                    insight_list_insights_params.InsightListInsightsParams,
                ),
            ),
            cast_to=InsightListInsightsResponse,
        )


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncInsightsResourceWithStreamingResponse(self)

    async def generate_insights(
        self,
        org_id: str,
        *,
        end_date: str,
        start_date: str,
        force_refresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightGenerateInsightsResponse:
        """
        Generate comprehensive AI analysis of call performance for a given time period

        Args:
          end_date: End date (YYYY-MM-DD)

          start_date: Start date (YYYY-MM-DD)

          force_refresh: Force regeneration (skip cache)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/analytics/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "force_refresh": force_refresh,
                    },
                    insight_generate_insights_params.InsightGenerateInsightsParams,
                ),
            ),
            cast_to=InsightGenerateInsightsResponse,
        )

    async def list_insights(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InsightListInsightsResponse:
        """
        Get a paginated list of previously generated insights

        Args:
          end_date: Filter by period end date (YYYY-MM-DD)

          limit: Number of items per page

          offset: Number of items to skip

          start_date: Filter by period start date (YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/analytics/insights",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "start_date": start_date,
                    },
                    insight_list_insights_params.InsightListInsightsParams,
                ),
            ),
            cast_to=InsightListInsightsResponse,
        )


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.generate_insights = to_raw_response_wrapper(
            insights.generate_insights,
        )
        self.list_insights = to_raw_response_wrapper(
            insights.list_insights,
        )


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.generate_insights = async_to_raw_response_wrapper(
            insights.generate_insights,
        )
        self.list_insights = async_to_raw_response_wrapper(
            insights.list_insights,
        )


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

        self.generate_insights = to_streamed_response_wrapper(
            insights.generate_insights,
        )
        self.list_insights = to_streamed_response_wrapper(
            insights.list_insights,
        )


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

        self.generate_insights = async_to_streamed_response_wrapper(
            insights.generate_insights,
        )
        self.list_insights = async_to_streamed_response_wrapper(
            insights.list_insights,
        )
