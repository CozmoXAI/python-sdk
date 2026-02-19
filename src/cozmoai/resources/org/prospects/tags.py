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
from ....types.org.prospects import tag_add_params
from ....types.org.response_error import ResponseError

__all__ = ["TagsResource", "AsyncTagsResource"]


class TagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return TagsResourceWithStreamingResponse(self)

    def add(
        self,
        prospect_id: str,
        *,
        org_id: str,
        tag_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseError:
        """
        Add one or more tags to a prospect

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
        return self._post(
            f"/org/{org_id}/prospects/{prospect_id}/tags",
            body=maybe_transform({"tag_ids": tag_ids}, tag_add_params.TagAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )

    def remove(
        self,
        tag_id: str,
        *,
        org_id: str,
        prospect_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseError:
        """
        Remove a specific tag from a prospect

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
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return self._delete(
            f"/org/{org_id}/prospects/{prospect_id}/tags/{tag_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )

    def remove_all(
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
        Remove all tags from a prospect

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
            f"/org/{org_id}/prospects/{prospect_id}/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )


class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncTagsResourceWithStreamingResponse(self)

    async def add(
        self,
        prospect_id: str,
        *,
        org_id: str,
        tag_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseError:
        """
        Add one or more tags to a prospect

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
        return await self._post(
            f"/org/{org_id}/prospects/{prospect_id}/tags",
            body=await async_maybe_transform({"tag_ids": tag_ids}, tag_add_params.TagAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )

    async def remove(
        self,
        tag_id: str,
        *,
        org_id: str,
        prospect_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseError:
        """
        Remove a specific tag from a prospect

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
        if not tag_id:
            raise ValueError(f"Expected a non-empty value for `tag_id` but received {tag_id!r}")
        return await self._delete(
            f"/org/{org_id}/prospects/{prospect_id}/tags/{tag_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )

    async def remove_all(
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
        Remove all tags from a prospect

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
            f"/org/{org_id}/prospects/{prospect_id}/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )


class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.add = to_raw_response_wrapper(
            tags.add,
        )
        self.remove = to_raw_response_wrapper(
            tags.remove,
        )
        self.remove_all = to_raw_response_wrapper(
            tags.remove_all,
        )


class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.add = async_to_raw_response_wrapper(
            tags.add,
        )
        self.remove = async_to_raw_response_wrapper(
            tags.remove,
        )
        self.remove_all = async_to_raw_response_wrapper(
            tags.remove_all,
        )


class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.add = to_streamed_response_wrapper(
            tags.add,
        )
        self.remove = to_streamed_response_wrapper(
            tags.remove,
        )
        self.remove_all = to_streamed_response_wrapper(
            tags.remove_all,
        )


class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.add = async_to_streamed_response_wrapper(
            tags.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            tags.remove,
        )
        self.remove_all = async_to_streamed_response_wrapper(
            tags.remove_all,
        )
