# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.org import api_key_create_api_key_params, api_key_update_api_key_scopes_params
from ..._base_client import make_request_options
from ...types.org.response import Response
from ...types.org.api_key_list_api_keys_response import APIKeyListAPIKeysResponse
from ...types.org.api_key_create_api_key_response import APIKeyCreateAPIKeyResponse

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def create_api_key(
        self,
        org_id: str,
        *,
        name: str,
        scopes: SequenceNotStr[str],
        expires_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyCreateAPIKeyResponse:
        """
        Create a new API key for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/api-keys",
            body=maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "expires_at": expires_at,
                },
                api_key_create_api_key_params.APIKeyCreateAPIKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyCreateAPIKeyResponse,
        )

    def list_api_keys(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListAPIKeysResponse:
        """
        List all API keys for the organization (keys are masked)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyListAPIKeysResponse,
        )

    def revoke_all_api_keys(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
        """
        Revokes all organization API keys (soft delete)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._delete(
            f"/org/{org_id}/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )

    def revoke_api_key(
        self,
        key_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
        """
        Revoke an API key (soft delete)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._delete(
            f"/org/{org_id}/api-keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )

    def update_api_key_scopes(
        self,
        key_id: str,
        *,
        org_id: str,
        scopes: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
        """
        Update the scopes of an existing API key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._patch(
            f"/org/{org_id}/api-keys/{key_id}/scopes",
            body=maybe_transform(
                {"scopes": scopes}, api_key_update_api_key_scopes_params.APIKeyUpdateAPIKeyScopesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def create_api_key(
        self,
        org_id: str,
        *,
        name: str,
        scopes: SequenceNotStr[str],
        expires_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyCreateAPIKeyResponse:
        """
        Create a new API key for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/api-keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "expires_at": expires_at,
                },
                api_key_create_api_key_params.APIKeyCreateAPIKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyCreateAPIKeyResponse,
        )

    async def list_api_keys(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListAPIKeysResponse:
        """
        List all API keys for the organization (keys are masked)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyListAPIKeysResponse,
        )

    async def revoke_all_api_keys(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
        """
        Revokes all organization API keys (soft delete)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._delete(
            f"/org/{org_id}/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )

    async def revoke_api_key(
        self,
        key_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
        """
        Revoke an API key (soft delete)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._delete(
            f"/org/{org_id}/api-keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )

    async def update_api_key_scopes(
        self,
        key_id: str,
        *,
        org_id: str,
        scopes: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Response:
        """
        Update the scopes of an existing API key

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._patch(
            f"/org/{org_id}/api-keys/{key_id}/scopes",
            body=await async_maybe_transform(
                {"scopes": scopes}, api_key_update_api_key_scopes_params.APIKeyUpdateAPIKeyScopesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Response,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create_api_key = to_raw_response_wrapper(
            api_keys.create_api_key,
        )
        self.list_api_keys = to_raw_response_wrapper(
            api_keys.list_api_keys,
        )
        self.revoke_all_api_keys = to_raw_response_wrapper(
            api_keys.revoke_all_api_keys,
        )
        self.revoke_api_key = to_raw_response_wrapper(
            api_keys.revoke_api_key,
        )
        self.update_api_key_scopes = to_raw_response_wrapper(
            api_keys.update_api_key_scopes,
        )


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create_api_key = async_to_raw_response_wrapper(
            api_keys.create_api_key,
        )
        self.list_api_keys = async_to_raw_response_wrapper(
            api_keys.list_api_keys,
        )
        self.revoke_all_api_keys = async_to_raw_response_wrapper(
            api_keys.revoke_all_api_keys,
        )
        self.revoke_api_key = async_to_raw_response_wrapper(
            api_keys.revoke_api_key,
        )
        self.update_api_key_scopes = async_to_raw_response_wrapper(
            api_keys.update_api_key_scopes,
        )


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create_api_key = to_streamed_response_wrapper(
            api_keys.create_api_key,
        )
        self.list_api_keys = to_streamed_response_wrapper(
            api_keys.list_api_keys,
        )
        self.revoke_all_api_keys = to_streamed_response_wrapper(
            api_keys.revoke_all_api_keys,
        )
        self.revoke_api_key = to_streamed_response_wrapper(
            api_keys.revoke_api_key,
        )
        self.update_api_key_scopes = to_streamed_response_wrapper(
            api_keys.update_api_key_scopes,
        )


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create_api_key = async_to_streamed_response_wrapper(
            api_keys.create_api_key,
        )
        self.list_api_keys = async_to_streamed_response_wrapper(
            api_keys.list_api_keys,
        )
        self.revoke_all_api_keys = async_to_streamed_response_wrapper(
            api_keys.revoke_all_api_keys,
        )
        self.revoke_api_key = async_to_streamed_response_wrapper(
            api_keys.revoke_api_key,
        )
        self.update_api_key_scopes = async_to_streamed_response_wrapper(
            api_keys.update_api_key_scopes,
        )
