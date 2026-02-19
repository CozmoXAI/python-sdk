# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .faqs import (
    FaqsResource,
    AsyncFaqsResource,
    FaqsResourceWithRawResponse,
    AsyncFaqsResourceWithRawResponse,
    FaqsResourceWithStreamingResponse,
    AsyncFaqsResourceWithStreamingResponse,
)
from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...types import (
    org_list_voices_params,
    org_list_audit_logs_params,
    org_send_chat_message_params,
    org_create_workflow_run_params,
)
from .batches import (
    BatchesResource,
    AsyncBatchesResource,
    BatchesResourceWithRawResponse,
    AsyncBatchesResourceWithRawResponse,
    BatchesResourceWithStreamingResponse,
    AsyncBatchesResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .chat.chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from .tags.tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .sip_trunks import (
    SipTrunksResource,
    AsyncSipTrunksResource,
    SipTrunksResourceWithRawResponse,
    AsyncSipTrunksResourceWithRawResponse,
    SipTrunksResourceWithStreamingResponse,
    AsyncSipTrunksResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .calls.calls import (
    CallsResource,
    AsyncCallsResource,
    CallsResourceWithRawResponse,
    AsyncCallsResourceWithRawResponse,
    CallsResourceWithStreamingResponse,
    AsyncCallsResourceWithStreamingResponse,
)
from .lists.lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from ..._streaming import Stream, AsyncStream
from .integrations import (
    IntegrationsResource,
    AsyncIntegrationsResource,
    IntegrationsResourceWithRawResponse,
    AsyncIntegrationsResourceWithRawResponse,
    IntegrationsResourceWithStreamingResponse,
    AsyncIntegrationsResourceWithStreamingResponse,
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
from .quality_rules import (
    QualityRulesResource,
    AsyncQualityRulesResource,
    QualityRulesResourceWithRawResponse,
    AsyncQualityRulesResourceWithRawResponse,
    QualityRulesResourceWithStreamingResponse,
    AsyncQualityRulesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .billing.billing import (
    BillingResource,
    AsyncBillingResource,
    BillingResourceWithRawResponse,
    AsyncBillingResourceWithRawResponse,
    BillingResourceWithStreamingResponse,
    AsyncBillingResourceWithStreamingResponse,
)
from .email_templates import (
    EmailTemplatesResource,
    AsyncEmailTemplatesResource,
    EmailTemplatesResourceWithRawResponse,
    AsyncEmailTemplatesResourceWithRawResponse,
    EmailTemplatesResourceWithStreamingResponse,
    AsyncEmailTemplatesResourceWithStreamingResponse,
)
from .analytics.analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)
from .outcome_definitions import (
    OutcomeDefinitionsResource,
    AsyncOutcomeDefinitionsResource,
    OutcomeDefinitionsResourceWithRawResponse,
    AsyncOutcomeDefinitionsResourceWithRawResponse,
    OutcomeDefinitionsResourceWithStreamingResponse,
    AsyncOutcomeDefinitionsResourceWithStreamingResponse,
)
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
from ...types.org_list_audit_logs_response import OrgListAuditLogsResponse
from ...types.org_send_chat_message_response import OrgSendChatMessageResponse
from ...types.org_create_workflow_run_response import OrgCreateWorkflowRunResponse

__all__ = ["OrgResource", "AsyncOrgResource"]


class OrgResource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        return AgentsResource(self._client)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def batches(self) -> BatchesResource:
        return BatchesResource(self._client)

    @cached_property
    def billing(self) -> BillingResource:
        return BillingResource(self._client)

    @cached_property
    def calls(self) -> CallsResource:
        return CallsResource(self._client)

    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def email_templates(self) -> EmailTemplatesResource:
        return EmailTemplatesResource(self._client)

    @cached_property
    def faqs(self) -> FaqsResource:
        return FaqsResource(self._client)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        return IntegrationsResource(self._client)

    @cached_property
    def lists(self) -> ListsResource:
        return ListsResource(self._client)

    @cached_property
    def outcome_definitions(self) -> OutcomeDefinitionsResource:
        return OutcomeDefinitionsResource(self._client)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        return PhoneNumbersResource(self._client)

    @cached_property
    def prospects(self) -> ProspectsResource:
        return ProspectsResource(self._client)

    @cached_property
    def quality_rules(self) -> QualityRulesResource:
        return QualityRulesResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def sip_trunks(self) -> SipTrunksResource:
        return SipTrunksResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        return WorkflowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return OrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
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

    def list_audit_logs(
        self,
        org_id: str,
        *,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgListAuditLogsResponse:
        """
        Returns a paginated list of audit logs for the organization (OWNER and ADMIN
        only)

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/audit-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    org_list_audit_logs_params.OrgListAuditLogsParams,
                ),
            ),
            cast_to=OrgListAuditLogsResponse,
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

    def send_chat_message(
        self,
        org_id: str,
        *,
        message: str,
        conversation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[OrgSendChatMessageResponse]:
        """
        Send a message to the analytics chat assistant and receive a streaming
        AI-generated response via Server-Sent Events

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._post(
            f"/org/{org_id}/chat-stream",
            body=maybe_transform(
                {
                    "message": message,
                    "conversation_id": conversation_id,
                },
                org_send_chat_message_params.OrgSendChatMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSendChatMessageResponse,
            stream=True,
            stream_cls=Stream[OrgSendChatMessageResponse],
        )


class AsyncOrgResource(AsyncAPIResource):
    @cached_property
    def agents(self) -> AsyncAgentsResource:
        return AsyncAgentsResource(self._client)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def batches(self) -> AsyncBatchesResource:
        return AsyncBatchesResource(self._client)

    @cached_property
    def billing(self) -> AsyncBillingResource:
        return AsyncBillingResource(self._client)

    @cached_property
    def calls(self) -> AsyncCallsResource:
        return AsyncCallsResource(self._client)

    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def email_templates(self) -> AsyncEmailTemplatesResource:
        return AsyncEmailTemplatesResource(self._client)

    @cached_property
    def faqs(self) -> AsyncFaqsResource:
        return AsyncFaqsResource(self._client)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        return AsyncIntegrationsResource(self._client)

    @cached_property
    def lists(self) -> AsyncListsResource:
        return AsyncListsResource(self._client)

    @cached_property
    def outcome_definitions(self) -> AsyncOutcomeDefinitionsResource:
        return AsyncOutcomeDefinitionsResource(self._client)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        return AsyncPhoneNumbersResource(self._client)

    @cached_property
    def prospects(self) -> AsyncProspectsResource:
        return AsyncProspectsResource(self._client)

    @cached_property
    def quality_rules(self) -> AsyncQualityRulesResource:
        return AsyncQualityRulesResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def sip_trunks(self) -> AsyncSipTrunksResource:
        return AsyncSipTrunksResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        return AsyncWorkflowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cozmoai-python#with_streaming_response
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

    async def list_audit_logs(
        self,
        org_id: str,
        *,
        page: int | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgListAuditLogsResponse:
        """
        Returns a paginated list of audit logs for the organization (OWNER and ADMIN
        only)

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/audit-logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    org_list_audit_logs_params.OrgListAuditLogsParams,
                ),
            ),
            cast_to=OrgListAuditLogsResponse,
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

    async def send_chat_message(
        self,
        org_id: str,
        *,
        message: str,
        conversation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[OrgSendChatMessageResponse]:
        """
        Send a message to the analytics chat assistant and receive a streaming
        AI-generated response via Server-Sent Events

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._post(
            f"/org/{org_id}/chat-stream",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "conversation_id": conversation_id,
                },
                org_send_chat_message_params.OrgSendChatMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrgSendChatMessageResponse,
            stream=True,
            stream_cls=AsyncStream[OrgSendChatMessageResponse],
        )


class OrgResourceWithRawResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.create_workflow_run = to_raw_response_wrapper(
            org.create_workflow_run,
        )
        self.list_audit_logs = to_raw_response_wrapper(
            org.list_audit_logs,
        )
        self.list_voices = to_raw_response_wrapper(
            org.list_voices,
        )
        self.send_chat_message = to_raw_response_wrapper(
            org.send_chat_message,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self._org.agents)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._org.analytics)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._org.api_keys)

    @cached_property
    def batches(self) -> BatchesResourceWithRawResponse:
        return BatchesResourceWithRawResponse(self._org.batches)

    @cached_property
    def billing(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self._org.billing)

    @cached_property
    def calls(self) -> CallsResourceWithRawResponse:
        return CallsResourceWithRawResponse(self._org.calls)

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._org.chat)

    @cached_property
    def email_templates(self) -> EmailTemplatesResourceWithRawResponse:
        return EmailTemplatesResourceWithRawResponse(self._org.email_templates)

    @cached_property
    def faqs(self) -> FaqsResourceWithRawResponse:
        return FaqsResourceWithRawResponse(self._org.faqs)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self._org.integrations)

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        return ListsResourceWithRawResponse(self._org.lists)

    @cached_property
    def outcome_definitions(self) -> OutcomeDefinitionsResourceWithRawResponse:
        return OutcomeDefinitionsResourceWithRawResponse(self._org.outcome_definitions)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithRawResponse:
        return PhoneNumbersResourceWithRawResponse(self._org.phone_numbers)

    @cached_property
    def prospects(self) -> ProspectsResourceWithRawResponse:
        return ProspectsResourceWithRawResponse(self._org.prospects)

    @cached_property
    def quality_rules(self) -> QualityRulesResourceWithRawResponse:
        return QualityRulesResourceWithRawResponse(self._org.quality_rules)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._org.runs)

    @cached_property
    def sip_trunks(self) -> SipTrunksResourceWithRawResponse:
        return SipTrunksResourceWithRawResponse(self._org.sip_trunks)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._org.tags)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._org.tools)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithRawResponse:
        return WorkflowsResourceWithRawResponse(self._org.workflows)


class AsyncOrgResourceWithRawResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.create_workflow_run = async_to_raw_response_wrapper(
            org.create_workflow_run,
        )
        self.list_audit_logs = async_to_raw_response_wrapper(
            org.list_audit_logs,
        )
        self.list_voices = async_to_raw_response_wrapper(
            org.list_voices,
        )
        self.send_chat_message = async_to_raw_response_wrapper(
            org.send_chat_message,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._org.agents)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._org.analytics)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._org.api_keys)

    @cached_property
    def batches(self) -> AsyncBatchesResourceWithRawResponse:
        return AsyncBatchesResourceWithRawResponse(self._org.batches)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self._org.billing)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithRawResponse:
        return AsyncCallsResourceWithRawResponse(self._org.calls)

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._org.chat)

    @cached_property
    def email_templates(self) -> AsyncEmailTemplatesResourceWithRawResponse:
        return AsyncEmailTemplatesResourceWithRawResponse(self._org.email_templates)

    @cached_property
    def faqs(self) -> AsyncFaqsResourceWithRawResponse:
        return AsyncFaqsResourceWithRawResponse(self._org.faqs)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self._org.integrations)

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        return AsyncListsResourceWithRawResponse(self._org.lists)

    @cached_property
    def outcome_definitions(self) -> AsyncOutcomeDefinitionsResourceWithRawResponse:
        return AsyncOutcomeDefinitionsResourceWithRawResponse(self._org.outcome_definitions)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        return AsyncPhoneNumbersResourceWithRawResponse(self._org.phone_numbers)

    @cached_property
    def prospects(self) -> AsyncProspectsResourceWithRawResponse:
        return AsyncProspectsResourceWithRawResponse(self._org.prospects)

    @cached_property
    def quality_rules(self) -> AsyncQualityRulesResourceWithRawResponse:
        return AsyncQualityRulesResourceWithRawResponse(self._org.quality_rules)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._org.runs)

    @cached_property
    def sip_trunks(self) -> AsyncSipTrunksResourceWithRawResponse:
        return AsyncSipTrunksResourceWithRawResponse(self._org.sip_trunks)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._org.tags)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._org.tools)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithRawResponse:
        return AsyncWorkflowsResourceWithRawResponse(self._org.workflows)


