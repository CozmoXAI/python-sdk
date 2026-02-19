# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.analytics import (
    WorkflowListWorkflowsResponse,
    WorkflowGetWorkflowAnalyticsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_workflow_analytics(self, client: Cozmoai) -> None:
        workflow = client.org.analytics.workflows.get_workflow_analytics(
            id="id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowGetWorkflowAnalyticsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_workflow_analytics_with_all_params(self, client: Cozmoai) -> None:
        workflow = client.org.analytics.workflows.get_workflow_analytics(
            id="id",
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(WorkflowGetWorkflowAnalyticsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_workflow_analytics(self, client: Cozmoai) -> None:
        response = client.org.analytics.workflows.with_raw_response.get_workflow_analytics(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowGetWorkflowAnalyticsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_workflow_analytics(self, client: Cozmoai) -> None:
        with client.org.analytics.workflows.with_streaming_response.get_workflow_analytics(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowGetWorkflowAnalyticsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_workflow_analytics(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.workflows.with_raw_response.get_workflow_analytics(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.analytics.workflows.with_raw_response.get_workflow_analytics(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_workflows(self, client: Cozmoai) -> None:
        workflow = client.org.analytics.workflows.list_workflows(
            org_id="org_id",
        )
        assert_matches_type(WorkflowListWorkflowsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_workflows_with_all_params(self, client: Cozmoai) -> None:
        workflow = client.org.analytics.workflows.list_workflows(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(WorkflowListWorkflowsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_workflows(self, client: Cozmoai) -> None:
        response = client.org.analytics.workflows.with_raw_response.list_workflows(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowListWorkflowsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_workflows(self, client: Cozmoai) -> None:
        with client.org.analytics.workflows.with_streaming_response.list_workflows(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowListWorkflowsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_workflows(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.analytics.workflows.with_raw_response.list_workflows(
                org_id="",
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_workflow_analytics(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.analytics.workflows.get_workflow_analytics(
            id="id",
            org_id="org_id",
        )
        assert_matches_type(WorkflowGetWorkflowAnalyticsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_workflow_analytics_with_all_params(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.analytics.workflows.get_workflow_analytics(
            id="id",
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(WorkflowGetWorkflowAnalyticsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_workflow_analytics(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.workflows.with_raw_response.get_workflow_analytics(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowGetWorkflowAnalyticsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_workflow_analytics(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.workflows.with_streaming_response.get_workflow_analytics(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowGetWorkflowAnalyticsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_workflow_analytics(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.workflows.with_raw_response.get_workflow_analytics(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.analytics.workflows.with_raw_response.get_workflow_analytics(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_workflows(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.analytics.workflows.list_workflows(
            org_id="org_id",
        )
        assert_matches_type(WorkflowListWorkflowsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_workflows_with_all_params(self, async_client: AsyncCozmoai) -> None:
        workflow = await async_client.org.analytics.workflows.list_workflows(
            org_id="org_id",
            end_date="end_date",
            start_date="start_date",
        )
        assert_matches_type(WorkflowListWorkflowsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_workflows(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.analytics.workflows.with_raw_response.list_workflows(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowListWorkflowsResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_workflows(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.analytics.workflows.with_streaming_response.list_workflows(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowListWorkflowsResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_workflows(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.analytics.workflows.with_raw_response.list_workflows(
                org_id="",
            )
