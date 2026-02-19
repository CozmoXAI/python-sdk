# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    IntegrationListResponse,
    ConnectedIntegrationResponse,
    IntegrationListConnectedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        integration = client.org.integrations.retrieve(
            id="id",
            org_id="org_id",
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.org.integrations.with_raw_response.retrieve(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.org.integrations.with_streaming_response.retrieve(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.integrations.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.integrations.with_raw_response.retrieve(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        integration = client.org.integrations.list(
            "org_id",
        )
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.integrations.with_raw_response.list(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.integrations.with_streaming_response.list(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationListResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.integrations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect(self, client: Cozmoai) -> None:
        integration = client.org.integrations.connect(
            org_id="org_id",
            slug="slug",
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect_with_all_params(self, client: Cozmoai) -> None:
        integration = client.org.integrations.connect(
            org_id="org_id",
            slug="slug",
            credentials=[0],
            settings=[0],
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: Cozmoai) -> None:
        response = client.org.integrations.with_raw_response.connect(
            org_id="org_id",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: Cozmoai) -> None:
        with client.org.integrations.with_streaming_response.connect(
            org_id="org_id",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_connect(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.integrations.with_raw_response.connect(
                org_id="",
                slug="slug",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disconnect(self, client: Cozmoai) -> None:
        integration = client.org.integrations.disconnect(
            id="id",
            org_id="org_id",
        )
        assert integration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disconnect(self, client: Cozmoai) -> None:
        response = client.org.integrations.with_raw_response.disconnect(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert integration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disconnect(self, client: Cozmoai) -> None:
        with client.org.integrations.with_streaming_response.disconnect(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert integration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disconnect(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.integrations.with_raw_response.disconnect(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.integrations.with_raw_response.disconnect(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_connected(self, client: Cozmoai) -> None:
        integration = client.org.integrations.list_connected(
            "org_id",
        )
        assert_matches_type(IntegrationListConnectedResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_connected(self, client: Cozmoai) -> None:
        response = client.org.integrations.with_raw_response.list_connected(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationListConnectedResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_connected(self, client: Cozmoai) -> None:
        with client.org.integrations.with_streaming_response.list_connected(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationListConnectedResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_connected(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.integrations.with_raw_response.list_connected(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_slug(self, client: Cozmoai) -> None:
        integration = client.org.integrations.retrieve_by_slug(
            slug="slug",
            org_id="org_id",
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_slug(self, client: Cozmoai) -> None:
        response = client.org.integrations.with_raw_response.retrieve_by_slug(
            slug="slug",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_slug(self, client: Cozmoai) -> None:
        with client.org.integrations.with_streaming_response.retrieve_by_slug(
            slug="slug",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_slug(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.integrations.with_raw_response.retrieve_by_slug(
                slug="slug",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.org.integrations.with_raw_response.retrieve_by_slug(
                slug="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle(self, client: Cozmoai) -> None:
        integration = client.org.integrations.toggle(
            id="id",
            org_id="org_id",
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_with_all_params(self, client: Cozmoai) -> None:
        integration = client.org.integrations.toggle(
            id="id",
            org_id="org_id",
            is_active=True,
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_toggle(self, client: Cozmoai) -> None:
        response = client.org.integrations.with_raw_response.toggle(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_toggle(self, client: Cozmoai) -> None:
        with client.org.integrations.with_streaming_response.toggle(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_toggle(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.integrations.with_raw_response.toggle(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.integrations.with_raw_response.toggle(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: Cozmoai) -> None:
        integration = client.org.integrations.update_settings(
            id="id",
            org_id="org_id",
            settings=[0],
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_settings(self, client: Cozmoai) -> None:
        response = client.org.integrations.with_raw_response.update_settings(
            id="id",
            org_id="org_id",
            settings=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_settings(self, client: Cozmoai) -> None:
        with client.org.integrations.with_streaming_response.update_settings(
            id="id",
            org_id="org_id",
            settings=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_settings(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.integrations.with_raw_response.update_settings(
                id="id",
                org_id="",
                settings=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.org.integrations.with_raw_response.update_settings(
                id="",
                org_id="org_id",
                settings=[0],
            )


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.retrieve(
            id="id",
            org_id="org_id",
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.integrations.with_raw_response.retrieve(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.integrations.with_streaming_response.retrieve(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.integrations.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.integrations.with_raw_response.retrieve(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.list(
            "org_id",
        )
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.integrations.with_raw_response.list(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.integrations.with_streaming_response.list(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationListResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.integrations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.connect(
            org_id="org_id",
            slug="slug",
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.connect(
            org_id="org_id",
            slug="slug",
            credentials=[0],
            settings=[0],
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.integrations.with_raw_response.connect(
            org_id="org_id",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.integrations.with_streaming_response.connect(
            org_id="org_id",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_connect(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.integrations.with_raw_response.connect(
                org_id="",
                slug="slug",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disconnect(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.disconnect(
            id="id",
            org_id="org_id",
        )
        assert integration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disconnect(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.integrations.with_raw_response.disconnect(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert integration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disconnect(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.integrations.with_streaming_response.disconnect(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert integration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disconnect(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.integrations.with_raw_response.disconnect(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.integrations.with_raw_response.disconnect(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_connected(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.list_connected(
            "org_id",
        )
        assert_matches_type(IntegrationListConnectedResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_connected(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.integrations.with_raw_response.list_connected(
            "org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationListConnectedResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_connected(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.integrations.with_streaming_response.list_connected(
            "org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationListConnectedResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_connected(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.integrations.with_raw_response.list_connected(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_slug(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.retrieve_by_slug(
            slug="slug",
            org_id="org_id",
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_slug(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.integrations.with_raw_response.retrieve_by_slug(
            slug="slug",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_slug(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.integrations.with_streaming_response.retrieve_by_slug(
            slug="slug",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_slug(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.integrations.with_raw_response.retrieve_by_slug(
                slug="slug",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.org.integrations.with_raw_response.retrieve_by_slug(
                slug="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.toggle(
            id="id",
            org_id="org_id",
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_with_all_params(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.toggle(
            id="id",
            org_id="org_id",
            is_active=True,
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_toggle(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.integrations.with_raw_response.toggle(
            id="id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_toggle(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.integrations.with_streaming_response.toggle(
            id="id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_toggle(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.integrations.with_raw_response.toggle(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.integrations.with_raw_response.toggle(
                id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncCozmoai) -> None:
        integration = await async_client.org.integrations.update_settings(
            id="id",
            org_id="org_id",
            settings=[0],
        )
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.integrations.with_raw_response.update_settings(
            id="id",
            org_id="org_id",
            settings=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.integrations.with_streaming_response.update_settings(
            id="id",
            org_id="org_id",
            settings=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(ConnectedIntegrationResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_settings(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.integrations.with_raw_response.update_settings(
                id="id",
                org_id="",
                settings=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.org.integrations.with_raw_response.update_settings(
                id="",
                org_id="org_id",
                settings=[0],
            )
