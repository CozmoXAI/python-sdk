# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    ListResponse,
    ListListResponse,
    DeleteListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        list_ = client.org.lists.create(
            org_id="org_id",
            name="x",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cozmoai) -> None:
        list_ = client.org.lists.create(
            org_id="org_id",
            name="x",
            source="CSV",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.org.lists.with_raw_response.create(
            org_id="org_id",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.org.lists.with_streaming_response.create(
            org_id="org_id",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.with_raw_response.create(
                org_id="",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        list_ = client.org.lists.retrieve(
            list_id="list_id",
            org_id="org_id",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.org.lists.with_raw_response.retrieve(
            list_id="list_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.org.lists.with_streaming_response.retrieve(
            list_id="list_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.with_raw_response.retrieve(
                list_id="list_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.org.lists.with_raw_response.retrieve(
                list_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        list_ = client.org.lists.update(
            list_id="list_id",
            org_id="org_id",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        list_ = client.org.lists.update(
            list_id="list_id",
            org_id="org_id",
            name="x",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.lists.with_raw_response.update(
            list_id="list_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.lists.with_streaming_response.update(
            list_id="list_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.with_raw_response.update(
                list_id="list_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.org.lists.with_raw_response.update(
                list_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        list_ = client.org.lists.list(
            org_id="org_id",
        )
        assert_matches_type(ListListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        list_ = client.org.lists.list(
            org_id="org_id",
            page=0,
            search="search",
            size=0,
            sort="name_asc",
            source="CSV",
        )
        assert_matches_type(ListListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.lists.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.lists.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        list_ = client.org.lists.delete(
            list_id="list_id",
            org_id="org_id",
        )
        assert_matches_type(DeleteListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.lists.with_raw_response.delete(
            list_id="list_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(DeleteListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.lists.with_streaming_response.delete(
            list_id="list_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(DeleteListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.with_raw_response.delete(
                list_id="list_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.org.lists.with_raw_response.delete(
                list_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_gdpr(self, client: Cozmoai) -> None:
        list_ = client.org.lists.delete_gdpr(
            list_id="list_id",
            org_id="org_id",
        )
        assert_matches_type(DeleteListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_gdpr(self, client: Cozmoai) -> None:
        response = client.org.lists.with_raw_response.delete_gdpr(
            list_id="list_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(DeleteListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_gdpr(self, client: Cozmoai) -> None:
        with client.org.lists.with_streaming_response.delete_gdpr(
            list_id="list_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(DeleteListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_gdpr(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.with_raw_response.delete_gdpr(
                list_id="list_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.org.lists.with_raw_response.delete_gdpr(
                list_id="",
                org_id="org_id",
            )


class TestAsyncLists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        list_ = await async_client.org.lists.create(
            org_id="org_id",
            name="x",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCozmoai) -> None:
        list_ = await async_client.org.lists.create(
            org_id="org_id",
            name="x",
            source="CSV",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.with_raw_response.create(
            org_id="org_id",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.with_streaming_response.create(
            org_id="org_id",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.with_raw_response.create(
                org_id="",
                name="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        list_ = await async_client.org.lists.retrieve(
            list_id="list_id",
            org_id="org_id",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.with_raw_response.retrieve(
            list_id="list_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.with_streaming_response.retrieve(
            list_id="list_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.with_raw_response.retrieve(
                list_id="list_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.org.lists.with_raw_response.retrieve(
                list_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        list_ = await async_client.org.lists.update(
            list_id="list_id",
            org_id="org_id",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        list_ = await async_client.org.lists.update(
            list_id="list_id",
            org_id="org_id",
            name="x",
        )
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.with_raw_response.update(
            list_id="list_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.with_streaming_response.update(
            list_id="list_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.with_raw_response.update(
                list_id="list_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.org.lists.with_raw_response.update(
                list_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        list_ = await async_client.org.lists.list(
            org_id="org_id",
        )
        assert_matches_type(ListListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        list_ = await async_client.org.lists.list(
            org_id="org_id",
            page=0,
            search="search",
            size=0,
            sort="name_asc",
            source="CSV",
        )
        assert_matches_type(ListListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        list_ = await async_client.org.lists.delete(
            list_id="list_id",
            org_id="org_id",
        )
        assert_matches_type(DeleteListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.with_raw_response.delete(
            list_id="list_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(DeleteListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.with_streaming_response.delete(
            list_id="list_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(DeleteListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.with_raw_response.delete(
                list_id="list_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.org.lists.with_raw_response.delete(
                list_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_gdpr(self, async_client: AsyncCozmoai) -> None:
        list_ = await async_client.org.lists.delete_gdpr(
            list_id="list_id",
            org_id="org_id",
        )
        assert_matches_type(DeleteListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_gdpr(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.with_raw_response.delete_gdpr(
            list_id="list_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(DeleteListResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_gdpr(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.with_streaming_response.delete_gdpr(
            list_id="list_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(DeleteListResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_gdpr(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.with_raw_response.delete_gdpr(
                list_id="list_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.org.lists.with_raw_response.delete_gdpr(
                list_id="",
                org_id="org_id",
            )
