# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.billing import (
    InvoiceListResponse,
    InvoiceGetPdfURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        invoice = client.org.billing.invoices.list(
            org_id="org_id",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        invoice = client.org.billing.invoices.list(
            org_id="org_id",
            end_date="end_date",
            invoice_status=["string"],
            page=0,
            payment_status=["string"],
            per_page=100,
            start_date="start_date",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.billing.invoices.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.billing.invoices.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.billing.invoices.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_pdf_url(self, client: Cozmoai) -> None:
        invoice = client.org.billing.invoices.get_pdf_url(
            org_id="org_id",
            invoice_id="invoice_id",
        )
        assert_matches_type(InvoiceGetPdfURLResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_pdf_url_with_all_params(self, client: Cozmoai) -> None:
        invoice = client.org.billing.invoices.get_pdf_url(
            org_id="org_id",
            invoice_id="invoice_id",
            url="url",
        )
        assert_matches_type(InvoiceGetPdfURLResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_pdf_url(self, client: Cozmoai) -> None:
        response = client.org.billing.invoices.with_raw_response.get_pdf_url(
            org_id="org_id",
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceGetPdfURLResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_pdf_url(self, client: Cozmoai) -> None:
        with client.org.billing.invoices.with_streaming_response.get_pdf_url(
            org_id="org_id",
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceGetPdfURLResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_pdf_url(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.billing.invoices.with_raw_response.get_pdf_url(
                org_id="",
                invoice_id="invoice_id",
            )


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        invoice = await async_client.org.billing.invoices.list(
            org_id="org_id",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        invoice = await async_client.org.billing.invoices.list(
            org_id="org_id",
            end_date="end_date",
            invoice_status=["string"],
            page=0,
            payment_status=["string"],
            per_page=100,
            start_date="start_date",
        )
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.billing.invoices.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceListResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.billing.invoices.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceListResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.billing.invoices.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_pdf_url(self, async_client: AsyncCozmoai) -> None:
        invoice = await async_client.org.billing.invoices.get_pdf_url(
            org_id="org_id",
            invoice_id="invoice_id",
        )
        assert_matches_type(InvoiceGetPdfURLResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_pdf_url_with_all_params(self, async_client: AsyncCozmoai) -> None:
        invoice = await async_client.org.billing.invoices.get_pdf_url(
            org_id="org_id",
            invoice_id="invoice_id",
            url="url",
        )
        assert_matches_type(InvoiceGetPdfURLResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_pdf_url(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.billing.invoices.with_raw_response.get_pdf_url(
            org_id="org_id",
            invoice_id="invoice_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceGetPdfURLResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_pdf_url(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.billing.invoices.with_streaming_response.get_pdf_url(
            org_id="org_id",
            invoice_id="invoice_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceGetPdfURLResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_pdf_url(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.billing.invoices.with_raw_response.get_pdf_url(
                org_id="",
                invoice_id="invoice_id",
            )
