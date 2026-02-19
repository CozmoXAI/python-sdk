# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...._base_client import make_request_options
from ....types.org.billing import ledger_list_params
from ....types.org.billing.ledger_list_response import LedgerListResponse
from ....types.org.billing.ledger_get_entry_response import LedgerGetEntryResponse

__all__ = ["LedgerResource", "AsyncLedgerResource"]


class LedgerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return LedgerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return LedgerResourceWithStreamingResponse(self)

    def list(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        event_type: str | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LedgerListResponse:
        """
        Get paginated list of billing ledger entries with filtering

        Args:
          end_date: Filter by end date (ISO 8601)

          event_type: Filter by event type (TOPUP, CALL_USAGE, RENTAL)

          page: Page number

          size: Page size

          start_date: Filter by start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/billing/ledger",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "event_type": event_type,
                        "page": page,
                        "size": size,
                        "start_date": start_date,
                    },
                    ledger_list_params.LedgerListParams,
                ),
            ),
            cast_to=LedgerListResponse,
        )

    def get_entry(
        self,
        entry_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LedgerGetEntryResponse:
        """
        Get a ledger entry with its usage breakdown

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._get(
            f"/org/{org_id}/billing/ledger/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerGetEntryResponse,
        )


class AsyncLedgerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLedgerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncLedgerResourceWithStreamingResponse(self)

    async def list(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        event_type: str | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LedgerListResponse:
        """
        Get paginated list of billing ledger entries with filtering

        Args:
          end_date: Filter by end date (ISO 8601)

          event_type: Filter by event type (TOPUP, CALL_USAGE, RENTAL)

          page: Page number

          size: Page size

          start_date: Filter by start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/billing/ledger",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "event_type": event_type,
                        "page": page,
                        "size": size,
                        "start_date": start_date,
                    },
                    ledger_list_params.LedgerListParams,
                ),
            ),
            cast_to=LedgerListResponse,
        )

    async def get_entry(
        self,
        entry_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LedgerGetEntryResponse:
        """
        Get a ledger entry with its usage breakdown

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._get(
            f"/org/{org_id}/billing/ledger/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LedgerGetEntryResponse,
        )


class LedgerResourceWithRawResponse:
    def __init__(self, ledger: LedgerResource) -> None:
        self._ledger = ledger

        self.list = to_raw_response_wrapper(
            ledger.list,
        )
        self.get_entry = to_raw_response_wrapper(
            ledger.get_entry,
        )


class AsyncLedgerResourceWithRawResponse:
    def __init__(self, ledger: AsyncLedgerResource) -> None:
        self._ledger = ledger

        self.list = async_to_raw_response_wrapper(
            ledger.list,
        )
        self.get_entry = async_to_raw_response_wrapper(
            ledger.get_entry,
        )


class LedgerResourceWithStreamingResponse:
    def __init__(self, ledger: LedgerResource) -> None:
        self._ledger = ledger

        self.list = to_streamed_response_wrapper(
            ledger.list,
        )
        self.get_entry = to_streamed_response_wrapper(
            ledger.get_entry,
        )


class AsyncLedgerResourceWithStreamingResponse:
    def __init__(self, ledger: AsyncLedgerResource) -> None:
        self._ledger = ledger

        self.list = async_to_streamed_response_wrapper(
            ledger.list,
        )
        self.get_entry = async_to_streamed_response_wrapper(
            ledger.get_entry,
        )
