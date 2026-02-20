# Me

Types:

```python
from cozmoai.types import MeListOrganizationsResponse
```

Methods:

- <code title="get /me/organizations">client.me.<a href="./src/cozmoai/resources/me.py">list_organizations</a>() -> <a href="./src/cozmoai/types/me_list_organizations_response.py">MeListOrganizationsResponse</a></code>

# Org

Types:

```python
from cozmoai.types import (
    OrgCreateWorkflowRunResponse,
    OrgListAuditLogsResponse,
    OrgListVoicesResponse,
    OrgSendChatMessageResponse,
)
```

Methods:

- <code title="post /org/{org_id}/workflow-runs">client.org.<a href="./src/cozmoai/resources/org/org.py">create_workflow_run</a>(org_id, \*\*<a href="src/cozmoai/types/org_create_workflow_run_params.py">params</a>) -> <a href="./src/cozmoai/types/org_create_workflow_run_response.py">OrgCreateWorkflowRunResponse</a></code>
- <code title="get /org/{org_id}/audit-logs">client.org.<a href="./src/cozmoai/resources/org/org.py">list_audit_logs</a>(org_id, \*\*<a href="src/cozmoai/types/org_list_audit_logs_params.py">params</a>) -> <a href="./src/cozmoai/types/org_list_audit_logs_response.py">OrgListAuditLogsResponse</a></code>
- <code title="get /org/{org_id}/voices">client.org.<a href="./src/cozmoai/resources/org/org.py">list_voices</a>(org_id, \*\*<a href="src/cozmoai/types/org_list_voices_params.py">params</a>) -> <a href="./src/cozmoai/types/org_list_voices_response.py">OrgListVoicesResponse</a></code>
- <code title="post /org/{org_id}/chat-stream">client.org.<a href="./src/cozmoai/resources/org/org.py">send_chat_message</a>(org_id, \*\*<a href="src/cozmoai/types/org_send_chat_message_params.py">params</a>) -> <a href="./src/cozmoai/types/org_send_chat_message_response.py">OrgSendChatMessageResponse</a></code>

## Agents

Types:

```python
from cozmoai.types.org import (
    Agent,
    BackgroundSoundConfig,
    GoodbyeConfig,
    PaginationMetaEvalsPostcall,
    RecallWebhook,
    RunTests,
    AgentListResponse,
    AgentDeleteResponse,
    AgentListEvalRunsResponse,
)
```

Methods:

- <code title="post /org/{org_id}/agents">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/agent_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent.py">Agent</a></code>
- <code title="get /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">retrieve</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agent.py">Agent</a></code>
- <code title="patch /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">update</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agent_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent.py">Agent</a></code>
- <code title="get /org/{org_id}/agents">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/agent_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">delete</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="get /org/{org_id}/agents/eval-runs">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">list_eval_runs</a>(org_id, \*\*<a href="src/cozmoai/types/org/agent_list_eval_runs_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent_list_eval_runs_response.py">AgentListEvalRunsResponse</a></code>
- <code title="post /org/{org_id}/agents/{agent_id}/run-specific-tests">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">run_specific_tests</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agent_run_specific_tests_params.py">params</a>) -> <a href="./src/cozmoai/types/org/run_tests.py">RunTests</a></code>
- <code title="post /org/{org_id}/agents/{agent_id}/run-tests">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">run_tests</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/run_tests.py">RunTests</a></code>

### SipTrunks

Types:

```python
from cozmoai.types.org.agents import (
    SipTrunkListResponse,
    SipTrunkAddResponse,
    SipTrunkRemoveResponse,
)
```

Methods:

- <code title="get /org/{org_id}/agents/{agent_id}/sip-trunks">client.org.agents.sip_trunks.<a href="./src/cozmoai/resources/org/agents/sip_trunks.py">list</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agents/sip_trunk_list_response.py">SipTrunkListResponse</a></code>
- <code title="post /org/{org_id}/agents/{agent_id}/sip-trunks">client.org.agents.sip_trunks.<a href="./src/cozmoai/resources/org/agents/sip_trunks.py">add</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agents/sip_trunk_add_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/sip_trunk_add_response.py">SipTrunkAddResponse</a></code>
- <code title="delete /org/{org_id}/agents/{agent_id}/sip-trunks/{trunk_id}">client.org.agents.sip_trunks.<a href="./src/cozmoai/resources/org/agents/sip_trunks.py">remove</a>(trunk_id, \*, org_id, agent_id) -> <a href="./src/cozmoai/types/org/agents/sip_trunk_remove_response.py">SipTrunkRemoveResponse</a></code>

### Tools

Types:

```python
from cozmoai.types.org.agents import (
    AgentTool,
    ToolUpdateResponse,
    ToolListResponse,
    ToolAddResponse,
    ToolRemoveResponse,
)
```

Methods:

