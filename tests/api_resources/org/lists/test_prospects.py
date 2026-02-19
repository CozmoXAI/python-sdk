# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.lists import (
    ProspectAddResponse,
    ProspectRemoveResponse,
    ListProspectOperationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProspects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Cozmoai) -> None:
        prospect = client.org.lists.prospects.add(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        )
        assert_matches_type(ProspectAddResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Cozmoai) -> None:
        response = client.org.lists.prospects.with_raw_response.add(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ProspectAddResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Cozmoai) -> None:
        with client.org.lists.prospects.with_streaming_response.add(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ProspectAddResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.prospects.with_raw_response.add(
                prospect_id="prospect_id",
                org_id="",
                list_id="list_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.org.lists.prospects.with_raw_response.add(
                prospect_id="prospect_id",
                org_id="org_id",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            client.org.lists.prospects.with_raw_response.add(
                prospect_id="",
                org_id="org_id",
                list_id="list_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_bulk(self, client: Cozmoai) -> None:
        prospect = client.org.lists.prospects.add_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_bulk(self, client: Cozmoai) -> None:
        response = client.org.lists.prospects.with_raw_response.add_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_bulk(self, client: Cozmoai) -> None:
        with client.org.lists.prospects.with_streaming_response.add_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_bulk(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.prospects.with_raw_response.add_bulk(
                list_id="list_id",
                org_id="",
                prospect_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.org.lists.prospects.with_raw_response.add_bulk(
                list_id="",
                org_id="org_id",
                prospect_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Cozmoai) -> None:
        prospect = client.org.lists.prospects.remove(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        )
        assert_matches_type(ProspectRemoveResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Cozmoai) -> None:
        response = client.org.lists.prospects.with_raw_response.remove(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ProspectRemoveResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Cozmoai) -> None:
        with client.org.lists.prospects.with_streaming_response.remove(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ProspectRemoveResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.prospects.with_raw_response.remove(
                prospect_id="prospect_id",
                org_id="",
                list_id="list_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.org.lists.prospects.with_raw_response.remove(
                prospect_id="prospect_id",
                org_id="org_id",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            client.org.lists.prospects.with_raw_response.remove(
                prospect_id="",
                org_id="org_id",
                list_id="list_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_bulk(self, client: Cozmoai) -> None:
        prospect = client.org.lists.prospects.remove_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_bulk(self, client: Cozmoai) -> None:
        response = client.org.lists.prospects.with_raw_response.remove_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_bulk(self, client: Cozmoai) -> None:
        with client.org.lists.prospects.with_streaming_response.remove_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_bulk(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.lists.prospects.with_raw_response.remove_bulk(
                list_id="list_id",
                org_id="",
                prospect_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.org.lists.prospects.with_raw_response.remove_bulk(
                list_id="",
                org_id="org_id",
                prospect_ids=["string"],
            )


class TestAsyncProspects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.lists.prospects.add(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        )
        assert_matches_type(ProspectAddResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.prospects.with_raw_response.add(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ProspectAddResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.prospects.with_streaming_response.add(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ProspectAddResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.add(
                prospect_id="prospect_id",
                org_id="",
                list_id="list_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.add(
                prospect_id="prospect_id",
                org_id="org_id",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.add(
                prospect_id="",
                org_id="org_id",
                list_id="list_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_bulk(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.lists.prospects.add_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_bulk(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.prospects.with_raw_response.add_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_bulk(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.prospects.with_streaming_response.add_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_bulk(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.add_bulk(
                list_id="list_id",
                org_id="",
                prospect_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.add_bulk(
                list_id="",
                org_id="org_id",
                prospect_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.lists.prospects.remove(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        )
        assert_matches_type(ProspectRemoveResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.prospects.with_raw_response.remove(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ProspectRemoveResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.prospects.with_streaming_response.remove(
            prospect_id="prospect_id",
            org_id="org_id",
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ProspectRemoveResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.remove(
                prospect_id="prospect_id",
                org_id="",
                list_id="list_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.remove(
                prospect_id="prospect_id",
                org_id="org_id",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.remove(
                prospect_id="",
                org_id="org_id",
                list_id="list_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_bulk(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.lists.prospects.remove_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_bulk(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.lists.prospects.with_raw_response.remove_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_bulk(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.lists.prospects.with_streaming_response.remove_bulk(
            list_id="list_id",
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ListProspectOperationResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_bulk(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.remove_bulk(
                list_id="list_id",
                org_id="",
                prospect_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.org.lists.prospects.with_raw_response.remove_bulk(
                list_id="",
                org_id="org_id",
                prospect_ids=["string"],
            )
