# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.agents import (
    SipTrunkAddResponse,
    SipTrunkListResponse,
    SipTrunkRemoveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSipTrunks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        sip_trunk = client.org.agents.sip_trunks.list(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(SipTrunkListResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.agents.sip_trunks.with_raw_response.list(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = response.parse()
        assert_matches_type(SipTrunkListResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.agents.sip_trunks.with_streaming_response.list(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = response.parse()
            assert_matches_type(SipTrunkListResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.sip_trunks.with_raw_response.list(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.sip_trunks.with_raw_response.list(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Cozmoai) -> None:
        sip_trunk = client.org.agents.sip_trunks.add(
            agent_id="agent_id",
            org_id="org_id",
            sip_trunk_id="sip_trunk_id",
        )
        assert_matches_type(SipTrunkAddResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Cozmoai) -> None:
        response = client.org.agents.sip_trunks.with_raw_response.add(
            agent_id="agent_id",
            org_id="org_id",
            sip_trunk_id="sip_trunk_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = response.parse()
        assert_matches_type(SipTrunkAddResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Cozmoai) -> None:
        with client.org.agents.sip_trunks.with_streaming_response.add(
            agent_id="agent_id",
            org_id="org_id",
            sip_trunk_id="sip_trunk_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = response.parse()
            assert_matches_type(SipTrunkAddResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.sip_trunks.with_raw_response.add(
                agent_id="agent_id",
                org_id="",
                sip_trunk_id="sip_trunk_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.sip_trunks.with_raw_response.add(
                agent_id="",
                org_id="org_id",
                sip_trunk_id="sip_trunk_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Cozmoai) -> None:
        sip_trunk = client.org.agents.sip_trunks.remove(
            trunk_id="trunk_id",
            org_id="org_id",
            agent_id="agent_id",
        )
        assert_matches_type(SipTrunkRemoveResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Cozmoai) -> None:
        response = client.org.agents.sip_trunks.with_raw_response.remove(
            trunk_id="trunk_id",
            org_id="org_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = response.parse()
        assert_matches_type(SipTrunkRemoveResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Cozmoai) -> None:
        with client.org.agents.sip_trunks.with_streaming_response.remove(
            trunk_id="trunk_id",
            org_id="org_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = response.parse()
            assert_matches_type(SipTrunkRemoveResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.agents.sip_trunks.with_raw_response.remove(
                trunk_id="trunk_id",
                org_id="",
                agent_id="agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.org.agents.sip_trunks.with_raw_response.remove(
                trunk_id="trunk_id",
                org_id="org_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trunk_id` but received ''"):
            client.org.agents.sip_trunks.with_raw_response.remove(
                trunk_id="",
                org_id="org_id",
                agent_id="agent_id",
            )


class TestAsyncSipTrunks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.agents.sip_trunks.list(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(SipTrunkListResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.sip_trunks.with_raw_response.list(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = await response.parse()
        assert_matches_type(SipTrunkListResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.sip_trunks.with_streaming_response.list(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = await response.parse()
            assert_matches_type(SipTrunkListResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.sip_trunks.with_raw_response.list(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.sip_trunks.with_raw_response.list(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.agents.sip_trunks.add(
            agent_id="agent_id",
            org_id="org_id",
            sip_trunk_id="sip_trunk_id",
        )
        assert_matches_type(SipTrunkAddResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.sip_trunks.with_raw_response.add(
            agent_id="agent_id",
            org_id="org_id",
            sip_trunk_id="sip_trunk_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = await response.parse()
        assert_matches_type(SipTrunkAddResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.sip_trunks.with_streaming_response.add(
            agent_id="agent_id",
            org_id="org_id",
            sip_trunk_id="sip_trunk_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = await response.parse()
            assert_matches_type(SipTrunkAddResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.sip_trunks.with_raw_response.add(
                agent_id="agent_id",
                org_id="",
                sip_trunk_id="sip_trunk_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.sip_trunks.with_raw_response.add(
                agent_id="",
                org_id="org_id",
                sip_trunk_id="sip_trunk_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.agents.sip_trunks.remove(
            trunk_id="trunk_id",
            org_id="org_id",
            agent_id="agent_id",
        )
        assert_matches_type(SipTrunkRemoveResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.agents.sip_trunks.with_raw_response.remove(
            trunk_id="trunk_id",
            org_id="org_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = await response.parse()
        assert_matches_type(SipTrunkRemoveResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.agents.sip_trunks.with_streaming_response.remove(
            trunk_id="trunk_id",
            org_id="org_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = await response.parse()
            assert_matches_type(SipTrunkRemoveResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.agents.sip_trunks.with_raw_response.remove(
                trunk_id="trunk_id",
                org_id="",
                agent_id="agent_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.org.agents.sip_trunks.with_raw_response.remove(
                trunk_id="trunk_id",
                org_id="org_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trunk_id` but received ''"):
            await async_client.org.agents.sip_trunks.with_raw_response.remove(
                trunk_id="",
                org_id="org_id",
                agent_id="agent_id",
            )
