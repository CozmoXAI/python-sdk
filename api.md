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
from cozmoai.types import OrgCreateWorkflowRunResponse, OrgListVoicesResponse
```

Methods:

- <code title="post /org/{org_id}/workflow-runs">client.org.<a href="./src/cozmoai/resources/org/org.py">create_workflow_run</a>(org_id, \*\*<a href="src/cozmoai/types/org_create_workflow_run_params.py">params</a>) -> <a href="./src/cozmoai/types/org_create_workflow_run_response.py">OrgCreateWorkflowRunResponse</a></code>
- <code title="get /org/{org_id}/voices">client.org.<a href="./src/cozmoai/resources/org/org.py">list_voices</a>(org_id, \*\*<a href="src/cozmoai/types/org_list_voices_params.py">params</a>) -> <a href="./src/cozmoai/types/org_list_voices_response.py">OrgListVoicesResponse</a></code>

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
)
```

Methods:

- <code title="post /org/{org_id}/agents">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/agent_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent.py">Agent</a></code>
- <code title="get /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">retrieve</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agent.py">Agent</a></code>
- <code title="patch /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">update</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agent_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent.py">Agent</a></code>
- <code title="get /org/{org_id}/agents">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/agent_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents/agents.py">delete</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agent_delete_response.py">AgentDeleteResponse</a></code>

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
from cozmoai.types.org.agents import PaginationMetaUnitTests
```

### UnitTests

Types:

```python
from cozmoai.types.org.agents import UnitTest
```

### Evals

Types:

```python
from cozmoai.types.org.agents import Eval
```

## Analytics

Types:

```python
from cozmoai.types.org import AnalyticsPeriod
```

## APIKeys

Types:

```python
from cozmoai.types.org import Response
```

## Batches

Types:

```python
from cozmoai.types.org import BatchResponse, PaginationMetaWorkflowBatches
```

## Billing

Types:

```python
from cozmoai.types.org import Numeric
```

### Invoices

Types:

```python
from cozmoai.types.org.billing import PaginationMetaBilling
```

## Calls

Types:

```python
from cozmoai.types.org import (
    CallEvaluation,
    CallToolLog,
    PaginationMetaCalls,
    CallListResponse,
    CallGetDetailsResponse,
    CallGetRecordingResponse,
    CallGetTranscriptResponse,
)
```

Methods:

- <code title="get /org/{org_id}/calls">client.org.calls.<a href="./src/cozmoai/resources/org/calls.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/call_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/call_list_response.py">CallListResponse</a></code>
- <code title="get /org/{org_id}/calls/{call_id}">client.org.calls.<a href="./src/cozmoai/resources/org/calls.py">get_details</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_get_details_response.py">CallGetDetailsResponse</a></code>
- <code title="get /org/{org_id}/calls/{call_id}/recording">client.org.calls.<a href="./src/cozmoai/resources/org/calls.py">get_recording</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_get_recording_response.py">CallGetRecordingResponse</a></code>
- <code title="get /org/{org_id}/calls/{call_id}/transcript">client.org.calls.<a href="./src/cozmoai/resources/org/calls.py">get_transcript</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_get_transcript_response.py">CallGetTranscriptResponse</a></code>

## EmailTemplates

Types:

```python
from cozmoai.types.org import Template
```

## Faqs

Types:

```python
from cozmoai.types.org import Faq
```

## Integrations

Types:

```python
from cozmoai.types.org import ConnectedIntegrationResponse
```

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
from cozmoai.types.org import OutcomeDefinition
```

## PhoneNumbers

Types:

```python
from cozmoai.types.org import (
    PaginationMetaTelephony,
    PhoneNumberResponse,
    PhoneNumberListResponse,
    PhoneNumberDeleteResponse,
)
```

Methods:

- <code title="post /org/{org_id}/phone-numbers">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/phone_number_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="get /org/{org_id}/phone-numbers/{number_id}">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">retrieve</a>(number_id, \*, org_id) -> <a href="./src/cozmoai/types/org/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="patch /org/{org_id}/phone-numbers/{number_id}">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">update</a>(number_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/phone_number_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/phone_number_response.py">PhoneNumberResponse</a></code>
- <code title="get /org/{org_id}/phone-numbers">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/phone_number_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/phone_number_list_response.py">PhoneNumberListResponse</a></code>
- <code title="delete /org/{org_id}/phone-numbers/{number_id}">client.org.phone_numbers.<a href="./src/cozmoai/resources/org/phone_numbers.py">delete</a>(number_id, \*, org_id) -> <a href="./src/cozmoai/types/org/phone_number_delete_response.py">PhoneNumberDeleteResponse</a></code>

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
from cozmoai.types.org import QualityRuleResponse
```

## Runs

Types:

```python
from cozmoai.types.org import PaginatedRunsExtendedResponse, ProspectInfo, RunResponse
```

## SipTrunks

Types:

```python
from cozmoai.types.org import SipTrunkResponse
```

## Tags

Types:

```python
from cozmoai.types.org import TagResponseTag
```

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
from cozmoai.types.org import ParameterProp, ToolResponse
```

## Workflows

Types:

```python
from cozmoai.types.org import (
    PaginationMetaWorkflows,
    WorkflowResponse,
    WorkflowListResponse,
    WorkflowDeleteResponse,
)
```

Methods:

- <code title="post /org/{org_id}/workflows">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/workflow_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/workflow_response.py">WorkflowResponse</a></code>
- <code title="get /org/{org_id}/workflows/{workflow_id}">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">retrieve</a>(workflow_id, \*, org_id) -> <a href="./src/cozmoai/types/org/workflow_response.py">WorkflowResponse</a></code>
- <code title="get /org/{org_id}/workflows">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/workflow_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/workflow_list_response.py">WorkflowListResponse</a></code>
- <code title="delete /org/{org_id}/workflows/{workflow_id}">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows/workflows.py">delete</a>(workflow_id, \*, org_id) -> <a href="./src/cozmoai/types/org/workflow_delete_response.py">WorkflowDeleteResponse</a></code>
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
