# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.org.agents import sip_trunk_add_params
from ....types.org.agents.sip_trunk_add_response import SipTrunkAddResponse
from ....types.org.agents.sip_trunk_list_response import SipTrunkListResponse
from ....types.org.agents.sip_trunk_remove_response import SipTrunkRemoveResponse

__all__ = ["SipTrunksResource", "AsyncSipTrunksResource"]


class SipTrunksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SipTrunksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return SipTrunksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SipTrunksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return SipTrunksResourceWithStreamingResponse(self)

    def list(
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
    ) -> SipTrunkListResponse:
        """
        Get all inbound SIP trunks allowed for an agent

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
            f"/org/{org_id}/agents/{agent_id}/sip-trunks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkListResponse,
        )

    def add(
        self,
        agent_id: str,
        *,
        org_id: str,
        sip_trunk_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkAddResponse:
        """Add an inbound SIP trunk to an agent's allowed list.

        Only INBOUND trunks can be
        added.

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
            f"/org/{org_id}/agents/{agent_id}/sip-trunks",
            body=maybe_transform({"sip_trunk_id": sip_trunk_id}, sip_trunk_add_params.SipTrunkAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkAddResponse,
        )

    def remove(
        self,
        trunk_id: str,
        *,
        org_id: str,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkRemoveResponse:
        """
        Remove a SIP trunk from an agent's allowed list

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
        if not trunk_id:
            raise ValueError(f"Expected a non-empty value for `trunk_id` but received {trunk_id!r}")
        return self._delete(
            f"/org/{org_id}/agents/{agent_id}/sip-trunks/{trunk_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkRemoveResponse,
        )


class AsyncSipTrunksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSipTrunksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSipTrunksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSipTrunksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncSipTrunksResourceWithStreamingResponse(self)

    async def list(
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
    ) -> SipTrunkListResponse:
        """
        Get all inbound SIP trunks allowed for an agent

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
            f"/org/{org_id}/agents/{agent_id}/sip-trunks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkListResponse,
        )

    async def add(
        self,
        agent_id: str,
        *,
        org_id: str,
        sip_trunk_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkAddResponse:
        """Add an inbound SIP trunk to an agent's allowed list.

        Only INBOUND trunks can be
        added.

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
            f"/org/{org_id}/agents/{agent_id}/sip-trunks",
            body=await async_maybe_transform({"sip_trunk_id": sip_trunk_id}, sip_trunk_add_params.SipTrunkAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkAddResponse,
        )

    async def remove(
        self,
        trunk_id: str,
        *,
        org_id: str,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkRemoveResponse:
        """
        Remove a SIP trunk from an agent's allowed list

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
        if not trunk_id:
            raise ValueError(f"Expected a non-empty value for `trunk_id` but received {trunk_id!r}")
        return await self._delete(
            f"/org/{org_id}/agents/{agent_id}/sip-trunks/{trunk_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkRemoveResponse,
        )


class SipTrunksResourceWithRawResponse:
    def __init__(self, sip_trunks: SipTrunksResource) -> None:
        self._sip_trunks = sip_trunks

        self.list = to_raw_response_wrapper(
            sip_trunks.list,
        )
        self.add = to_raw_response_wrapper(
            sip_trunks.add,
        )
        self.remove = to_raw_response_wrapper(
            sip_trunks.remove,
        )


class AsyncSipTrunksResourceWithRawResponse:
    def __init__(self, sip_trunks: AsyncSipTrunksResource) -> None:
        self._sip_trunks = sip_trunks

        self.list = async_to_raw_response_wrapper(
            sip_trunks.list,
        )
        self.add = async_to_raw_response_wrapper(
            sip_trunks.add,
        )
        self.remove = async_to_raw_response_wrapper(
            sip_trunks.remove,
        )


class SipTrunksResourceWithStreamingResponse:
    def __init__(self, sip_trunks: SipTrunksResource) -> None:
        self._sip_trunks = sip_trunks

        self.list = to_streamed_response_wrapper(
            sip_trunks.list,
        )
        self.add = to_streamed_response_wrapper(
            sip_trunks.add,
        )
        self.remove = to_streamed_response_wrapper(
            sip_trunks.remove,
        )


class AsyncSipTrunksResourceWithStreamingResponse:
    def __init__(self, sip_trunks: AsyncSipTrunksResource) -> None:
        self._sip_trunks = sip_trunks

        self.list = async_to_streamed_response_wrapper(
            sip_trunks.list,
        )
        self.add = async_to_streamed_response_wrapper(
            sip_trunks.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            sip_trunks.remove,
        )
