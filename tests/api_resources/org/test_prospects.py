# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    ResponseError,
    ProspectResponse,
    ProspectListResponse,
    ProspectListCallsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProspects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.create(
            org_id="org_id",
            phone="phone",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.create(
            org_id="org_id",
            phone="phone",
            country="country",
            custom_data={"foo": "bar"},
            email="email",
            external_id="external_id",
            first_name="first_name",
            last_name="last_name",
            status="status",
            timezone="timezone",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.org.prospects.with_raw_response.create(
            org_id="org_id",
            phone="phone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.org.prospects.with_streaming_response.create(
            org_id="org_id",
            phone="phone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ProspectResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.with_raw_response.create(
                org_id="",
                phone="phone",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.retrieve(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.org.prospects.with_raw_response.retrieve(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.org.prospects.with_streaming_response.retrieve(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ProspectResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.with_raw_response.retrieve(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            client.org.prospects.with_raw_response.retrieve(
                prospect_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.update(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.update(
            prospect_id="prospect_id",
            org_id="org_id",
            country="country",
            custom_data={"foo": "bar"},
            email="email",
            external_id="external_id",
            first_name="first_name",
            last_name="last_name",
            list_id="list_id",
            phone="phone",
            status="status",
            timezone="timezone",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.prospects.with_raw_response.update(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.prospects.with_streaming_response.update(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ProspectResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.with_raw_response.update(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            client.org.prospects.with_raw_response.update(
                prospect_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.list(
            org_id="org_id",
        )
        assert_matches_type(ProspectListResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.list(
            org_id="org_id",
            country="country",
            list_id="list_id",
            no_list=True,
            page=0,
            search="search",
            size=0,
            status="status",
            tag_id="tag_id",
        )
        assert_matches_type(ProspectListResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.prospects.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ProspectListResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.prospects.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ProspectListResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.delete(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ResponseError, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.prospects.with_raw_response.delete(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ResponseError, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.prospects.with_streaming_response.delete(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ResponseError, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.with_raw_response.delete(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            client.org.prospects.with_raw_response.delete(
                prospect_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_hard_delete(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.hard_delete(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ResponseError, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_hard_delete(self, client: Cozmoai) -> None:
        response = client.org.prospects.with_raw_response.hard_delete(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ResponseError, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_hard_delete(self, client: Cozmoai) -> None:
        with client.org.prospects.with_streaming_response.hard_delete(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ResponseError, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_hard_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.with_raw_response.hard_delete(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            client.org.prospects.with_raw_response.hard_delete(
                prospect_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_calls(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.list_calls(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ProspectListCallsResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_calls_with_all_params(self, client: Cozmoai) -> None:
        prospect = client.org.prospects.list_calls(
            prospect_id="prospect_id",
            org_id="org_id",
            page=0,
            size=100,
        )
        assert_matches_type(ProspectListCallsResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_calls(self, client: Cozmoai) -> None:
        response = client.org.prospects.with_raw_response.list_calls(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = response.parse()
        assert_matches_type(ProspectListCallsResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_calls(self, client: Cozmoai) -> None:
        with client.org.prospects.with_streaming_response.list_calls(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = response.parse()
            assert_matches_type(ProspectListCallsResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_calls(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.prospects.with_raw_response.list_calls(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            client.org.prospects.with_raw_response.list_calls(
                prospect_id="",
                org_id="org_id",
            )


class TestAsyncProspects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.create(
            org_id="org_id",
            phone="phone",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.create(
            org_id="org_id",
            phone="phone",
            country="country",
            custom_data={"foo": "bar"},
            email="email",
            external_id="external_id",
            first_name="first_name",
            last_name="last_name",
            status="status",
            timezone="timezone",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.with_raw_response.create(
            org_id="org_id",
            phone="phone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.with_streaming_response.create(
            org_id="org_id",
            phone="phone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ProspectResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.with_raw_response.create(
                org_id="",
                phone="phone",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.retrieve(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.with_raw_response.retrieve(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.with_streaming_response.retrieve(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ProspectResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.with_raw_response.retrieve(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            await async_client.org.prospects.with_raw_response.retrieve(
                prospect_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.update(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.update(
            prospect_id="prospect_id",
            org_id="org_id",
            country="country",
            custom_data={"foo": "bar"},
            email="email",
            external_id="external_id",
            first_name="first_name",
            last_name="last_name",
            list_id="list_id",
            phone="phone",
            status="status",
            timezone="timezone",
        )
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.with_raw_response.update(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ProspectResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.with_streaming_response.update(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ProspectResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.with_raw_response.update(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            await async_client.org.prospects.with_raw_response.update(
                prospect_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.list(
            org_id="org_id",
        )
        assert_matches_type(ProspectListResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.list(
            org_id="org_id",
            country="country",
            list_id="list_id",
            no_list=True,
            page=0,
            search="search",
            size=0,
            status="status",
            tag_id="tag_id",
        )
        assert_matches_type(ProspectListResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ProspectListResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ProspectListResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.delete(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ResponseError, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.with_raw_response.delete(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ResponseError, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.with_streaming_response.delete(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ResponseError, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.with_raw_response.delete(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            await async_client.org.prospects.with_raw_response.delete(
                prospect_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_hard_delete(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.hard_delete(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ResponseError, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_hard_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.with_raw_response.hard_delete(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ResponseError, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_hard_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.with_streaming_response.hard_delete(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ResponseError, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_hard_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.with_raw_response.hard_delete(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            await async_client.org.prospects.with_raw_response.hard_delete(
                prospect_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_calls(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.list_calls(
            prospect_id="prospect_id",
            org_id="org_id",
        )
        assert_matches_type(ProspectListCallsResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_calls_with_all_params(self, async_client: AsyncCozmoai) -> None:
        prospect = await async_client.org.prospects.list_calls(
            prospect_id="prospect_id",
            org_id="org_id",
            page=0,
            size=100,
        )
        assert_matches_type(ProspectListCallsResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_calls(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.prospects.with_raw_response.list_calls(
            prospect_id="prospect_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prospect = await response.parse()
        assert_matches_type(ProspectListCallsResponse, prospect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_calls(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.prospects.with_streaming_response.list_calls(
            prospect_id="prospect_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prospect = await response.parse()
            assert_matches_type(ProspectListCallsResponse, prospect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_calls(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.prospects.with_raw_response.list_calls(
                prospect_id="prospect_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prospect_id` but received ''"):
            await async_client.org.prospects.with_raw_response.list_calls(
                prospect_id="",
                org_id="org_id",
            )
