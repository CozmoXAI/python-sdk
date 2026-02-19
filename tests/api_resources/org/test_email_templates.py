# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types.org import (
    Template,
    EmailTemplateListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        email_template = client.org.email_templates.create(
            org_id="org_id",
            body_html="body_html",
            name="x",
            subject="x",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cozmoai) -> None:
        email_template = client.org.email_templates.create(
            org_id="org_id",
            body_html="body_html",
            name="x",
            subject="x",
            body_text="body_text",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.org.email_templates.with_raw_response.create(
            org_id="org_id",
            body_html="body_html",
            name="x",
            subject="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = response.parse()
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.org.email_templates.with_streaming_response.create(
            org_id="org_id",
            body_html="body_html",
            name="x",
            subject="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = response.parse()
            assert_matches_type(Template, email_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.email_templates.with_raw_response.create(
                org_id="",
                body_html="body_html",
                name="x",
                subject="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        email_template = client.org.email_templates.retrieve(
            template_id="template_id",
            org_id="org_id",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.org.email_templates.with_raw_response.retrieve(
            template_id="template_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = response.parse()
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.org.email_templates.with_streaming_response.retrieve(
            template_id="template_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = response.parse()
            assert_matches_type(Template, email_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.email_templates.with_raw_response.retrieve(
                template_id="template_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.org.email_templates.with_raw_response.retrieve(
                template_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        email_template = client.org.email_templates.update(
            template_id="template_id",
            org_id="org_id",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        email_template = client.org.email_templates.update(
            template_id="template_id",
            org_id="org_id",
            body_html="body_html",
            body_text="body_text",
            name="x",
            subject="x",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.org.email_templates.with_raw_response.update(
            template_id="template_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = response.parse()
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.org.email_templates.with_streaming_response.update(
            template_id="template_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = response.parse()
            assert_matches_type(Template, email_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.email_templates.with_raw_response.update(
                template_id="template_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.org.email_templates.with_raw_response.update(
                template_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        email_template = client.org.email_templates.list(
            org_id="org_id",
        )
        assert_matches_type(EmailTemplateListResponse, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        email_template = client.org.email_templates.list(
            org_id="org_id",
            page=0,
            search="search",
            size=0,
        )
        assert_matches_type(EmailTemplateListResponse, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.org.email_templates.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = response.parse()
        assert_matches_type(EmailTemplateListResponse, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.org.email_templates.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = response.parse()
            assert_matches_type(EmailTemplateListResponse, email_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.email_templates.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        email_template = client.org.email_templates.delete(
            template_id="template_id",
            org_id="org_id",
        )
        assert email_template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.org.email_templates.with_raw_response.delete(
            template_id="template_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = response.parse()
        assert email_template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.org.email_templates.with_streaming_response.delete(
            template_id="template_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = response.parse()
            assert email_template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.org.email_templates.with_raw_response.delete(
                template_id="template_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.org.email_templates.with_raw_response.delete(
                template_id="",
                org_id="org_id",
            )


class TestAsyncEmailTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        email_template = await async_client.org.email_templates.create(
            org_id="org_id",
            body_html="body_html",
            name="x",
            subject="x",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCozmoai) -> None:
        email_template = await async_client.org.email_templates.create(
            org_id="org_id",
            body_html="body_html",
            name="x",
            subject="x",
            body_text="body_text",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.email_templates.with_raw_response.create(
            org_id="org_id",
            body_html="body_html",
            name="x",
            subject="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = await response.parse()
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.email_templates.with_streaming_response.create(
            org_id="org_id",
            body_html="body_html",
            name="x",
            subject="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = await response.parse()
            assert_matches_type(Template, email_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.email_templates.with_raw_response.create(
                org_id="",
                body_html="body_html",
                name="x",
                subject="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        email_template = await async_client.org.email_templates.retrieve(
            template_id="template_id",
            org_id="org_id",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.email_templates.with_raw_response.retrieve(
            template_id="template_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = await response.parse()
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.email_templates.with_streaming_response.retrieve(
            template_id="template_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = await response.parse()
            assert_matches_type(Template, email_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.email_templates.with_raw_response.retrieve(
                template_id="template_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.org.email_templates.with_raw_response.retrieve(
                template_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        email_template = await async_client.org.email_templates.update(
            template_id="template_id",
            org_id="org_id",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        email_template = await async_client.org.email_templates.update(
            template_id="template_id",
            org_id="org_id",
            body_html="body_html",
            body_text="body_text",
            name="x",
            subject="x",
        )
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.email_templates.with_raw_response.update(
            template_id="template_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = await response.parse()
        assert_matches_type(Template, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.email_templates.with_streaming_response.update(
            template_id="template_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = await response.parse()
            assert_matches_type(Template, email_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.email_templates.with_raw_response.update(
                template_id="template_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.org.email_templates.with_raw_response.update(
                template_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        email_template = await async_client.org.email_templates.list(
            org_id="org_id",
        )
        assert_matches_type(EmailTemplateListResponse, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        email_template = await async_client.org.email_templates.list(
            org_id="org_id",
            page=0,
            search="search",
            size=0,
        )
        assert_matches_type(EmailTemplateListResponse, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.email_templates.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = await response.parse()
        assert_matches_type(EmailTemplateListResponse, email_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.email_templates.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = await response.parse()
            assert_matches_type(EmailTemplateListResponse, email_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.email_templates.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        email_template = await async_client.org.email_templates.delete(
            template_id="template_id",
            org_id="org_id",
        )
        assert email_template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.org.email_templates.with_raw_response.delete(
            template_id="template_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_template = await response.parse()
        assert email_template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.org.email_templates.with_streaming_response.delete(
            template_id="template_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_template = await response.parse()
            assert email_template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.org.email_templates.with_raw_response.delete(
                template_id="template_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.org.email_templates.with_raw_response.delete(
                template_id="",
                org_id="org_id",
            )
