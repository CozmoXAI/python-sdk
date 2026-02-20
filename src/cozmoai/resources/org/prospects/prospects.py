# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .bulk import (
    BulkResource,
    AsyncBulkResource,
    BulkResourceWithRawResponse,
    AsyncBulkResourceWithRawResponse,
    BulkResourceWithStreamingResponse,
    AsyncBulkResourceWithStreamingResponse,
)
from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
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
from ....types.org import (
    prospect_list_params,
    prospect_create_params,
    prospect_update_params,
    prospect_list_calls_params,
)
from ...._base_client import make_request_options
from ....types.org.response_error import ResponseError
from ....types.org.prospect_response import ProspectResponse
from ....types.org.prospect_list_response import ProspectListResponse
from ....types.org.prospect_list_calls_response import ProspectListCallsResponse

__all__ = ["ProspectsResource", "AsyncProspectsResource"]


class ProspectsResource(SyncAPIResource):
    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def bulk(self) -> BulkResource:
        return BulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProspectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ProspectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProspectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return ProspectsResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        phone: str,
        country: str | Omit = omit,
        custom_data: Dict[str, object] | Omit = omit,
        email: str | Omit = omit,
        external_id: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        status: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectResponse:
        """Create a new prospect in the organization.

        Country and timezone are
        auto-detected from phone if not provided.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/prospects",
            body=maybe_transform(
                {
                    "phone": phone,
                    "country": country,
                    "custom_data": custom_data,
                    "email": email,
                    "external_id": external_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "status": status,
                    "timezone": timezone,
                },
                prospect_create_params.ProspectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectResponse,
        )

    def retrieve(
        self,
        prospect_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectResponse:
        """
        Get a single prospect by ID with associated tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return self._get(
            f"/org/{org_id}/prospects/{prospect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectResponse,
        )

    def update(
        self,
        prospect_id: str,
        *,
        org_id: str,
        country: str | Omit = omit,
        custom_data: Dict[str, object] | Omit = omit,
        email: str | Omit = omit,
        external_id: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        list_id: str | Omit = omit,
        phone: str | Omit = omit,
        status: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectResponse:
        """Update prospect information.

        Supports partial updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return self._patch(
            f"/org/{org_id}/prospects/{prospect_id}",
            body=maybe_transform(
                {
                    "country": country,
                    "custom_data": custom_data,
                    "email": email,
                    "external_id": external_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "list_id": list_id,
                    "phone": phone,
                    "status": status,
                    "timezone": timezone,
                },
                prospect_update_params.ProspectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectResponse,
        )

    def list(
        self,
        org_id: str,
        *,
        country: str | Omit = omit,
        list_id: str | Omit = omit,
        no_list: bool | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        size: int | Omit = omit,
        status: str | Omit = omit,
        tag_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectListResponse:
        """
        Get a paginated list of prospects with optional filters

        Args:
          country: Filter by country code

          list_id: Filter by prospect list ID

          no_list: Filter prospects without a list

          page: Page number

          search: Search in name, phone, email

          size: Page size

          status: Filter by status

          tag_id: Filter by tag ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/prospects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "list_id": list_id,
                        "no_list": no_list,
                        "page": page,
                        "search": search,
                        "size": size,
                        "status": status,
                        "tag_id": tag_id,
                    },
                    prospect_list_params.ProspectListParams,
                ),
            ),
            cast_to=ProspectListResponse,
        )

    def delete(
        self,
        prospect_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseError:
        """
        Soft delete a prospect (sets deleted_at timestamp)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return self._delete(
            f"/org/{org_id}/prospects/{prospect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )

    def list_calls(
        self,
        prospect_id: str,
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
    ) -> ProspectListCallsResponse:
        """
        Returns a paginated list of calls for a specific prospect

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
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return self._get(
            f"/org/{org_id}/prospects/{prospect_id}/calls",
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
                    prospect_list_calls_params.ProspectListCallsParams,
                ),
            ),
            cast_to=ProspectListCallsResponse,
        )