- <code title="patch /org/{org_id}/agents/{agent_id}/tools/{tool_id}">client.org.agents.tools.<a href="./src/cozmoai/resources/org/agents/tools.py">update</a>(tool_id, \*, org_id, agent_id, \*\*<a href="src/cozmoai/types/org/agents/tool_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/tool_update_response.py">ToolUpdateResponse</a></code>
- <code title="get /org/{org_id}/agents/{agent_id}/tools">client.org.agents.tools.<a href="./src/cozmoai/resources/org/agents/tools.py">list</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agents/tool_list_response.py">ToolListResponse</a></code>
- <code title="post /org/{org_id}/agents/{agent_id}/tools">client.org.agents.tools.<a href="./src/cozmoai/resources/org/agents/tools.py">add</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agents/tool_add_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/tool_add_response.py">ToolAddResponse</a></code>
- <code title="delete /org/{org_id}/agents/{agent_id}/tools/{tool_id}">client.org.agents.tools.<a href="./src/cozmoai/resources/org/agents/tools.py">remove</a>(tool_id, \*, org_id, agent_id) -> <a href="./src/cozmoai/types/org/agents/tool_remove_response.py">ToolRemoveResponse</a></code>

### UnitTestRuns

Types:

```python
from cozmoai.types.org.agents import PaginationMetaUnitTests, UnitTestRunLatestResponse
```

Methods:

- <code title="get /org/{org_id}/agents/{agent_id}/unit-test-runs/latest">client.org.agents.unit_test_runs.<a href="./src/cozmoai/resources/org/agents/unit_test_runs.py">latest</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agents/unit_test_run_latest_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/unit_test_run_latest_response.py">UnitTestRunLatestResponse</a></code>

### UnitTests

Types:

```python
from cozmoai.types.org.agents import (
    UnitTest,
    UnitTestListResponse,
    UnitTestDeleteResponse,
    UnitTestGenerateResponse,
)
```

Methods:

- <code title="post /org/{org_id}/agents/{agent_id}/unit-tests">client.org.agents.unit_tests.<a href="./src/cozmoai/resources/org/agents/unit_tests.py">create</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agents/unit_test_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/unit_test.py">UnitTest</a></code>
- <code title="put /org/{org_id}/agents/{agent_id}/unit-tests/{test_id}">client.org.agents.unit_tests.<a href="./src/cozmoai/resources/org/agents/unit_tests.py">update</a>(test_id, \*, org_id, agent_id, \*\*<a href="src/cozmoai/types/org/agents/unit_test_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/unit_test.py">UnitTest</a></code>
- <code title="get /org/{org_id}/agents/{agent_id}/unit-tests">client.org.agents.unit_tests.<a href="./src/cozmoai/resources/org/agents/unit_tests.py">list</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agents/unit_test_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/unit_test_list_response.py">UnitTestListResponse</a></code>
- <code title="post /org/{org_id}/agents/{agent_id}/unit-tests/delete">client.org.agents.unit_tests.<a href="./src/cozmoai/resources/org/agents/unit_tests.py">delete</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agents/unit_test_delete_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/unit_test_delete_response.py">UnitTestDeleteResponse</a></code>
- <code title="post /org/{org_id}/agents/{agent_id}/unit-tests/generate">client.org.agents.unit_tests.<a href="./src/cozmoai/resources/org/agents/unit_tests.py">generate</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agents/unit_test_generate_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/unit_test_generate_response.py">UnitTestGenerateResponse</a></code>

### Evals

Types:

```python
from cozmoai.types.org.agents import Eval, EvalListResponse
```

Methods:

- <code title="post /org/{org_id}/agents/evals">client.org.agents.evals.<a href="./src/cozmoai/resources/org/agents/evals.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/agents/eval_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/eval.py">Eval</a></code>
- <code title="put /org/{org_id}/agents/evals/{evalId}">client.org.agents.evals.<a href="./src/cozmoai/resources/org/agents/evals.py">update</a>(eval_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agents/eval_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/eval.py">Eval</a></code>
- <code title="get /org/{org_id}/agents/evals">client.org.agents.evals.<a href="./src/cozmoai/resources/org/agents/evals.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/agents/eval_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agents/eval_list_response.py">EvalListResponse</a></code>
- <code title="delete /org/{org_id}/agents/evals/{evalId}">client.org.agents.evals.<a href="./src/cozmoai/resources/org/agents/evals.py">delete</a>(eval_id, \*, org_id) -> None</code>

## Analytics

Types:

```python
from cozmoai.types.org import (
    AnalyticsPeriod,
    AnalyticsGetDashboardSummaryResponse,
    AnalyticsGetProspectAnalyticsResponse,
    AnalyticsListAgentsResponse,
    AnalyticsListBatchesResponse,
)
```

Methods:

- <code title="get /org/{org_id}/analytics/dashboard">client.org.analytics.<a href="./src/cozmoai/resources/org/analytics/analytics.py">get_dashboard_summary</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics_get_dashboard_summary_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics_get_dashboard_summary_response.py">AnalyticsGetDashboardSummaryResponse</a></code>
- <code title="get /org/{org_id}/analytics/prospects">client.org.analytics.<a href="./src/cozmoai/resources/org/analytics/analytics.py">get_prospect_analytics</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics_get_prospect_analytics_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics_get_prospect_analytics_response.py">AnalyticsGetProspectAnalyticsResponse</a></code>
- <code title="get /org/{org_id}/analytics/agents">client.org.analytics.<a href="./src/cozmoai/resources/org/analytics/analytics.py">list_agents</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics_list_agents_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics_list_agents_response.py">AnalyticsListAgentsResponse</a></code>
- <code title="get /org/{org_id}/analytics/batches">client.org.analytics.<a href="./src/cozmoai/resources/org/analytics/analytics.py">list_batches</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics_list_batches_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics_list_batches_response.py">AnalyticsListBatchesResponse</a></code>

### Calls

Types:

```python
from cozmoai.types.org.analytics import (
    CallGetCallCostsResponse,
    CallListCallsResponse,
    CallListCallsByHourResponse,
)
```

Methods:

- <code title="get /org/{org_id}/analytics/calls/costs">client.org.analytics.calls.<a href="./src/cozmoai/resources/org/analytics/calls.py">get_call_costs</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics/call_get_call_costs_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics/call_get_call_costs_response.py">CallGetCallCostsResponse</a></code>
- <code title="get /org/{org_id}/analytics/calls">client.org.analytics.calls.<a href="./src/cozmoai/resources/org/analytics/calls.py">list_calls</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics/call_list_calls_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics/call_list_calls_response.py">CallListCallsResponse</a></code>
- <code title="get /org/{org_id}/analytics/calls/by-hour">client.org.analytics.calls.<a href="./src/cozmoai/resources/org/analytics/calls.py">list_calls_by_hour</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics/call_list_calls_by_hour_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics/call_list_calls_by_hour_response.py">CallListCallsByHourResponse</a></code>

### Insights

Types:

```python
from cozmoai.types.org.analytics import InsightGenerateInsightsResponse, InsightListInsightsResponse
```

Methods:

- <code title="post /org/{org_id}/analytics/insights">client.org.analytics.insights.<a href="./src/cozmoai/resources/org/analytics/insights.py">generate_insights</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics/insight_generate_insights_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics/insight_generate_insights_response.py">InsightGenerateInsightsResponse</a></code>
- <code title="get /org/{org_id}/analytics/insights">client.org.analytics.insights.<a href="./src/cozmoai/resources/org/analytics/insights.py">list_insights</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics/insight_list_insights_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics/insight_list_insights_response.py">InsightListInsightsResponse</a></code>

### Workflows

Types:

```python
from cozmoai.types.org.analytics import (
    WorkflowGetWorkflowAnalyticsResponse,
    WorkflowListWorkflowsResponse,
)
```

Methods:

- <code title="get /org/{org_id}/analytics/workflows/{id}">client.org.analytics.workflows.<a href="./src/cozmoai/resources/org/analytics/workflows.py">get_workflow_analytics</a>(id, \*, org_id, \*\*<a href="src/cozmoai/types/org/analytics/workflow_get_workflow_analytics_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics/workflow_get_workflow_analytics_response.py">WorkflowGetWorkflowAnalyticsResponse</a></code>
- <code title="get /org/{org_id}/analytics/workflows">client.org.analytics.workflows.<a href="./src/cozmoai/resources/org/analytics/workflows.py">list_workflows</a>(org_id, \*\*<a href="src/cozmoai/types/org/analytics/workflow_list_workflows_params.py">params</a>) -> <a href="./src/cozmoai/types/org/analytics/workflow_list_workflows_response.py">WorkflowListWorkflowsResponse</a></code>

## APIKeys

Types:

```python
from cozmoai.types.org import Response, APIKeyCreateAPIKeyResponse, APIKeyListAPIKeysResponse
```

Methods:

- <code title="post /org/{org_id}/api-keys">client.org.api_keys.<a href="./src/cozmoai/resources/org/api_keys.py">create_api_key</a>(org_id, \*\*<a href="src/cozmoai/types/org/api_key_create_api_key_params.py">params</a>) -> <a href="./src/cozmoai/types/org/api_key_create_api_key_response.py">APIKeyCreateAPIKeyResponse</a></code>
- <code title="get /org/{org_id}/api-keys">client.org.api_keys.<a href="./src/cozmoai/resources/org/api_keys.py">list_api_keys</a>(org_id) -> <a href="./src/cozmoai/types/org/api_key_list_api_keys_response.py">APIKeyListAPIKeysResponse</a></code>
- <code title="delete /org/{org_id}/api-keys">client.org.api_keys.<a href="./src/cozmoai/resources/org/api_keys.py">revoke_all_api_keys</a>(org_id) -> <a href="./src/cozmoai/types/org/response.py">Response</a></code>
- <code title="delete /org/{org_id}/api-keys/{key_id}">client.org.api_keys.<a href="./src/cozmoai/resources/org/api_keys.py">revoke_api_key</a>(key_id, \*, org_id) -> <a href="./src/cozmoai/types/org/response.py">Response</a></code>
- <code title="patch /org/{org_id}/api-keys/{key_id}/scopes">client.org.api_keys.<a href="./src/cozmoai/resources/org/api_keys.py">update_api_key_scopes</a>(key_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/api_key_update_api_key_scopes_params.py">params</a>) -> <a href="./src/cozmoai/types/org/response.py">Response</a></code>

## Batches

Types:

```python
from cozmoai.types.org import (
    BatchResponse,
    PaginationMetaWorkflowBatches,
    BatchListWorkflowRunsResponse,
)
```

Methods:

- <code title="get /org/{org_id}/batches/{batch_id}">client.org.batches.<a href="./src/cozmoai/resources/org/batches.py">get_workflow_batch</a>(batch_id, \*, org_id) -> <a href="./src/cozmoai/types/org/batch_response.py">BatchResponse</a></code>
- <code title="get /org/{org_id}/batches/{batch_id}/runs">client.org.batches.<a href="./src/cozmoai/resources/org/batches.py">list_workflow_runs</a>(batch_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/batch_list_workflow_runs_params.py">params</a>) -> <a href="./src/cozmoai/types/org/batch_list_workflow_runs_response.py">BatchListWorkflowRunsResponse</a></code>
- <code title="patch /org/{org_id}/batches/{batch_id}">client.org.batches.<a href="./src/cozmoai/resources/org/batches.py">update_batch_status</a>(batch_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/batch_update_batch_status_params.py">params</a>) -> <a href="./src/cozmoai/types/org/batch_response.py">BatchResponse</a></code>

## Billing

Types:

```python
from cozmoai.types.org import (
    Numeric,
    BillingGetBalanceResponse,
    BillingGetSummaryResponse,
    BillingGetUsageSummaryResponse,
    BillingInitiateTopupResponse,
)
```

Methods:

- <code title="get /org/{org_id}/billing/balance">client.org.billing.<a href="./src/cozmoai/resources/org/billing/billing.py">get_balance</a>(org_id) -> <a href="./src/cozmoai/types/org/billing_get_balance_response.py">BillingGetBalanceResponse</a></code>
- <code title="get /org/{org_id}/billing/summary">client.org.billing.<a href="./src/cozmoai/resources/org/billing/billing.py">get_summary</a>(org_id) -> <a href="./src/cozmoai/types/org/billing_get_summary_response.py">BillingGetSummaryResponse</a></code>
- <code title="get /org/{org_id}/billing/usage">client.org.billing.<a href="./src/cozmoai/resources/org/billing/billing.py">get_usage_summary</a>(org_id, \*\*<a href="src/cozmoai/types/org/billing_get_usage_summary_params.py">params</a>) -> <a href="./src/cozmoai/types/org/billing_get_usage_summary_response.py">BillingGetUsageSummaryResponse</a></code>
- <code title="post /org/{org_id}/billing/topup">client.org.billing.<a href="./src/cozmoai/resources/org/billing/billing.py">initiate_topup</a>(org_id, \*\*<a href="src/cozmoai/types/org/billing_initiate_topup_params.py">params</a>) -> <a href="./src/cozmoai/types/org/billing_initiate_topup_response.py">BillingInitiateTopupResponse</a></code>

### Invoices

Types:

```python
from cozmoai.types.org.billing import (
    PaginationMetaBilling,
    InvoiceListResponse,
    InvoiceGetPdfURLResponse,
)
```

Methods:

- <code title="get /org/{org_id}/billing/invoices">client.org.billing.invoices.<a href="./src/cozmoai/resources/org/billing/invoices.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/billing/invoice_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/billing/invoice_list_response.py">InvoiceListResponse</a></code>
- <code title="get /org/{org_id}/billing/invoices/pdf">client.org.billing.invoices.<a href="./src/cozmoai/resources/org/billing/invoices.py">get_pdf_url</a>(org_id, \*\*<a href="src/cozmoai/types/org/billing/invoice_get_pdf_url_params.py">params</a>) -> <a href="./src/cozmoai/types/org/billing/invoice_get_pdf_url_response.py">InvoiceGetPdfURLResponse</a></code>

### Ledger

Types:

```python
from cozmoai.types.org.billing import LedgerListResponse, LedgerGetEntryResponse
```

Methods:

- <code title="get /org/{org_id}/billing/ledger">client.org.billing.ledger.<a href="./src/cozmoai/resources/org/billing/ledger.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/billing/ledger_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/billing/ledger_list_response.py">LedgerListResponse</a></code>
- <code title="get /org/{org_id}/billing/ledger/{entry_id}">client.org.billing.ledger.<a href="./src/cozmoai/resources/org/billing/ledger.py">get_entry</a>(entry_id, \*, org_id) -> <a href="./src/cozmoai/types/org/billing/ledger_get_entry_response.py">LedgerGetEntryResponse</a></code>

## Calls

Types:

```python
from cozmoai.types.org import (
    CallEvaluation,
    CallToolLog,
    PaginationMetaCalls,
    CallListResponse,
    CallCreateDashboardCallResponse,
    CallGetDetailsResponse,
    CallGetEvaluationsResponse,
    CallGetRecordingResponse,
    CallGetToolLogsResponse,
    CallGetTranscriptResponse,
)
```

Methods:

- <code title="get /org/{org_id}/calls">client.org.calls.<a href="./src/cozmoai/resources/org/calls/calls.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/call_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/call_list_response.py">CallListResponse</a></code>
- <code title="post /org/{org_id}/calls">client.org.calls.<a href="./src/cozmoai/resources/org/calls/calls.py">create_dashboard_call</a>(org_id, \*\*<a href="src/cozmoai/types/org/call_create_dashboard_call_params.py">params</a>) -> <a href="./src/cozmoai/types/org/call_create_dashboard_call_response.py">CallCreateDashboardCallResponse</a></code>
- <code title="get /org/{org_id}/calls/{call_id}">client.org.calls.<a href="./src/cozmoai/resources/org/calls/calls.py">get_details</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_get_details_response.py">CallGetDetailsResponse</a></code>
- <code title="get /org/{org_id}/calls/{call_id}/evaluations">client.org.calls.<a href="./src/cozmoai/resources/org/calls/calls.py">get_evaluations</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_get_evaluations_response.py">CallGetEvaluationsResponse</a></code>
- <code title="get /org/{org_id}/calls/{call_id}/recording">client.org.calls.<a href="./src/cozmoai/resources/org/calls/calls.py">get_recording</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_get_recording_response.py">CallGetRecordingResponse</a></code>
- <code title="get /org/{org_id}/calls/{call_id}/tool-logs">client.org.calls.<a href="./src/cozmoai/resources/org/calls/calls.py">get_tool_logs</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_get_tool_logs_response.py">CallGetToolLogsResponse</a></code>
- <code title="get /org/{org_id}/calls/{call_id}/transcript">client.org.calls.<a href="./src/cozmoai/resources/org/calls/calls.py">get_transcript</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_get_transcript_response.py">CallGetTranscriptResponse</a></code>

### Export

Types:

```python
from cozmoai.types.org.calls import ExportGetCountResponse, ExportGetCsvResponse
```

Methods:

- <code title="get /org/{org_id}/calls/export/count">client.org.calls.export.<a href="./src/cozmoai/resources/org/calls/export.py">get_count</a>(org_id, \*\*<a href="src/cozmoai/types/org/calls/export_get_count_params.py">params</a>) -> <a href="./src/cozmoai/types/org/calls/export_get_count_response.py">ExportGetCountResponse</a></code>
- <code title="get /org/{org_id}/calls/export">client.org.calls.export.<a href="./src/cozmoai/resources/org/calls/export.py">get_csv</a>(org_id, \*\*<a href="src/cozmoai/types/org/calls/export_get_csv_params.py">params</a>) -> str</code>

## Chat

Types:

```python
from cozmoai.types.org import ChatSendMessageResponse
```

Methods:

- <code title="post /org/{org_id}/chat">client.org.chat.<a href="./src/cozmoai/resources/org/chat/chat.py">send_message</a>(org_id, \*\*<a href="src/cozmoai/types/org/chat_send_message_params.py">params</a>) -> <a href="./src/cozmoai/types/org/chat_send_message_response.py">ChatSendMessageResponse</a></code>

### Conversations

Types:

```python
from cozmoai.types.org.chat import (
    ConversationListResponse,
    ConversationDeleteResponse,
    ConversationGetResponse,
)
```

Methods:

- <code title="get /org/{org_id}/chat/conversations">client.org.chat.conversations.<a href="./src/cozmoai/resources/org/chat/conversations.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/chat/conversation_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/chat/conversation_list_response.py">ConversationListResponse</a></code>
- <code title="delete /org/{org_id}/chat/conversations/{conversation_id}">client.org.chat.conversations.<a href="./src/cozmoai/resources/org/chat/conversations.py">delete</a>(conversation_id, \*, org_id) -> <a href="./src/cozmoai/types/org/chat/conversation_delete_response.py">ConversationDeleteResponse</a></code>
- <code title="get /org/{org_id}/chat/conversations/{conversation_id}">client.org.chat.conversations.<a href="./src/cozmoai/resources/org/chat/conversations.py">get</a>(conversation_id, \*, org_id) -> <a href="./src/cozmoai/types/org/chat/conversation_get_response.py">ConversationGetResponse</a></code>

## EmailTemplates

Types:

```python
from cozmoai.types.org import Template, EmailTemplateListResponse
```

Methods:

- <code title="post /org/{org_id}/email-templates">client.org.email_templates.<a href="./src/cozmoai/resources/org/email_templates.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/email_template_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/template.py">Template</a></code>
- <code title="get /org/{org_id}/email-templates/{template_id}">client.org.email_templates.<a href="./src/cozmoai/resources/org/email_templates.py">retrieve</a>(template_id, \*, org_id) -> <a href="./src/cozmoai/types/org/template.py">Template</a></code>
- <code title="patch /org/{org_id}/email-templates/{template_id}">client.org.email_templates.<a href="./src/cozmoai/resources/org/email_templates.py">update</a>(template_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/email_template_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/template.py">Template</a></code>
- <code title="get /org/{org_id}/email-templates">client.org.email_templates.<a href="./src/cozmoai/resources/org/email_templates.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/email_template_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/email_template_list_response.py">EmailTemplateListResponse</a></code>
- <code title="delete /org/{org_id}/email-templates/{template_id}">client.org.email_templates.<a href="./src/cozmoai/resources/org/email_templates.py">delete</a>(template_id, \*, org_id) -> None</code>

## Faqs

Types:

```python
from cozmoai.types.org import Faq, FaqListResponse
```

Methods:

- <code title="post /org/{org_id}/faqs">client.org.faqs.<a href="./src/cozmoai/resources/org/faqs.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/faq_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/faq.py">Faq</a></code>
- <code title="get /org/{org_id}/faqs/{faq_id}">client.org.faqs.<a href="./src/cozmoai/resources/org/faqs.py">retrieve</a>(faq_id, \*, org_id) -> <a href="./src/cozmoai/types/org/faq.py">Faq</a></code>
- <code title="patch /org/{org_id}/faqs/{faq_id}">client.org.faqs.<a href="./src/cozmoai/resources/org/faqs.py">update</a>(faq_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/faq_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/faq.py">Faq</a></code>
- <code title="get /org/{org_id}/faqs">client.org.faqs.<a href="./src/cozmoai/resources/org/faqs.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/faq_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/faq_list_response.py">FaqListResponse</a></code>
- <code title="delete /org/{org_id}/faqs/{faq_id}">client.org.faqs.<a href="./src/cozmoai/resources/org/faqs.py">delete</a>(faq_id, \*, org_id) -> None</code>

## Integrations

Types:

```python
from cozmoai.types.org import (
    ConnectedIntegrationResponse,
    IntegrationListResponse,
    IntegrationListConnectedResponse,
)
```

Methods:

- <code title="get /org/{org_id}/integrations/{id}">client.org.integrations.<a href="./src/cozmoai/resources/org/integrations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/cozmoai/types/org/connected_integration_response.py">ConnectedIntegrationResponse</a></code>
- <code title="get /org/{org_id}/integrations">client.org.integrations.<a href="./src/cozmoai/resources/org/integrations.py">list</a>(org_id) -> <a href="./src/cozmoai/types/org/integration_list_response.py">IntegrationListResponse</a></code>
- <code title="post /org/{org_id}/integrations">client.org.integrations.<a href="./src/cozmoai/resources/org/integrations.py">connect</a>(org_id, \*\*<a href="src/cozmoai/types/org/integration_connect_params.py">params</a>) -> <a href="./src/cozmoai/types/org/connected_integration_response.py">ConnectedIntegrationResponse</a></code>
- <code title="delete /org/{org_id}/integrations/{id}">client.org.integrations.<a href="./src/cozmoai/resources/org/integrations.py">disconnect</a>(id, \*, org_id) -> None</code>
- <code title="get /org/{org_id}/integrations/connected">client.org.integrations.<a href="./src/cozmoai/resources/org/integrations.py">list_connected</a>(org_id) -> <a href="./src/cozmoai/types/org/integration_list_connected_response.py">IntegrationListConnectedResponse</a></code>
- <code title="get /org/{org_id}/integrations/slug/{slug}">client.org.integrations.<a href="./src/cozmoai/resources/org/integrations.py">retrieve_by_slug</a>(slug, \*, org_id) -> <a href="./src/cozmoai/types/org/connected_integration_response.py">ConnectedIntegrationResponse</a></code>
- <code title="patch /org/{org_id}/integrations/{id}/toggle">client.org.integrations.<a href="./src/cozmoai/resources/org/integrations.py">toggle</a>(id, \*, org_id, \*\*<a href="src/cozmoai/types/org/integration_toggle_params.py">params</a>) -> <a href="./src/cozmoai/types/org/connected_integration_response.py">ConnectedIntegrationResponse</a></code>
- <code title="patch /org/{org_id}/integrations/{id}/settings">client.org.integrations.<a href="./src/cozmoai/resources/org/integrations.py">update_settings</a>(id, \*, org_id, \*\*<a href="src/cozmoai/types/org/integration_update_settings_params.py">params</a>) -> <a href="./src/cozmoai/types/org/connected_integration_response.py">ConnectedIntegrationResponse</a></code>

## Lists

Types:

```python
from cozmoai.types.org import DeleteListResponse, ListResponse, ListListResponse
```

Methods:

- <code title="post /org/{org_id}/lists">client.org.lists.<a href="./src/cozmoai/resources/org/lists/lists.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/list_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/list_response.py">ListResponse</a></code>
- <code title="get /org/{org_id}/lists/{list_id}">client.org.lists.<a href="./src/cozmoai/resources/org/lists/lists.py">retrieve</a>(list_id, \*, org_id) -> <a href="./src/cozmoai/types/org/list_response.py">ListResponse</a></code>
- <code title="patch /org/{org_id}/lists/{list_id}">client.org.lists.<a href="./src/cozmoai/resources/org/lists/lists.py">update</a>(list_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/list_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/list_response.py">ListResponse</a></code>
- <code title="get /org/{org_id}/lists">client.org.lists.<a href="./src/cozmoai/resources/org/lists/lists.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/list_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/list_list_response.py">ListListResponse</a></code>
- <code title="delete /org/{org_id}/lists/{list_id}">client.org.lists.<a href="./src/cozmoai/resources/org/lists/lists.py">delete</a>(list_id, \*, org_id) -> <a href="./src/cozmoai/types/org/delete_list_response.py">DeleteListResponse</a></code>
- <code title="delete /org/{org_id}/lists/{list_id}/gdpr">client.org.lists.<a href="./src/cozmoai/resources/org/lists/lists.py">delete_gdpr</a>(list_id, \*, org_id) -> <a href="./src/cozmoai/types/org/delete_list_response.py">DeleteListResponse</a></code>

### Prospects

Types:

```python
from cozmoai.types.org.lists import (
    ListProspectOperationResponse,
    ProspectAddResponse,
    ProspectRemoveResponse,
)
```

Methods:

- <code title="put /org/{org_id}/lists/{list_id}/prospects/{prospect_id}">client.org.lists.prospects.<a href="./src/cozmoai/resources/org/lists/prospects.py">add</a>(prospect_id, \*, org_id, list_id) -> <a href="./src/cozmoai/types/org/lists/prospect_add_response.py">ProspectAddResponse</a></code>
- <code title="post /org/{org_id}/lists/{list_id}/prospects">client.org.lists.prospects.<a href="./src/cozmoai/resources/org/lists/prospects.py">add_bulk</a>(list_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/lists/prospect_add_bulk_params.py">params</a>) -> <a href="./src/cozmoai/types/org/lists/list_prospect_operation_response.py">ListProspectOperationResponse</a></code>
- <code title="delete /org/{org_id}/lists/{list_id}/prospects/{prospect_id}">client.org.lists.prospects.<a href="./src/cozmoai/resources/org/lists/prospects.py">remove</a>(prospect_id, \*, org_id, list_id) -> <a href="./src/cozmoai/types/org/lists/prospect_remove_response.py">ProspectRemoveResponse</a></code>
- <code title="delete /org/{org_id}/lists/{list_id}/prospects">client.org.lists.prospects.<a href="./src/cozmoai/resources/org/lists/prospects.py">remove_bulk</a>(list_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/lists/prospect_remove_bulk_params.py">params</a>) -> <a href="./src/cozmoai/types/org/lists/list_prospect_operation_response.py">ListProspectOperationResponse</a></code>

## OutcomeDefinitions

Types:

```python
from cozmoai.types.org import OutcomeDefinition, OutcomeDefinitionListResponse
```

Methods:

- <code title="post /org/{org_id}/outcome-definitions">client.org.outcome_definitions.<a href="./src/cozmoai/resources/org/outcome_definitions.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/outcome_definition_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/outcome_definition.py">OutcomeDefinition</a></code>
- <code title="patch /org/{org_id}/outcome-definitions/{id}">client.org.outcome_definitions.<a href="./src/cozmoai/resources/org/outcome_definitions.py">update</a>(id, \*, org_id, \*\*<a href="src/cozmoai/types/org/outcome_definition_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/outcome_definition.py">OutcomeDefinition</a></code>
- <code title="get /org/{org_id}/outcome-definitions">client.org.outcome_definitions.<a href="./src/cozmoai/resources/org/outcome_definitions.py">list</a>(org_id) -> <a href="./src/cozmoai/types/org/outcome_definition_list_response.py">OutcomeDefinitionListResponse</a></code>
- <code title="delete /org/{org_id}/outcome-definitions/{id}">client.org.outcome_definitions.<a href="./src/cozmoai/resources/org/outcome_definitions.py">delete</a>(id, \*, org_id) -> None</code>

## PhoneNumbers

Types:

```python
from cozmoai.types.org import (
    PaginationMetaTelephony,
    PhoneNumberResponse,
    PhoneNumberListResponse,
    PhoneNumberDeleteResponse,
    PhoneNumberCreateBulkResponse,
)
```

Methods:

- <code title="post /org/{org_id}/phone-numbers">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/phone_number_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="get /org/{org_id}/phone-numbers/{number_id}">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">retrieve</a>(number_id, \*, org_id) -> <a href="./src/cozmoai/types/org/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="patch /org/{org_id}/phone-numbers/{number_id}">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">update</a>(number_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/phone_number_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="get /org/{org_id}/phone-numbers">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/phone_number_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/phone_number_list_response.py">PhoneNumberListResponse</a></code>
- <code title="delete /org/{org_id}/phone-numbers/{number_id}">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">delete</a>(number_id, \*, org_id) -> <a href="./src/cozmoai/types/org/phone_number_delete_response.py">PhoneNumberDeleteResponse</a></code>
- <code title="post /org/{org_id}/phone-numbers/bulk">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">create_bulk</a>(org_id, \*\*<a href="src/cozmoai/types/org/phone_number_create_bulk_params.py">params</a>) -> <a href="./src/cozmoai/types/org/phone_number_create_bulk_response.py">PhoneNumberCreateBulkResponse</a></code>

## Prospects

Types:

```python
from cozmoai.types.org import (
    ProspectResponse,
    ResponseError,
    TagResponseProspect,
    ProspectListResponse,
    ProspectListCallsResponse,
)
```

Methods:

- <code title="post /org/{org_id}/prospects">client.org.prospects.<a href="./src/cozmoai/resources/org/prospects/prospects.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/prospect_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/prospect_response.py">ProspectResponse</a></code>
- <code title="get /org/{org_id}/prospects/{prospect_id}">client.org.prospects.<a href="./src/cozmoai/resources/org/prospects/prospects.py">retrieve</a>(prospect_id, \*, org_id) -> <a href="./src/cozmoai/types/org/prospect_response.py">ProspectResponse</a></code>
- <code title="patch /org/{org_id}/prospects/{prospect_id}">client.org.prospects.<a href="./src/cozmoai/resources/org/prospects/prospects.py">update</a>(prospect_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/prospect_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/prospect_response.py">ProspectResponse</a></code>
- <code title="get /org/{org_id}/prospects">client.org.prospects.<a href="./src/cozmoai/resources/org/prospects/prospects.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/prospect_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/prospect_list_response.py">ProspectListResponse</a></code>
- <code title="delete /org/{org_id}/prospects/{prospect_id}">client.org.prospects.<a href="./src/cozmoai/resources/org/prospects/prospects.py">delete</a>(prospect_id, \*, org_id) -> <a href="./src/cozmoai/types/org/response_error.py">ResponseError</a></code>
- <code title="delete /org/{org_id}/prospects/{prospect_id}/gdpr">client.org.prospects.<a href="./src/cozmoai/resources/org/prospects/prospects.py">hard_delete</a>(prospect_id, \*, org_id) -> <a href="./src/cozmoai/types/org/response_error.py">ResponseError</a></code>
- <code title="get /org/{org_id}/prospects/{prospect_id}/calls">client.org.prospects.<a href="./src/cozmoai/resources/org/prospects/prospects.py">list_calls</a>(prospect_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/prospect_list_calls_params.py">params</a>) -> <a href="./src/cozmoai/types/org/prospect_list_calls_response.py">ProspectListCallsResponse</a></code>

### Tags

Methods:

- <code title="post /org/{org_id}/prospects/{prospect_id}/tags">client.org.prospects.tags.<a href="./src/cozmoai/resources/org/prospects/tags.py">add</a>(prospect_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/prospects/tag_add_params.py">params</a>) -> <a href="./src/cozmoai/types/org/response_error.py">ResponseError</a></code>
- <code title="delete /org/{org_id}/prospects/{prospect_id}/tags/{tag_id}">client.org.prospects.tags.<a href="./src/cozmoai/resources/org/prospects/tags.py">remove</a>(tag_id, \*, org_id, prospect_id) -> <a href="./src/cozmoai/types/org/response_error.py">ResponseError</a></code>
- <code title="delete /org/{org_id}/prospects/{prospect_id}/tags">client.org.prospects.tags.<a href="./src/cozmoai/resources/org/prospects/tags.py">remove_all</a>(prospect_id, \*, org_id) -> <a href="./src/cozmoai/types/org/response_error.py">ResponseError</a></code>

### Bulk

Types:

```python
from cozmoai.types.org.prospects import BulkOperationResponseProspects, BulkImportResponse
```

Methods:

- <code title="patch /org/{org_id}/prospects/bulk">client.org.prospects.bulk.<a href="./src/cozmoai/resources/org/prospects/bulk.py">update</a>(org_id, \*\*<a href="src/cozmoai/types/org/prospects/bulk_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/prospects/bulk_operation_response_prospects.py">BulkOperationResponseProspects</a></code>
- <code title="delete /org/{org_id}/prospects/bulk">client.org.prospects.bulk.<a href="./src/cozmoai/resources/org/prospects/bulk.py">delete</a>(org_id, \*\*<a href="src/cozmoai/types/org/prospects/bulk_delete_params.py">params</a>) -> <a href="./src/cozmoai/types/org/prospects/bulk_operation_response_prospects.py">BulkOperationResponseProspects</a></code>
- <code title="post /org/{org_id}/prospects/bulk">client.org.prospects.bulk.<a href="./src/cozmoai/resources/org/prospects/bulk.py">import\_</a>(org_id, \*\*<a href="src/cozmoai/types/org/prospects/bulk_import_params.py">params</a>) -> <a href="./src/cozmoai/types/org/prospects/bulk_import_response.py">BulkImportResponse</a></code>

## QualityRules

Types:

```python
from cozmoai.types.org import QualityRuleResponse, QualityRuleListResponse
```

Methods:

- <code title="post /org/{org_id}/quality-rules">client.org.quality_rules.<a href="./src/cozmoai/resources/org/quality_rules.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/quality_rule_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/quality_rule_response.py">QualityRuleResponse</a></code>
- <code title="get /org/{org_id}/quality-rules/{rule_id}">client.org.quality_rules.<a href="./src/cozmoai/resources/org/quality_rules.py">retrieve</a>(rule_id, \*, org_id) -> <a href="./src/cozmoai/types/org/quality_rule_response.py">QualityRuleResponse</a></code>
- <code title="patch /org/{org_id}/quality-rules/{rule_id}">client.org.quality_rules.<a href="./src/cozmoai/resources/org/quality_rules.py">update</a>(rule_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/quality_rule_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/quality_rule_response.py">QualityRuleResponse</a></code>
- <code title="get /org/{org_id}/quality-rules">client.org.quality_rules.<a href="./src/cozmoai/resources/org/quality_rules.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/quality_rule_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/quality_rule_list_response.py">QualityRuleListResponse</a></code>
- <code title="delete /org/{org_id}/quality-rules/{rule_id}">client.org.quality_rules.<a href="./src/cozmoai/resources/org/quality_rules.py">delete</a>(rule_id, \*, org_id) -> None</code>

## Runs

Types:

```python
from cozmoai.types.org import PaginatedRunsExtendedResponse, ProspectInfo, RunResponse
```

Methods:

- <code title="get /org/{org_id}/runs/{run_id}">client.org.runs.<a href="./src/cozmoai/resources/org/runs.py">retrieve</a>(run_id, \*, org_id) -> <a href="./src/cozmoai/types/org/run_response.py">RunResponse</a></code>
- <code title="get /org/{org_id}/runs">client.org.runs.<a href="./src/cozmoai/resources/org/runs.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/run_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/paginated_runs_extended_response.py">PaginatedRunsExtendedResponse</a></code>

## SipTrunks

Types:

```python
from cozmoai.types.org import (
    SipTrunkResponse,
    SipTrunkRetrieveResponse,
    SipTrunkDeleteResponse,
    SipTrunkRetrieveSipTrunksResponse,
    SipTrunkSipTrunksResponse,
)
```

Methods:

- <code title="get /org/{org_id}/sip-trunks/{trunk_id}">client.org.sip_trunks.<a href="./src/cozmoai/resources/org/sip_trunks.py">retrieve</a>(trunk_id, \*, org_id) -> <a href="./src/cozmoai/types/org/sip_trunk_retrieve_response.py">SipTrunkRetrieveResponse</a></code>
- <code title="patch /org/{org_id}/sip-trunks/{trunk_id}">client.org.sip_trunks.<a href="./src/cozmoai/resources/org/sip_trunks.py">update</a>(trunk_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/sip_trunk_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/sip_trunk_response.py">SipTrunkResponse</a></code>
- <code title="delete /org/{org_id}/sip-trunks/{trunk_id}">client.org.sip_trunks.<a href="./src/cozmoai/resources/org/sip_trunks.py">delete</a>(trunk_id, \*, org_id) -> <a href="./src/cozmoai/types/org/sip_trunk_delete_response.py">SipTrunkDeleteResponse</a></code>
- <code title="get /org/{org_id}/sip-trunks">client.org.sip_trunks.<a href="./src/cozmoai/resources/org/sip_trunks.py">retrieve_sip_trunks</a>(org_id, \*\*<a href="src/cozmoai/types/org/sip_trunk_retrieve_sip_trunks_params.py">params</a>) -> <a href="./src/cozmoai/types/org/sip_trunk_retrieve_sip_trunks_response.py">SipTrunkRetrieveSipTrunksResponse</a></code>
- <code title="post /org/{org_id}/sip-trunks">client.org.sip_trunks.<a href="./src/cozmoai/resources/org/sip_trunks.py">sip_trunks</a>(org_id, \*\*<a href="src/cozmoai/types/org/sip_trunk_sip_trunks_params.py">params</a>) -> <a href="./src/cozmoai/types/org/sip_trunk_sip_trunks_response.py">SipTrunkSipTrunksResponse</a></code>

## Tags

Types:

```python
from cozmoai.types.org import TagResponseTag, TagListResponse, TagDeleteResponse
```

Methods:

- <code title="post /org/{org_id}/tags">client.org.tags.<a href="./src/cozmoai/resources/org/tags/tags.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/tag_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/tag_response_tag.py">TagResponseTag</a></code>
- <code title="get /org/{org_id}/tags/{tag_id}">client.org.tags.<a href="./src/cozmoai/resources/org/tags/tags.py">retrieve</a>(tag_id, \*, org_id) -> <a href="./src/cozmoai/types/org/tag_response_tag.py">TagResponseTag</a></code>
- <code title="patch /org/{org_id}/tags/{tag_id}">client.org.tags.<a href="./src/cozmoai/resources/org/tags/tags.py">update</a>(tag_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/tag_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/tag_response_tag.py">TagResponseTag</a></code>
- <code title="get /org/{org_id}/tags">client.org.tags.<a href="./src/cozmoai/resources/org/tags/tags.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/tag_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /org/{org_id}/tags/{tag_id}">client.org.tags.<a href="./src/cozmoai/resources/org/tags/tags.py">delete</a>(tag_id, \*, org_id) -> <a href="./src/cozmoai/types/org/tag_delete_response.py">TagDeleteResponse</a></code>

### Prospects

Types:

```python
from cozmoai.types.org.tags import BulkOperationResponseTags
```

Methods:

- <code title="post /org/{org_id}/tags/{tag_id}/prospects">client.org.tags.prospects.<a href="./src/cozmoai/resources/org/tags/prospects.py">create</a>(tag_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/tags/prospect_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/tags/bulk_operation_response_tags.py">BulkOperationResponseTags</a></code>
- <code title="delete /org/{org_id}/tags/{tag_id}/prospects">client.org.tags.prospects.<a href="./src/cozmoai/resources/org/tags/prospects.py">delete_all</a>(tag_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/tags/prospect_delete_all_params.py">params</a>) -> <a href="./src/cozmoai/types/org/tags/bulk_operation_response_tags.py">BulkOperationResponseTags</a></code>

## Tools

Types:

```python
from cozmoai.types.org import ParameterProp, ToolResponse, ToolListResponse
```

Methods:

- <code title="post /org/{org_id}/tools">client.org.tools.<a href="./src/cozmoai/resources/org/tools.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/tool_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/tool_response.py">ToolResponse</a></code>
- <code title="get /org/{org_id}/tools/{tool_id}">client.org.tools.<a href="./src/cozmoai/resources/org/tools.py">retrieve</a>(tool_id, \*, org_id) -> <a href="./src/cozmoai/types/org/tool_response.py">ToolResponse</a></code>
- <code title="patch /org/{org_id}/tools/{tool_id}">client.org.tools.<a href="./src/cozmoai/resources/org/tools.py">update</a>(tool_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/tool_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/tool_response.py">ToolResponse</a></code>
- <code title="get /org/{org_id}/tools">client.org.tools.<a href="./src/cozmoai/resources/org/tools.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/tool_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/tool_list_response.py">ToolListResponse</a></code>
- <code title="delete /org/{org_id}/tools/{tool_id}">client.org.tools.<a href="./src/cozmoai/resources/org/tools.py">delete</a>(tool_id, \*, org_id) -> <a href="./src/cozmoai/types/org/response_error.py">ResponseError</a></code>

## Workflows

Types:

```python
from cozmoai.types.org import (
    PaginationMetaWorkflows,
    WorkflowResponse,
    WorkflowListResponse,
    WorkflowDeleteResponse,
    WorkflowRetrieveCallsResponse,
)
```

Methods:

- <code title="post /org/{org_id}/workflows">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/workflow_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/workflow_response.py">WorkflowResponse</a></code>
- <code title="get /org/{org_id}/workflows/{workflow_id}">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">retrieve</a>(workflow_id, \*, org_id) -> <a href="./src/cozmoai/types/org/workflow_response.py">WorkflowResponse</a></code>
- <code title="post /org/{org_id}/workflows/{workflow_id}/restore/{version}">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">update</a>(version, \*, org_id, workflow_id) -> <a href="./src/cozmoai/types/org/workflow_response.py">WorkflowResponse</a></code>
- <code title="get /org/{org_id}/workflows">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/workflow_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/workflow_list_response.py">WorkflowListResponse</a></code>
- <code title="delete /org/{org_id}/workflows/{workflow_id}">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">delete</a>(workflow_id, \*, org_id) -> <a href="./src/cozmoai/types/org/workflow_delete_response.py">WorkflowDeleteResponse</a></code>
- <code title="post /org/{org_id}/workflows/{workflow_id}/duplicate">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">duplicate</a>(workflow_id, \*, org_id) -> <a href="./src/cozmoai/types/org/workflow_response.py">WorkflowResponse</a></code>
- <code title="get /org/{org_id}/workflow/{node_id}/calls">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">retrieve_calls</a>(node_id, \*, org_id) -> <a href="./src/cozmoai/types/org/workflow_retrieve_calls_response.py">WorkflowRetrieveCallsResponse</a></code>
- <code title="get /org/{org_id}/workflows/{workflow_id}/runs">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">retrieve_runs</a>(workflow_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/workflow_retrieve_runs_params.py">params</a>) -> <a href="./src/cozmoai/types/org/paginated_runs_extended_response.py">PaginatedRunsExtendedResponse</a></code>
- <code title="put /org/{org_id}/workflows/{workflow_id}/definition">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">update_definition</a>(workflow_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/workflow_update_definition_params.py">params</a>) -> <a href="./src/cozmoai/types/org/workflow_response.py">WorkflowResponse</a></code>

### Batches

Types:

```python
from cozmoai.types.org.workflows import BatchListResponse
```

Methods:

- <code title="post /org/{org_id}/workflows/{workflow_id}/batches">client.org.workflows.batches.<a href="./src/cozmoai/resources/org/workflows/batches.py">create</a>(workflow_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/workflows/batch_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/batch_response.py">BatchResponse</a></code>
- <code title="get /org/{org_id}/workflows/{workflow_id}/batches">client.org.workflows.batches.<a href="./src/cozmoai/resources/org/workflows/batches.py">list</a>(workflow_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/workflows/batch_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/workflows/batch_list_response.py">BatchListResponse</a></code>

### Versions

Types:

```python
from cozmoai.types.org.workflows import VersionRetrieveResponse, VersionListResponse
```

Methods:

- <code title="get /org/{org_id}/workflows/{workflow_id}/versions/{version}">client.org.workflows.versions.<a href="./src/cozmoai/resources/org/workflows/versions.py">retrieve</a>(version, \*, org_id, workflow_id) -> <a href="./src/cozmoai/types/org/workflows/version_retrieve_response.py">VersionRetrieveResponse</a></code>
- <code title="get /org/{org_id}/workflows/{workflow_id}/versions">client.org.workflows.versions.<a href="./src/cozmoai/resources/org/workflows/versions.py">list</a>(workflow_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/workflows/version_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/workflows/version_list_response.py">VersionListResponse</a></code>

# Organizations

Methods:

- <code title="post /organizations/{org_id}/leave">client.organizations.<a href="./src/cozmoai/resources/organizations/organizations.py">leave</a>(org_id) -> <a href="./src/cozmoai/types/org/response_error.py">ResponseError</a></code>

## Members

Types:

```python
from cozmoai.types.organizations import MemberListResponse
```

Methods:

- <code title="get /organizations/{org_id}/members">client.organizations.members.<a href="./src/cozmoai/resources/organizations/members.py">list</a>(org_id) -> <a href="./src/cozmoai/types/organizations/member_list_response.py">MemberListResponse</a></code>
- <code title="delete /organizations/{org_id}/members/{user_id}">client.organizations.members.<a href="./src/cozmoai/resources/organizations/members.py">remove</a>(user_id, \*, org_id) -> <a href="./src/cozmoai/types/org/response_error.py">ResponseError</a></code>
- <code title="patch /organizations/{org_id}/members/{user_id}">client.organizations.members.<a href="./src/cozmoai/resources/organizations/members.py">update_role</a>(user_id, \*, org_id, \*\*<a href="src/cozmoai/types/organizations/member_update_role_params.py">params</a>) -> <a href="./src/cozmoai/types/org/response_error.py">ResponseError</a></code>
