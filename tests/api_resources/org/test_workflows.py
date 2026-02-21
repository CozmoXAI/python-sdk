# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import WorkflowListResponse, WorkflowRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.retrieve(
                workflow_id="workflow_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.org.workflows.with_raw_response.retrieve(
                workflow_id="",
                org_id="org_id",
            )

    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.list(
            org_id="org_id",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.list(
            org_id="org_id",
            is_active=True,
            page=0,
            search="search",
            size=0,
            trigger_type="trigger_type",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.list(
                org_id="",
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.retrieve(
                workflow_id="workflow_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.org.workflows.with_raw_response.retrieve(
                workflow_id="",
                org_id="org_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.list(
            org_id="org_id",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.list(
            org_id="org_id",
            is_active=True,
            page=0,
            search="search",
            size=0,
            trigger_type="trigger_type",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowListResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.list(
                org_id="",
            )
