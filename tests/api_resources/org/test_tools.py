# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    ToolResponse,
    ResponseError,
    ToolListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        tool = client.org.tools.create(
            org_id="org_id",
            description="description",
            method="GET",
            name="x",
            url="url",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cozmoai) -> None:
        tool = client.org.tools.create(
            org_id="org_id",
            description="description",
            method="GET",
            name="x",
            url="url",
            body="body",
            filler_phrases=["string"],
            headers=[0],
            parameters=[
                {
                    "name": "name",
                    "type": "type",
                    "description": "description",
                    "required": True,
                }
            ],
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.org.tools.with_raw_response.create(
            org_id="org_id",
            description="description",
            method="GET",
            name="x",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.org.tools.with_streaming_response.create(
            org_id="org_id",
            description="description",
            method="GET",
            name="x",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.tools.with_raw_response.create(
                org_id="",
                description="description",
                method="GET",
                name="x",
                url="url",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        tool = client.org.tools.retrieve(
            tool_id="tool_id",
            org_id="org_id",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.org.tools.with_raw_response.retrieve(
            tool_id="tool_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.org.tools.with_streaming_response.retrieve(
            tool_id="tool_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.tools.with_raw_response.retrieve(
                tool_id="tool_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.org.tools.with_raw_response.retrieve(
                tool_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        tool = client.org.tools.update(
            tool_id="tool_id",
            org_id="org_id",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        tool = client.org.tools.update(
            tool_id="tool_id",
            org_id="org_id",
            body="body",
            description="description",
            filler_phrases=["string"],
            headers=[0],
            method="GET",
            name="x",
            parameters=[
                {
                    "name": "name",
                    "type": "type",
                    "description": "description",
                    "required": True,
                }
            ],
            url="url",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.tools.with_raw_response.update(
            tool_id="tool_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.tools.with_streaming_response.update(
            tool_id="tool_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.tools.with_raw_response.update(
                tool_id="tool_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.org.tools.with_raw_response.update(
                tool_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        tool = client.org.tools.list(
            org_id="org_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        tool = client.org.tools.list(
            org_id="org_id",
            page=1,
            size=1,
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.tools.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.tools.with_streaming_response.list(
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
            client.org.tools.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        tool = client.org.tools.delete(
            tool_id="tool_id",
            org_id="org_id",
        )
        assert_matches_type(ResponseError, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.tools.with_raw_response.delete(
            tool_id="tool_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ResponseError, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.tools.with_streaming_response.delete(
            tool_id="tool_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ResponseError, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.tools.with_raw_response.delete(
                tool_id="tool_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.org.tools.with_raw_response.delete(
                tool_id="",
                org_id="org_id",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.tools.create(
            org_id="org_id",
            description="description",
            method="GET",
            name="x",
            url="url",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.tools.create(
            org_id="org_id",
            description="description",
            method="GET",
            name="x",
            url="url",
            body="body",
            filler_phrases=["string"],
            headers=[0],
            parameters=[
                {
                    "name": "name",
                    "type": "type",
                    "description": "description",
                    "required": True,
                }
            ],
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.tools.with_raw_response.create(
            org_id="org_id",
            description="description",
            method="GET",
            name="x",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.tools.with_streaming_response.create(
            org_id="org_id",
            description="description",
            method="GET",
            name="x",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.tools.with_raw_response.create(
                org_id="",
                description="description",
                method="GET",
                name="x",
                url="url",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.tools.retrieve(
            tool_id="tool_id",
            org_id="org_id",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.tools.with_raw_response.retrieve(
            tool_id="tool_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.tools.with_streaming_response.retrieve(
            tool_id="tool_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.tools.with_raw_response.retrieve(
                tool_id="tool_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.org.tools.with_raw_response.retrieve(
                tool_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.tools.update(
            tool_id="tool_id",
            org_id="org_id",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.tools.update(
            tool_id="tool_id",
            org_id="org_id",
            body="body",
            description="description",
            filler_phrases=["string"],
            headers=[0],
            method="GET",
            name="x",
            parameters=[
                {
                    "name": "name",
                    "type": "type",
                    "description": "description",
                    "required": True,
                }
            ],
            url="url",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.tools.with_raw_response.update(
            tool_id="tool_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.tools.with_streaming_response.update(
            tool_id="tool_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.tools.with_raw_response.update(
                tool_id="tool_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.org.tools.with_raw_response.update(
                tool_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.tools.list(
            org_id="org_id",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.tools.list(
            org_id="org_id",
            page=1,
            size=1,
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.tools.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.tools.with_streaming_response.list(
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
            await async_client.org.tools.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        tool = await async_client.org.tools.delete(
            tool_id="tool_id",
            org_id="org_id",
        )
        assert_matches_type(ResponseError, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.tools.with_raw_response.delete(
            tool_id="tool_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ResponseError, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.tools.with_streaming_response.delete(
            tool_id="tool_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ResponseError, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.tools.with_raw_response.delete(
                tool_id="tool_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.org.tools.with_raw_response.delete(
                tool_id="",
                org_id="org_id",
            )
