# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    WorkflowResponse,
    WorkflowListResponse,
    WorkflowDeleteResponse,
    PaginatedRunsExtendedResponse,
    WorkflowRetrieveCallsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.create(
            org_id="org_id",
            definition=[0],
            name="x",
            trigger_type="trigger_type",
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.create(
            org_id="org_id",
            definition=[0],
            name="x",
            trigger_type="trigger_type",
            description="description",
            is_active=True,
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.create(
            org_id="org_id",
            definition=[0],
            name="x",
            trigger_type="trigger_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.create(
            org_id="org_id",
            definition=[0],
            name="x",
            trigger_type="trigger_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.create(
                org_id="",
                definition=[0],
                name="x",
                trigger_type="trigger_type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.update(
            version=0,
            org_id="org_id",
            workflow_id="workflow_id",
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.update(
            version=0,
            org_id="org_id",
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.update(
            version=0,
            org_id="org_id",
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.update(
                version=0,
                org_id="",
                workflow_id="workflow_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.org.workflows.with_raw_response.update(
                version=0,
                org_id="org_id",
                workflow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.list(
            org_id="org_id",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.delete(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowDeleteResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.delete(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowDeleteResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.delete(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowDeleteResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.delete(
                workflow_id="workflow_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.org.workflows.with_raw_response.delete(
                workflow_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_duplicate(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.duplicate(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_duplicate(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.duplicate(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_duplicate(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.duplicate(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_duplicate(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.duplicate(
                workflow_id="workflow_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.org.workflows.with_raw_response.duplicate(
                workflow_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_calls(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.retrieve_calls(
            node_id="node_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowRetrieveCallsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_calls(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.retrieve_calls(
            node_id="node_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowRetrieveCallsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_calls(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.retrieve_calls(
            node_id="node_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowRetrieveCallsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_calls(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.retrieve_calls(
                node_id="node_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.org.workflows.with_raw_response.retrieve_calls(
                node_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_runs(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.retrieve_runs(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(PaginatedRunsExtendedResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_runs_with_all_params(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.retrieve_runs(
            workflow_id="workflow_id",
            org_id="org_id",
            batch_id="batch_id",
            end_date="end_date",
            limit=0,
            page=0,
            prospect_id="prospect_id",
            sort="sort",
            start_date="start_date",
            status="status",
            workflow_version_id="workflow_version_id",
        )
        assert_matches_type(PaginatedRunsExtendedResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_runs(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.retrieve_runs(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(PaginatedRunsExtendedResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_runs(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.retrieve_runs(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(PaginatedRunsExtendedResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_runs(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.retrieve_runs(
                workflow_id="workflow_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.org.workflows.with_raw_response.retrieve_runs(
                workflow_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_definition(self, client: Cozmoai) -> None:
        workflow = client.org.workflows.update_definition(
            workflow_id="workflow_id",
            org_id="org_id",
            definition=[0],
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_definition(self, client: Cozmoai) -> None:
        response = client.org.workflows.with_raw_response.update_definition(
            workflow_id="workflow_id",
            org_id="org_id",
            definition=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_definition(self, client: Cozmoai) -> None:
        with client.org.workflows.with_streaming_response.update_definition(
            workflow_id="workflow_id",
            org_id="org_id",
            definition=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_definition(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.workflows.with_raw_response.update_definition(
                workflow_id="workflow_id",
                org_id="",
                definition=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.org.workflows.with_raw_response.update_definition(
                workflow_id="",
                org_id="org_id",
                definition=[0],
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.create(
            org_id="org_id",
            definition=[0],
            name="x",
            trigger_type="trigger_type",
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.create(
            org_id="org_id",
            definition=[0],
            name="x",
            trigger_type="trigger_type",
            description="description",
            is_active=True,
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.create(
            org_id="org_id",
            definition=[0],
            name="x",
            trigger_type="trigger_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.create(
            org_id="org_id",
            definition=[0],
            name="x",
            trigger_type="trigger_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.create(
                org_id="",
                definition=[0],
                name="x",
                trigger_type="trigger_type",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.retrieve(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.update(
            version=0,
            org_id="org_id",
            workflow_id="workflow_id",
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.update(
            version=0,
            org_id="org_id",
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.update(
            version=0,
            org_id="org_id",
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.update(
                version=0,
                org_id="",
                workflow_id="workflow_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.org.workflows.with_raw_response.update(
                version=0,
                org_id="org_id",
                workflow_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.list(
            org_id="org_id",
        )
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowListResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.delete(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowDeleteResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.delete(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowDeleteResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.delete(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowDeleteResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.delete(
                workflow_id="workflow_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.org.workflows.with_raw_response.delete(
                workflow_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_duplicate(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.duplicate(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_duplicate(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.duplicate(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_duplicate(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.duplicate(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_duplicate(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.duplicate(
                workflow_id="workflow_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.org.workflows.with_raw_response.duplicate(
                workflow_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_calls(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.retrieve_calls(
            node_id="node_id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowRetrieveCallsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_calls(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.retrieve_calls(
            node_id="node_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowRetrieveCallsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_calls(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.retrieve_calls(
            node_id="node_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowRetrieveCallsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_calls(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.retrieve_calls(
                node_id="node_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.org.workflows.with_raw_response.retrieve_calls(
                node_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_runs(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.retrieve_runs(
            workflow_id="workflow_id",
            org_id="org_id",
        )
        assert_matches_type(PaginatedRunsExtendedResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_runs_with_all_params(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.retrieve_runs(
            workflow_id="workflow_id",
            org_id="org_id",
            batch_id="batch_id",
            end_date="end_date",
            limit=0,
            page=0,
            prospect_id="prospect_id",
            sort="sort",
            start_date="start_date",
            status="status",
            workflow_version_id="workflow_version_id",
        )
        assert_matches_type(PaginatedRunsExtendedResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_runs(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.retrieve_runs(
            workflow_id="workflow_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(PaginatedRunsExtendedResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_runs(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.retrieve_runs(
            workflow_id="workflow_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(PaginatedRunsExtendedResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_runs(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.retrieve_runs(
                workflow_id="workflow_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.org.workflows.with_raw_response.retrieve_runs(
                workflow_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_definition(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.workflows.update_definition(
            workflow_id="workflow_id",
            org_id="org_id",
            definition=[0],
        )
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_definition(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.workflows.with_raw_response.update_definition(
            workflow_id="workflow_id",
            org_id="org_id",
            definition=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_definition(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.workflows.with_streaming_response.update_definition(
            workflow_id="workflow_id",
            org_id="org_id",
            definition=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_definition(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.workflows.with_raw_response.update_definition(
                workflow_id="workflow_id",
                org_id="",
                definition=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.org.workflows.with_raw_response.update_definition(
                workflow_id="",
                org_id="org_id",
                definition=[0],
            )
