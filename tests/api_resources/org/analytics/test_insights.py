# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.analytics import (
    InsightListInsightsResponse,
    InsightGenerateInsightsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_insights(self, client: Cozmoai) -> None:
        insight = client.org.analytics.insights.generate_insights(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(InsightGenerateInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_insights_with_all_params(self, client: Cozmoai) -> None:
        insight = client.org.analytics.insights.generate_insights(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
            force_refresh=True,
        )
        assert_matches_type(InsightGenerateInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_insights(self, client: Cozmoai) -> None:
        response = client.org.analytics.insights.with_raw_response.generate_insights(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightGenerateInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_insights(self, client: Cozmoai) -> None:
        with client.org.analytics.insights.with_streaming_response.generate_insights(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightGenerateInsightsResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate_insights(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.insights.with_raw_response.generate_insights(
                org_id="",
                end_date="end_date",
                start_date="start_date",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_insights(self, client: Cozmoai) -> None:
        insight = client.org.analytics.insights.list_insights(
            org_id="org_id",
        )
        assert_matches_type(InsightListInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_insights_with_all_params(self, client: Cozmoai) -> None:
        insight = client.org.analytics.insights.list_insights(
            org_id="org_id",
            end_date="end_date",
            limit=1,
            offset=0,
            start_date="start_date",
        )
        assert_matches_type(InsightListInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_insights(self, client: Cozmoai) -> None:
        response = client.org.analytics.insights.with_raw_response.list_insights(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightListInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_insights(self, client: Cozmoai) -> None:
        with client.org.analytics.insights.with_streaming_response.list_insights(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightListInsightsResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_insights(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.insights.with_raw_response.list_insights(
                org_id="",
            )


class TestAsyncInsights:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_insights(self, async_client: AsyncCozmoai) -> None:
        insight = await async_client.org.analytics.insights.generate_insights(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(InsightGenerateInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_insights_with_all_params(self, async_client: AsyncCozmoai) -> None:
        insight = await async_client.org.analytics.insights.generate_insights(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
            force_refresh=True,
        )
        assert_matches_type(InsightGenerateInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_insights(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.insights.with_raw_response.generate_insights(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightGenerateInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_insights(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.insights.with_streaming_response.generate_insights(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightGenerateInsightsResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate_insights(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.insights.with_raw_response.generate_insights(
                org_id="",
                end_date="end_date",
                start_date="start_date",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_insights(self, async_client: AsyncCozmoai) -> None:
        insight = await async_client.org.analytics.insights.list_insights(
            org_id="org_id",
        )
        assert_matches_type(InsightListInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_insights_with_all_params(self, async_client: AsyncCozmoai) -> None:
        insight = await async_client.org.analytics.insights.list_insights(
            org_id="org_id",
            end_date="end_date",
            limit=1,
            offset=0,
            start_date="start_date",
        )
        assert_matches_type(InsightListInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_insights(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.insights.with_raw_response.list_insights(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightListInsightsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_insights(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.insights.with_streaming_response.list_insights(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightListInsightsResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_insights(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.insights.with_raw_response.list_insights(
                org_id="",
            )
