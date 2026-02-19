# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.tags import BulkOperationResponseTags

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProspects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        prospect = client.org.tags.prospects.create(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.org.tags.prospects.with_raw_response.create(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.org.tags.prospects.with_streaming_response.create(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.tags.prospects.with_raw_response.create(
                tag_id="tag_id",
                org_id="",
                prospect_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            client.org.tags.prospects.with_raw_response.create(
                tag_id="",
                org_id="org_id",
                prospect_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Cozmoai) -> None:
        prospect = client.org.tags.prospects.delete_all(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Cozmoai) -> None:
        response = client.org.tags.prospects.with_raw_response.delete_all(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Cozmoai) -> None:
        with client.org.tags.prospects.with_streaming_response.delete_all(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_all(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.tags.prospects.with_raw_response.delete_all(
                tag_id="tag_id",
                org_id="",
                prospect_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            client.org.tags.prospects.with_raw_response.delete_all(
                tag_id="",
                org_id="org_id",
                prospect_ids=["string"],
            )


class TestAsyncProspects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.tags.prospects.create(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.tags.prospects.with_raw_response.create(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.tags.prospects.with_streaming_response.create(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.tags.prospects.with_raw_response.create(
                tag_id="tag_id",
                org_id="",
                prospect_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            await async_client.org.tags.prospects.with_raw_response.create(
                tag_id="",
                org_id="org_id",
                prospect_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.tags.prospects.delete_all(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.tags.prospects.with_raw_response.delete_all(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.tags.prospects.with_streaming_response.delete_all(
            tag_id="tag_id",
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(BulkOperationResponseTags, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.tags.prospects.with_raw_response.delete_all(
                tag_id="tag_id",
                org_id="",
                prospect_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            await async_client.org.tags.prospects.with_raw_response.delete_all(
                tag_id="",
                org_id="org_id",
                prospect_ids=["string"],
            )
