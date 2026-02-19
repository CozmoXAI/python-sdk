# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    BillingGetBalanceResponse,
    BillingGetSummaryResponse,
    BillingInitiateTopupResponse,
    BillingGetUsageSummaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_balance(self, client: Cozmoai) -> None:
        billing = client.org.billing.get_balance(
            "org_id",
        )
        assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_balance(self, client: Cozmoai) -> None:
        response = client.org.billing.with_raw_response.get_balance(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_balance(self, client: Cozmoai) -> None:
        with client.org.billing.with_streaming_response.get_balance(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_balance(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.billing.with_raw_response.get_balance(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_summary(self, client: Cozmoai) -> None:
        billing = client.org.billing.get_summary(
            "org_id",
        )
        assert_matches_type(BillingGetSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_summary(self, client: Cozmoai) -> None:
        response = client.org.billing.with_raw_response.get_summary(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingGetSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_summary(self, client: Cozmoai) -> None:
        with client.org.billing.with_streaming_response.get_summary(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingGetSummaryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_summary(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.billing.with_raw_response.get_summary(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_usage_summary(self, client: Cozmoai) -> None:
        billing = client.org.billing.get_usage_summary(
            org_id="org_id",
        )
        assert_matches_type(BillingGetUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_usage_summary_with_all_params(self, client: Cozmoai) -> None:
        billing = client.org.billing.get_usage_summary(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(BillingGetUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_usage_summary(self, client: Cozmoai) -> None:
        response = client.org.billing.with_raw_response.get_usage_summary(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingGetUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_usage_summary(self, client: Cozmoai) -> None:
        with client.org.billing.with_streaming_response.get_usage_summary(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingGetUsageSummaryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_usage_summary(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.billing.with_raw_response.get_usage_summary(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initiate_topup(self, client: Cozmoai) -> None:
        billing = client.org.billing.initiate_topup(
            org_id="org_id",
            amount=0,
        )
        assert_matches_type(BillingInitiateTopupResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initiate_topup(self, client: Cozmoai) -> None:
        response = client.org.billing.with_raw_response.initiate_topup(
            org_id="org_id",
            amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingInitiateTopupResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initiate_topup(self, client: Cozmoai) -> None:
        with client.org.billing.with_streaming_response.initiate_topup(
            org_id="org_id",
            amount=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingInitiateTopupResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_initiate_topup(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.billing.with_raw_response.initiate_topup(
                org_id="",
                amount=0,
            )


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_balance(self, async_client: AsyncCozmoai) -> None:
        billing = await async_client.org.billing.get_balance(
            "org_id",
        )
        assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_balance(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.billing.with_raw_response.get_balance(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_balance(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.billing.with_streaming_response.get_balance(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_balance(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.billing.with_raw_response.get_balance(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_summary(self, async_client: AsyncCozmoai) -> None:
        billing = await async_client.org.billing.get_summary(
            "org_id",
        )
        assert_matches_type(BillingGetSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_summary(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.billing.with_raw_response.get_summary(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingGetSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_summary(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.billing.with_streaming_response.get_summary(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingGetSummaryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_summary(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.billing.with_raw_response.get_summary(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_usage_summary(self, async_client: AsyncCozmoai) -> None:
        billing = await async_client.org.billing.get_usage_summary(
            org_id="org_id",
        )
        assert_matches_type(BillingGetUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_usage_summary_with_all_params(self, async_client: AsyncCozmoai) -> None:
        billing = await async_client.org.billing.get_usage_summary(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(BillingGetUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_usage_summary(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.billing.with_raw_response.get_usage_summary(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingGetUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_usage_summary(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.billing.with_streaming_response.get_usage_summary(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingGetUsageSummaryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_usage_summary(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.billing.with_raw_response.get_usage_summary(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initiate_topup(self, async_client: AsyncCozmoai) -> None:
        billing = await async_client.org.billing.initiate_topup(
            org_id="org_id",
            amount=0,
        )
        assert_matches_type(BillingInitiateTopupResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initiate_topup(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.billing.with_raw_response.initiate_topup(
            org_id="org_id",
            amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingInitiateTopupResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_topup(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.billing.with_streaming_response.initiate_topup(
            org_id="org_id",
            amount=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingInitiateTopupResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_initiate_topup(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.billing.with_raw_response.initiate_topup(
                org_id="",
                amount=0,
            )
