# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.org import outcome_definition_create_params, outcome_definition_update_params
from ..._base_client import make_request_options
from ...types.org.outcome_definition import OutcomeDefinition
from ...types.org.outcome_definition_list_response import OutcomeDefinitionListResponse

__all__ = ["OutcomeDefinitionsResource", "AsyncOutcomeDefinitionsResource"]


class OutcomeDefinitionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutcomeDefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return OutcomeDefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutcomeDefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return OutcomeDefinitionsResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        display_name: str,
        key: str,
        value_type: Literal["BOOLEAN", "TEXT", "NUMBER", "DATE", "JSON"],
        description: str | Omit = omit,
        is_unique_per_call: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutcomeDefinition:
        """
        Creates a custom outcome definition for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/outcome-definitions",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "key": key,
                    "value_type": value_type,
                    "description": description,
                    "is_unique_per_call": is_unique_per_call,
                },
                outcome_definition_create_params.OutcomeDefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutcomeDefinition,
        )

    def update(
        self,
        id: str,
        *,
        org_id: str,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        is_unique_per_call: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutcomeDefinition:
        """
        Updates a custom outcome definition (platform definitions cannot be modified)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/org/{org_id}/outcome-definitions/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "is_unique_per_call": is_unique_per_call,
                },
                outcome_definition_update_params.OutcomeDefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutcomeDefinition,
        )

    def list(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutcomeDefinitionListResponse:
        """
        Returns all platform and custom outcome definitions for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/outcome-definitions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutcomeDefinitionListResponse,
        )

    def delete(
        self,
        id: str,
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
        Deletes an outcome definition for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/org/{org_id}/outcome-definitions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOutcomeDefinitionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutcomeDefinitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOutcomeDefinitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutcomeDefinitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncOutcomeDefinitionsResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        display_name: str,
        key: str,
        value_type: Literal["BOOLEAN", "TEXT", "NUMBER", "DATE", "JSON"],
        description: str | Omit = omit,
        is_unique_per_call: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutcomeDefinition:
        """
        Creates a custom outcome definition for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/outcome-definitions",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "key": key,
                    "value_type": value_type,
                    "description": description,
                    "is_unique_per_call": is_unique_per_call,
                },
                outcome_definition_create_params.OutcomeDefinitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutcomeDefinition,
        )

    async def update(
        self,
        id: str,
        *,
        org_id: str,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        is_unique_per_call: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutcomeDefinition:
        """
        Updates a custom outcome definition (platform definitions cannot be modified)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/org/{org_id}/outcome-definitions/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "is_unique_per_call": is_unique_per_call,
                },
                outcome_definition_update_params.OutcomeDefinitionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutcomeDefinition,
        )

    async def list(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OutcomeDefinitionListResponse:
        """
        Returns all platform and custom outcome definitions for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/outcome-definitions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutcomeDefinitionListResponse,
        )

    async def delete(
        self,
        id: str,
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
        Deletes an outcome definition for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/org/{org_id}/outcome-definitions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OutcomeDefinitionsResourceWithRawResponse:
    def __init__(self, outcome_definitions: OutcomeDefinitionsResource) -> None:
        self._outcome_definitions = outcome_definitions

        self.create = to_raw_response_wrapper(
            outcome_definitions.create,
        )
        self.update = to_raw_response_wrapper(
            outcome_definitions.update,
        )
        self.list = to_raw_response_wrapper(
            outcome_definitions.list,
        )
        self.delete = to_raw_response_wrapper(
            outcome_definitions.delete,
        )


class AsyncOutcomeDefinitionsResourceWithRawResponse:
    def __init__(self, outcome_definitions: AsyncOutcomeDefinitionsResource) -> None:
        self._outcome_definitions = outcome_definitions

        self.create = async_to_raw_response_wrapper(
            outcome_definitions.create,
        )
        self.update = async_to_raw_response_wrapper(
            outcome_definitions.update,
        )
        self.list = async_to_raw_response_wrapper(
            outcome_definitions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            outcome_definitions.delete,
        )


class OutcomeDefinitionsResourceWithStreamingResponse:
    def __init__(self, outcome_definitions: OutcomeDefinitionsResource) -> None:
        self._outcome_definitions = outcome_definitions

        self.create = to_streamed_response_wrapper(
            outcome_definitions.create,
        )
        self.update = to_streamed_response_wrapper(
            outcome_definitions.update,
        )
        self.list = to_streamed_response_wrapper(
            outcome_definitions.list,
        )
        self.delete = to_streamed_response_wrapper(
            outcome_definitions.delete,
        )


class AsyncOutcomeDefinitionsResourceWithStreamingResponse:
    def __init__(self, outcome_definitions: AsyncOutcomeDefinitionsResource) -> None:
        self._outcome_definitions = outcome_definitions

        self.create = async_to_streamed_response_wrapper(
            outcome_definitions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            outcome_definitions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            outcome_definitions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            outcome_definitions.delete,
        )
