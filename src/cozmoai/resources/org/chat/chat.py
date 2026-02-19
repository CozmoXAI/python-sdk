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
from ....types.org import chat_send_message_params
from .conversations import (
    ConversationsResource,
    AsyncConversationsResource,
    ConversationsResourceWithRawResponse,
    AsyncConversationsResourceWithRawResponse,
    ConversationsResourceWithStreamingResponse,
    AsyncConversationsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.org.chat_send_message_response import ChatSendMessageResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def conversations(self) -> ConversationsResource:
        return ConversationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def send_message(
        self,
        org_id: str,
        *,
        message: str,
        conversation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSendMessageResponse:
        """
        Send a message to the analytics chat assistant and receive an AI-generated
        response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/chat",
            body=maybe_transform(
                {
                    "message": message,
                    "conversation_id": conversation_id,
                },
                chat_send_message_params.ChatSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSendMessageResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        return AsyncConversationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def send_message(
        self,
        org_id: str,
        *,
        message: str,
        conversation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSendMessageResponse:
        """
        Send a message to the analytics chat assistant and receive an AI-generated
        response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/chat",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "conversation_id": conversation_id,
                },
                chat_send_message_params.ChatSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSendMessageResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.send_message = to_raw_response_wrapper(
            chat.send_message,
        )

    @cached_property
    def conversations(self) -> ConversationsResourceWithRawResponse:
        return ConversationsResourceWithRawResponse(self._chat.conversations)


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.send_message = async_to_raw_response_wrapper(
            chat.send_message,
        )

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithRawResponse:
        return AsyncConversationsResourceWithRawResponse(self._chat.conversations)


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.send_message = to_streamed_response_wrapper(
            chat.send_message,
        )

    @cached_property
    def conversations(self) -> ConversationsResourceWithStreamingResponse:
        return ConversationsResourceWithStreamingResponse(self._chat.conversations)


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.send_message = async_to_streamed_response_wrapper(
            chat.send_message,
        )

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithStreamingResponse:
        return AsyncConversationsResourceWithStreamingResponse(self._chat.conversations)
