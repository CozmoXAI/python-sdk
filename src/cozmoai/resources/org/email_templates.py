# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.org import email_template_list_params, email_template_create_params, email_template_update_params
from ..._base_client import make_request_options
from ...types.org.template import Template
from ...types.org.email_template_list_response import EmailTemplateListResponse

__all__ = ["EmailTemplatesResource", "AsyncEmailTemplatesResource"]


class EmailTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return EmailTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return EmailTemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        org_id: str,
        *,
        body_html: str,
        name: str,
        subject: str,
        body_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Template:
        """
        Create a new email template for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/email-templates",
            body=maybe_transform(
                {
                    "body_html": body_html,
                    "name": name,
                    "subject": subject,
                    "body_text": body_text,
                },
                email_template_create_params.EmailTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )

    def retrieve(
        self,
        template_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Template:
        """
        Get a single email template by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._get(
            f"/org/{org_id}/email-templates/{template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )

    def update(
        self,
        template_id: str,
        *,
        org_id: str,
        body_html: str | Omit = omit,
        body_text: str | Omit = omit,
        name: str | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Template:
        """
        Update email template properties (name, subject, body_html, body_text)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._patch(
            f"/org/{org_id}/email-templates/{template_id}",
            body=maybe_transform(
                {
                    "body_html": body_html,
                    "body_text": body_text,
                    "name": name,
                    "subject": subject,
                },
                email_template_update_params.EmailTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )

    def list(
        self,
        org_id: str,
        *,
        page: int | Omit = omit,
        search: str | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateListResponse:
        """
        Get all email templates for the organization with pagination

        Args:
          page: Page number (default: 1)

          search: Search in template name

          size: Page size (default: 20, max: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/email-templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "search": search,
                        "size": size,
                    },
                    email_template_list_params.EmailTemplateListParams,
                ),
            ),
            cast_to=EmailTemplateListResponse,
        )

    def delete(
        self,
        template_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Soft-delete an email template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/org/{org_id}/email-templates/{template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEmailTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
        """
        return AsyncEmailTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        org_id: str,
        *,
        body_html: str,
        name: str,
        subject: str,
        body_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Template:
        """
        Create a new email template for the organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/email-templates",
            body=await async_maybe_transform(
                {
                    "body_html": body_html,
                    "name": name,
                    "subject": subject,
                    "body_text": body_text,
                },
                email_template_create_params.EmailTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )

    async def retrieve(
        self,
        template_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Template:
        """
        Get a single email template by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._get(
            f"/org/{org_id}/email-templates/{template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )

    async def update(
        self,
        template_id: str,
        *,
        org_id: str,
        body_html: str | Omit = omit,
        body_text: str | Omit = omit,
        name: str | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Template:
        """
        Update email template properties (name, subject, body_html, body_text)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._patch(
            f"/org/{org_id}/email-templates/{template_id}",
            body=await async_maybe_transform(
                {
                    "body_html": body_html,
                    "body_text": body_text,
                    "name": name,
                    "subject": subject,
                },
                email_template_update_params.EmailTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Template,
        )

    async def list(
        self,
        org_id: str,
        *,
        page: int | Omit = omit,
        search: str | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateListResponse:
        """
        Get all email templates for the organization with pagination

        Args:
          page: Page number (default: 1)

          search: Search in template name

          size: Page size (default: 20, max: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/email-templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "search": search,
                        "size": size,
                    },
                    email_template_list_params.EmailTemplateListParams,
                ),
            ),
            cast_to=EmailTemplateListResponse,
        )

    async def delete(
        self,
        template_id: str,
        *,
        org_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Soft-delete an email template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/org/{org_id}/email-templates/{template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EmailTemplatesResourceWithRawResponse:
    def __init__(self, email_templates: EmailTemplatesResource) -> None:
        self._email_templates = email_templates

        self.create = to_raw_response_wrapper(
            email_templates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            email_templates.retrieve,
        )
        self.update = to_raw_response_wrapper(
            email_templates.update,
        )
        self.list = to_raw_response_wrapper(
            email_templates.list,
        )
        self.delete = to_raw_response_wrapper(
            email_templates.delete,
        )


class AsyncEmailTemplatesResourceWithRawResponse:
    def __init__(self, email_templates: AsyncEmailTemplatesResource) -> None:
        self._email_templates = email_templates

        self.create = async_to_raw_response_wrapper(
            email_templates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            email_templates.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            email_templates.update,
        )
        self.list = async_to_raw_response_wrapper(
            email_templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            email_templates.delete,
        )


class EmailTemplatesResourceWithStreamingResponse:
    def __init__(self, email_templates: EmailTemplatesResource) -> None:
        self._email_templates = email_templates

        self.create = to_streamed_response_wrapper(
            email_templates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            email_templates.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            email_templates.update,
        )
        self.list = to_streamed_response_wrapper(
            email_templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            email_templates.delete,
        )


class AsyncEmailTemplatesResourceWithStreamingResponse:
    def __init__(self, email_templates: AsyncEmailTemplatesResource) -> None:
        self._email_templates = email_templates

        self.create = async_to_streamed_response_wrapper(
            email_templates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            email_templates.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            email_templates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            email_templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            email_templates.delete,
        )
