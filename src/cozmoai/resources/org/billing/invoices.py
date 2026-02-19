# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.org.billing import invoice_list_params, invoice_get_pdf_url_params
from ....types.org.billing.invoice_list_response import InvoiceListResponse
from ....types.org.billing.invoice_get_pdf_url_response import InvoiceGetPdfURLResponse

__all__ = ["InvoicesResource", "AsyncInvoicesResource"]


class InvoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return InvoicesResourceWithStreamingResponse(self)

    def list(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        invoice_status: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        payment_status: SequenceNotStr[str] | Omit = omit,
        per_page: int | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceListResponse:
        """
        Get paginated list of invoices with optional filtering

        Args:
          end_date: Filter by end date (ISO 8601)

          invoice_status: Filter by invoice status (DRAFT, FINALIZED, VOIDED)

          page: Page number

          payment_status: Filter by payment status (INITIATED, PENDING, SUCCEEDED, etc.)

          per_page: Items per page

          start_date: Filter by start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/billing/invoices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "invoice_status": invoice_status,
                        "page": page,
                        "payment_status": payment_status,
                        "per_page": per_page,
                        "start_date": start_date,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            cast_to=InvoiceListResponse,
        )

    def get_pdf_url(
        self,
        org_id: str,
        *,
        invoice_id: str,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceGetPdfURLResponse:
        """
        Get the PDF URL for a specific invoice

        Args:
          invoice_id: Invoice ID

          url: Return URL (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/billing/invoices/pdf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "invoice_id": invoice_id,
                        "url": url,
                    },
                    invoice_get_pdf_url_params.InvoiceGetPdfURLParams,
                ),
            ),
            cast_to=InvoiceGetPdfURLResponse,
        )


class AsyncInvoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncInvoicesResourceWithStreamingResponse(self)

    async def list(
        self,
        org_id: str,
        *,
        end_date: str | Omit = omit,
        invoice_status: SequenceNotStr[str] | Omit = omit,
        page: int | Omit = omit,
        payment_status: SequenceNotStr[str] | Omit = omit,
        per_page: int | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceListResponse:
        """
        Get paginated list of invoices with optional filtering

        Args:
          end_date: Filter by end date (ISO 8601)

          invoice_status: Filter by invoice status (DRAFT, FINALIZED, VOIDED)

          page: Page number

          payment_status: Filter by payment status (INITIATED, PENDING, SUCCEEDED, etc.)

          per_page: Items per page

          start_date: Filter by start date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/billing/invoices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "invoice_status": invoice_status,
                        "page": page,
                        "payment_status": payment_status,
                        "per_page": per_page,
                        "start_date": start_date,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            cast_to=InvoiceListResponse,
        )

    async def get_pdf_url(
        self,
        org_id: str,
        *,
        invoice_id: str,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceGetPdfURLResponse:
        """
        Get the PDF URL for a specific invoice

        Args:
          invoice_id: Invoice ID

          url: Return URL (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/billing/invoices/pdf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "invoice_id": invoice_id,
                        "url": url,
                    },
                    invoice_get_pdf_url_params.InvoiceGetPdfURLParams,
                ),
            ),
            cast_to=InvoiceGetPdfURLResponse,
        )


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.list = to_raw_response_wrapper(
            invoices.list,
        )
        self.get_pdf_url = to_raw_response_wrapper(
            invoices.get_pdf_url,
        )


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.list = async_to_raw_response_wrapper(
            invoices.list,
        )
        self.get_pdf_url = async_to_raw_response_wrapper(
            invoices.get_pdf_url,
        )


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.list = to_streamed_response_wrapper(
            invoices.list,
        )
        self.get_pdf_url = to_streamed_response_wrapper(
            invoices.get_pdf_url,
        )


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
        self.get_pdf_url = async_to_streamed_response_wrapper(
            invoices.get_pdf_url,
        )
