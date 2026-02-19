# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.analytics import (
    CallListCallsResponse,
    CallGetCallCostsResponse,
    CallListCallsByHourResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_call_costs(self, client: Cozmoai) -> None:
        call = client.org.analytics.calls.get_call_costs(
            org_id="org_id",
        )
        assert_matches_type(CallGetCallCostsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_call_costs_with_all_params(self, client: Cozmoai) -> None:
        call = client.org.analytics.calls.get_call_costs(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(CallGetCallCostsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_call_costs(self, client: Cozmoai) -> None:
        response = client.org.analytics.calls.with_raw_response.get_call_costs(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetCallCostsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_call_costs(self, client: Cozmoai) -> None:
        with client.org.analytics.calls.with_streaming_response.get_call_costs(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetCallCostsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_call_costs(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.calls.with_raw_response.get_call_costs(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_calls(self, client: Cozmoai) -> None:
        call = client.org.analytics.calls.list_calls(
            org_id="org_id",
        )
        assert_matches_type(CallListCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_calls_with_all_params(self, client: Cozmoai) -> None:
        call = client.org.analytics.calls.list_calls(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(CallListCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_calls(self, client: Cozmoai) -> None:
        response = client.org.analytics.calls.with_raw_response.list_calls(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_calls(self, client: Cozmoai) -> None:
        with client.org.analytics.calls.with_streaming_response.list_calls(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListCallsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_calls(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.calls.with_raw_response.list_calls(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_calls_by_hour(self, client: Cozmoai) -> None:
        call = client.org.analytics.calls.list_calls_by_hour(
            org_id="org_id",
        )
        assert_matches_type(CallListCallsByHourResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_calls_by_hour_with_all_params(self, client: Cozmoai) -> None:
        call = client.org.analytics.calls.list_calls_by_hour(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(CallListCallsByHourResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_calls_by_hour(self, client: Cozmoai) -> None:
        response = client.org.analytics.calls.with_raw_response.list_calls_by_hour(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListCallsByHourResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_calls_by_hour(self, client: Cozmoai) -> None:
        with client.org.analytics.calls.with_streaming_response.list_calls_by_hour(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListCallsByHourResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_calls_by_hour(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.calls.with_raw_response.list_calls_by_hour(
                org_id="",
            )


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_call_costs(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.analytics.calls.get_call_costs(
            org_id="org_id",
        )
        assert_matches_type(CallGetCallCostsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_call_costs_with_all_params(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.analytics.calls.get_call_costs(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(CallGetCallCostsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_call_costs(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.calls.with_raw_response.get_call_costs(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetCallCostsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_call_costs(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.calls.with_streaming_response.get_call_costs(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetCallCostsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_call_costs(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.calls.with_raw_response.get_call_costs(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_calls(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.analytics.calls.list_calls(
            org_id="org_id",
        )
        assert_matches_type(CallListCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_calls_with_all_params(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.analytics.calls.list_calls(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(CallListCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_calls(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.calls.with_raw_response.list_calls(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListCallsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_calls(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.calls.with_streaming_response.list_calls(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListCallsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_calls(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.calls.with_raw_response.list_calls(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_calls_by_hour(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.analytics.calls.list_calls_by_hour(
            org_id="org_id",
        )
        assert_matches_type(CallListCallsByHourResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_calls_by_hour_with_all_params(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.analytics.calls.list_calls_by_hour(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(CallListCallsByHourResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_calls_by_hour(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.calls.with_raw_response.list_calls_by_hour(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListCallsByHourResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_calls_by_hour(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.calls.with_streaming_response.list_calls_by_hour(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListCallsByHourResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_calls_by_hour(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.calls.with_raw_response.list_calls_by_hour(
                org_id="",
            )
