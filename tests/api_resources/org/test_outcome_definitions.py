# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    OutcomeDefinition,
    OutcomeDefinitionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutcomeDefinitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        outcome_definition = client.org.outcome_definitions.create(
            org_id="org_id",
            display_name="display_name",
            key="key",
            value_type="BOOLEAN",
        )
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cozmoai) -> None:
        outcome_definition = client.org.outcome_definitions.create(
            org_id="org_id",
            display_name="display_name",
            key="key",
            value_type="BOOLEAN",
            description="description",
            is_unique_per_call=True,
        )
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.org.outcome_definitions.with_raw_response.create(
            org_id="org_id",
            display_name="display_name",
            key="key",
            value_type="BOOLEAN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outcome_definition = response.parse()
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.org.outcome_definitions.with_streaming_response.create(
            org_id="org_id",
            display_name="display_name",
            key="key",
            value_type="BOOLEAN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outcome_definition = response.parse()
            assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.outcome_definitions.with_raw_response.create(
                org_id="",
                display_name="display_name",
                key="key",
                value_type="BOOLEAN",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        outcome_definition = client.org.outcome_definitions.update(
            id="id",
            org_id="org_id",
        )
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        outcome_definition = client.org.outcome_definitions.update(
            id="id",
            org_id="org_id",
            description="description",
            display_name="display_name",
            is_unique_per_call=True,
        )
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.outcome_definitions.with_raw_response.update(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outcome_definition = response.parse()
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.outcome_definitions.with_streaming_response.update(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outcome_definition = response.parse()
            assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.outcome_definitions.with_raw_response.update(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.outcome_definitions.with_raw_response.update(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        outcome_definition = client.org.outcome_definitions.list(
            "org_id",
        )
        assert_matches_type(OutcomeDefinitionListResponse, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.outcome_definitions.with_raw_response.list(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outcome_definition = response.parse()
        assert_matches_type(OutcomeDefinitionListResponse, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.outcome_definitions.with_streaming_response.list(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outcome_definition = response.parse()
            assert_matches_type(OutcomeDefinitionListResponse, outcome_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.outcome_definitions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        outcome_definition = client.org.outcome_definitions.delete(
            id="id",
            org_id="org_id",
        )
        assert outcome_definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.outcome_definitions.with_raw_response.delete(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outcome_definition = response.parse()
        assert outcome_definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.outcome_definitions.with_streaming_response.delete(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outcome_definition = response.parse()
            assert outcome_definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.outcome_definitions.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.outcome_definitions.with_raw_response.delete(
                id="",
                org_id="org_id",
            )


class TestAsyncOutcomeDefinitions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        outcome_definition = await async_client.org.outcome_definitions.create(
            org_id="org_id",
            display_name="display_name",
            key="key",
            value_type="BOOLEAN",
        )
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCozmoai) -> None:
        outcome_definition = await async_client.org.outcome_definitions.create(
            org_id="org_id",
            display_name="display_name",
            key="key",
            value_type="BOOLEAN",
            description="description",
            is_unique_per_call=True,
        )
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.outcome_definitions.with_raw_response.create(
            org_id="org_id",
            display_name="display_name",
            key="key",
            value_type="BOOLEAN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outcome_definition = await response.parse()
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.outcome_definitions.with_streaming_response.create(
            org_id="org_id",
            display_name="display_name",
            key="key",
            value_type="BOOLEAN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outcome_definition = await response.parse()
            assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.outcome_definitions.with_raw_response.create(
                org_id="",
                display_name="display_name",
                key="key",
                value_type="BOOLEAN",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        outcome_definition = await async_client.org.outcome_definitions.update(
            id="id",
            org_id="org_id",
        )
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        outcome_definition = await async_client.org.outcome_definitions.update(
            id="id",
            org_id="org_id",
            description="description",
            display_name="display_name",
            is_unique_per_call=True,
        )
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.outcome_definitions.with_raw_response.update(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outcome_definition = await response.parse()
        assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.outcome_definitions.with_streaming_response.update(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outcome_definition = await response.parse()
            assert_matches_type(OutcomeDefinition, outcome_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.outcome_definitions.with_raw_response.update(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.outcome_definitions.with_raw_response.update(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        outcome_definition = await async_client.org.outcome_definitions.list(
            "org_id",
        )
        assert_matches_type(OutcomeDefinitionListResponse, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.outcome_definitions.with_raw_response.list(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outcome_definition = await response.parse()
        assert_matches_type(OutcomeDefinitionListResponse, outcome_definition, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.outcome_definitions.with_streaming_response.list(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outcome_definition = await response.parse()
            assert_matches_type(OutcomeDefinitionListResponse, outcome_definition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.outcome_definitions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        outcome_definition = await async_client.org.outcome_definitions.delete(
            id="id",
            org_id="org_id",
        )
        assert outcome_definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.outcome_definitions.with_raw_response.delete(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outcome_definition = await response.parse()
        assert outcome_definition is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.outcome_definitions.with_streaming_response.delete(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outcome_definition = await response.parse()
            assert outcome_definition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.outcome_definitions.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.outcome_definitions.with_raw_response.delete(
                id="",
                org_id="org_id",
            )
