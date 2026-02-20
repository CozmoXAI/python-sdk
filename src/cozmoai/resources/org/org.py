# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .calls import (
    CallsResource,
    AsyncCallsResource,
    CallsResourceWithRawResponse,
    AsyncCallsResourceWithRawResponse,
    CallsResourceWithStreamingResponse,
    AsyncCallsResourceWithStreamingResponse,
)
from ...types import org_list_voices_params, org_create_workflow_run_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .tags.tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .lists.lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from .agents.agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)
from .phone_numbers import (
    PhoneNumbersResource,
    AsyncPhoneNumbersResource,
    PhoneNumbersResourceWithRawResponse,
    AsyncPhoneNumbersResourceWithRawResponse,
    PhoneNumbersResourceWithStreamingResponse,
    AsyncPhoneNumbersResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .prospects.prospects import (
    ProspectsResource,
    AsyncProspectsResource,
    ProspectsResourceWithRawResponse,
    AsyncProspectsResourceWithRawResponse,
    ProspectsResourceWithStreamingResponse,
    AsyncProspectsResourceWithStreamingResponse,
)
from .workflows.workflows import (
    WorkflowsResource,
    AsyncWorkflowsResource,
    WorkflowsResourceWithRawResponse,
    AsyncWorkflowsResourceWithRawResponse,
    WorkflowsResourceWithStreamingResponse,
    AsyncWorkflowsResourceWithStreamingResponse,
)
from ...types.org_list_voices_response import OrgListVoicesResponse
from ...types.org_create_workflow_run_response import OrgCreateWorkflowRunResponse

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        return AgentsResource(self._client)

    @cached_property
    def calls(self) -> CallsResource:
        return CallsResource(self._client)

    @cached_property
    def lists(self) -> ListsResource:
        return ListsResource(self._client)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        return PhoneNumbersResource(self._client)

    @cached_property
    def prospects(self) -> ProspectsResource:
        return ProspectsResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        return WorkflowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return OrgResourceWithStreamingResponse(self)

    def create_workflow_run(
        self,
        org_id: str,
        *,
        prospect: org_create_workflow_run_params.Prospect,
        workflow_id: str,
        scheduled_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgCreateWorkflowRunResponse:
        """
        Create a new workflow run with prospect creation in a single operation (API
        endpoint)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            f"/org/{org_id}/workflow-runs",
            body=maybe_transform(
                {
                    "prospect": prospect,
                    "workflow_id": workflow_id,
                    "scheduled_at": scheduled_at,
                },
                org_create_workflow_run_params.OrgCreateWorkflowRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgCreateWorkflowRunResponse,
        )

    def list_voices(
        self,
        org_id: str,
        *,
        provider: Literal["elevenlabs", "cartesia", "openai"],
        next_page: str | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgListVoicesResponse:
        """
        Get a paginated list of available voices from the specified provider

        Args:
          provider: Voice provider

          next_page: Cursor for next page - used for native pagination (cartesia, elevenlabs)

          page: Page number (default: 1) - used for offset pagination

          size: Page size (default: 50, max: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/voices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "provider": provider,
                        "next_page": next_page,
                        "page": page,
                        "size": size,
                    },
                    org_list_voices_params.OrgListVoicesParams,
                ),
            ),
            cast_to=OrgListVoicesResponse,
        )


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def agents(self) -> AsyncAgentsResource:
        return AsyncAgentsResource(self._client)

    @cached_property
    def calls(self) -> AsyncCallsResource:
        return AsyncCallsResource(self._client)

    @cached_property
    def lists(self) -> AsyncListsResource:
        return AsyncListsResource(self._client)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        return AsyncPhoneNumbersResource(self._client)

    @cached_property
    def prospects(self) -> AsyncProspectsResource:
        return AsyncProspectsResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        return AsyncWorkflowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncOrgResourceWithStreamingResponse(self)

    async def create_workflow_run(
        self,
        org_id: str,
        *,
        prospect: org_create_workflow_run_params.Prospect,
        workflow_id: str,
        scheduled_at: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgCreateWorkflowRunResponse:
        """
        Create a new workflow run with prospect creation in a single operation (API
        endpoint)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            f"/org/{org_id}/workflow-runs",
            body=await async_maybe_transform(
                {
                    "prospect": prospect,
                    "workflow_id": workflow_id,
                    "scheduled_at": scheduled_at,
                },
                org_create_workflow_run_params.OrgCreateWorkflowRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgCreateWorkflowRunResponse,
        )

    async def list_voices(
        self,
        org_id: str,
        *,
        provider: Literal["elevenlabs", "cartesia", "openai"],
        next_page: str | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgListVoicesResponse:
        """
        Get a paginated list of available voices from the specified provider

        Args:
          provider: Voice provider

          next_page: Cursor for next page - used for native pagination (cartesia, elevenlabs)

          page: Page number (default: 1) - used for offset pagination

          size: Page size (default: 50, max: 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/voices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "provider": provider,
                        "next_page": next_page,
                        "page": page,
                        "size": size,
                    },
                    org_list_voices_params.OrgListVoicesParams,
                ),
            ),
            cast_to=OrgListVoicesResponse,
        )


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.create_workflow_run = to_raw_response_wrapper(
            org.create_workflow_run,
        )
        self.list_voices = to_raw_response_wrapper(
            org.list_voices,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self._org.agents)

    @cached_property
    def calls(self) -> CallsResourceWithRawResponse:
        return CallsResourceWithRawResponse(self._org.calls)

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        return ListsResourceWithRawResponse(self._org.lists)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithRawResponse:
        return PhoneNumbersResourceWithRawResponse(self._org.phone_numbers)

    @cached_property
    def prospects(self) -> ProspectsResourceWithRawResponse:
        return ProspectsResourceWithRawResponse(self._org.prospects)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._org.tags)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithRawResponse:
        return WorkflowsResourceWithRawResponse(self._org.workflows)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.create_workflow_run = async_to_raw_response_wrapper(
            org.create_workflow_run,
        )
        self.list_voices = async_to_raw_response_wrapper(
            org.list_voices,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._org.agents)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithRawResponse:
        return AsyncCallsResourceWithRawResponse(self._org.calls)

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        return AsyncListsResourceWithRawResponse(self._org.lists)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        return AsyncPhoneNumbersResourceWithRawResponse(self._org.phone_numbers)

    @cached_property
    def prospects(self) -> AsyncProspectsResourceWithRawResponse:
        return AsyncProspectsResourceWithRawResponse(self._org.prospects)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._org.tags)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithRawResponse:
        return AsyncWorkflowsResourceWithRawResponse(self._org.workflows)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.create_workflow_run = to_streamed_response_wrapper(
            org.create_workflow_run,
        )
        self.list_voices = to_streamed_response_wrapper(
            org.list_voices,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._org.agents)

    @cached_property
    def calls(self) -> CallsResourceWithStreamingResponse:
        return CallsResourceWithStreamingResponse(self._org.calls)

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        return ListsResourceWithStreamingResponse(self._org.lists)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithStreamingResponse:
        return PhoneNumbersResourceWithStreamingResponse(self._org.phone_numbers)

    @cached_property
    def prospects(self) -> ProspectsResourceWithStreamingResponse:
        return ProspectsResourceWithStreamingResponse(self._org.prospects)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._org.tags)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithStreamingResponse:
        return WorkflowsResourceWithStreamingResponse(self._org.workflows)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.create_workflow_run = async_to_streamed_response_wrapper(
            org.create_workflow_run,
        )
        self.list_voices = async_to_streamed_response_wrapper(
            org.list_voices,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._org.agents)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithStreamingResponse:
        return AsyncCallsResourceWithStreamingResponse(self._org.calls)

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        return AsyncListsResourceWithStreamingResponse(self._org.lists)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        return AsyncPhoneNumbersResourceWithStreamingResponse(self._org.phone_numbers)

    @cached_property
    def prospects(self) -> AsyncProspectsResourceWithStreamingResponse:
        return AsyncProspectsResourceWithStreamingResponse(self._org.prospects)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._org.tags)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        return AsyncWorkflowsResourceWithStreamingResponse(self._org.workflows)
