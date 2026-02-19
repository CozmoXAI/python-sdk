# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.org.calls import export_get_csv_params, export_get_count_params
from ....types.org.calls.export_get_count_response import ExportGetCountResponse

__all__ = ["ExportResource", "AsyncExportResource"]


class ExportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return ExportResourceWithStreamingResponse(self)

    def get_count(
        self,
        org_id: str,
        *,
        agent_id: str | Omit = omit,
        direction: str | Omit = omit,
        end_date: str | Omit = omit,
        min_duration: int | Omit = omit,
        phone: str | Omit = omit,
        prospect_external_id: str | Omit = omit,
        prospect_id: str | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportGetCountResponse:
        """
        Returns the total count of calls matching the export filters

        Args:
          agent_id: Filter by agent ID

          direction: Filter by direction

          end_date: Filter by end date (ISO 8601)

          min_duration: Filter by minimum duration in seconds

          phone: Search by phone number

          prospect_external_id: Filter by prospect external ID

          prospect_id: Filter by prospect ID

          start_date: Filter by start date (ISO 8601)

          status: Filter by status

          workflow_id: Filter by workflow ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            f"/org/{org_id}/calls/export/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "direction": direction,
                        "end_date": end_date,
                        "min_duration": min_duration,
                        "phone": phone,
                        "prospect_external_id": prospect_external_id,
                        "prospect_id": prospect_id,
                        "start_date": start_date,
                        "status": status,
                        "workflow_id": workflow_id,
                    },
                    export_get_count_params.ExportGetCountParams,
                ),
            ),
            cast_to=ExportGetCountResponse,
        )

    def get_csv(
        self,
        org_id: str,
        *,
        agent_id: str | Omit = omit,
        direction: str | Omit = omit,
        end_date: str | Omit = omit,
        min_duration: int | Omit = omit,
        phone: str | Omit = omit,
        prospect_external_id: str | Omit = omit,
        prospect_id: str | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Returns a CSV file containing all calls matching the filters (max 10,000)

        Args:
          agent_id: Filter by agent ID

          direction: Filter by direction

          end_date: Filter by end date (ISO 8601)

          min_duration: Filter by minimum duration in seconds

          phone: Search by phone number

          prospect_external_id: Filter by prospect external ID

          prospect_id: Filter by prospect ID

          start_date: Filter by start date (ISO 8601)

          status: Filter by status

          workflow_id: Filter by workflow ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return self._get(
            f"/org/{org_id}/calls/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "direction": direction,
                        "end_date": end_date,
                        "min_duration": min_duration,
                        "phone": phone,
                        "prospect_external_id": prospect_external_id,
                        "prospect_id": prospect_id,
                        "start_date": start_date,
                        "status": status,
                        "workflow_id": workflow_id,
                    },
                    export_get_csv_params.ExportGetCsvParams,
                ),
            ),
            cast_to=str,
        )


class AsyncExportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/CozmoXAI/python-sdk#with_streaming_response
        """
        return AsyncExportResourceWithStreamingResponse(self)

    async def get_count(
        self,
        org_id: str,
        *,
        agent_id: str | Omit = omit,
        direction: str | Omit = omit,
        end_date: str | Omit = omit,
        min_duration: int | Omit = omit,
        phone: str | Omit = omit,
        prospect_external_id: str | Omit = omit,
        prospect_id: str | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportGetCountResponse:
        """
        Returns the total count of calls matching the export filters

        Args:
          agent_id: Filter by agent ID

          direction: Filter by direction

          end_date: Filter by end date (ISO 8601)

          min_duration: Filter by minimum duration in seconds

          phone: Search by phone number

          prospect_external_id: Filter by prospect external ID

          prospect_id: Filter by prospect ID

          start_date: Filter by start date (ISO 8601)

          status: Filter by status

          workflow_id: Filter by workflow ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            f"/org/{org_id}/calls/export/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "direction": direction,
                        "end_date": end_date,
                        "min_duration": min_duration,
                        "phone": phone,
                        "prospect_external_id": prospect_external_id,
                        "prospect_id": prospect_id,
                        "start_date": start_date,
                        "status": status,
                        "workflow_id": workflow_id,
                    },
                    export_get_count_params.ExportGetCountParams,
                ),
            ),
            cast_to=ExportGetCountResponse,
        )

    async def get_csv(
        self,
        org_id: str,
        *,
        agent_id: str | Omit = omit,
        direction: str | Omit = omit,
        end_date: str | Omit = omit,
        min_duration: int | Omit = omit,
        phone: str | Omit = omit,
        prospect_external_id: str | Omit = omit,
        prospect_id: str | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Returns a CSV file containing all calls matching the filters (max 10,000)

        Args:
          agent_id: Filter by agent ID

          direction: Filter by direction

          end_date: Filter by end date (ISO 8601)

          min_duration: Filter by minimum duration in seconds

          phone: Search by phone number

          prospect_external_id: Filter by prospect external ID

          prospect_id: Filter by prospect ID

          start_date: Filter by start date (ISO 8601)

          status: Filter by status

          workflow_id: Filter by workflow ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        extra_headers = {"Accept": "text/csv", **(extra_headers or {})}
        return await self._get(
            f"/org/{org_id}/calls/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "direction": direction,
                        "end_date": end_date,
                        "min_duration": min_duration,
                        "phone": phone,
                        "prospect_external_id": prospect_external_id,
                        "prospect_id": prospect_id,
                        "start_date": start_date,
                        "status": status,
                        "workflow_id": workflow_id,
                    },
                    export_get_csv_params.ExportGetCsvParams,
                ),
            ),
            cast_to=str,
        )


class ExportResourceWithRawResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.get_count = to_raw_response_wrapper(
            export.get_count,
        )
        self.get_csv = to_raw_response_wrapper(
            export.get_csv,
        )


class AsyncExportResourceWithRawResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.get_count = async_to_raw_response_wrapper(
            export.get_count,
        )
        self.get_csv = async_to_raw_response_wrapper(
            export.get_csv,
        )


class ExportResourceWithStreamingResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.get_count = to_streamed_response_wrapper(
            export.get_count,
        )
        self.get_csv = to_streamed_response_wrapper(
            export.get_csv,
        )


class AsyncExportResourceWithStreamingResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.get_count = async_to_streamed_response_wrapper(
            export.get_count,
        )
        self.get_csv = async_to_streamed_response_wrapper(
            export.get_csv,
        )
