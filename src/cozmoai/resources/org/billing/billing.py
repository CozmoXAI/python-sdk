# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .ledger import (
    LedgerResource,
    AsyncLedgerResource,
    LedgerResourceWithRawResponse,
    AsyncLedgerResourceWithRawResponse,
    LedgerResourceWithStreamingResponse,
    AsyncLedgerResourceWithStreamingResponse,
)
from .invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)
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
from ....types.org import billing_initiate_topup_params, billing_get_usage_summary_params
from ...._base_client import make_request_options
from ....types.org.billing_get_balance_response import BillingGetBalanceResponse
from ....types.org.billing_get_summary_response import BillingGetSummaryResponse
from ....types.org.billing_initiate_topup_response import BillingInitiateTopupResponse
from ....types.org.billing_get_usage_summary_response import BillingGetUsageSummaryResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def ledger(self) -> LedgerResource:
        return LedgerResource(self._client)

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def get_balance(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetBalanceResponse:
        """
        Get the current credits balance and billing tier

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/billing/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetBalanceResponse,
        )

    def get_summary(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetSummaryResponse:
        """
        Get comprehensive billing summary including balance, monthly totals, and daily
        report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/billing/summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetSummaryResponse,
        )

    def get_usage_summary(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetUsageSummaryResponse:
        """
        Get usage summary grouped by product type

        Args:
          end_date: Filter by end date (ISO 8601)

          start_date: Filter by start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/billing/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    billing_get_usage_summary_params.BillingGetUsageSummaryParams,
                ),
            ),
            cast_to=BillingGetUsageSummaryResponse,
        )

    def initiate_topup(
        self,
        org_id: str,
        *,
        amount: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingInitiateTopupResponse:
        """
        Initiate a credit top-up and return redirect URL to payment provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/billing/topup",
            body=maybe_transform({"amount": amount}, billing_initiate_topup_params.BillingInitiateTopupParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingInitiateTopupResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def ledger(self) -> AsyncLedgerResource:
        return AsyncLedgerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def get_balance(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetBalanceResponse:
        """
        Get the current credits balance and billing tier

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/billing/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetBalanceResponse,
        )

    async def get_summary(
        self,
        org_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetSummaryResponse:
        """
        Get comprehensive billing summary including balance, monthly totals, and daily
        report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/billing/summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetSummaryResponse,
        )

    async def get_usage_summary(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetUsageSummaryResponse:
        """
        Get usage summary grouped by product type

        Args:
          end_date: Filter by end date (ISO 8601)

          start_date: Filter by start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/billing/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    billing_get_usage_summary_params.BillingGetUsageSummaryParams,
                ),
            ),
            cast_to=BillingGetUsageSummaryResponse,
        )

    async def initiate_topup(
        self,
        org_id: str,
        *,
        amount: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingInitiateTopupResponse:
        """
        Initiate a credit top-up and return redirect URL to payment provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/billing/topup",
            body=await async_maybe_transform(
                {"amount": amount}, billing_initiate_topup_params.BillingInitiateTopupParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingInitiateTopupResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_balance = to_raw_response_wrapper(
            billing.get_balance,
        )
        self.get_summary = to_raw_response_wrapper(
            billing.get_summary,
        )
        self.get_usage_summary = to_raw_response_wrapper(
            billing.get_usage_summary,
        )
        self.initiate_topup = to_raw_response_wrapper(
            billing.initiate_topup,
        )

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._billing.invoices)

    @cached_property
    def ledger(self) -> LedgerResourceWithRawResponse:
        return LedgerResourceWithRawResponse(self._billing.ledger)


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_balance = async_to_raw_response_wrapper(
            billing.get_balance,
        )
        self.get_summary = async_to_raw_response_wrapper(
            billing.get_summary,
        )
        self.get_usage_summary = async_to_raw_response_wrapper(
            billing.get_usage_summary,
        )
        self.initiate_topup = async_to_raw_response_wrapper(
            billing.initiate_topup,
        )

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._billing.invoices)

    @cached_property
    def ledger(self) -> AsyncLedgerResourceWithRawResponse:
        return AsyncLedgerResourceWithRawResponse(self._billing.ledger)


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_balance = to_streamed_response_wrapper(
            billing.get_balance,
        )
        self.get_summary = to_streamed_response_wrapper(
            billing.get_summary,
        )
        self.get_usage_summary = to_streamed_response_wrapper(
            billing.get_usage_summary,
        )
        self.initiate_topup = to_streamed_response_wrapper(
            billing.initiate_topup,
        )

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._billing.invoices)

    @cached_property
    def ledger(self) -> LedgerResourceWithStreamingResponse:
        return LedgerResourceWithStreamingResponse(self._billing.ledger)


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_balance = async_to_streamed_response_wrapper(
            billing.get_balance,
        )
        self.get_summary = async_to_streamed_response_wrapper(
            billing.get_summary,
        )
        self.get_usage_summary = async_to_streamed_response_wrapper(
            billing.get_usage_summary,
        )
        self.initiate_topup = async_to_streamed_response_wrapper(
            billing.initiate_topup,
        )

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._billing.invoices)

    @cached_property
    def ledger(self) -> AsyncLedgerResourceWithStreamingResponse:
        return AsyncLedgerResourceWithStreamingResponse(self._billing.ledger)
