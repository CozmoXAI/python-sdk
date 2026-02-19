# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.org import faq_list_params, faq_create_params, faq_update_params
from ..._base_client import make_request_options
from ...types.org.faq import Faq
from ...types.org.faq_list_response import FaqListResponse

__all__ = ["FaqsResource", "AsyncFaqsResource"]


class FaqsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FaqsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return FaqsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FaqsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return FaqsResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        answer: str,
        question: str,
        instruction: str | Omit = omit,
        logic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Faq:
        """
        Create a new FAQ for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/faqs",
            body=maybe_transform(
                {
                    "answer": answer,
                    "question": question,
                    "instruction": instruction,
                    "logic": logic,
                },
                faq_create_params.FaqCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Faq,
        )

    def retrieve(
        self,
        faq_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Faq:
        """
        Get a single FAQ by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not faq_id:
            raise ValueError(f"Expected a non-empty value for `faq_id` but received {faq_id!r}")
        return self._get(
            f"/org/{org_id}/faqs/{faq_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Faq,
        )

    def update(
        self,
        faq_id: str,
        *,
        org_id: str,
        answer: str | Omit = omit,
        instruction: str | Omit = omit,
        logic: str | Omit = omit,
        question: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Faq:
        """
        Update FAQ properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not faq_id:
            raise ValueError(f"Expected a non-empty value for `faq_id` but received {faq_id!r}")
        return self._patch(
            f"/org/{org_id}/faqs/{faq_id}",
            body=maybe_transform(
                {
                    "answer": answer,
                    "instruction": instruction,
                    "logic": logic,
                    "question": question,
                },
                faq_update_params.FaqUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Faq,
        )

    def list(
        self,
        org_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaqListResponse:
        """
        Get all FAQs for the organization with pagination

        Args:
          cursor: Pagination cursor

          limit: Number of items to return (default 20, max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/faqs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    faq_list_params.FaqListParams,
                ),
            ),
            cast_to=FaqListResponse,
        )

    def delete(
        self,
        faq_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an FAQ

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not faq_id:
            raise ValueError(f"Expected a non-empty value for `faq_id` but received {faq_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/org/{org_id}/faqs/{faq_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFaqsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFaqsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFaqsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFaqsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncFaqsResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        answer: str,
        question: str,
        instruction: str | Omit = omit,
        logic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Faq:
        """
        Create a new FAQ for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/faqs",
            body=await async_maybe_transform(
                {
                    "answer": answer,
                    "question": question,
                    "instruction": instruction,
                    "logic": logic,
                },
                faq_create_params.FaqCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Faq,
        )

    async def retrieve(
        self,
        faq_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Faq:
        """
        Get a single FAQ by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not faq_id:
            raise ValueError(f"Expected a non-empty value for `faq_id` but received {faq_id!r}")
        return await self._get(
            f"/org/{org_id}/faqs/{faq_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Faq,
        )

    async def update(
        self,
        faq_id: str,
        *,
        org_id: str,
        answer: str | Omit = omit,
        instruction: str | Omit = omit,
        logic: str | Omit = omit,
        question: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Faq:
        """
        Update FAQ properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not faq_id:
            raise ValueError(f"Expected a non-empty value for `faq_id` but received {faq_id!r}")
        return await self._patch(
            f"/org/{org_id}/faqs/{faq_id}",
            body=await async_maybe_transform(
                {
                    "answer": answer,
                    "instruction": instruction,
                    "logic": logic,
                    "question": question,
                },
                faq_update_params.FaqUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Faq,
        )

    async def list(
        self,
        org_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaqListResponse:
        """
        Get all FAQs for the organization with pagination

        Args:
          cursor: Pagination cursor

          limit: Number of items to return (default 20, max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/faqs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    faq_list_params.FaqListParams,
                ),
            ),
            cast_to=FaqListResponse,
        )

    async def delete(
        self,
        faq_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an FAQ

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not faq_id:
            raise ValueError(f"Expected a non-empty value for `faq_id` but received {faq_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/org/{org_id}/faqs/{faq_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FaqsResourceWithRawResponse:
    def __init__(self, faqs: FaqsResource) -> None:
        self._faqs = faqs

        self.create = to_raw_response_wrapper(
            faqs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            faqs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            faqs.update,
        )
        self.list = to_raw_response_wrapper(
            faqs.list,
        )
        self.delete = to_raw_response_wrapper(
            faqs.delete,
        )


class AsyncFaqsResourceWithRawResponse:
    def __init__(self, faqs: AsyncFaqsResource) -> None:
        self._faqs = faqs

        self.create = async_to_raw_response_wrapper(
            faqs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            faqs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            faqs.update,
        )
        self.list = async_to_raw_response_wrapper(
            faqs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            faqs.delete,
        )


class FaqsResourceWithStreamingResponse:
    def __init__(self, faqs: FaqsResource) -> None:
        self._faqs = faqs

        self.create = to_streamed_response_wrapper(
            faqs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            faqs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            faqs.update,
        )
        self.list = to_streamed_response_wrapper(
            faqs.list,
        )
        self.delete = to_streamed_response_wrapper(
            faqs.delete,
        )


class AsyncFaqsResourceWithStreamingResponse:
    def __init__(self, faqs: AsyncFaqsResource) -> None:
        self._faqs = faqs

        self.create = async_to_streamed_response_wrapper(
            faqs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            faqs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            faqs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            faqs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            faqs.delete,
        )
