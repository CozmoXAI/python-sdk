# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.agents import UnitTestRunLatestResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUnitTestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_latest(self, client: Cozmoai) -> None:
        unit_test_run = client.org.agents.unit_test_runs.latest(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(UnitTestRunLatestResponse, unit_test_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_latest_with_all_params(self, client: Cozmoai) -> None:
        unit_test_run = client.org.agents.unit_test_runs.latest(
            agent_id="agent_id",
            org_id="org_id",
            page=0,
            size=0,
        )
        assert_matches_type(UnitTestRunLatestResponse, unit_test_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_latest(self, client: Cozmoai) -> None:
        response = client.org.agents.unit_test_runs.with_raw_response.latest(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test_run = response.parse()
        assert_matches_type(UnitTestRunLatestResponse, unit_test_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_latest(self, client: Cozmoai) -> None:
        with client.org.agents.unit_test_runs.with_streaming_response.latest(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test_run = response.parse()
            assert_matches_type(UnitTestRunLatestResponse, unit_test_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_latest(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.unit_test_runs.with_raw_response.latest(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.unit_test_runs.with_raw_response.latest(
                agent_id="",
                org_id="org_id",
            )


class TestAsyncUnitTestRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_latest(self, async_client: AsyncCozmoai) -> None:
        unit_test_run = await async_client.org.agents.unit_test_runs.latest(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(UnitTestRunLatestResponse, unit_test_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_latest_with_all_params(self, async_client: AsyncCozmoai) -> None:
        unit_test_run = await async_client.org.agents.unit_test_runs.latest(
            agent_id="agent_id",
            org_id="org_id",
            page=0,
            size=0,
        )
        assert_matches_type(UnitTestRunLatestResponse, unit_test_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_latest(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.unit_test_runs.with_raw_response.latest(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test_run = await response.parse()
        assert_matches_type(UnitTestRunLatestResponse, unit_test_run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_latest(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.unit_test_runs.with_streaming_response.latest(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test_run = await response.parse()
            assert_matches_type(UnitTestRunLatestResponse, unit_test_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_latest(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.unit_test_runs.with_raw_response.latest(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.unit_test_runs.with_raw_response.latest(
                agent_id="",
                org_id="org_id",
            )
