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
from ...types.org import quality_rule_list_params, quality_rule_create_params, quality_rule_update_params
from ..._base_client import make_request_options
from ...types.org.quality_rule_response import QualityRuleResponse
from ...types.org.quality_rule_list_response import QualityRuleListResponse

__all__ = ["QualityRulesResource", "AsyncQualityRulesResource"]


class QualityRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QualityRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return QualityRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualityRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return QualityRulesResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        key: str,
        penalty: int,
        prompt: str,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityRuleResponse:
        """
        Create a new quality rule for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/quality-rules",
            body=maybe_transform(
                {
                    "key": key,
                    "penalty": penalty,
                    "prompt": prompt,
                    "is_active": is_active,
                },
                quality_rule_create_params.QualityRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualityRuleResponse,
        )

    def retrieve(
        self,
        rule_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityRuleResponse:
        """
        Get a quality rule by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get(
            f"/org/{org_id}/quality-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualityRuleResponse,
        )

    def update(
        self,
        rule_id: str,
        *,
        org_id: str,
        is_active: bool | Omit = omit,
        key: str | Omit = omit,
        penalty: int | Omit = omit,
        prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityRuleResponse:
        """
        Update an existing quality rule

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._patch(
            f"/org/{org_id}/quality-rules/{rule_id}",
            body=maybe_transform(
                {
                    "is_active": is_active,
                    "key": key,
                    "penalty": penalty,
                    "prompt": prompt,
                },
                quality_rule_update_params.QualityRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualityRuleResponse,
        )

    def list(
        self,
        org_id: str,
        *,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityRuleListResponse:
        """
        Get all quality rules (global + organization-specific)

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
        return self._get(
            f"/org/{org_id}/quality-rules",
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
                    quality_rule_list_params.QualityRuleListParams,
                ),
            ),
            cast_to=QualityRuleListResponse,
        )

    def delete(
        self,
        rule_id: str,
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
        Delete a quality rule by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/org/{org_id}/quality-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncQualityRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQualityRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncQualityRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualityRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncQualityRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        key: str,
        penalty: int,
        prompt: str,
        is_active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityRuleResponse:
        """
        Create a new quality rule for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/quality-rules",
            body=await async_maybe_transform(
                {
                    "key": key,
                    "penalty": penalty,
                    "prompt": prompt,
                    "is_active": is_active,
                },
                quality_rule_create_params.QualityRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualityRuleResponse,
        )

    async def retrieve(
        self,
        rule_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityRuleResponse:
        """
        Get a quality rule by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._get(
            f"/org/{org_id}/quality-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualityRuleResponse,
        )

    async def update(
        self,
        rule_id: str,
        *,
        org_id: str,
        is_active: bool | Omit = omit,
        key: str | Omit = omit,
        penalty: int | Omit = omit,
        prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityRuleResponse:
        """
        Update an existing quality rule

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._patch(
            f"/org/{org_id}/quality-rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "is_active": is_active,
                    "key": key,
                    "penalty": penalty,
                    "prompt": prompt,
                },
                quality_rule_update_params.QualityRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QualityRuleResponse,
        )

    async def list(
        self,
        org_id: str,
        *,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QualityRuleListResponse:
        """
        Get all quality rules (global + organization-specific)

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
        return await self._get(
            f"/org/{org_id}/quality-rules",
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
                    quality_rule_list_params.QualityRuleListParams,
                ),
            ),
            cast_to=QualityRuleListResponse,
        )

    async def delete(
        self,
        rule_id: str,
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
        Delete a quality rule by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/org/{org_id}/quality-rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class QualityRulesResourceWithRawResponse:
    def __init__(self, quality_rules: QualityRulesResource) -> None:
        self._quality_rules = quality_rules

        self.create = to_raw_response_wrapper(
            quality_rules.create,
        )
        self.retrieve = to_raw_response_wrapper(
            quality_rules.retrieve,
        )
        self.update = to_raw_response_wrapper(
            quality_rules.update,
        )
        self.list = to_raw_response_wrapper(
            quality_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            quality_rules.delete,
        )


class AsyncQualityRulesResourceWithRawResponse:
    def __init__(self, quality_rules: AsyncQualityRulesResource) -> None:
        self._quality_rules = quality_rules

        self.create = async_to_raw_response_wrapper(
            quality_rules.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            quality_rules.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            quality_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            quality_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            quality_rules.delete,
        )


class QualityRulesResourceWithStreamingResponse:
    def __init__(self, quality_rules: QualityRulesResource) -> None:
        self._quality_rules = quality_rules

        self.create = to_streamed_response_wrapper(
            quality_rules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            quality_rules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            quality_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            quality_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            quality_rules.delete,
        )


class AsyncQualityRulesResourceWithStreamingResponse:
    def __init__(self, quality_rules: AsyncQualityRulesResource) -> None:
        self._quality_rules = quality_rules

        self.create = async_to_streamed_response_wrapper(
            quality_rules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            quality_rules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            quality_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            quality_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            quality_rules.delete,
        )
