# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types import (
    OrgListVoicesResponse,
    OrgCreateWorkflowRunResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrg:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_workflow_run(self, client: Cozmoai) -> None:
        org = client.org.create_workflow_run(
            org_id="org_id",
            prospect={"phone": "phone"},
            workflow_id="workflow_id",
        )
        assert_matches_type(OrgCreateWorkflowRunResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_workflow_run_with_all_params(self, client: Cozmoai) -> None:
        org = client.org.create_workflow_run(
            org_id="org_id",
            prospect={
                "phone": "phone",
                "country": "country",
                "custom_data": {"foo": "bar"},
                "email": "email",
                "external_id": "external_id",
                "first_name": "first_name",
                "last_name": "last_name",
                "timezone": "timezone",
            },
            workflow_id="workflow_id",
            scheduled_at="scheduled_at",
        )
        assert_matches_type(OrgCreateWorkflowRunResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_workflow_run(self, client: Cozmoai) -> None:
        response = client.org.with_raw_response.create_workflow_run(
            org_id="org_id",
            prospect={"phone": "phone"},
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgCreateWorkflowRunResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_workflow_run(self, client: Cozmoai) -> None:
        with client.org.with_streaming_response.create_workflow_run(
            org_id="org_id",
            prospect={"phone": "phone"},
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgCreateWorkflowRunResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_workflow_run(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.with_raw_response.create_workflow_run(
                org_id="",
                prospect={"phone": "phone"},
                workflow_id="workflow_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_voices(self, client: Cozmoai) -> None:
        org = client.org.list_voices(
            org_id="org_id",
            provider="elevenlabs",
        )
        assert_matches_type(OrgListVoicesResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_voices_with_all_params(self, client: Cozmoai) -> None:
        org = client.org.list_voices(
            org_id="org_id",
            provider="elevenlabs",
            next_page="next_page",
            page=0,
            size=0,
        )
        assert_matches_type(OrgListVoicesResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_voices(self, client: Cozmoai) -> None:
        response = client.org.with_raw_response.list_voices(
            org_id="org_id",
            provider="elevenlabs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = response.parse()
        assert_matches_type(OrgListVoicesResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_voices(self, client: Cozmoai) -> None:
        with client.org.with_streaming_response.list_voices(
            org_id="org_id",
            provider="elevenlabs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = response.parse()
            assert_matches_type(OrgListVoicesResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_voices(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.with_raw_response.list_voices(
                org_id="",
                provider="elevenlabs",
            )


class TestAsyncOrg:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_workflow_run(self, async_client: AsyncCozmoai) -> None:
        org = await async_client.org.create_workflow_run(
            org_id="org_id",
            prospect={"phone": "phone"},
            workflow_id="workflow_id",
        )
        assert_matches_type(OrgCreateWorkflowRunResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_workflow_run_with_all_params(self, async_client: AsyncCozmoai) -> None:
        org = await async_client.org.create_workflow_run(
            org_id="org_id",
            prospect={
                "phone": "phone",
                "country": "country",
                "custom_data": {"foo": "bar"},
                "email": "email",
                "external_id": "external_id",
                "first_name": "first_name",
                "last_name": "last_name",
                "timezone": "timezone",
            },
            workflow_id="workflow_id",
            scheduled_at="scheduled_at",
        )
        assert_matches_type(OrgCreateWorkflowRunResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_workflow_run(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.with_raw_response.create_workflow_run(
            org_id="org_id",
            prospect={"phone": "phone"},
            workflow_id="workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgCreateWorkflowRunResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_workflow_run(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.with_streaming_response.create_workflow_run(
            org_id="org_id",
            prospect={"phone": "phone"},
            workflow_id="workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgCreateWorkflowRunResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_workflow_run(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.with_raw_response.create_workflow_run(
                org_id="",
                prospect={"phone": "phone"},
                workflow_id="workflow_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_voices(self, async_client: AsyncCozmoai) -> None:
        org = await async_client.org.list_voices(
            org_id="org_id",
            provider="elevenlabs",
        )
        assert_matches_type(OrgListVoicesResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_voices_with_all_params(self, async_client: AsyncCozmoai) -> None:
        org = await async_client.org.list_voices(
            org_id="org_id",
            provider="elevenlabs",
            next_page="next_page",
            page=0,
            size=0,
        )
        assert_matches_type(OrgListVoicesResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_voices(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.with_raw_response.list_voices(
            org_id="org_id",
            provider="elevenlabs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        org = await response.parse()
        assert_matches_type(OrgListVoicesResponse, org, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_voices(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.with_streaming_response.list_voices(
            org_id="org_id",
            provider="elevenlabs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            org = await response.parse()
            assert_matches_type(OrgListVoicesResponse, org, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_voices(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.with_raw_response.list_voices(
                org_id="",
                provider="elevenlabs",
            )
