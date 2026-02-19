# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
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
from ....types.org.tags import prospect_create_params, prospect_delete_all_params
from ....types.org.tags.bulk_operation_response_tags import BulkOperationResponseTags

__all__ = ["ProspectsResource", "AsyncProspectsResource"]


class ProspectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProspectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return ProspectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProspectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return ProspectsResourceWithStreamingResponse(self)

    def create(
        self,
        tag_id: str,
        *,
        org_id: str,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkOperationResponseTags:
        """
        Add this tag to multiple prospects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return self._post(
            f"/org/{org_id}/tags/{tag_id}/prospects",
            body=maybe_transform({"prospect_ids": prospect_ids}, prospect_create_params.ProspectCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperationResponseTags,
        )

    def delete_all(
        self,
        tag_id: str,
        *,
        org_id: str,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkOperationResponseTags:
        """
        Remove this tag from multiple prospects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return self._delete(
            f"/org/{org_id}/tags/{tag_id}/prospects",
            body=maybe_transform({"prospect_ids": prospect_ids}, prospect_delete_all_params.ProspectDeleteAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperationResponseTags,
        )


class AsyncProspectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProspectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProspectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProspectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncProspectsResourceWithStreamingResponse(self)

    async def create(
        self,
        tag_id: str,
        *,
        org_id: str,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkOperationResponseTags:
        """
        Add this tag to multiple prospects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return await self._post(
            f"/org/{org_id}/tags/{tag_id}/prospects",
            body=await async_maybe_transform(
                {"prospect_ids": prospect_ids}, prospect_create_params.ProspectCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperationResponseTags,
        )

    async def delete_all(
        self,
        tag_id: str,
        *,
        org_id: str,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkOperationResponseTags:
        """
        Remove this tag from multiple prospects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return await self._delete(
            f"/org/{org_id}/tags/{tag_id}/prospects",
            body=await async_maybe_transform(
                {"prospect_ids": prospect_ids}, prospect_delete_all_params.ProspectDeleteAllParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperationResponseTags,
        )


class ProspectsResourceWithRawResponse:
    def __init__(self, prospects: ProspectsResource) -> None:
        self._prospects = prospects

        self.create = to_raw_response_wrapper(
            prospects.create,
        )
        self.delete_all = to_raw_response_wrapper(
            prospects.delete_all,
        )


class AsyncProspectsResourceWithRawResponse:
    def __init__(self, prospects: AsyncProspectsResource) -> None:
        self._prospects = prospects

        self.create = async_to_raw_response_wrapper(
            prospects.create,
        )
        self.delete_all = async_to_raw_response_wrapper(
            prospects.delete_all,
        )


class ProspectsResourceWithStreamingResponse:
    def __init__(self, prospects: ProspectsResource) -> None:
        self._prospects = prospects

        self.create = to_streamed_response_wrapper(
            prospects.create,
        )
        self.delete_all = to_streamed_response_wrapper(
            prospects.delete_all,
        )


class AsyncProspectsResourceWithStreamingResponse:
    def __init__(self, prospects: AsyncProspectsResource) -> None:
        self._prospects = prospects

        self.create = async_to_streamed_response_wrapper(
            prospects.create,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            prospects.delete_all,
        )
