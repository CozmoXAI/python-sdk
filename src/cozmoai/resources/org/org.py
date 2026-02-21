# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .calls import (
    CallsResource,
    AsyncCallsResource,
    CallsResourceWithRawResponse,
    AsyncCallsResourceWithRawResponse,
    CallsResourceWithStreamingResponse,
    AsyncCallsResourceWithStreamingResponse,
)
from .agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)
from ...types import org_list_voices_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .workflows import (
    WorkflowsResource,
    AsyncWorkflowsResource,
    WorkflowsResourceWithRawResponse,
    AsyncWorkflowsResourceWithRawResponse,
    WorkflowsResourceWithStreamingResponse,
    AsyncWorkflowsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.org_list_voices_response import OrgListVoicesResponse

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        return AgentsResource(self._client)

    @cached_property
    def calls(self) -> CallsResource:
        return CallsResource(self._client)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        return WorkflowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return OrgResourceWithStreamingResponse(self)

    def list_voices(
        self,
        org_id: str,
        *,
        provider: Literal["elevenlabs", "cartesia", "openai", "cambai", "sarvam", "inworld", "minimax"],
        model: str | Omit = omit,
        next_page: str | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgListVoicesResponse:
        """
        Get a paginated list of available voices from the specified provider

        Args:
          provider: Voice provider

          model: Filter by model (e.g., bulbul:v2, bulbul:v3-beta) - only for sarvam provider

          next_page: Cursor for next page - used for native pagination (cartesia, elevenlabs)

          page: Page number (default: 1) - used for offset pagination

          size: Page size (default: 50, max: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/voices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "provider": provider,
                        "model": model,
                        "next_page": next_page,
                        "page": page,
                        "size": size,
                    },
                    org_list_voices_params.OrgListVoicesParams,
                ),
            ),
            cast_to=OrgListVoicesResponse,
        )


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def agents(self) -> AsyncAgentsResource:
        return AsyncAgentsResource(self._client)

    @cached_property
    def calls(self) -> AsyncCallsResource:
        return AsyncCallsResource(self._client)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        return AsyncWorkflowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncOrgResourceWithStreamingResponse(self)

    async def list_voices(
        self,
        org_id: str,
        *,
        provider: Literal["elevenlabs", "cartesia", "openai", "cambai", "sarvam", "inworld", "minimax"],
        model: str | Omit = omit,
        next_page: str | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgListVoicesResponse:
        """
        Get a paginated list of available voices from the specified provider

        Args:
          provider: Voice provider

          model: Filter by model (e.g., bulbul:v2, bulbul:v3-beta) - only for sarvam provider

          next_page: Cursor for next page - used for native pagination (cartesia, elevenlabs)

          page: Page number (default: 1) - used for offset pagination

          size: Page size (default: 50, max: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/voices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "provider": provider,
                        "model": model,
                        "next_page": next_page,
                        "page": page,
                        "size": size,
                    },
                    org_list_voices_params.OrgListVoicesParams,
                ),
            ),
            cast_to=OrgListVoicesResponse,
        )


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.list_voices = to_raw_response_wrapper(
            org.list_voices,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self._org.agents)

    @cached_property
    def calls(self) -> CallsResourceWithRawResponse:
        return CallsResourceWithRawResponse(self._org.calls)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithRawResponse:
        return WorkflowsResourceWithRawResponse(self._org.workflows)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.list_voices = async_to_raw_response_wrapper(
            org.list_voices,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._org.agents)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithRawResponse:
        return AsyncCallsResourceWithRawResponse(self._org.calls)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithRawResponse:
        return AsyncWorkflowsResourceWithRawResponse(self._org.workflows)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.list_voices = to_streamed_response_wrapper(
            org.list_voices,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._org.agents)

    @cached_property
    def calls(self) -> CallsResourceWithStreamingResponse:
        return CallsResourceWithStreamingResponse(self._org.calls)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithStreamingResponse:
        return WorkflowsResourceWithStreamingResponse(self._org.workflows)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.list_voices = async_to_streamed_response_wrapper(
            org.list_voices,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._org.agents)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithStreamingResponse:
        return AsyncCallsResourceWithStreamingResponse(self._org.calls)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        return AsyncWorkflowsResourceWithStreamingResponse(self._org.workflows)
