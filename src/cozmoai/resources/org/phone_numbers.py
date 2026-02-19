# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
    phone_number_list_params,
    phone_number_create_params,
    phone_number_update_params,
    phone_number_create_bulk_params,
)
from ..._base_client import make_request_options
from ...types.org.phone_number_response import PhoneNumberResponse
from ...types.org.phone_number_list_response import PhoneNumberListResponse
from ...types.org.phone_number_delete_response import PhoneNumberDeleteResponse
from ...types.org.phone_number_create_bulk_response import PhoneNumberCreateBulkResponse

__all__ = ["PhoneNumbersResource", "AsyncPhoneNumbersResource"]


class PhoneNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return PhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return PhoneNumbersResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        number: str,
        sip_trunk_id: str,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Creates a new phone number and associates it with a SIP trunk

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/phone-numbers",
            body=maybe_transform(
                {
                    "number": number,
                    "sip_trunk_id": sip_trunk_id,
                    "label": label,
                },
                phone_number_create_params.PhoneNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    def retrieve(
        self,
        number_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Returns a phone number with its associated trunk information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not number_id:
            raise ValueError(f"Expected a non-empty value for `number_id` but received {number_id!r}")
        return self._get(
            f"/org/{org_id}/phone-numbers/{number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    def update(
        self,
        number_id: str,
        *,
        org_id: str,
        is_verified: bool | Omit = omit,
        label: str | Omit = omit,
        sip_trunk_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Updates the specified phone number's configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not number_id:
            raise ValueError(f"Expected a non-empty value for `number_id` but received {number_id!r}")
        return self._patch(
            f"/org/{org_id}/phone-numbers/{number_id}",
            body=maybe_transform(
                {
                    "is_verified": is_verified,
                    "label": label,
                    "sip_trunk_id": sip_trunk_id,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    def list(
        self,
        org_id: str,
        *,
        direction: Literal["inbound", "outbound"] | Omit = omit,
        is_verified: bool | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sip_trunk_id: str | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberListResponse:
        """
        Returns a paginated list of phone numbers for the organization

        Args:
          direction: Filter by SIP trunk type/direction

          is_verified: Filter by verification status

          page: Page number

          search: Search by number or label

          sip_trunk_id: Filter by SIP trunk ID

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/phone-numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "is_verified": is_verified,
                        "page": page,
                        "search": search,
                        "sip_trunk_id": sip_trunk_id,
                        "size": size,
                    },
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            cast_to=PhoneNumberListResponse,
        )

    def delete(
        self,
        number_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberDeleteResponse:
        """
        Deletes the specified phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not number_id:
            raise ValueError(f"Expected a non-empty value for `number_id` but received {number_id!r}")
        return self._delete(
            f"/org/{org_id}/phone-numbers/{number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberDeleteResponse,
        )

    def create_bulk(
        self,
        org_id: str,
        *,
        numbers: Iterable[phone_number_create_bulk_params.Number],
        sip_trunk_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberCreateBulkResponse:
        """
        Creates multiple phone numbers and associates them with a SIP trunk

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/phone-numbers/bulk",
            body=maybe_transform(
                {
                    "numbers": numbers,
                    "sip_trunk_id": sip_trunk_id,
                },
                phone_number_create_bulk_params.PhoneNumberCreateBulkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCreateBulkResponse,
        )


class AsyncPhoneNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncPhoneNumbersResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        number: str,
        sip_trunk_id: str,
        label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Creates a new phone number and associates it with a SIP trunk

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/phone-numbers",
            body=await async_maybe_transform(
                {
                    "number": number,
                    "sip_trunk_id": sip_trunk_id,
                    "label": label,
                },
                phone_number_create_params.PhoneNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    async def retrieve(
        self,
        number_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Returns a phone number with its associated trunk information

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not number_id:
            raise ValueError(f"Expected a non-empty value for `number_id` but received {number_id!r}")
        return await self._get(
            f"/org/{org_id}/phone-numbers/{number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    async def update(
        self,
        number_id: str,
        *,
        org_id: str,
        is_verified: bool | Omit = omit,
        label: str | Omit = omit,
        sip_trunk_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Updates the specified phone number's configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not number_id:
            raise ValueError(f"Expected a non-empty value for `number_id` but received {number_id!r}")
        return await self._patch(
            f"/org/{org_id}/phone-numbers/{number_id}",
            body=await async_maybe_transform(
                {
                    "is_verified": is_verified,
                    "label": label,
                    "sip_trunk_id": sip_trunk_id,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    async def list(
        self,
        org_id: str,
        *,
        direction: Literal["inbound", "outbound"] | Omit = omit,
        is_verified: bool | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sip_trunk_id: str | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberListResponse:
        """
        Returns a paginated list of phone numbers for the organization

        Args:
          direction: Filter by SIP trunk type/direction

          is_verified: Filter by verification status

          page: Page number

          search: Search by number or label

          sip_trunk_id: Filter by SIP trunk ID

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/phone-numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "is_verified": is_verified,
                        "page": page,
                        "search": search,
                        "sip_trunk_id": sip_trunk_id,
                        "size": size,
                    },
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            cast_to=PhoneNumberListResponse,
        )

    async def delete(
        self,
        number_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberDeleteResponse:
        """
        Deletes the specified phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not number_id:
            raise ValueError(f"Expected a non-empty value for `number_id` but received {number_id!r}")
        return await self._delete(
            f"/org/{org_id}/phone-numbers/{number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberDeleteResponse,
        )

    async def create_bulk(
        self,
        org_id: str,
        *,
        numbers: Iterable[phone_number_create_bulk_params.Number],
        sip_trunk_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberCreateBulkResponse:
        """
        Creates multiple phone numbers and associates them with a SIP trunk

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/phone-numbers/bulk",
            body=await async_maybe_transform(
                {
                    "numbers": numbers,
                    "sip_trunk_id": sip_trunk_id,
                },
                phone_number_create_bulk_params.PhoneNumberCreateBulkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberCreateBulkResponse,
        )


class PhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.create = to_raw_response_wrapper(
            phone_numbers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.delete = to_raw_response_wrapper(
            phone_numbers.delete,
        )
        self.create_bulk = to_raw_response_wrapper(
            phone_numbers.create_bulk,
        )


class AsyncPhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.create = async_to_raw_response_wrapper(
            phone_numbers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            phone_numbers.delete,
        )
        self.create_bulk = async_to_raw_response_wrapper(
            phone_numbers.create_bulk,
        )


class PhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.create = to_streamed_response_wrapper(
            phone_numbers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.delete = to_streamed_response_wrapper(
            phone_numbers.delete,
        )
        self.create_bulk = to_streamed_response_wrapper(
            phone_numbers.create_bulk,
        )


class AsyncPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.create = async_to_streamed_response_wrapper(
            phone_numbers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            phone_numbers.delete,
        )
        self.create_bulk = async_to_streamed_response_wrapper(
            phone_numbers.create_bulk,
        )
