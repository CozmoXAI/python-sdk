# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .prospects import (
    ProspectsResource,
    AsyncProspectsResource,
    ProspectsResourceWithRawResponse,
    AsyncProspectsResourceWithRawResponse,
    ProspectsResourceWithStreamingResponse,
    AsyncProspectsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TagsResource", "AsyncTagsResource"]


class TagsResource(SyncAPIResource):
    @cached_property
    def prospects(self) -> ProspectsResource:
        return ProspectsResource(self._client)

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


class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def prospects(self) -> AsyncProspectsResource:
        return AsyncProspectsResource(self._client)

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


class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

    @cached_property
    def prospects(self) -> ProspectsResourceWithRawResponse:
        return ProspectsResourceWithRawResponse(self._tags.prospects)


class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

    @cached_property
    def prospects(self) -> AsyncProspectsResourceWithRawResponse:
        return AsyncProspectsResourceWithRawResponse(self._tags.prospects)


class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

    @cached_property
    def prospects(self) -> ProspectsResourceWithStreamingResponse:
        return ProspectsResourceWithStreamingResponse(self._tags.prospects)


class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

    @cached_property
    def prospects(self) -> AsyncProspectsResourceWithStreamingResponse:
        return AsyncProspectsResourceWithStreamingResponse(self._tags.prospects)
