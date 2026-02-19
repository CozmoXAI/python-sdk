# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
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
from ...types.org import tool_list_params, tool_create_params, tool_update_params
from ..._base_client import make_request_options
from ...types.org.tool_response import ToolResponse
from ...types.org.response_error import ResponseError
from ...types.org.tool_list_response import ToolListResponse
from ...types.org.parameter_prop_param import ParameterPropParam

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        description: str,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
        name: str,
        url: str,
        body: str | Omit = omit,
        filler_phrases: SequenceNotStr[str] | Omit = omit,
        headers: Iterable[int] | Omit = omit,
        parameters: Iterable[ParameterPropParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolResponse:
        """
        Create a new tool definition with HTTP endpoint configuration and parameters

        Args:
          body: Request body template

          filler_phrases: Phrases to say while tool is executing

          headers: JSON object of headers

          parameters: Tool parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/tools",
            body=maybe_transform(
                {
                    "description": description,
                    "method": method,
                    "name": name,
                    "url": url,
                    "body": body,
                    "filler_phrases": filler_phrases,
                    "headers": headers,
                    "parameters": parameters,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
        )

    def retrieve(
        self,
        tool_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolResponse:
        """
        Get a single tool by ID with all its parameters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._get(
            f"/org/{org_id}/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
        )

    def update(
        self,
        tool_id: str,
        *,
        org_id: str,
        body: str | Omit = omit,
        description: str | Omit = omit,
        filler_phrases: SequenceNotStr[str] | Omit = omit,
        headers: Iterable[int] | Omit = omit,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"] | Omit = omit,
        name: str | Omit = omit,
        parameters: Iterable[ParameterPropParam] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolResponse:
        """Update tool definition.

        Supports partial updates. If parameters are provided,
        they replace all existing parameters.

        Args:
          parameters: If provided, replaces all existing parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._patch(
            f"/org/{org_id}/tools/{tool_id}",
            body=maybe_transform(
                {
                    "body": body,
                    "description": description,
                    "filler_phrases": filler_phrases,
                    "headers": headers,
                    "method": method,
                    "name": name,
                    "parameters": parameters,
                    "url": url,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
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
    ) -> ToolListResponse:
        """
        Get a paginated list of tool definitions for an organization

        Args:
          page: Page number

          size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/tools",
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
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    def delete(
        self,
        tool_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseError:
        """Delete a tool by ID.

        Also removes all associated parameters (cascade delete).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return self._delete(
            f"/org/{org_id}/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        description: str,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
        name: str,
        url: str,
        body: str | Omit = omit,
        filler_phrases: SequenceNotStr[str] | Omit = omit,
        headers: Iterable[int] | Omit = omit,
        parameters: Iterable[ParameterPropParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolResponse:
        """
        Create a new tool definition with HTTP endpoint configuration and parameters

        Args:
          body: Request body template

          filler_phrases: Phrases to say while tool is executing

          headers: JSON object of headers

          parameters: Tool parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/tools",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "method": method,
                    "name": name,
                    "url": url,
                    "body": body,
                    "filler_phrases": filler_phrases,
                    "headers": headers,
                    "parameters": parameters,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
        )

    async def retrieve(
        self,
        tool_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolResponse:
        """
        Get a single tool by ID with all its parameters

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._get(
            f"/org/{org_id}/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
        )

    async def update(
        self,
        tool_id: str,
        *,
        org_id: str,
        body: str | Omit = omit,
        description: str | Omit = omit,
        filler_phrases: SequenceNotStr[str] | Omit = omit,
        headers: Iterable[int] | Omit = omit,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"] | Omit = omit,
        name: str | Omit = omit,
        parameters: Iterable[ParameterPropParam] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolResponse:
        """Update tool definition.

        Supports partial updates. If parameters are provided,
        they replace all existing parameters.

        Args:
          parameters: If provided, replaces all existing parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._patch(
            f"/org/{org_id}/tools/{tool_id}",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "description": description,
                    "filler_phrases": filler_phrases,
                    "headers": headers,
                    "method": method,
                    "name": name,
                    "parameters": parameters,
                    "url": url,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
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
    ) -> ToolListResponse:
        """
        Get a paginated list of tool definitions for an organization

        Args:
          page: Page number

          size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/tools",
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
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    async def delete(
        self,
        tool_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseError:
        """Delete a tool by ID.

        Also removes all associated parameters (cascade delete).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not tool_id:
            raise ValueError(f"Expected a non-empty value for `tool_id` but received {tool_id!r}")
        return await self._delete(
            f"/org/{org_id}/tools/{tool_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseError,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_raw_response_wrapper(
            tools.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tools.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tools.update,
        )
        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.delete = to_raw_response_wrapper(
            tools.delete,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_raw_response_wrapper(
            tools.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tools.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tools.update,
        )
        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tools.delete,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_streamed_response_wrapper(
            tools.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tools.update,
        )
        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = to_streamed_response_wrapper(
            tools.delete,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_streamed_response_wrapper(
            tools.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tools.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tools.delete,
        )