class OrgResourceWithStreamingResponse:
    def __init__(self, org: OrgResource) -> None:
        self._org = org

        self.create_workflow_run = to_streamed_response_wrapper(
            org.create_workflow_run,
        )
        self.list_audit_logs = to_streamed_response_wrapper(
            org.list_audit_logs,
        )
        self.list_voices = to_streamed_response_wrapper(
            org.list_voices,
        )
        self.send_chat_message = to_streamed_response_wrapper(
            org.send_chat_message,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._org.agents)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._org.analytics)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._org.api_keys)

    @cached_property
    def batches(self) -> BatchesResourceWithStreamingResponse:
        return BatchesResourceWithStreamingResponse(self._org.batches)

    @cached_property
    def billing(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self._org.billing)

    @cached_property
    def calls(self) -> CallsResourceWithStreamingResponse:
        return CallsResourceWithStreamingResponse(self._org.calls)

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._org.chat)

    @cached_property
    def email_templates(self) -> EmailTemplatesResourceWithStreamingResponse:
        return EmailTemplatesResourceWithStreamingResponse(self._org.email_templates)

    @cached_property
    def faqs(self) -> FaqsResourceWithStreamingResponse:
        return FaqsResourceWithStreamingResponse(self._org.faqs)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self._org.integrations)

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        return ListsResourceWithStreamingResponse(self._org.lists)

    @cached_property
    def outcome_definitions(self) -> OutcomeDefinitionsResourceWithStreamingResponse:
        return OutcomeDefinitionsResourceWithStreamingResponse(self._org.outcome_definitions)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithStreamingResponse:
        return PhoneNumbersResourceWithStreamingResponse(self._org.phone_numbers)

    @cached_property
    def prospects(self) -> ProspectsResourceWithStreamingResponse:
        return ProspectsResourceWithStreamingResponse(self._org.prospects)

    @cached_property
    def quality_rules(self) -> QualityRulesResourceWithStreamingResponse:
        return QualityRulesResourceWithStreamingResponse(self._org.quality_rules)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._org.runs)

    @cached_property
    def sip_trunks(self) -> SipTrunksResourceWithStreamingResponse:
        return SipTrunksResourceWithStreamingResponse(self._org.sip_trunks)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._org.tags)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._org.tools)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithStreamingResponse:
        return WorkflowsResourceWithStreamingResponse(self._org.workflows)


