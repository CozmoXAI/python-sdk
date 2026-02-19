# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    QualityRuleResponse,
    QualityRuleListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQualityRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        quality_rule = client.org.quality_rules.create(
            org_id="org_id",
            key="x",
            penalty=0,
            prompt="prompt",
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cozmoai) -> None:
        quality_rule = client.org.quality_rules.create(
            org_id="org_id",
            key="x",
            penalty=0,
            prompt="prompt",
            is_active=True,
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.org.quality_rules.with_raw_response.create(
            org_id="org_id",
            key="x",
            penalty=0,
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = response.parse()
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.org.quality_rules.with_streaming_response.create(
            org_id="org_id",
            key="x",
            penalty=0,
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = response.parse()
            assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.quality_rules.with_raw_response.create(
                org_id="",
                key="x",
                penalty=0,
                prompt="prompt",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        quality_rule = client.org.quality_rules.retrieve(
            rule_id="rule_id",
            org_id="org_id",
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.org.quality_rules.with_raw_response.retrieve(
            rule_id="rule_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = response.parse()
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.org.quality_rules.with_streaming_response.retrieve(
            rule_id="rule_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = response.parse()
            assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.quality_rules.with_raw_response.retrieve(
                rule_id="rule_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.org.quality_rules.with_raw_response.retrieve(
                rule_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        quality_rule = client.org.quality_rules.update(
            rule_id="rule_id",
            org_id="org_id",
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        quality_rule = client.org.quality_rules.update(
            rule_id="rule_id",
            org_id="org_id",
            is_active=True,
            key="x",
            penalty=0,
            prompt="prompt",
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.quality_rules.with_raw_response.update(
            rule_id="rule_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = response.parse()
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.quality_rules.with_streaming_response.update(
            rule_id="rule_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = response.parse()
            assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.quality_rules.with_raw_response.update(
                rule_id="rule_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.org.quality_rules.with_raw_response.update(
                rule_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        quality_rule = client.org.quality_rules.list(
            org_id="org_id",
        )
        assert_matches_type(QualityRuleListResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        quality_rule = client.org.quality_rules.list(
            org_id="org_id",
            page=0,
            size=0,
        )
        assert_matches_type(QualityRuleListResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.quality_rules.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = response.parse()
        assert_matches_type(QualityRuleListResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.quality_rules.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = response.parse()
            assert_matches_type(QualityRuleListResponse, quality_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.quality_rules.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        quality_rule = client.org.quality_rules.delete(
            rule_id="rule_id",
            org_id="org_id",
        )
        assert quality_rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.quality_rules.with_raw_response.delete(
            rule_id="rule_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = response.parse()
        assert quality_rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.quality_rules.with_streaming_response.delete(
            rule_id="rule_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = response.parse()
            assert quality_rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.quality_rules.with_raw_response.delete(
                rule_id="rule_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.org.quality_rules.with_raw_response.delete(
                rule_id="",
                org_id="org_id",
            )


class TestAsyncQualityRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        quality_rule = await async_client.org.quality_rules.create(
            org_id="org_id",
            key="x",
            penalty=0,
            prompt="prompt",
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCozmoai) -> None:
        quality_rule = await async_client.org.quality_rules.create(
            org_id="org_id",
            key="x",
            penalty=0,
            prompt="prompt",
            is_active=True,
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.quality_rules.with_raw_response.create(
            org_id="org_id",
            key="x",
            penalty=0,
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = await response.parse()
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.quality_rules.with_streaming_response.create(
            org_id="org_id",
            key="x",
            penalty=0,
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = await response.parse()
            assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.quality_rules.with_raw_response.create(
                org_id="",
                key="x",
                penalty=0,
                prompt="prompt",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        quality_rule = await async_client.org.quality_rules.retrieve(
            rule_id="rule_id",
            org_id="org_id",
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.quality_rules.with_raw_response.retrieve(
            rule_id="rule_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = await response.parse()
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.quality_rules.with_streaming_response.retrieve(
            rule_id="rule_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = await response.parse()
            assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.quality_rules.with_raw_response.retrieve(
                rule_id="rule_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.org.quality_rules.with_raw_response.retrieve(
                rule_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        quality_rule = await async_client.org.quality_rules.update(
            rule_id="rule_id",
            org_id="org_id",
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        quality_rule = await async_client.org.quality_rules.update(
            rule_id="rule_id",
            org_id="org_id",
            is_active=True,
            key="x",
            penalty=0,
            prompt="prompt",
        )
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.quality_rules.with_raw_response.update(
            rule_id="rule_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = await response.parse()
        assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.quality_rules.with_streaming_response.update(
            rule_id="rule_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = await response.parse()
            assert_matches_type(QualityRuleResponse, quality_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.quality_rules.with_raw_response.update(
                rule_id="rule_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.org.quality_rules.with_raw_response.update(
                rule_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        quality_rule = await async_client.org.quality_rules.list(
            org_id="org_id",
        )
        assert_matches_type(QualityRuleListResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        quality_rule = await async_client.org.quality_rules.list(
            org_id="org_id",
            page=0,
            size=0,
        )
        assert_matches_type(QualityRuleListResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.quality_rules.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = await response.parse()
        assert_matches_type(QualityRuleListResponse, quality_rule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.quality_rules.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = await response.parse()
            assert_matches_type(QualityRuleListResponse, quality_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.quality_rules.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        quality_rule = await async_client.org.quality_rules.delete(
            rule_id="rule_id",
            org_id="org_id",
        )
        assert quality_rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.quality_rules.with_raw_response.delete(
            rule_id="rule_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quality_rule = await response.parse()
        assert quality_rule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.quality_rules.with_streaming_response.delete(
            rule_id="rule_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quality_rule = await response.parse()
            assert quality_rule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.quality_rules.with_raw_response.delete(
                rule_id="rule_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.org.quality_rules.with_raw_response.delete(
                rule_id="",
                org_id="org_id",
            )
