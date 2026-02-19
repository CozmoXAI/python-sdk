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
from ....types.org.agents import unit_test_run_latest_params
from ....types.org.agents.unit_test_run_latest_response import UnitTestRunLatestResponse

__all__ = ["UnitTestRunsResource", "AsyncUnitTestRunsResource"]


class UnitTestRunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnitTestRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return UnitTestRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnitTestRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return UnitTestRunsResourceWithStreamingResponse(self)

    def latest(
        self,
        agent_id: str,
        *,
        org_id: str,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTestRunLatestResponse:
        """
        Get the latest test run results for an agent

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/org/{org_id}/agents/{agent_id}/unit-test-runs/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    unit_test_run_latest_params.UnitTestRunLatestParams,
                ),
            ),
            cast_to=UnitTestRunLatestResponse,
        )


class AsyncUnitTestRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnitTestRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUnitTestRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnitTestRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncUnitTestRunsResourceWithStreamingResponse(self)

    async def latest(
        self,
        agent_id: str,
        *,
        org_id: str,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTestRunLatestResponse:
        """
        Get the latest test run results for an agent

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/org/{org_id}/agents/{agent_id}/unit-test-runs/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    unit_test_run_latest_params.UnitTestRunLatestParams,
                ),
            ),
            cast_to=UnitTestRunLatestResponse,
        )


class UnitTestRunsResourceWithRawResponse:
    def __init__(self, unit_test_runs: UnitTestRunsResource) -> None:
        self._unit_test_runs = unit_test_runs

        self.latest = to_raw_response_wrapper(
            unit_test_runs.latest,
        )


class AsyncUnitTestRunsResourceWithRawResponse:
    def __init__(self, unit_test_runs: AsyncUnitTestRunsResource) -> None:
        self._unit_test_runs = unit_test_runs

        self.latest = async_to_raw_response_wrapper(
            unit_test_runs.latest,
        )


class UnitTestRunsResourceWithStreamingResponse:
    def __init__(self, unit_test_runs: UnitTestRunsResource) -> None:
        self._unit_test_runs = unit_test_runs

        self.latest = to_streamed_response_wrapper(
            unit_test_runs.latest,
        )


class AsyncUnitTestRunsResourceWithStreamingResponse:
    def __init__(self, unit_test_runs: AsyncUnitTestRunsResource) -> None:
        self._unit_test_runs = unit_test_runs

        self.latest = async_to_streamed_response_wrapper(
            unit_test_runs.latest,
        )
