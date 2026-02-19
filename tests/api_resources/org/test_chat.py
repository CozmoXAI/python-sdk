# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import ChatSendMessageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_message(self, client: Cozmoai) -> None:
        chat = client.org.chat.send_message(
            org_id="org_id",
            message="x",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_message_with_all_params(self, client: Cozmoai) -> None:
        chat = client.org.chat.send_message(
            org_id="org_id",
            message="x",
            conversation_id="conversation_id",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_message(self, client: Cozmoai) -> None:
        response = client.org.chat.with_raw_response.send_message(
            org_id="org_id",
            message="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_message(self, client: Cozmoai) -> None:
        with client.org.chat.with_streaming_response.send_message(
            org_id="org_id",
            message="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send_message(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.chat.with_raw_response.send_message(
                org_id="",
                message="x",
            )


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_message(self, async_client: AsyncCozmoai) -> None:
        chat = await async_client.org.chat.send_message(
            org_id="org_id",
            message="x",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_message_with_all_params(self, async_client: AsyncCozmoai) -> None:
        chat = await async_client.org.chat.send_message(
            org_id="org_id",
            message="x",
            conversation_id="conversation_id",
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.chat.with_raw_response.send_message(
            org_id="org_id",
            message="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.chat.with_streaming_response.send_message(
            org_id="org_id",
            message="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send_message(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.chat.with_raw_response.send_message(
                org_id="",
                message="x",
            )
