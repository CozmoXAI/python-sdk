# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    CallListResponse,
    CallGetDetailsResponse,
    CallGetToolLogsResponse,
    CallGetRecordingResponse,
    CallGetTranscriptResponse,
    CallGetEvaluationsResponse,
    CallCreateDashboardCallResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        call = client.org.calls.list(
            org_id="org_id",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        call = client.org.calls.list(
            org_id="org_id",
            agent_id="agent_id",
            direction="direction",
            end_date="end_date",
            min_duration=0,
            page=0,
            phone="phone",
            prospect_external_id="prospect_external_id",
            prospect_id="prospect_id",
            size=100,
            start_date="start_date",
            status="status",
            workflow_id="workflow_id",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.calls.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.calls.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.calls.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_dashboard_call(self, client: Cozmoai) -> None:
        call = client.org.calls.create_dashboard_call(
            org_id="org_id",
            agent_id="agent_id",
            from_number="from_number",
            phone_number="phone_number",
        )
        assert_matches_type(CallCreateDashboardCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_dashboard_call_with_all_params(self, client: Cozmoai) -> None:
        call = client.org.calls.create_dashboard_call(
            org_id="org_id",
            agent_id="agent_id",
            from_number="from_number",
            phone_number="phone_number",
            extras={"foo": "string"},
        )
        assert_matches_type(CallCreateDashboardCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_dashboard_call(self, client: Cozmoai) -> None:
        response = client.org.calls.with_raw_response.create_dashboard_call(
            org_id="org_id",
            agent_id="agent_id",
            from_number="from_number",
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallCreateDashboardCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_dashboard_call(self, client: Cozmoai) -> None:
        with client.org.calls.with_streaming_response.create_dashboard_call(
            org_id="org_id",
            agent_id="agent_id",
            from_number="from_number",
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallCreateDashboardCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_dashboard_call(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.calls.with_raw_response.create_dashboard_call(
                org_id="",
                agent_id="agent_id",
                from_number="from_number",
                phone_number="phone_number",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_details(self, client: Cozmoai) -> None:
        call = client.org.calls.get_details(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetDetailsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_details(self, client: Cozmoai) -> None:
        response = client.org.calls.with_raw_response.get_details(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetDetailsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_details(self, client: Cozmoai) -> None:
        with client.org.calls.with_streaming_response.get_details(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetDetailsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_details(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.calls.with_raw_response.get_details(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.org.calls.with_raw_response.get_details(
                call_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_evaluations(self, client: Cozmoai) -> None:
        call = client.org.calls.get_evaluations(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetEvaluationsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_evaluations(self, client: Cozmoai) -> None:
        response = client.org.calls.with_raw_response.get_evaluations(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetEvaluationsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_evaluations(self, client: Cozmoai) -> None:
        with client.org.calls.with_streaming_response.get_evaluations(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetEvaluationsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_evaluations(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.calls.with_raw_response.get_evaluations(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.org.calls.with_raw_response.get_evaluations(
                call_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_recording(self, client: Cozmoai) -> None:
        call = client.org.calls.get_recording(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetRecordingResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_recording(self, client: Cozmoai) -> None:
        response = client.org.calls.with_raw_response.get_recording(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetRecordingResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_recording(self, client: Cozmoai) -> None:
        with client.org.calls.with_streaming_response.get_recording(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetRecordingResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_recording(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.calls.with_raw_response.get_recording(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.org.calls.with_raw_response.get_recording(
                call_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_tool_logs(self, client: Cozmoai) -> None:
        call = client.org.calls.get_tool_logs(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetToolLogsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_tool_logs(self, client: Cozmoai) -> None:
        response = client.org.calls.with_raw_response.get_tool_logs(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetToolLogsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_tool_logs(self, client: Cozmoai) -> None:
        with client.org.calls.with_streaming_response.get_tool_logs(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetToolLogsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_tool_logs(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.calls.with_raw_response.get_tool_logs(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.org.calls.with_raw_response.get_tool_logs(
                call_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_transcript(self, client: Cozmoai) -> None:
        call = client.org.calls.get_transcript(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetTranscriptResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_transcript(self, client: Cozmoai) -> None:
        response = client.org.calls.with_raw_response.get_transcript(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallGetTranscriptResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_transcript(self, client: Cozmoai) -> None:
        with client.org.calls.with_streaming_response.get_transcript(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallGetTranscriptResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_transcript(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.calls.with_raw_response.get_transcript(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.org.calls.with_raw_response.get_transcript(
                call_id="",
                org_id="org_id",
            )


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.calls.list(
            org_id="org_id",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.calls.list(
            org_id="org_id",
            agent_id="agent_id",
            direction="direction",
            end_date="end_date",
            min_duration=0,
            page=0,
            phone="phone",
            prospect_external_id="prospect_external_id",
            prospect_id="prospect_id",
            size=100,
            start_date="start_date",
            status="status",
            workflow_id="workflow_id",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.calls.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.calls.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.calls.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_dashboard_call(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.calls.create_dashboard_call(
            org_id="org_id",
            agent_id="agent_id",
            from_number="from_number",
            phone_number="phone_number",
        )
        assert_matches_type(CallCreateDashboardCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_dashboard_call_with_all_params(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.calls.create_dashboard_call(
            org_id="org_id",
            agent_id="agent_id",
            from_number="from_number",
            phone_number="phone_number",
            extras={"foo": "string"},
        )
        assert_matches_type(CallCreateDashboardCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_dashboard_call(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.calls.with_raw_response.create_dashboard_call(
            org_id="org_id",
            agent_id="agent_id",
            from_number="from_number",
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallCreateDashboardCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_dashboard_call(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.calls.with_streaming_response.create_dashboard_call(
            org_id="org_id",
            agent_id="agent_id",
            from_number="from_number",
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallCreateDashboardCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_dashboard_call(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.calls.with_raw_response.create_dashboard_call(
                org_id="",
                agent_id="agent_id",
                from_number="from_number",
                phone_number="phone_number",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_details(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.calls.get_details(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetDetailsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_details(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.calls.with_raw_response.get_details(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetDetailsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_details(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.calls.with_streaming_response.get_details(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetDetailsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_details(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_details(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_details(
                call_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_evaluations(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.calls.get_evaluations(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetEvaluationsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_evaluations(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.calls.with_raw_response.get_evaluations(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetEvaluationsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_evaluations(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.calls.with_streaming_response.get_evaluations(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetEvaluationsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_evaluations(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_evaluations(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_evaluations(
                call_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_recording(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.calls.get_recording(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetRecordingResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_recording(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.calls.with_raw_response.get_recording(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetRecordingResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_recording(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.calls.with_streaming_response.get_recording(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetRecordingResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_recording(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_recording(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_recording(
                call_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_tool_logs(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.calls.get_tool_logs(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetToolLogsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_tool_logs(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.calls.with_raw_response.get_tool_logs(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetToolLogsResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_tool_logs(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.calls.with_streaming_response.get_tool_logs(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetToolLogsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_tool_logs(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_tool_logs(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_tool_logs(
                call_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_transcript(self, async_client: AsyncCozmoai) -> None:
        call = await async_client.org.calls.get_transcript(
            call_id="call_id",
            org_id="org_id",
        )
        assert_matches_type(CallGetTranscriptResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_transcript(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.calls.with_raw_response.get_transcript(
            call_id="call_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallGetTranscriptResponse, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_transcript(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.calls.with_streaming_response.get_transcript(
            call_id="call_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallGetTranscriptResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_transcript(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_transcript(
                call_id="call_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.org.calls.with_raw_response.get_transcript(
                call_id="",
                org_id="org_id",
            )
