from __future__ import annotations

import httpx

from ..types import agent_session_start_params
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
from ..types.agent_session_response import AgentSessionResponse
from ..types.agent_session_start_response import AgentSessionStartResponse

__all__ = ["AgentSessionsResource", "AsyncAgentSessionsResource"]


class AgentSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AgentSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AgentSessionsResourceWithStreamingResponse(self)

    def start(
        self,
        session_id: str,
        *,
        agent_id: str,
        instruction: str,
        title: str | Omit = omit,
        source: str | Omit = omit,
        prospect_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSessionStartResponse:
        """
        Creates the session record, appends the initial user message event, and
        signals the agent workflow — all in one call.

        Args:
          session_id: A UUID v4 to assign to the new session.

          agent_id: UUID of the agent to run. Required.

          instruction: The initial message / instruction to send to the agent. Required.

          title: Title for the session. Defaults to the first 100 chars of instruction.

          source: Source identifier. Defaults to 'command-center'.

          prospect_id: UUID of a prospect to associate with this session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/agent-sessions/{session_id}/start",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "instruction": instruction,
                    "title": title,
                    "source": source,
                    "prospect_id": prospect_id,
                },
                agent_session_start_params.AgentSessionStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSessionStartResponse,
        )

    def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSessionResponse:
        """
        Returns full details for a specific agent session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/agent-sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSessionResponse,
        )


class AsyncAgentSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncAgentSessionsResourceWithStreamingResponse(self)

    async def start(
        self,
        session_id: str,
        *,
        agent_id: str,
        instruction: str,
        title: str | Omit = omit,
        source: str | Omit = omit,
        prospect_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSessionStartResponse:
        """
        Creates the session record, appends the initial user message event, and
        signals the agent workflow — all in one call.

        Args:
          session_id: A UUID v4 to assign to the new session.

          agent_id: UUID of the agent to run. Required.

          instruction: The initial message / instruction to send to the agent. Required.

          title: Title for the session. Defaults to the first 100 chars of instruction.

          source: Source identifier. Defaults to 'command-center'.

          prospect_id: UUID of a prospect to associate with this session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/agent-sessions/{session_id}/start",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "instruction": instruction,
                    "title": title,
                    "source": source,
                    "prospect_id": prospect_id,
                },
                agent_session_start_params.AgentSessionStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSessionStartResponse,
        )

    async def retrieve(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentSessionResponse:
        """
        Returns full details for a specific agent session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/agent-sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentSessionResponse,
        )


class AgentSessionsResourceWithRawResponse:
    def __init__(self, agent_sessions: AgentSessionsResource) -> None:
        self._agent_sessions = agent_sessions

        self.start = to_raw_response_wrapper(
            agent_sessions.start,
        )
        self.retrieve = to_raw_response_wrapper(
            agent_sessions.retrieve,
        )


class AsyncAgentSessionsResourceWithRawResponse:
    def __init__(self, agent_sessions: AsyncAgentSessionsResource) -> None:
        self._agent_sessions = agent_sessions

        self.start = async_to_raw_response_wrapper(
            agent_sessions.start,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agent_sessions.retrieve,
        )


class AgentSessionsResourceWithStreamingResponse:
    def __init__(self, agent_sessions: AgentSessionsResource) -> None:
        self._agent_sessions = agent_sessions

        self.start = to_streamed_response_wrapper(
            agent_sessions.start,
        )
        self.retrieve = to_streamed_response_wrapper(
            agent_sessions.retrieve,
        )


class AsyncAgentSessionsResourceWithStreamingResponse:
    def __init__(self, agent_sessions: AsyncAgentSessionsResource) -> None:
        self._agent_sessions = agent_sessions

        self.start = async_to_streamed_response_wrapper(
            agent_sessions.start,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agent_sessions.retrieve,
        )
