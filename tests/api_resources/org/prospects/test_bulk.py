# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org.prospects import (
    BulkImportResponse,
    BulkOperationResponseProspects,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        bulk = client.org.prospects.bulk.update(
            org_id="org_id",
            prospect_ids=["string"],
            updates={},
        )
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        bulk = client.org.prospects.bulk.update(
            org_id="org_id",
            prospect_ids=["string"],
            updates={
                "country": "country",
                "custom_data": {"foo": "bar"},
                "email": "email",
                "external_id": "external_id",
                "first_name": "first_name",
                "last_name": "last_name",
                "list_id": "list_id",
                "remove_from_list": True,
                "status": "status",
                "timezone": "timezone",
            },
        )
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.prospects.bulk.with_raw_response.update(
            org_id="org_id",
            prospect_ids=["string"],
            updates={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.prospects.bulk.with_streaming_response.update(
            org_id="org_id",
            prospect_ids=["string"],
            updates={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.bulk.with_raw_response.update(
                org_id="",
                prospect_ids=["string"],
                updates={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        bulk = client.org.prospects.bulk.delete(
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.prospects.bulk.with_raw_response.delete(
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.prospects.bulk.with_streaming_response.delete(
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.bulk.with_raw_response.delete(
                org_id="",
                prospect_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import(self, client: Cozmoai) -> None:
        bulk = client.org.prospects.bulk.import_(
            org_id="org_id",
            file=b"raw file contents",
            list_name="list_name",
        )
        assert_matches_type(BulkImportResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import(self, client: Cozmoai) -> None:
        response = client.org.prospects.bulk.with_raw_response.import_(
            org_id="org_id",
            file=b"raw file contents",
            list_name="list_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkImportResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import(self, client: Cozmoai) -> None:
        with client.org.prospects.bulk.with_streaming_response.import_(
            org_id="org_id",
            file=b"raw file contents",
            list_name="list_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkImportResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_import(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.bulk.with_raw_response.import_(
                org_id="",
                file=b"raw file contents",
                list_name="list_name",
            )


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        bulk = await async_client.org.prospects.bulk.update(
            org_id="org_id",
            prospect_ids=["string"],
            updates={},
        )
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        bulk = await async_client.org.prospects.bulk.update(
            org_id="org_id",
            prospect_ids=["string"],
            updates={
                "country": "country",
                "custom_data": {"foo": "bar"},
                "email": "email",
                "external_id": "external_id",
                "first_name": "first_name",
                "last_name": "last_name",
                "list_id": "list_id",
                "remove_from_list": True,
                "status": "status",
                "timezone": "timezone",
            },
        )
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.bulk.with_raw_response.update(
            org_id="org_id",
            prospect_ids=["string"],
            updates={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.bulk.with_streaming_response.update(
            org_id="org_id",
            prospect_ids=["string"],
            updates={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.bulk.with_raw_response.update(
                org_id="",
                prospect_ids=["string"],
                updates={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        bulk = await async_client.org.prospects.bulk.delete(
            org_id="org_id",
            prospect_ids=["string"],
        )
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.bulk.with_raw_response.delete(
            org_id="org_id",
            prospect_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.bulk.with_streaming_response.delete(
            org_id="org_id",
            prospect_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkOperationResponseProspects, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.bulk.with_raw_response.delete(
                org_id="",
                prospect_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import(self, async_client: AsyncCozmoai) -> None:
        bulk = await async_client.org.prospects.bulk.import_(
            org_id="org_id",
            file=b"raw file contents",
            list_name="list_name",
        )
        assert_matches_type(BulkImportResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.bulk.with_raw_response.import_(
            org_id="org_id",
            file=b"raw file contents",
            list_name="list_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkImportResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.bulk.with_streaming_response.import_(
            org_id="org_id",
            file=b"raw file contents",
            list_name="list_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkImportResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_import(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.bulk.with_raw_response.import_(
                org_id="",
                file=b"raw file contents",
                list_name="list_name",
            )
