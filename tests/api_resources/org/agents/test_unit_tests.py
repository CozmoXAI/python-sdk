# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.agents import (
    UnitTest,
    UnitTestListResponse,
    UnitTestDeleteResponse,
    UnitTestGenerateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUnitTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        unit_test = client.org.agents.unit_tests.create(
            agent_id="agent_id",
            org_id="org_id",
            answer_prompt="answer_prompt",
            question_prompt="question_prompt",
            question_variance="low",
        )
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cozmoai) -> None:
        unit_test = client.org.agents.unit_tests.create(
            agent_id="agent_id",
            org_id="org_id",
            answer_prompt="answer_prompt",
            question_prompt="question_prompt",
            question_variance="low",
            function_tool_assertion="function_tool_assertion",
            title="title",
            yaml_config="yaml_config",
        )
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.org.agents.unit_tests.with_raw_response.create(
            agent_id="agent_id",
            org_id="org_id",
            answer_prompt="answer_prompt",
            question_prompt="question_prompt",
            question_variance="low",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = response.parse()
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.org.agents.unit_tests.with_streaming_response.create(
            agent_id="agent_id",
            org_id="org_id",
            answer_prompt="answer_prompt",
            question_prompt="question_prompt",
            question_variance="low",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = response.parse()
            assert_matches_type(UnitTest, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.create(
                agent_id="agent_id",
                org_id="",
                answer_prompt="answer_prompt",
                question_prompt="question_prompt",
                question_variance="low",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.create(
                agent_id="",
                org_id="org_id",
                answer_prompt="answer_prompt",
                question_prompt="question_prompt",
                question_variance="low",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        unit_test = client.org.agents.unit_tests.update(
            test_id="test_id",
            org_id="org_id",
            agent_id="agent_id",
        )
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        unit_test = client.org.agents.unit_tests.update(
            test_id="test_id",
            org_id="org_id",
            agent_id="agent_id",
            answer_prompt="answer_prompt",
            function_tool_assertion="function_tool_assertion",
            question_prompt="question_prompt",
            question_variance="low",
            title="title",
            yaml_config="yaml_config",
        )
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.agents.unit_tests.with_raw_response.update(
            test_id="test_id",
            org_id="org_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = response.parse()
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.agents.unit_tests.with_streaming_response.update(
            test_id="test_id",
            org_id="org_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = response.parse()
            assert_matches_type(UnitTest, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.update(
                test_id="test_id",
                org_id="",
                agent_id="agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.update(
                test_id="test_id",
                org_id="org_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.update(
                test_id="",
                org_id="org_id",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        unit_test = client.org.agents.unit_tests.list(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(UnitTestListResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        unit_test = client.org.agents.unit_tests.list(
            agent_id="agent_id",
            org_id="org_id",
            page=0,
            size=0,
        )
        assert_matches_type(UnitTestListResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.agents.unit_tests.with_raw_response.list(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = response.parse()
        assert_matches_type(UnitTestListResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.agents.unit_tests.with_streaming_response.list(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = response.parse()
            assert_matches_type(UnitTestListResponse, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.list(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.list(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        unit_test = client.org.agents.unit_tests.delete(
            agent_id="agent_id",
            org_id="org_id",
            ids=["string"],
        )
        assert_matches_type(UnitTestDeleteResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.agents.unit_tests.with_raw_response.delete(
            agent_id="agent_id",
            org_id="org_id",
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = response.parse()
        assert_matches_type(UnitTestDeleteResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.agents.unit_tests.with_streaming_response.delete(
            agent_id="agent_id",
            org_id="org_id",
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = response.parse()
            assert_matches_type(UnitTestDeleteResponse, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.delete(
                agent_id="agent_id",
                org_id="",
                ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.delete(
                agent_id="",
                org_id="org_id",
                ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate(self, client: Cozmoai) -> None:
        unit_test = client.org.agents.unit_tests.generate(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(UnitTestGenerateResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_with_all_params(self, client: Cozmoai) -> None:
        unit_test = client.org.agents.unit_tests.generate(
            agent_id="agent_id",
            org_id="org_id",
            count=1,
        )
        assert_matches_type(UnitTestGenerateResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate(self, client: Cozmoai) -> None:
        response = client.org.agents.unit_tests.with_raw_response.generate(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = response.parse()
        assert_matches_type(UnitTestGenerateResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate(self, client: Cozmoai) -> None:
        with client.org.agents.unit_tests.with_streaming_response.generate(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = response.parse()
            assert_matches_type(UnitTestGenerateResponse, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.generate(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.unit_tests.with_raw_response.generate(
                agent_id="",
                org_id="org_id",
            )


class TestAsyncUnitTests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        unit_test = await async_client.org.agents.unit_tests.create(
            agent_id="agent_id",
            org_id="org_id",
            answer_prompt="answer_prompt",
            question_prompt="question_prompt",
            question_variance="low",
        )
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCozmoai) -> None:
        unit_test = await async_client.org.agents.unit_tests.create(
            agent_id="agent_id",
            org_id="org_id",
            answer_prompt="answer_prompt",
            question_prompt="question_prompt",
            question_variance="low",
            function_tool_assertion="function_tool_assertion",
            title="title",
            yaml_config="yaml_config",
        )
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.unit_tests.with_raw_response.create(
            agent_id="agent_id",
            org_id="org_id",
            answer_prompt="answer_prompt",
            question_prompt="question_prompt",
            question_variance="low",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = await response.parse()
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.unit_tests.with_streaming_response.create(
            agent_id="agent_id",
            org_id="org_id",
            answer_prompt="answer_prompt",
            question_prompt="question_prompt",
            question_variance="low",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = await response.parse()
            assert_matches_type(UnitTest, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.create(
                agent_id="agent_id",
                org_id="",
                answer_prompt="answer_prompt",
                question_prompt="question_prompt",
                question_variance="low",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.create(
                agent_id="",
                org_id="org_id",
                answer_prompt="answer_prompt",
                question_prompt="question_prompt",
                question_variance="low",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        unit_test = await async_client.org.agents.unit_tests.update(
            test_id="test_id",
            org_id="org_id",
            agent_id="agent_id",
        )
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        unit_test = await async_client.org.agents.unit_tests.update(
            test_id="test_id",
            org_id="org_id",
            agent_id="agent_id",
            answer_prompt="answer_prompt",
            function_tool_assertion="function_tool_assertion",
            question_prompt="question_prompt",
            question_variance="low",
            title="title",
            yaml_config="yaml_config",
        )
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.unit_tests.with_raw_response.update(
            test_id="test_id",
            org_id="org_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = await response.parse()
        assert_matches_type(UnitTest, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.unit_tests.with_streaming_response.update(
            test_id="test_id",
            org_id="org_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = await response.parse()
            assert_matches_type(UnitTest, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.update(
                test_id="test_id",
                org_id="",
                agent_id="agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.update(
                test_id="test_id",
                org_id="org_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.update(
                test_id="",
                org_id="org_id",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        unit_test = await async_client.org.agents.unit_tests.list(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(UnitTestListResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        unit_test = await async_client.org.agents.unit_tests.list(
            agent_id="agent_id",
            org_id="org_id",
            page=0,
            size=0,
        )
        assert_matches_type(UnitTestListResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.unit_tests.with_raw_response.list(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = await response.parse()
        assert_matches_type(UnitTestListResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.unit_tests.with_streaming_response.list(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = await response.parse()
            assert_matches_type(UnitTestListResponse, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.list(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.list(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        unit_test = await async_client.org.agents.unit_tests.delete(
            agent_id="agent_id",
            org_id="org_id",
            ids=["string"],
        )
        assert_matches_type(UnitTestDeleteResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.unit_tests.with_raw_response.delete(
            agent_id="agent_id",
            org_id="org_id",
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = await response.parse()
        assert_matches_type(UnitTestDeleteResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.unit_tests.with_streaming_response.delete(
            agent_id="agent_id",
            org_id="org_id",
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = await response.parse()
            assert_matches_type(UnitTestDeleteResponse, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.delete(
                agent_id="agent_id",
                org_id="",
                ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.delete(
                agent_id="",
                org_id="org_id",
                ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate(self, async_client: AsyncCozmoai) -> None:
        unit_test = await async_client.org.agents.unit_tests.generate(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(UnitTestGenerateResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncCozmoai) -> None:
        unit_test = await async_client.org.agents.unit_tests.generate(
            agent_id="agent_id",
            org_id="org_id",
            count=1,
        )
        assert_matches_type(UnitTestGenerateResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.unit_tests.with_raw_response.generate(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        unit_test = await response.parse()
        assert_matches_type(UnitTestGenerateResponse, unit_test, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.unit_tests.with_streaming_response.generate(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            unit_test = await response.parse()
            assert_matches_type(UnitTestGenerateResponse, unit_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.generate(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.unit_tests.with_raw_response.generate(
                agent_id="",
                org_id="org_id",
            )
