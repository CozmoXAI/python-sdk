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
from ....types.org.lists import prospect_add_bulk_params, prospect_remove_bulk_params
from ....types.org.lists.prospect_add_response import ProspectAddResponse
from ....types.org.lists.prospect_remove_response import ProspectRemoveResponse
from ....types.org.lists.list_prospect_operation_response import ListProspectOperationResponse

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

    def add(
        self,
        prospect_id: str,
        *,
        org_id: str,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectAddResponse:
        """
        Add a single prospect to a prospect list (moves if already in another list)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return self._put(
            f"/org/{org_id}/lists/{list_id}/prospects/{prospect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectAddResponse,
        )

    def add_bulk(
        self,
        list_id: str,
        *,
        org_id: str,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListProspectOperationResponse:
        """
        Add multiple prospects to a prospect list (moves if already in another list)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._post(
            f"/org/{org_id}/lists/{list_id}/prospects",
            body=maybe_transform({"prospect_ids": prospect_ids}, prospect_add_bulk_params.ProspectAddBulkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListProspectOperationResponse,
        )

    def remove(
        self,
        prospect_id: str,
        *,
        org_id: str,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectRemoveResponse:
        """
        Remove a single prospect from a prospect list (sets list_id to NULL)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return self._delete(
            f"/org/{org_id}/lists/{list_id}/prospects/{prospect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectRemoveResponse,
        )

    def remove_bulk(
        self,
        list_id: str,
        *,
        org_id: str,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListProspectOperationResponse:
        """
        Remove multiple prospects from a prospect list (sets list_id to NULL)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._delete(
            f"/org/{org_id}/lists/{list_id}/prospects",
            body=maybe_transform({"prospect_ids": prospect_ids}, prospect_remove_bulk_params.ProspectRemoveBulkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListProspectOperationResponse,
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

    async def add(
        self,
        prospect_id: str,
        *,
        org_id: str,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectAddResponse:
        """
        Add a single prospect to a prospect list (moves if already in another list)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return await self._put(
            f"/org/{org_id}/lists/{list_id}/prospects/{prospect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectAddResponse,
        )

    async def add_bulk(
        self,
        list_id: str,
        *,
        org_id: str,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListProspectOperationResponse:
        """
        Add multiple prospects to a prospect list (moves if already in another list)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._post(
            f"/org/{org_id}/lists/{list_id}/prospects",
            body=await async_maybe_transform(
                {"prospect_ids": prospect_ids}, prospect_add_bulk_params.ProspectAddBulkParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListProspectOperationResponse,
        )

    async def remove(
        self,
        prospect_id: str,
        *,
        org_id: str,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProspectRemoveResponse:
        """
        Remove a single prospect from a prospect list (sets list_id to NULL)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not prospect_id:
            raise ValueError(f"Expected a non-empty value for `prospect_id` but received {prospect_id!r}")
        return await self._delete(
            f"/org/{org_id}/lists/{list_id}/prospects/{prospect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProspectRemoveResponse,
        )

    async def remove_bulk(
        self,
        list_id: str,
        *,
        org_id: str,
        prospect_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListProspectOperationResponse:
        """
        Remove multiple prospects from a prospect list (sets list_id to NULL)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._delete(
            f"/org/{org_id}/lists/{list_id}/prospects",
            body=await async_maybe_transform(
                {"prospect_ids": prospect_ids}, prospect_remove_bulk_params.ProspectRemoveBulkParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListProspectOperationResponse,
        )


class ProspectsResourceWithRawResponse:
    def __init__(self, prospects: ProspectsResource) -> None:
        self._prospects = prospects

        self.add = to_raw_response_wrapper(
            prospects.add,
        )
        self.add_bulk = to_raw_response_wrapper(
            prospects.add_bulk,
        )
        self.remove = to_raw_response_wrapper(
            prospects.remove,
        )
        self.remove_bulk = to_raw_response_wrapper(
            prospects.remove_bulk,
        )


class AsyncProspectsResourceWithRawResponse:
    def __init__(self, prospects: AsyncProspectsResource) -> None:
        self._prospects = prospects

        self.add = async_to_raw_response_wrapper(
            prospects.add,
        )
        self.add_bulk = async_to_raw_response_wrapper(
            prospects.add_bulk,
        )
        self.remove = async_to_raw_response_wrapper(
            prospects.remove,
        )
        self.remove_bulk = async_to_raw_response_wrapper(
            prospects.remove_bulk,
        )


class ProspectsResourceWithStreamingResponse:
    def __init__(self, prospects: ProspectsResource) -> None:
        self._prospects = prospects

        self.add = to_streamed_response_wrapper(
            prospects.add,
        )
        self.add_bulk = to_streamed_response_wrapper(
            prospects.add_bulk,
        )
        self.remove = to_streamed_response_wrapper(
            prospects.remove,
        )
        self.remove_bulk = to_streamed_response_wrapper(
            prospects.remove_bulk,
        )


class AsyncProspectsResourceWithStreamingResponse:
    def __init__(self, prospects: AsyncProspectsResource) -> None:
        self._prospects = prospects

        self.add = async_to_streamed_response_wrapper(
            prospects.add,
        )
        self.add_bulk = async_to_streamed_response_wrapper(
            prospects.add_bulk,
        )
        self.remove = async_to_streamed_response_wrapper(
            prospects.remove,
        )
        self.remove_bulk = async_to_streamed_response_wrapper(
            prospects.remove_bulk,
        )
