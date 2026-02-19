# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    SipTrunkResponse,
    SipTrunkDeleteResponse,
    SipTrunkRetrieveResponse,
    SipTrunkSipTrunksResponse,
    SipTrunkRetrieveSipTrunksResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSipTrunks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        sip_trunk = client.org.sip_trunks.retrieve(
            trunk_id="trunk_id",
            org_id="org_id",
        )
        assert_matches_type(SipTrunkRetrieveResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.org.sip_trunks.with_raw_response.retrieve(
            trunk_id="trunk_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = response.parse()
        assert_matches_type(SipTrunkRetrieveResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.org.sip_trunks.with_streaming_response.retrieve(
            trunk_id="trunk_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = response.parse()
            assert_matches_type(SipTrunkRetrieveResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.sip_trunks.with_raw_response.retrieve(
                trunk_id="trunk_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trunk_id` but received ''"):
            client.org.sip_trunks.with_raw_response.retrieve(
                trunk_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        sip_trunk = client.org.sip_trunks.update(
            trunk_id="trunk_id",
            org_id="org_id",
        )
        assert_matches_type(SipTrunkResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        sip_trunk = client.org.sip_trunks.update(
            trunk_id="trunk_id",
            org_id="org_id",
            is_active=True,
            max_concurrency=0,
            name="name",
        )
        assert_matches_type(SipTrunkResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.sip_trunks.with_raw_response.update(
            trunk_id="trunk_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = response.parse()
        assert_matches_type(SipTrunkResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.sip_trunks.with_streaming_response.update(
            trunk_id="trunk_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = response.parse()
            assert_matches_type(SipTrunkResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.sip_trunks.with_raw_response.update(
                trunk_id="trunk_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trunk_id` but received ''"):
            client.org.sip_trunks.with_raw_response.update(
                trunk_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        sip_trunk = client.org.sip_trunks.delete(
            trunk_id="trunk_id",
            org_id="org_id",
        )
        assert_matches_type(SipTrunkDeleteResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.sip_trunks.with_raw_response.delete(
            trunk_id="trunk_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = response.parse()
        assert_matches_type(SipTrunkDeleteResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.sip_trunks.with_streaming_response.delete(
            trunk_id="trunk_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = response.parse()
            assert_matches_type(SipTrunkDeleteResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.sip_trunks.with_raw_response.delete(
                trunk_id="trunk_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trunk_id` but received ''"):
            client.org.sip_trunks.with_raw_response.delete(
                trunk_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_sip_trunks(self, client: Cozmoai) -> None:
        sip_trunk = client.org.sip_trunks.retrieve_sip_trunks(
            org_id="org_id",
        )
        assert_matches_type(SipTrunkRetrieveSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_sip_trunks_with_all_params(self, client: Cozmoai) -> None:
        sip_trunk = client.org.sip_trunks.retrieve_sip_trunks(
            org_id="org_id",
            is_active=True,
            page=0,
            provider="provider",
            size=100,
        )
        assert_matches_type(SipTrunkRetrieveSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_sip_trunks(self, client: Cozmoai) -> None:
        response = client.org.sip_trunks.with_raw_response.retrieve_sip_trunks(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = response.parse()
        assert_matches_type(SipTrunkRetrieveSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_sip_trunks(self, client: Cozmoai) -> None:
        with client.org.sip_trunks.with_streaming_response.retrieve_sip_trunks(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = response.parse()
            assert_matches_type(SipTrunkRetrieveSipTrunksResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_sip_trunks(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.sip_trunks.with_raw_response.retrieve_sip_trunks(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sip_trunks(self, client: Cozmoai) -> None:
        sip_trunk = client.org.sip_trunks.sip_trunks(
            org_id="org_id",
            address="address",
            name="name",
            phone_numbers=["string"],
            provider="twilio",
        )
        assert_matches_type(SipTrunkSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sip_trunks_with_all_params(self, client: Cozmoai) -> None:
        sip_trunk = client.org.sip_trunks.sip_trunks(
            org_id="org_id",
            address="address",
            name="name",
            phone_numbers=["string"],
            provider="twilio",
            auth_password="auth_password",
            auth_username="auth_username",
            max_concurrency=0,
        )
        assert_matches_type(SipTrunkSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sip_trunks(self, client: Cozmoai) -> None:
        response = client.org.sip_trunks.with_raw_response.sip_trunks(
            org_id="org_id",
            address="address",
            name="name",
            phone_numbers=["string"],
            provider="twilio",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = response.parse()
        assert_matches_type(SipTrunkSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sip_trunks(self, client: Cozmoai) -> None:
        with client.org.sip_trunks.with_streaming_response.sip_trunks(
            org_id="org_id",
            address="address",
            name="name",
            phone_numbers=["string"],
            provider="twilio",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = response.parse()
            assert_matches_type(SipTrunkSipTrunksResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_sip_trunks(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.sip_trunks.with_raw_response.sip_trunks(
                org_id="",
                address="address",
                name="name",
                phone_numbers=["string"],
                provider="twilio",
            )


class TestAsyncSipTrunks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.sip_trunks.retrieve(
            trunk_id="trunk_id",
            org_id="org_id",
        )
        assert_matches_type(SipTrunkRetrieveResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.sip_trunks.with_raw_response.retrieve(
            trunk_id="trunk_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = await response.parse()
        assert_matches_type(SipTrunkRetrieveResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.sip_trunks.with_streaming_response.retrieve(
            trunk_id="trunk_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = await response.parse()
            assert_matches_type(SipTrunkRetrieveResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.sip_trunks.with_raw_response.retrieve(
                trunk_id="trunk_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trunk_id` but received ''"):
            await async_client.org.sip_trunks.with_raw_response.retrieve(
                trunk_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.sip_trunks.update(
            trunk_id="trunk_id",
            org_id="org_id",
        )
        assert_matches_type(SipTrunkResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.sip_trunks.update(
            trunk_id="trunk_id",
            org_id="org_id",
            is_active=True,
            max_concurrency=0,
            name="name",
        )
        assert_matches_type(SipTrunkResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.sip_trunks.with_raw_response.update(
            trunk_id="trunk_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = await response.parse()
        assert_matches_type(SipTrunkResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.sip_trunks.with_streaming_response.update(
            trunk_id="trunk_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = await response.parse()
            assert_matches_type(SipTrunkResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.sip_trunks.with_raw_response.update(
                trunk_id="trunk_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trunk_id` but received ''"):
            await async_client.org.sip_trunks.with_raw_response.update(
                trunk_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.sip_trunks.delete(
            trunk_id="trunk_id",
            org_id="org_id",
        )
        assert_matches_type(SipTrunkDeleteResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.sip_trunks.with_raw_response.delete(
            trunk_id="trunk_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = await response.parse()
        assert_matches_type(SipTrunkDeleteResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.sip_trunks.with_streaming_response.delete(
            trunk_id="trunk_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = await response.parse()
            assert_matches_type(SipTrunkDeleteResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.sip_trunks.with_raw_response.delete(
                trunk_id="trunk_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trunk_id` but received ''"):
            await async_client.org.sip_trunks.with_raw_response.delete(
                trunk_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_sip_trunks(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.sip_trunks.retrieve_sip_trunks(
            org_id="org_id",
        )
        assert_matches_type(SipTrunkRetrieveSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_sip_trunks_with_all_params(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.sip_trunks.retrieve_sip_trunks(
            org_id="org_id",
            is_active=True,
            page=0,
            provider="provider",
            size=100,
        )
        assert_matches_type(SipTrunkRetrieveSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_sip_trunks(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.sip_trunks.with_raw_response.retrieve_sip_trunks(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = await response.parse()
        assert_matches_type(SipTrunkRetrieveSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_sip_trunks(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.sip_trunks.with_streaming_response.retrieve_sip_trunks(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = await response.parse()
            assert_matches_type(SipTrunkRetrieveSipTrunksResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_sip_trunks(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.sip_trunks.with_raw_response.retrieve_sip_trunks(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sip_trunks(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.sip_trunks.sip_trunks(
            org_id="org_id",
            address="address",
            name="name",
            phone_numbers=["string"],
            provider="twilio",
        )
        assert_matches_type(SipTrunkSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sip_trunks_with_all_params(self, async_client: AsyncCozmoai) -> None:
        sip_trunk = await async_client.org.sip_trunks.sip_trunks(
            org_id="org_id",
            address="address",
            name="name",
            phone_numbers=["string"],
            provider="twilio",
            auth_password="auth_password",
            auth_username="auth_username",
            max_concurrency=0,
        )
        assert_matches_type(SipTrunkSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sip_trunks(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.sip_trunks.with_raw_response.sip_trunks(
            org_id="org_id",
            address="address",
            name="name",
            phone_numbers=["string"],
            provider="twilio",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_trunk = await response.parse()
        assert_matches_type(SipTrunkSipTrunksResponse, sip_trunk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sip_trunks(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.sip_trunks.with_streaming_response.sip_trunks(
            org_id="org_id",
            address="address",
            name="name",
            phone_numbers=["string"],
            provider="twilio",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_trunk = await response.parse()
            assert_matches_type(SipTrunkSipTrunksResponse, sip_trunk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_sip_trunks(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.sip_trunks.with_raw_response.sip_trunks(
                org_id="",
                address="address",
                name="name",
                phone_numbers=["string"],
                provider="twilio",
            )