class AsyncProspectsResource(AsyncAPIResource):
    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def bulk(self) -> AsyncBulkResource:
        return AsyncBulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProspectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProspectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProspectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncProspectsResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        phone: str,
        country: str | Omit = omit,
        custom_data: Dict[str, object] | Omit = omit,
        email: str | Omit = omit,
        external_id: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        status: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectResponse:
        """Create a new prospect in the organization.

        Country and timezone are
        auto-detected from phone if not provided.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/prospects",
            body=await async_maybe_transform(
                {
                    "phone": phone,
                    "country": country,
                    "custom_data": custom_data,
                    "email": email,
                    "external_id": external_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "status": status,
                    "timezone": timezone,
                },
                prospect_create_params.ProspectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectResponse,
        )

    async def retrieve(
        self,
        prospect_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectResponse:
        """
        Get a single prospect by ID with associated tags

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return await self._get(
            f"/org/{org_id}/prospects/{prospect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectResponse,
        )

    async def update(
        self,
        prospect_id: str,
        *,
        org_id: str,
        country: str | Omit = omit,
        custom_data: Dict[str, object] | Omit = omit,
        email: str | Omit = omit,
        external_id: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        list_id: str | Omit = omit,
        phone: str | Omit = omit,
        status: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectResponse:
        """Update prospect information.

        Supports partial updates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return await self._patch(
            f"/org/{org_id}/prospects/{prospect_id}",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "custom_data": custom_data,
                    "email": email,
                    "external_id": external_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "list_id": list_id,
                    "phone": phone,
                    "status": status,
                    "timezone": timezone,
                },
                prospect_update_params.ProspectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectResponse,
        )

    async def list(
        self,
        org_id: str,
        *,
        country: str | Omit = omit,
        list_id: str | Omit = omit,
        no_list: bool | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        size: int | Omit = omit,
        status: str | Omit = omit,
        tag_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectListResponse:
        """
        Get a paginated list of prospects with optional filters

        Args:
          country: Filter by country code

          list_id: Filter by prospect list ID

          no_list: Filter prospects without a list

          page: Page number

          search: Search in name, phone, email

          size: Page size

          status: Filter by status

          tag_id: Filter by tag ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/prospects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "list_id": list_id,
                        "no_list": no_list,
                        "page": page,
                        "search": search,
                        "size": size,
                        "status": status,
                        "tag_id": tag_id,
                    },
                    prospect_list_params.ProspectListParams,
                ),
            ),
            cast_to=ProspectListResponse,
        )

    async def delete(
        self,
        prospect_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseError:
        """
        Soft delete a prospect (sets deleted_at timestamp)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return await self._delete(
            f"/org/{org_id}/prospects/{prospect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )

    async def list_calls(
        self,
        prospect_id: str,
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
    ) -> ProspectListCallsResponse:
        """
        Returns a paginated list of calls for a specific prospect

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
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return await self._get(
            f"/org/{org_id}/prospects/{prospect_id}/calls",
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
                    prospect_list_calls_params.ProspectListCallsParams,
                ),
            ),
            cast_to=ProspectListCallsResponse,
        )


class ProspectsResourceWithRawResponse:
    def __init__(self, prospects: ProspectsResource) -> None:
        self._prospects = prospects

        self.create = to_raw_response_wrapper(
            prospects.create,
        )
        self.retrieve = to_raw_response_wrapper(
            prospects.retrieve,
        )
        self.update = to_raw_response_wrapper(
            prospects.update,
        )
        self.list = to_raw_response_wrapper(
            prospects.list,
        )
        self.delete = to_raw_response_wrapper(
            prospects.delete,
        )
        self.list_calls = to_raw_response_wrapper(
            prospects.list_calls,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._prospects.tags)

    @cached_property
    def bulk(self) -> BulkResourceWithRawResponse:
        return BulkResourceWithRawResponse(self._prospects.bulk)


class AsyncProspectsResourceWithRawResponse:
    def __init__(self, prospects: AsyncProspectsResource) -> None:
        self._prospects = prospects

        self.create = async_to_raw_response_wrapper(
            prospects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            prospects.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            prospects.update,
        )
        self.list = async_to_raw_response_wrapper(
            prospects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            prospects.delete,
        )
        self.list_calls = async_to_raw_response_wrapper(
            prospects.list_calls,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._prospects.tags)

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithRawResponse:
        return AsyncBulkResourceWithRawResponse(self._prospects.bulk)


class ProspectsResourceWithStreamingResponse:
    def __init__(self, prospects: ProspectsResource) -> None:
        self._prospects = prospects

        self.create = to_streamed_response_wrapper(
            prospects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            prospects.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            prospects.update,
        )
        self.list = to_streamed_response_wrapper(
            prospects.list,
        )
        self.delete = to_streamed_response_wrapper(
            prospects.delete,
        )
        self.list_calls = to_streamed_response_wrapper(
            prospects.list_calls,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._prospects.tags)

    @cached_property
    def bulk(self) -> BulkResourceWithStreamingResponse:
        return BulkResourceWithStreamingResponse(self._prospects.bulk)


class AsyncProspectsResourceWithStreamingResponse:
    def __init__(self, prospects: AsyncProspectsResource) -> None:
        self._prospects = prospects

        self.create = async_to_streamed_response_wrapper(
            prospects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            prospects.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            prospects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            prospects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            prospects.delete,
        )
        self.list_calls = async_to_streamed_response_wrapper(
            prospects.list_calls,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._prospects.tags)

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        return AsyncBulkResourceWithStreamingResponse(self._prospects.bulk)
