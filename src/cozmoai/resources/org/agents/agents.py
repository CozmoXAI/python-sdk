# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from .evals import (
    EvalsResource,
    AsyncEvalsResource,
    EvalsResourceWithRawResponse,
    AsyncEvalsResourceWithRawResponse,
    EvalsResourceWithStreamingResponse,
    AsyncEvalsResourceWithStreamingResponse,
)
from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .sip_trunks import (
    SipTrunksResource,
    AsyncSipTrunksResource,
    SipTrunksResourceWithRawResponse,
    AsyncSipTrunksResourceWithRawResponse,
    SipTrunksResourceWithStreamingResponse,
    AsyncSipTrunksResourceWithStreamingResponse,
)
from .unit_tests import (
    UnitTestsResource,
    AsyncUnitTestsResource,
    UnitTestsResourceWithRawResponse,
    AsyncUnitTestsResourceWithRawResponse,
    UnitTestsResourceWithStreamingResponse,
    AsyncUnitTestsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.org import (
    agent_list_params,
    agent_create_params,
    agent_update_params,
    agent_list_eval_runs_params,
    agent_run_specific_tests_params,
)
from .unit_test_runs import (
    UnitTestRunsResource,
    AsyncUnitTestRunsResource,
    UnitTestRunsResourceWithRawResponse,
    AsyncUnitTestRunsResourceWithRawResponse,
    UnitTestRunsResourceWithStreamingResponse,
    AsyncUnitTestRunsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.org.agent import Agent
from ....types.org.run_tests import RunTests
from ....types.org.agent_list_response import AgentListResponse
from ....types.org.goodbye_config_param import GoodbyeConfigParam
from ....types.org.recall_webhook_param import RecallWebhookParam
from ....types.org.agent_delete_response import AgentDeleteResponse
from ....types.org.agent_list_eval_runs_response import AgentListEvalRunsResponse
from ....types.org.background_sound_config_param import BackgroundSoundConfigParam

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def sip_trunks(self) -> SipTrunksResource:
        return SipTrunksResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def unit_test_runs(self) -> UnitTestRunsResource:
        return UnitTestRunsResource(self._client)

    @cached_property
    def unit_tests(self) -> UnitTestsResource:
        return UnitTestsResource(self._client)

    @cached_property
    def evals(self) -> EvalsResource:
        return EvalsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        name: str,
        prompt_template: str,
        type: Literal["voice", "chat", "video"],
        allowed_sip_trunks: SequenceNotStr[str] | Omit = omit,
        background_sound: BackgroundSoundConfigParam | Omit = omit,
        goodbye_config: GoodbyeConfigParam | Omit = omit,
        greeting_config: Dict[str, object] | Omit = omit,
        llm_config: Dict[str, object] | Omit = omit,
        plugins: Iterable[object] | Omit = omit,
        precall_webhook: RecallWebhookParam | Omit = omit,
        transcriber_config: Dict[str, object] | Omit = omit,
        vad_config: Dict[str, object] | Omit = omit,
        voice_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Create a new AI agent in the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/agents",
            body=maybe_transform(
                {
                    "name": name,
                    "prompt_template": prompt_template,
                    "type": type,
                    "allowed_sip_trunks": allowed_sip_trunks,
                    "background_sound": background_sound,
                    "goodbye_config": goodbye_config,
                    "greeting_config": greeting_config,
                    "llm_config": llm_config,
                    "plugins": plugins,
                    "precall_webhook": precall_webhook,
                    "transcriber_config": transcriber_config,
                    "vad_config": vad_config,
                    "voice_config": voice_config,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Get agent details by ID

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
        return self._get(
            f"/org/{org_id}/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def update(
        self,
        agent_id: str,
        *,
        org_id: str,
        allowed_sip_trunks: SequenceNotStr[str] | Omit = omit,
        background_sound: BackgroundSoundConfigParam | Omit = omit,
        goodbye_config: GoodbyeConfigParam | Omit = omit,
        greeting_config: Dict[str, object] | Omit = omit,
        llm_config: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        plugins: Iterable[object] | Omit = omit,
        precall_webhook: RecallWebhookParam | Omit = omit,
        prompt_template: str | Omit = omit,
        transcriber_config: Dict[str, object] | Omit = omit,
        type: Literal["voice", "chat", "video"] | Omit = omit,
        vad_config: Dict[str, object] | Omit = omit,
        voice_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Update agent details (partial update)

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
        return self._patch(
            f"/org/{org_id}/agents/{agent_id}",
            body=maybe_transform(
                {
                    "allowed_sip_trunks": allowed_sip_trunks,
                    "background_sound": background_sound,
                    "goodbye_config": goodbye_config,
                    "greeting_config": greeting_config,
                    "llm_config": llm_config,
                    "name": name,
                    "plugins": plugins,
                    "precall_webhook": precall_webhook,
                    "prompt_template": prompt_template,
                    "transcriber_config": transcriber_config,
                    "type": type,
                    "vad_config": vad_config,
                    "voice_config": voice_config,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def list(
        self,
        org_id: str,
        *,
        page: int | Omit = omit,
        search: str | Omit = omit,
        size: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Get a paginated list of agents for the organization

        Args:
          page: Page number

          search: Search by agent name

          size: Page size

          type: Filter by agent type (voice or chat)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "search": search,
                        "size": size,
                        "type": type,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDeleteResponse:
        """
        Delete an agent by ID

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
        return self._delete(
            f"/org/{org_id}/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    def list_eval_runs(
        self,
        org_id: str,
        *,
        agent_id: str,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListEvalRunsResponse:
        """
        Get evaluation runs with pagination

        Args:
          agent_id: Agent ID

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/agents/eval-runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "page": page,
                        "size": size,
                    },
                    agent_list_eval_runs_params.AgentListEvalRunsParams,
                ),
            ),
            cast_to=AgentListEvalRunsResponse,
        )

    def run_specific_tests(
        self,
        agent_id: str,
        *,
        org_id: str,
        unit_test_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunTests:
        """
        Trigger execution of specific unit tests

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
            f"/org/{org_id}/agents/{agent_id}/run-specific-tests",
            body=maybe_transform(
                {"unit_test_ids": unit_test_ids}, agent_run_specific_tests_params.AgentRunSpecificTestsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunTests,
        )

    def run_tests(
        self,
        agent_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunTests:
        """
        Trigger execution of all unit tests for an agent

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
            f"/org/{org_id}/agents/{agent_id}/run-tests",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunTests,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def sip_trunks(self) -> AsyncSipTrunksResource:
        return AsyncSipTrunksResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def unit_test_runs(self) -> AsyncUnitTestRunsResource:
        return AsyncUnitTestRunsResource(self._client)

    @cached_property
    def unit_tests(self) -> AsyncUnitTestsResource:
        return AsyncUnitTestsResource(self._client)

    @cached_property
    def evals(self) -> AsyncEvalsResource:
        return AsyncEvalsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        name: str,
        prompt_template: str,
        type: Literal["voice", "chat", "video"],
        allowed_sip_trunks: SequenceNotStr[str] | Omit = omit,
        background_sound: BackgroundSoundConfigParam | Omit = omit,
        goodbye_config: GoodbyeConfigParam | Omit = omit,
        greeting_config: Dict[str, object] | Omit = omit,
        llm_config: Dict[str, object] | Omit = omit,
        plugins: Iterable[object] | Omit = omit,
        precall_webhook: RecallWebhookParam | Omit = omit,
        transcriber_config: Dict[str, object] | Omit = omit,
        vad_config: Dict[str, object] | Omit = omit,
        voice_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Create a new AI agent in the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/agents",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "prompt_template": prompt_template,
                    "type": type,
                    "allowed_sip_trunks": allowed_sip_trunks,
                    "background_sound": background_sound,
                    "goodbye_config": goodbye_config,
                    "greeting_config": greeting_config,
                    "llm_config": llm_config,
                    "plugins": plugins,
                    "precall_webhook": precall_webhook,
                    "transcriber_config": transcriber_config,
                    "vad_config": vad_config,
                    "voice_config": voice_config,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Get agent details by ID

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
        return await self._get(
            f"/org/{org_id}/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def update(
        self,
        agent_id: str,
        *,
        org_id: str,
        allowed_sip_trunks: SequenceNotStr[str] | Omit = omit,
        background_sound: BackgroundSoundConfigParam | Omit = omit,
        goodbye_config: GoodbyeConfigParam | Omit = omit,
        greeting_config: Dict[str, object] | Omit = omit,
        llm_config: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        plugins: Iterable[object] | Omit = omit,
        precall_webhook: RecallWebhookParam | Omit = omit,
        prompt_template: str | Omit = omit,
        transcriber_config: Dict[str, object] | Omit = omit,
        type: Literal["voice", "chat", "video"] | Omit = omit,
        vad_config: Dict[str, object] | Omit = omit,
        voice_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Update agent details (partial update)

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
        return await self._patch(
            f"/org/{org_id}/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "allowed_sip_trunks": allowed_sip_trunks,
                    "background_sound": background_sound,
                    "goodbye_config": goodbye_config,
                    "greeting_config": greeting_config,
                    "llm_config": llm_config,
                    "name": name,
                    "plugins": plugins,
                    "precall_webhook": precall_webhook,
                    "prompt_template": prompt_template,
                    "transcriber_config": transcriber_config,
                    "type": type,
                    "vad_config": vad_config,
                    "voice_config": voice_config,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def list(
        self,
        org_id: str,
        *,
        page: int | Omit = omit,
        search: str | Omit = omit,
        size: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Get a paginated list of agents for the organization

        Args:
          page: Page number

          search: Search by agent name

          size: Page size

          type: Filter by agent type (voice or chat)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "search": search,
                        "size": size,
                        "type": type,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDeleteResponse:
        """
        Delete an agent by ID

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
        return await self._delete(
            f"/org/{org_id}/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDeleteResponse,
        )

    async def list_eval_runs(
        self,
        org_id: str,
        *,
        agent_id: str,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListEvalRunsResponse:
        """
        Get evaluation runs with pagination

        Args:
          agent_id: Agent ID

          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/agents/eval-runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "page": page,
                        "size": size,
                    },
                    agent_list_eval_runs_params.AgentListEvalRunsParams,
                ),
            ),
            cast_to=AgentListEvalRunsResponse,
        )

    async def run_specific_tests(
        self,
        agent_id: str,
        *,
        org_id: str,
        unit_test_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunTests:
        """
        Trigger execution of specific unit tests

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
            f"/org/{org_id}/agents/{agent_id}/run-specific-tests",
            body=await async_maybe_transform(
                {"unit_test_ids": unit_test_ids}, agent_run_specific_tests_params.AgentRunSpecificTestsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunTests,
        )

    async def run_tests(
        self,
        agent_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunTests:
        """
        Trigger execution of all unit tests for an agent

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
            f"/org/{org_id}/agents/{agent_id}/run-tests",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunTests,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.list_eval_runs = to_raw_response_wrapper(
            agents.list_eval_runs,
        )
        self.run_specific_tests = to_raw_response_wrapper(
            agents.run_specific_tests,
        )
        self.run_tests = to_raw_response_wrapper(
            agents.run_tests,
        )

    @cached_property
    def sip_trunks(self) -> SipTrunksResourceWithRawResponse:
        return SipTrunksResourceWithRawResponse(self._agents.sip_trunks)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def unit_test_runs(self) -> UnitTestRunsResourceWithRawResponse:
        return UnitTestRunsResourceWithRawResponse(self._agents.unit_test_runs)

    @cached_property
    def unit_tests(self) -> UnitTestsResourceWithRawResponse:
        return UnitTestsResourceWithRawResponse(self._agents.unit_tests)

    @cached_property
    def evals(self) -> EvalsResourceWithRawResponse:
        return EvalsResourceWithRawResponse(self._agents.evals)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.list_eval_runs = async_to_raw_response_wrapper(
            agents.list_eval_runs,
        )
        self.run_specific_tests = async_to_raw_response_wrapper(
            agents.run_specific_tests,
        )
        self.run_tests = async_to_raw_response_wrapper(
            agents.run_tests,
        )

    @cached_property
    def sip_trunks(self) -> AsyncSipTrunksResourceWithRawResponse:
        return AsyncSipTrunksResourceWithRawResponse(self._agents.sip_trunks)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._agents.tools)

    @cached_property
    def unit_test_runs(self) -> AsyncUnitTestRunsResourceWithRawResponse:
        return AsyncUnitTestRunsResourceWithRawResponse(self._agents.unit_test_runs)

    @cached_property
    def unit_tests(self) -> AsyncUnitTestsResourceWithRawResponse:
        return AsyncUnitTestsResourceWithRawResponse(self._agents.unit_tests)

    @cached_property
    def evals(self) -> AsyncEvalsResourceWithRawResponse:
        return AsyncEvalsResourceWithRawResponse(self._agents.evals)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.list_eval_runs = to_streamed_response_wrapper(
            agents.list_eval_runs,
        )
        self.run_specific_tests = to_streamed_response_wrapper(
            agents.run_specific_tests,
        )
        self.run_tests = to_streamed_response_wrapper(
            agents.run_tests,
        )

    @cached_property
    def sip_trunks(self) -> SipTrunksResourceWithStreamingResponse:
        return SipTrunksResourceWithStreamingResponse(self._agents.sip_trunks)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def unit_test_runs(self) -> UnitTestRunsResourceWithStreamingResponse:
        return UnitTestRunsResourceWithStreamingResponse(self._agents.unit_test_runs)

    @cached_property
    def unit_tests(self) -> UnitTestsResourceWithStreamingResponse:
        return UnitTestsResourceWithStreamingResponse(self._agents.unit_tests)

    @cached_property
    def evals(self) -> EvalsResourceWithStreamingResponse:
        return EvalsResourceWithStreamingResponse(self._agents.evals)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.list_eval_runs = async_to_streamed_response_wrapper(
            agents.list_eval_runs,
        )
        self.run_specific_tests = async_to_streamed_response_wrapper(
            agents.run_specific_tests,
        )
        self.run_tests = async_to_streamed_response_wrapper(
            agents.run_tests,
        )

    @cached_property
    def sip_trunks(self) -> AsyncSipTrunksResourceWithStreamingResponse:
        return AsyncSipTrunksResourceWithStreamingResponse(self._agents.sip_trunks)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._agents.tools)

    @cached_property
    def unit_test_runs(self) -> AsyncUnitTestRunsResourceWithStreamingResponse:
        return AsyncUnitTestRunsResourceWithStreamingResponse(self._agents.unit_test_runs)

    @cached_property
    def unit_tests(self) -> AsyncUnitTestsResourceWithStreamingResponse:
        return AsyncUnitTestsResourceWithStreamingResponse(self._agents.unit_tests)

    @cached_property
    def evals(self) -> AsyncEvalsResourceWithStreamingResponse:
        return AsyncEvalsResourceWithStreamingResponse(self._agents.evals)
