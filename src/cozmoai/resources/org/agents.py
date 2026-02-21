# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.org import (
    agent_list_params,
    agent_create_params,
    agent_update_params,
)
from ..._base_client import make_request_options
from ...types.org.agent_response import AgentResponse
from ...types.org.llm_config_param import LlmConfigParam
from ...types.org.vad_config_param import VadConfigParam
from ...types.org.extra_config_param import ExtraConfigParam
from ...types.org.voice_config_param import VoiceConfigParam
from ...types.org.agent_list_response import AgentListResponse
from ...types.org.goodbye_config_param import GoodbyeConfigParam
from ...types.org.agent_delete_response import AgentDeleteResponse
from ...types.org.greeting_config_param import GreetingConfigParam
from ...types.org.transcriber_config_param import TranscriberConfigParam
from ...types.org.room_duration_config_param import RoomDurationConfigParam
from ...types.org.background_sound_config_param import BackgroundSoundConfigParam

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
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
        extra_config: ExtraConfigParam | Omit = omit,
        goodbye_config: GoodbyeConfigParam | Omit = omit,
        greeting_config: GreetingConfigParam | Omit = omit,
        llm_config: LlmConfigParam | Omit = omit,
        plugins: Iterable[object] | Omit = omit,
        precall_webhook: agent_create_params.PrecallWebhook | Omit = omit,
        room_duration_config: RoomDurationConfigParam | Omit = omit,
        transcriber_config: TranscriberConfigParam | Omit = omit,
        vad_config: VadConfigParam | Omit = omit,
        voice_config: VoiceConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
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
                    "extra_config": extra_config,
                    "goodbye_config": goodbye_config,
                    "greeting_config": greeting_config,
                    "llm_config": llm_config,
                    "plugins": plugins,
                    "precall_webhook": precall_webhook,
                    "room_duration_config": room_duration_config,
                    "transcriber_config": transcriber_config,
                    "vad_config": vad_config,
                    "voice_config": voice_config,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
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
    ) -> AgentResponse:
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
            cast_to=AgentResponse,
        )

    def update(
        self,
        agent_id: str,
        *,
        org_id: str,
        allowed_sip_trunks: SequenceNotStr[str] | Omit = omit,
        background_sound: BackgroundSoundConfigParam | Omit = omit,
        extra_config: ExtraConfigParam | Omit = omit,
        goodbye_config: GoodbyeConfigParam | Omit = omit,
        greeting_config: GreetingConfigParam | Omit = omit,
        llm_config: LlmConfigParam | Omit = omit,
        name: str | Omit = omit,
        plugins: Iterable[object] | Omit = omit,
        precall_webhook: agent_update_params.PrecallWebhook | Omit = omit,
        prompt_template: str | Omit = omit,
        room_duration_config: RoomDurationConfigParam | Omit = omit,
        transcriber_config: TranscriberConfigParam | Omit = omit,
        type: Literal["voice", "chat", "video"] | Omit = omit,
        vad_config: VadConfigParam | Omit = omit,
        voice_config: VoiceConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
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
                    "extra_config": extra_config,
                    "goodbye_config": goodbye_config,
                    "greeting_config": greeting_config,
                    "llm_config": llm_config,
                    "name": name,
                    "plugins": plugins,
                    "precall_webhook": precall_webhook,
                    "prompt_template": prompt_template,
                    "room_duration_config": room_duration_config,
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
            cast_to=AgentResponse,
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


class AsyncAgentsResource(AsyncAPIResource):
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
        extra_config: ExtraConfigParam | Omit = omit,
        goodbye_config: GoodbyeConfigParam | Omit = omit,
        greeting_config: GreetingConfigParam | Omit = omit,
        llm_config: LlmConfigParam | Omit = omit,
        plugins: Iterable[object] | Omit = omit,
        precall_webhook: agent_create_params.PrecallWebhook | Omit = omit,
        room_duration_config: RoomDurationConfigParam | Omit = omit,
        transcriber_config: TranscriberConfigParam | Omit = omit,
        vad_config: VadConfigParam | Omit = omit,
        voice_config: VoiceConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
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
                    "extra_config": extra_config,
                    "goodbye_config": goodbye_config,
                    "greeting_config": greeting_config,
                    "llm_config": llm_config,
                    "plugins": plugins,
                    "precall_webhook": precall_webhook,
                    "room_duration_config": room_duration_config,
                    "transcriber_config": transcriber_config,
                    "vad_config": vad_config,
                    "voice_config": voice_config,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
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
    ) -> AgentResponse:
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
            cast_to=AgentResponse,
        )

    async def update(
        self,
        agent_id: str,
        *,
        org_id: str,
        allowed_sip_trunks: SequenceNotStr[str] | Omit = omit,
        background_sound: BackgroundSoundConfigParam | Omit = omit,
        extra_config: ExtraConfigParam | Omit = omit,
        goodbye_config: GoodbyeConfigParam | Omit = omit,
        greeting_config: GreetingConfigParam | Omit = omit,
        llm_config: LlmConfigParam | Omit = omit,
        name: str | Omit = omit,
        plugins: Iterable[object] | Omit = omit,
        precall_webhook: agent_update_params.PrecallWebhook | Omit = omit,
        prompt_template: str | Omit = omit,
        room_duration_config: RoomDurationConfigParam | Omit = omit,
        transcriber_config: TranscriberConfigParam | Omit = omit,
        type: Literal["voice", "chat", "video"] | Omit = omit,
        vad_config: VadConfigParam | Omit = omit,
        voice_config: VoiceConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
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
                    "extra_config": extra_config,
                    "goodbye_config": goodbye_config,
                    "greeting_config": greeting_config,
                    "llm_config": llm_config,
                    "name": name,
                    "plugins": plugins,
                    "precall_webhook": precall_webhook,
                    "prompt_template": prompt_template,
                    "room_duration_config": room_duration_config,
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
            cast_to=AgentResponse,
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
