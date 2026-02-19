# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    BatchResponse,
    BatchListWorkflowRunsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_workflow_batch(self, client: Cozmoai) -> None:
        batch = client.org.batches.get_workflow_batch(
            batch_id="batch_id",
            org_id="org_id",
        )
        assert_matches_type(BatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_workflow_batch(self, client: Cozmoai) -> None:
        response = client.org.batches.with_raw_response.get_workflow_batch(
            batch_id="batch_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_workflow_batch(self, client: Cozmoai) -> None:
        with client.org.batches.with_streaming_response.get_workflow_batch(
            batch_id="batch_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_workflow_batch(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.batches.with_raw_response.get_workflow_batch(
                batch_id="batch_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.org.batches.with_raw_response.get_workflow_batch(
                batch_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_workflow_runs(self, client: Cozmoai) -> None:
        batch = client.org.batches.list_workflow_runs(
            batch_id="batch_id",
            org_id="org_id",
        )
        assert_matches_type(BatchListWorkflowRunsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_workflow_runs_with_all_params(self, client: Cozmoai) -> None:
        batch = client.org.batches.list_workflow_runs(
            batch_id="batch_id",
            org_id="org_id",
            limit=0,
            page=0,
            status="status",
        )
        assert_matches_type(BatchListWorkflowRunsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_workflow_runs(self, client: Cozmoai) -> None:
        response = client.org.batches.with_raw_response.list_workflow_runs(
            batch_id="batch_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchListWorkflowRunsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_workflow_runs(self, client: Cozmoai) -> None:
        with client.org.batches.with_streaming_response.list_workflow_runs(
            batch_id="batch_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchListWorkflowRunsResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_workflow_runs(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.batches.with_raw_response.list_workflow_runs(
                batch_id="batch_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.org.batches.with_raw_response.list_workflow_runs(
                batch_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_batch_status(self, client: Cozmoai) -> None:
        batch = client.org.batches.update_batch_status(
            batch_id="batch_id",
            org_id="org_id",
            status="PENDING",
        )
        assert_matches_type(BatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_batch_status(self, client: Cozmoai) -> None:
        response = client.org.batches.with_raw_response.update_batch_status(
            batch_id="batch_id",
            org_id="org_id",
            status="PENDING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_batch_status(self, client: Cozmoai) -> None:
        with client.org.batches.with_streaming_response.update_batch_status(
            batch_id="batch_id",
            org_id="org_id",
            status="PENDING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_batch_status(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.batches.with_raw_response.update_batch_status(
                batch_id="batch_id",
                org_id="",
                status="PENDING",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.org.batches.with_raw_response.update_batch_status(
                batch_id="",
                org_id="org_id",
                status="PENDING",
            )


class TestAsyncBatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_workflow_batch(self, async_client: AsyncCozmoai) -> None:
        batch = await async_client.org.batches.get_workflow_batch(
            batch_id="batch_id",
            org_id="org_id",
        )
        assert_matches_type(BatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_workflow_batch(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.batches.with_raw_response.get_workflow_batch(
            batch_id="batch_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_workflow_batch(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.batches.with_streaming_response.get_workflow_batch(
            batch_id="batch_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_workflow_batch(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.batches.with_raw_response.get_workflow_batch(
                batch_id="batch_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.org.batches.with_raw_response.get_workflow_batch(
                batch_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_workflow_runs(self, async_client: AsyncCozmoai) -> None:
        batch = await async_client.org.batches.list_workflow_runs(
            batch_id="batch_id",
            org_id="org_id",
        )
        assert_matches_type(BatchListWorkflowRunsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_workflow_runs_with_all_params(self, async_client: AsyncCozmoai) -> None:
        batch = await async_client.org.batches.list_workflow_runs(
            batch_id="batch_id",
            org_id="org_id",
            limit=0,
            page=0,
            status="status",
        )
        assert_matches_type(BatchListWorkflowRunsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_workflow_runs(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.batches.with_raw_response.list_workflow_runs(
            batch_id="batch_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchListWorkflowRunsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_workflow_runs(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.batches.with_streaming_response.list_workflow_runs(
            batch_id="batch_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchListWorkflowRunsResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_workflow_runs(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.batches.with_raw_response.list_workflow_runs(
                batch_id="batch_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.org.batches.with_raw_response.list_workflow_runs(
                batch_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_batch_status(self, async_client: AsyncCozmoai) -> None:
        batch = await async_client.org.batches.update_batch_status(
            batch_id="batch_id",
            org_id="org_id",
            status="PENDING",
        )
        assert_matches_type(BatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_batch_status(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.batches.with_raw_response.update_batch_status(
            batch_id="batch_id",
            org_id="org_id",
            status="PENDING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch_status(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.batches.with_streaming_response.update_batch_status(
            batch_id="batch_id",
            org_id="org_id",
            status="PENDING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_batch_status(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.batches.with_raw_response.update_batch_status(
                batch_id="batch_id",
                org_id="",
                status="PENDING",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.org.batches.with_raw_response.update_batch_status(
                batch_id="",
                org_id="org_id",
                status="PENDING",
            )