class AsyncOrgResourceWithStreamingResponse:
    def __init__(self, org: AsyncOrgResource) -> None:
        self._org = org

        self.create_workflow_run = async_to_streamed_response_wrapper(
            org.create_workflow_run,
        )
        self.list_audit_logs = async_to_streamed_response_wrapper(
            org.list_audit_logs,
        )
        self.list_voices = async_to_streamed_response_wrapper(
            org.list_voices,
        )
        self.send_chat_message = async_to_streamed_response_wrapper(
            org.send_chat_message,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._org.agents)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._org.analytics)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._org.api_keys)

    @cached_property
    def batches(self) -> AsyncBatchesResourceWithStreamingResponse:
        return AsyncBatchesResourceWithStreamingResponse(self._org.batches)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self._org.billing)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithStreamingResponse:
        return AsyncCallsResourceWithStreamingResponse(self._org.calls)

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._org.chat)

    @cached_property
    def email_templates(self) -> AsyncEmailTemplatesResourceWithStreamingResponse:
        return AsyncEmailTemplatesResourceWithStreamingResponse(self._org.email_templates)

    @cached_property
    def faqs(self) -> AsyncFaqsResourceWithStreamingResponse:
        return AsyncFaqsResourceWithStreamingResponse(self._org.faqs)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self._org.integrations)

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        return AsyncListsResourceWithStreamingResponse(self._org.lists)

    @cached_property
    def outcome_definitions(self) -> AsyncOutcomeDefinitionsResourceWithStreamingResponse:
        return AsyncOutcomeDefinitionsResourceWithStreamingResponse(self._org.outcome_definitions)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        return AsyncPhoneNumbersResourceWithStreamingResponse(self._org.phone_numbers)

    @cached_property
    def prospects(self) -> AsyncProspectsResourceWithStreamingResponse:
        return AsyncProspectsResourceWithStreamingResponse(self._org.prospects)

    @cached_property
    def quality_rules(self) -> AsyncQualityRulesResourceWithStreamingResponse:
        return AsyncQualityRulesResourceWithStreamingResponse(self._org.quality_rules)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._org.runs)

    @cached_property
    def sip_trunks(self) -> AsyncSipTrunksResourceWithStreamingResponse:
        return AsyncSipTrunksResourceWithStreamingResponse(self._org.sip_trunks)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._org.tags)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._org.tools)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        return AsyncWorkflowsResourceWithStreamingResponse(self._org.workflows)
