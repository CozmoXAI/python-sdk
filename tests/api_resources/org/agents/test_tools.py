# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.agents import (
    ToolAddResponse,
    ToolListResponse,
    ToolRemoveResponse,
    ToolUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        tool = client.org.agents.tools.update(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        tool = client.org.agents.tools.update(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
            config_override={"foo": "bar"},
            is_enabled=True,
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.agents.tools.with_raw_response.update(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.agents.tools.with_streaming_response.update(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolUpdateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.tools.with_raw_response.update(
                tool_id="tool_id",
                org_id="",
                agent_id="agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.tools.with_raw_response.update(
                tool_id="tool_id",
                org_id="org_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.org.agents.tools.with_raw_response.update(
                tool_id="",
                org_id="org_id",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        tool = client.org.agents.tools.list(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.agents.tools.with_raw_response.list(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.agents.tools.with_streaming_response.list(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.tools.with_raw_response.list(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.tools.with_raw_response.list(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Cozmoai) -> None:
        tool = client.org.agents.tools.add(
            agent_id="agent_id",
            org_id="org_id",
            tool_id="tool_id",
        )
        assert_matches_type(ToolAddResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Cozmoai) -> None:
        tool = client.org.agents.tools.add(
            agent_id="agent_id",
            org_id="org_id",
            tool_id="tool_id",
            config_override={"foo": "bar"},
            is_enabled=True,
        )
        assert_matches_type(ToolAddResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Cozmoai) -> None:
        response = client.org.agents.tools.with_raw_response.add(
            agent_id="agent_id",
            org_id="org_id",
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolAddResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Cozmoai) -> None:
        with client.org.agents.tools.with_streaming_response.add(
            agent_id="agent_id",
            org_id="org_id",
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolAddResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.tools.with_raw_response.add(
                agent_id="agent_id",
                org_id="",
                tool_id="tool_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.tools.with_raw_response.add(
                agent_id="",
                org_id="org_id",
                tool_id="tool_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Cozmoai) -> None:
        tool = client.org.agents.tools.remove(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        )
        assert_matches_type(ToolRemoveResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Cozmoai) -> None:
        response = client.org.agents.tools.with_raw_response.remove(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolRemoveResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Cozmoai) -> None:
        with client.org.agents.tools.with_streaming_response.remove(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolRemoveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.tools.with_raw_response.remove(
                tool_id="tool_id",
                org_id="",
                agent_id="agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.tools.with_raw_response.remove(
                tool_id="tool_id",
                org_id="org_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.org.agents.tools.with_raw_response.remove(
                tool_id="",
                org_id="org_id",
                agent_id="agent_id",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.agents.tools.update(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.agents.tools.update(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
            config_override={"foo": "bar"},
            is_enabled=True,
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.tools.with_raw_response.update(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.tools.with_streaming_response.update(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolUpdateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.update(
                tool_id="tool_id",
                org_id="",
                agent_id="agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.update(
                tool_id="tool_id",
                org_id="org_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.update(
                tool_id="",
                org_id="org_id",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.agents.tools.list(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.tools.with_raw_response.list(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.tools.with_streaming_response.list(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.list(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.list(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.agents.tools.add(
            agent_id="agent_id",
            org_id="org_id",
            tool_id="tool_id",
        )
        assert_matches_type(ToolAddResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.agents.tools.add(
            agent_id="agent_id",
            org_id="org_id",
            tool_id="tool_id",
            config_override={"foo": "bar"},
            is_enabled=True,
        )
        assert_matches_type(ToolAddResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.tools.with_raw_response.add(
            agent_id="agent_id",
            org_id="org_id",
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolAddResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.tools.with_streaming_response.add(
            agent_id="agent_id",
            org_id="org_id",
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolAddResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.add(
                agent_id="agent_id",
                org_id="",
                tool_id="tool_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.add(
                agent_id="",
                org_id="org_id",
                tool_id="tool_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.agents.tools.remove(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        )
        assert_matches_type(ToolRemoveResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.tools.with_raw_response.remove(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolRemoveResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.tools.with_streaming_response.remove(
            tool_id="tool_id",
            org_id="org_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolRemoveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.remove(
                tool_id="tool_id",
                org_id="",
                agent_id="agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.remove(
                tool_id="tool_id",
                org_id="org_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.org.agents.tools.with_raw_response.remove(
                tool_id="",
                org_id="org_id",
                agent_id="agent_id",
            )
