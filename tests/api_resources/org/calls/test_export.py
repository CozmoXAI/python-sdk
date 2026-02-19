# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.calls import (
    ExportGetCountResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_count(self, client: Cozmoai) -> None:
        export = client.org.calls.export.get_count(
            org_id="org_id",
        )
        assert_matches_type(ExportGetCountResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_count_with_all_params(self, client: Cozmoai) -> None:
        export = client.org.calls.export.get_count(
            org_id="org_id",
            agent_id="agent_id",
            direction="direction",
            end_date="end_date",
            min_duration=0,
            phone="phone",
            prospect_external_id="prospect_external_id",
            prospect_id="prospect_id",
            start_date="start_date",
            status="status",
            workflow_id="workflow_id",
        )
        assert_matches_type(ExportGetCountResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_count(self, client: Cozmoai) -> None:
        response = client.org.calls.export.with_raw_response.get_count(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ExportGetCountResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_count(self, client: Cozmoai) -> None:
        with client.org.calls.export.with_streaming_response.get_count(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ExportGetCountResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_count(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.calls.export.with_raw_response.get_count(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_csv(self, client: Cozmoai) -> None:
        export = client.org.calls.export.get_csv(
            org_id="org_id",
        )
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_csv_with_all_params(self, client: Cozmoai) -> None:
        export = client.org.calls.export.get_csv(
            org_id="org_id",
            agent_id="agent_id",
            direction="direction",
            end_date="end_date",
            min_duration=0,
            phone="phone",
            prospect_external_id="prospect_external_id",
            prospect_id="prospect_id",
            start_date="start_date",
            status="status",
            workflow_id="workflow_id",
        )
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_csv(self, client: Cozmoai) -> None:
        response = client.org.calls.export.with_raw_response.get_csv(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_csv(self, client: Cozmoai) -> None:
        with client.org.calls.export.with_streaming_response.get_csv(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(str, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_csv(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.calls.export.with_raw_response.get_csv(
                org_id="",
            )


class TestAsyncExport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_count(self, async_client: AsyncCozmoai) -> None:
        export = await async_client.org.calls.export.get_count(
            org_id="org_id",
        )
        assert_matches_type(ExportGetCountResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_count_with_all_params(self, async_client: AsyncCozmoai) -> None:
        export = await async_client.org.calls.export.get_count(
            org_id="org_id",
            agent_id="agent_id",
            direction="direction",
            end_date="end_date",
            min_duration=0,
            phone="phone",
            prospect_external_id="prospect_external_id",
            prospect_id="prospect_id",
            start_date="start_date",
            status="status",
            workflow_id="workflow_id",
        )
        assert_matches_type(ExportGetCountResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_count(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.calls.export.with_raw_response.get_count(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ExportGetCountResponse, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_count(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.calls.export.with_streaming_response.get_count(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ExportGetCountResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_count(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.calls.export.with_raw_response.get_count(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_csv(self, async_client: AsyncCozmoai) -> None:
        export = await async_client.org.calls.export.get_csv(
            org_id="org_id",
        )
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_csv_with_all_params(self, async_client: AsyncCozmoai) -> None:
        export = await async_client.org.calls.export.get_csv(
            org_id="org_id",
            agent_id="agent_id",
            direction="direction",
            end_date="end_date",
            min_duration=0,
            phone="phone",
            prospect_external_id="prospect_external_id",
            prospect_id="prospect_id",
            start_date="start_date",
            status="status",
            workflow_id="workflow_id",
        )
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_csv(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.calls.export.with_raw_response.get_csv(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(str, export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_csv(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.calls.export.with_streaming_response.get_csv(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(str, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_csv(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.calls.export.with_raw_response.get_csv(
                org_id="",
            )
