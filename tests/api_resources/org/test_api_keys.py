# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    Response,
    APIKeyListAPIKeysResponse,
    APIKeyCreateAPIKeyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_api_key(self, client: Cozmoai) -> None:
        api_key = client.org.api_keys.create_api_key(
            org_id="org_id",
            name="name",
            scopes=["string"],
        )
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_api_key_with_all_params(self, client: Cozmoai) -> None:
        api_key = client.org.api_keys.create_api_key(
            org_id="org_id",
            name="name",
            scopes=["string"],
            expires_at="expires_at",
        )
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_api_key(self, client: Cozmoai) -> None:
        response = client.org.api_keys.with_raw_response.create_api_key(
            org_id="org_id",
            name="name",
            scopes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_api_key(self, client: Cozmoai) -> None:
        with client.org.api_keys.with_streaming_response.create_api_key(
            org_id="org_id",
            name="name",
            scopes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_api_key(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.api_keys.with_raw_response.create_api_key(
                org_id="",
                name="name",
                scopes=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_api_keys(self, client: Cozmoai) -> None:
        api_key = client.org.api_keys.list_api_keys(
            "org_id",
        )
        assert_matches_type(APIKeyListAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_api_keys(self, client: Cozmoai) -> None:
        response = client.org.api_keys.with_raw_response.list_api_keys(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyListAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_api_keys(self, client: Cozmoai) -> None:
        with client.org.api_keys.with_streaming_response.list_api_keys(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyListAPIKeysResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_api_keys(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.api_keys.with_raw_response.list_api_keys(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke_all_api_keys(self, client: Cozmoai) -> None:
        api_key = client.org.api_keys.revoke_all_api_keys(
            "org_id",
        )
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke_all_api_keys(self, client: Cozmoai) -> None:
        response = client.org.api_keys.with_raw_response.revoke_all_api_keys(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke_all_api_keys(self, client: Cozmoai) -> None:
        with client.org.api_keys.with_streaming_response.revoke_all_api_keys(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(Response, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke_all_api_keys(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.api_keys.with_raw_response.revoke_all_api_keys(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke_api_key(self, client: Cozmoai) -> None:
        api_key = client.org.api_keys.revoke_api_key(
            key_id="key_id",
            org_id="org_id",
        )
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke_api_key(self, client: Cozmoai) -> None:
        response = client.org.api_keys.with_raw_response.revoke_api_key(
            key_id="key_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke_api_key(self, client: Cozmoai) -> None:
        with client.org.api_keys.with_streaming_response.revoke_api_key(
            key_id="key_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(Response, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke_api_key(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.api_keys.with_raw_response.revoke_api_key(
                key_id="key_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.org.api_keys.with_raw_response.revoke_api_key(
                key_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_api_key_scopes(self, client: Cozmoai) -> None:
        api_key = client.org.api_keys.update_api_key_scopes(
            key_id="key_id",
            org_id="org_id",
            scopes=["string"],
        )
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_api_key_scopes(self, client: Cozmoai) -> None:
        response = client.org.api_keys.with_raw_response.update_api_key_scopes(
            key_id="key_id",
            org_id="org_id",
            scopes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_api_key_scopes(self, client: Cozmoai) -> None:
        with client.org.api_keys.with_streaming_response.update_api_key_scopes(
            key_id="key_id",
            org_id="org_id",
            scopes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(Response, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_api_key_scopes(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.api_keys.with_raw_response.update_api_key_scopes(
                key_id="key_id",
                org_id="",
                scopes=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.org.api_keys.with_raw_response.update_api_key_scopes(
                key_id="",
                org_id="org_id",
                scopes=["string"],
            )


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_api_key(self, async_client: AsyncCozmoai) -> None:
        api_key = await async_client.org.api_keys.create_api_key(
            org_id="org_id",
            name="name",
            scopes=["string"],
        )
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_api_key_with_all_params(self, async_client: AsyncCozmoai) -> None:
        api_key = await async_client.org.api_keys.create_api_key(
            org_id="org_id",
            name="name",
            scopes=["string"],
            expires_at="expires_at",
        )
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_api_key(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.api_keys.with_raw_response.create_api_key(
            org_id="org_id",
            name="name",
            scopes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_api_key(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.api_keys.with_streaming_response.create_api_key(
            org_id="org_id",
            name="name",
            scopes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyCreateAPIKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_api_key(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.api_keys.with_raw_response.create_api_key(
                org_id="",
                name="name",
                scopes=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_api_keys(self, async_client: AsyncCozmoai) -> None:
        api_key = await async_client.org.api_keys.list_api_keys(
            "org_id",
        )
        assert_matches_type(APIKeyListAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_api_keys(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.api_keys.with_raw_response.list_api_keys(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyListAPIKeysResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_api_keys(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.api_keys.with_streaming_response.list_api_keys(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyListAPIKeysResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_api_keys(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.api_keys.with_raw_response.list_api_keys(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke_all_api_keys(self, async_client: AsyncCozmoai) -> None:
        api_key = await async_client.org.api_keys.revoke_all_api_keys(
            "org_id",
        )
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke_all_api_keys(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.api_keys.with_raw_response.revoke_all_api_keys(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke_all_api_keys(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.api_keys.with_streaming_response.revoke_all_api_keys(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(Response, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke_all_api_keys(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.api_keys.with_raw_response.revoke_all_api_keys(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke_api_key(self, async_client: AsyncCozmoai) -> None:
        api_key = await async_client.org.api_keys.revoke_api_key(
            key_id="key_id",
            org_id="org_id",
        )
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke_api_key(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.api_keys.with_raw_response.revoke_api_key(
            key_id="key_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke_api_key(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.api_keys.with_streaming_response.revoke_api_key(
            key_id="key_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(Response, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke_api_key(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.api_keys.with_raw_response.revoke_api_key(
                key_id="key_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.org.api_keys.with_raw_response.revoke_api_key(
                key_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_api_key_scopes(self, async_client: AsyncCozmoai) -> None:
        api_key = await async_client.org.api_keys.update_api_key_scopes(
            key_id="key_id",
            org_id="org_id",
            scopes=["string"],
        )
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_api_key_scopes(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.api_keys.with_raw_response.update_api_key_scopes(
            key_id="key_id",
            org_id="org_id",
            scopes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(Response, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_api_key_scopes(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.api_keys.with_streaming_response.update_api_key_scopes(
            key_id="key_id",
            org_id="org_id",
            scopes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(Response, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_api_key_scopes(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.api_keys.with_raw_response.update_api_key_scopes(
                key_id="key_id",
                org_id="",
                scopes=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.org.api_keys.with_raw_response.update_api_key_scopes(
                key_id="",
                org_id="org_id",
                scopes=["string"],
            )
