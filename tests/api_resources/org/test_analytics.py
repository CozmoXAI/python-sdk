# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    AnalyticsListAgentsResponse,
    AnalyticsListBatchesResponse,
    AnalyticsGetDashboardSummaryResponse,
    AnalyticsGetProspectAnalyticsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_dashboard_summary(self, client: Cozmoai) -> None:
        analytics = client.org.analytics.get_dashboard_summary(
            org_id="org_id",
        )
        assert_matches_type(AnalyticsGetDashboardSummaryResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_dashboard_summary_with_all_params(self, client: Cozmoai) -> None:
        analytics = client.org.analytics.get_dashboard_summary(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AnalyticsGetDashboardSummaryResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_dashboard_summary(self, client: Cozmoai) -> None:
        response = client.org.analytics.with_raw_response.get_dashboard_summary(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetDashboardSummaryResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_dashboard_summary(self, client: Cozmoai) -> None:
        with client.org.analytics.with_streaming_response.get_dashboard_summary(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetDashboardSummaryResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_dashboard_summary(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.with_raw_response.get_dashboard_summary(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_prospect_analytics(self, client: Cozmoai) -> None:
        analytics = client.org.analytics.get_prospect_analytics(
            org_id="org_id",
        )
        assert_matches_type(AnalyticsGetProspectAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_prospect_analytics_with_all_params(self, client: Cozmoai) -> None:
        analytics = client.org.analytics.get_prospect_analytics(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AnalyticsGetProspectAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_prospect_analytics(self, client: Cozmoai) -> None:
        response = client.org.analytics.with_raw_response.get_prospect_analytics(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetProspectAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_prospect_analytics(self, client: Cozmoai) -> None:
        with client.org.analytics.with_streaming_response.get_prospect_analytics(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetProspectAnalyticsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_prospect_analytics(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.with_raw_response.get_prospect_analytics(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_agents(self, client: Cozmoai) -> None:
        analytics = client.org.analytics.list_agents(
            org_id="org_id",
        )
        assert_matches_type(AnalyticsListAgentsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_agents_with_all_params(self, client: Cozmoai) -> None:
        analytics = client.org.analytics.list_agents(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AnalyticsListAgentsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_agents(self, client: Cozmoai) -> None:
        response = client.org.analytics.with_raw_response.list_agents(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsListAgentsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_agents(self, client: Cozmoai) -> None:
        with client.org.analytics.with_streaming_response.list_agents(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsListAgentsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_agents(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.with_raw_response.list_agents(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_batches(self, client: Cozmoai) -> None:
        analytics = client.org.analytics.list_batches(
            org_id="org_id",
        )
        assert_matches_type(AnalyticsListBatchesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_batches_with_all_params(self, client: Cozmoai) -> None:
        analytics = client.org.analytics.list_batches(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AnalyticsListBatchesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_batches(self, client: Cozmoai) -> None:
        response = client.org.analytics.with_raw_response.list_batches(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsListBatchesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_batches(self, client: Cozmoai) -> None:
        with client.org.analytics.with_streaming_response.list_batches(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsListBatchesResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_batches(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.with_raw_response.list_batches(
                org_id="",
            )


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_dashboard_summary(self, async_client: AsyncCozmoai) -> None:
        analytics = await async_client.org.analytics.get_dashboard_summary(
            org_id="org_id",
        )
        assert_matches_type(AnalyticsGetDashboardSummaryResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_dashboard_summary_with_all_params(self, async_client: AsyncCozmoai) -> None:
        analytics = await async_client.org.analytics.get_dashboard_summary(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AnalyticsGetDashboardSummaryResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_dashboard_summary(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.with_raw_response.get_dashboard_summary(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetDashboardSummaryResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_dashboard_summary(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.with_streaming_response.get_dashboard_summary(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetDashboardSummaryResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_dashboard_summary(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.with_raw_response.get_dashboard_summary(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_prospect_analytics(self, async_client: AsyncCozmoai) -> None:
        analytics = await async_client.org.analytics.get_prospect_analytics(
            org_id="org_id",
        )
        assert_matches_type(AnalyticsGetProspectAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_prospect_analytics_with_all_params(self, async_client: AsyncCozmoai) -> None:
        analytics = await async_client.org.analytics.get_prospect_analytics(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AnalyticsGetProspectAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_prospect_analytics(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.with_raw_response.get_prospect_analytics(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetProspectAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_prospect_analytics(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.with_streaming_response.get_prospect_analytics(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetProspectAnalyticsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_prospect_analytics(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.with_raw_response.get_prospect_analytics(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_agents(self, async_client: AsyncCozmoai) -> None:
        analytics = await async_client.org.analytics.list_agents(
            org_id="org_id",
        )
        assert_matches_type(AnalyticsListAgentsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_agents_with_all_params(self, async_client: AsyncCozmoai) -> None:
        analytics = await async_client.org.analytics.list_agents(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AnalyticsListAgentsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_agents(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.with_raw_response.list_agents(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsListAgentsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_agents(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.with_streaming_response.list_agents(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsListAgentsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_agents(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.with_raw_response.list_agents(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_batches(self, async_client: AsyncCozmoai) -> None:
        analytics = await async_client.org.analytics.list_batches(
            org_id="org_id",
        )
        assert_matches_type(AnalyticsListBatchesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_batches_with_all_params(self, async_client: AsyncCozmoai) -> None:
        analytics = await async_client.org.analytics.list_batches(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(AnalyticsListBatchesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_batches(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.with_raw_response.list_batches(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsListBatchesResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_batches(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.with_streaming_response.list_batches(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsListBatchesResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_batches(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.with_raw_response.list_batches(
                org_id="",
            )
