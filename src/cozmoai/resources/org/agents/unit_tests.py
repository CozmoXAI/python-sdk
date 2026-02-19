# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.org.agents import (
    unit_test_list_params,
    unit_test_create_params,
    unit_test_delete_params,
    unit_test_update_params,
    unit_test_generate_params,
)
from ....types.org.agents.unit_test import UnitTest
from ....types.org.agents.unit_test_list_response import UnitTestListResponse
from ....types.org.agents.unit_test_delete_response import UnitTestDeleteResponse
from ....types.org.agents.unit_test_generate_response import UnitTestGenerateResponse

__all__ = ["UnitTestsResource", "AsyncUnitTestsResource"]


class UnitTestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnitTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return UnitTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnitTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return UnitTestsResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        org_id: str,
        answer_prompt: str,
        question_prompt: str,
        question_variance: Literal["low", "med", "high"],
        function_tool_assertion: str | Omit = omit,
        title: str | Omit = omit,
        yaml_config: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTest:
        """
        Create a new unit test for an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/org/{org_id}/agents/{agent_id}/unit-tests",
            body=maybe_transform(
                {
                    "answer_prompt": answer_prompt,
                    "question_prompt": question_prompt,
                    "question_variance": question_variance,
                    "function_tool_assertion": function_tool_assertion,
                    "title": title,
                    "yaml_config": yaml_config,
                },
                unit_test_create_params.UnitTestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTest,
        )

    def update(
        self,
        test_id: str,
        *,
        org_id: str,
        agent_id: str,
        answer_prompt: str | Omit = omit,
        function_tool_assertion: str | Omit = omit,
        question_prompt: str | Omit = omit,
        question_variance: Literal["low", "med", "high"] | Omit = omit,
        title: str | Omit = omit,
        yaml_config: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTest:
        """
        Update an existing unit test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return self._put(
            f"/org/{org_id}/agents/{agent_id}/unit-tests/{test_id}",
            body=maybe_transform(
                {
                    "answer_prompt": answer_prompt,
                    "function_tool_assertion": function_tool_assertion,
                    "question_prompt": question_prompt,
                    "question_variance": question_variance,
                    "title": title,
                    "yaml_config": yaml_config,
                },
                unit_test_update_params.UnitTestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTest,
        )

    def list(
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
    ) -> UnitTestListResponse:
        """
        Get all unit tests for a specific agent

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
            f"/org/{org_id}/agents/{agent_id}/unit-tests",
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
                    unit_test_list_params.UnitTestListParams,
                ),
            ),
            cast_to=UnitTestListResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        org_id: str,
        ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTestDeleteResponse:
        """
        Delete multiple unit tests by IDs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/org/{org_id}/agents/{agent_id}/unit-tests/delete",
            body=maybe_transform({"ids": ids}, unit_test_delete_params.UnitTestDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTestDeleteResponse,
        )

    def generate(
        self,
        agent_id: str,
        *,
        org_id: str,
        count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTestGenerateResponse:
        """
        Auto-generate unit tests for an agent using AI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/org/{org_id}/agents/{agent_id}/unit-tests/generate",
            body=maybe_transform({"count": count}, unit_test_generate_params.UnitTestGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTestGenerateResponse,
        )


class AsyncUnitTestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnitTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUnitTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnitTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncUnitTestsResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        org_id: str,
        answer_prompt: str,
        question_prompt: str,
        question_variance: Literal["low", "med", "high"],
        function_tool_assertion: str | Omit = omit,
        title: str | Omit = omit,
        yaml_config: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTest:
        """
        Create a new unit test for an agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/org/{org_id}/agents/{agent_id}/unit-tests",
            body=await async_maybe_transform(
                {
                    "answer_prompt": answer_prompt,
                    "question_prompt": question_prompt,
                    "question_variance": question_variance,
                    "function_tool_assertion": function_tool_assertion,
                    "title": title,
                    "yaml_config": yaml_config,
                },
                unit_test_create_params.UnitTestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTest,
        )

    async def update(
        self,
        test_id: str,
        *,
        org_id: str,
        agent_id: str,
        answer_prompt: str | Omit = omit,
        function_tool_assertion: str | Omit = omit,
        question_prompt: str | Omit = omit,
        question_variance: Literal["low", "med", "high"] | Omit = omit,
        title: str | Omit = omit,
        yaml_config: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTest:
        """
        Update an existing unit test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not test_id:
            raise ValueError(f"Expected a non-empty value for `test_id` but received {test_id!r}")
        return await self._put(
            f"/org/{org_id}/agents/{agent_id}/unit-tests/{test_id}",
            body=await async_maybe_transform(
                {
                    "answer_prompt": answer_prompt,
                    "function_tool_assertion": function_tool_assertion,
                    "question_prompt": question_prompt,
                    "question_variance": question_variance,
                    "title": title,
                    "yaml_config": yaml_config,
                },
                unit_test_update_params.UnitTestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTest,
        )

    async def list(
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
    ) -> UnitTestListResponse:
        """
        Get all unit tests for a specific agent

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
            f"/org/{org_id}/agents/{agent_id}/unit-tests",
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
                    unit_test_list_params.UnitTestListParams,
                ),
            ),
            cast_to=UnitTestListResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        org_id: str,
        ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTestDeleteResponse:
        """
        Delete multiple unit tests by IDs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/org/{org_id}/agents/{agent_id}/unit-tests/delete",
            body=await async_maybe_transform({"ids": ids}, unit_test_delete_params.UnitTestDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTestDeleteResponse,
        )

    async def generate(
        self,
        agent_id: str,
        *,
        org_id: str,
        count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnitTestGenerateResponse:
        """
        Auto-generate unit tests for an agent using AI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/org/{org_id}/agents/{agent_id}/unit-tests/generate",
            body=await async_maybe_transform({"count": count}, unit_test_generate_params.UnitTestGenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnitTestGenerateResponse,
        )


class UnitTestsResourceWithRawResponse:
    def __init__(self, unit_tests: UnitTestsResource) -> None:
        self._unit_tests = unit_tests

        self.create = to_raw_response_wrapper(
            unit_tests.create,
        )
        self.update = to_raw_response_wrapper(
            unit_tests.update,
        )
        self.list = to_raw_response_wrapper(
            unit_tests.list,
        )
        self.delete = to_raw_response_wrapper(
            unit_tests.delete,
        )
        self.generate = to_raw_response_wrapper(
            unit_tests.generate,
        )


class AsyncUnitTestsResourceWithRawResponse:
    def __init__(self, unit_tests: AsyncUnitTestsResource) -> None:
        self._unit_tests = unit_tests

        self.create = async_to_raw_response_wrapper(
            unit_tests.create,
        )
        self.update = async_to_raw_response_wrapper(
            unit_tests.update,
        )
        self.list = async_to_raw_response_wrapper(
            unit_tests.list,
        )
        self.delete = async_to_raw_response_wrapper(
            unit_tests.delete,
        )
        self.generate = async_to_raw_response_wrapper(
            unit_tests.generate,
        )


class UnitTestsResourceWithStreamingResponse:
    def __init__(self, unit_tests: UnitTestsResource) -> None:
        self._unit_tests = unit_tests

        self.create = to_streamed_response_wrapper(
            unit_tests.create,
        )
        self.update = to_streamed_response_wrapper(
            unit_tests.update,
        )
        self.list = to_streamed_response_wrapper(
            unit_tests.list,
        )
        self.delete = to_streamed_response_wrapper(
            unit_tests.delete,
        )
        self.generate = to_streamed_response_wrapper(
            unit_tests.generate,
        )


class AsyncUnitTestsResourceWithStreamingResponse:
    def __init__(self, unit_tests: AsyncUnitTestsResource) -> None:
        self._unit_tests = unit_tests

        self.create = async_to_streamed_response_wrapper(
            unit_tests.create,
        )
        self.update = async_to_streamed_response_wrapper(
            unit_tests.update,
        )
        self.list = async_to_streamed_response_wrapper(
            unit_tests.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            unit_tests.delete,
        )
        self.generate = async_to_streamed_response_wrapper(
            unit_tests.generate,
        )
