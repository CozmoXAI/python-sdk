# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.org import sip_trunk_update_params, sip_trunk_sip_trunks_params, sip_trunk_retrieve_sip_trunks_params
from ..._base_client import make_request_options
from ...types.org.sip_trunk_response import SipTrunkResponse
from ...types.org.sip_trunk_delete_response import SipTrunkDeleteResponse
from ...types.org.sip_trunk_retrieve_response import SipTrunkRetrieveResponse
from ...types.org.sip_trunk_sip_trunks_response import SipTrunkSipTrunksResponse
from ...types.org.sip_trunk_retrieve_sip_trunks_response import SipTrunkRetrieveSipTrunksResponse

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

    def retrieve(
        self,
        trunk_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkRetrieveResponse:
        """
        Returns a SIP trunk with its associated phone numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not trunk_id:
            raise ValueError(f"Expected a non-empty value for `trunk_id` but received {trunk_id!r}")
        return self._get(
            f"/org/{org_id}/sip-trunks/{trunk_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkRetrieveResponse,
        )

    def update(
        self,
        trunk_id: str,
        *,
        org_id: str,
        is_active: bool | Omit = omit,
        max_concurrency: int | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkResponse:
        """
        Updates the specified SIP trunk's configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not trunk_id:
            raise ValueError(f"Expected a non-empty value for `trunk_id` but received {trunk_id!r}")
        return self._patch(
            f"/org/{org_id}/sip-trunks/{trunk_id}",
            body=maybe_transform(
                {
                    "is_active": is_active,
                    "max_concurrency": max_concurrency,
                    "name": name,
                },
                sip_trunk_update_params.SipTrunkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkResponse,
        )

    def delete(
        self,
        trunk_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkDeleteResponse:
        """
        Deletes the specified SIP trunk and its associated phone numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not trunk_id:
            raise ValueError(f"Expected a non-empty value for `trunk_id` but received {trunk_id!r}")
        return self._delete(
            f"/org/{org_id}/sip-trunks/{trunk_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkDeleteResponse,
        )

    def retrieve_sip_trunks(
        self,
        org_id: str,
        *,
        is_active: bool | Omit = omit,
        page: int | Omit = omit,
        provider: str | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkRetrieveSipTrunksResponse:
        """
        Returns a paginated list of SIP trunks for the organization

        Args:
          is_active: Filter by active status

          page: Page number

          provider: Filter by provider (TWILIO, TELNYX, VONAGE, GENERIC)

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/sip-trunks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_active": is_active,
                        "page": page,
                        "provider": provider,
                        "size": size,
                    },
                    sip_trunk_retrieve_sip_trunks_params.SipTrunkRetrieveSipTrunksParams,
                ),
            ),
            cast_to=SipTrunkRetrieveSipTrunksResponse,
        )

    def sip_trunks(
        self,
        org_id: str,
        *,
        address: str,
        name: str,
        phone_numbers: SequenceNotStr[str],
        provider: Literal["twilio", "telnyx", "custom", "did-logic", "vonage", "other"],
        auth_password: str | Omit = omit,
        auth_username: str | Omit = omit,
        max_concurrency: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkSipTrunksResponse:
        """
        Creates a new SIP trunk pair (inbound and outbound) with the specified phone
        numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/sip-trunks",
            body=maybe_transform(
                {
                    "address": address,
                    "name": name,
                    "phone_numbers": phone_numbers,
                    "provider": provider,
                    "auth_password": auth_password,
                    "auth_username": auth_username,
                    "max_concurrency": max_concurrency,
                },
                sip_trunk_sip_trunks_params.SipTrunkSipTrunksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkSipTrunksResponse,
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

    async def retrieve(
        self,
        trunk_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkRetrieveResponse:
        """
        Returns a SIP trunk with its associated phone numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not trunk_id:
            raise ValueError(f"Expected a non-empty value for `trunk_id` but received {trunk_id!r}")
        return await self._get(
            f"/org/{org_id}/sip-trunks/{trunk_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkRetrieveResponse,
        )

    async def update(
        self,
        trunk_id: str,
        *,
        org_id: str,
        is_active: bool | Omit = omit,
        max_concurrency: int | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkResponse:
        """
        Updates the specified SIP trunk's configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not trunk_id:
            raise ValueError(f"Expected a non-empty value for `trunk_id` but received {trunk_id!r}")
        return await self._patch(
            f"/org/{org_id}/sip-trunks/{trunk_id}",
            body=await async_maybe_transform(
                {
                    "is_active": is_active,
                    "max_concurrency": max_concurrency,
                    "name": name,
                },
                sip_trunk_update_params.SipTrunkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkResponse,
        )

    async def delete(
        self,
        trunk_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkDeleteResponse:
        """
        Deletes the specified SIP trunk and its associated phone numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not trunk_id:
            raise ValueError(f"Expected a non-empty value for `trunk_id` but received {trunk_id!r}")
        return await self._delete(
            f"/org/{org_id}/sip-trunks/{trunk_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkDeleteResponse,
        )

    async def retrieve_sip_trunks(
        self,
        org_id: str,
        *,
        is_active: bool | Omit = omit,
        page: int | Omit = omit,
        provider: str | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkRetrieveSipTrunksResponse:
        """
        Returns a paginated list of SIP trunks for the organization

        Args:
          is_active: Filter by active status

          page: Page number

          provider: Filter by provider (TWILIO, TELNYX, VONAGE, GENERIC)

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/sip-trunks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_active": is_active,
                        "page": page,
                        "provider": provider,
                        "size": size,
                    },
                    sip_trunk_retrieve_sip_trunks_params.SipTrunkRetrieveSipTrunksParams,
                ),
            ),
            cast_to=SipTrunkRetrieveSipTrunksResponse,
        )

    async def sip_trunks(
        self,
        org_id: str,
        *,
        address: str,
        name: str,
        phone_numbers: SequenceNotStr[str],
        provider: Literal["twilio", "telnyx", "custom", "did-logic", "vonage", "other"],
        auth_password: str | Omit = omit,
        auth_username: str | Omit = omit,
        max_concurrency: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SipTrunkSipTrunksResponse:
        """
        Creates a new SIP trunk pair (inbound and outbound) with the specified phone
        numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/sip-trunks",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "name": name,
                    "phone_numbers": phone_numbers,
                    "provider": provider,
                    "auth_password": auth_password,
                    "auth_username": auth_username,
                    "max_concurrency": max_concurrency,
                },
                sip_trunk_sip_trunks_params.SipTrunkSipTrunksParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SipTrunkSipTrunksResponse,
        )


class SipTrunksResourceWithRawResponse:
    def __init__(self, sip_trunks: SipTrunksResource) -> None:
        self._sip_trunks = sip_trunks

        self.retrieve = to_raw_response_wrapper(
            sip_trunks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sip_trunks.update,
        )
        self.delete = to_raw_response_wrapper(
            sip_trunks.delete,
        )
        self.retrieve_sip_trunks = to_raw_response_wrapper(
            sip_trunks.retrieve_sip_trunks,
        )
        self.sip_trunks = to_raw_response_wrapper(
            sip_trunks.sip_trunks,
        )


class AsyncSipTrunksResourceWithRawResponse:
    def __init__(self, sip_trunks: AsyncSipTrunksResource) -> None:
        self._sip_trunks = sip_trunks

        self.retrieve = async_to_raw_response_wrapper(
            sip_trunks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sip_trunks.update,
        )
        self.delete = async_to_raw_response_wrapper(
            sip_trunks.delete,
        )
        self.retrieve_sip_trunks = async_to_raw_response_wrapper(
            sip_trunks.retrieve_sip_trunks,
        )
        self.sip_trunks = async_to_raw_response_wrapper(
            sip_trunks.sip_trunks,
        )


class SipTrunksResourceWithStreamingResponse:
    def __init__(self, sip_trunks: SipTrunksResource) -> None:
        self._sip_trunks = sip_trunks

        self.retrieve = to_streamed_response_wrapper(
            sip_trunks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sip_trunks.update,
        )
        self.delete = to_streamed_response_wrapper(
            sip_trunks.delete,
        )
        self.retrieve_sip_trunks = to_streamed_response_wrapper(
            sip_trunks.retrieve_sip_trunks,
        )
        self.sip_trunks = to_streamed_response_wrapper(
            sip_trunks.sip_trunks,
        )


class AsyncSipTrunksResourceWithStreamingResponse:
    def __init__(self, sip_trunks: AsyncSipTrunksResource) -> None:
        self._sip_trunks = sip_trunks

        self.retrieve = async_to_streamed_response_wrapper(
            sip_trunks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sip_trunks.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            sip_trunks.delete,
        )
        self.retrieve_sip_trunks = async_to_streamed_response_wrapper(
            sip_trunks.retrieve_sip_trunks,
        )
        self.sip_trunks = async_to_streamed_response_wrapper(
            sip_trunks.sip_trunks,
        )
