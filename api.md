# Org

Types:

```python
from cozmoai.types import OrgListVoicesResponse
```

Methods:

- <code title="get /org/{org_id}/voices">client.org.<a href="./src/cozmoai/resources/org/org.py">list_voices</a>(org_id, \*\*<a href="src/cozmoai/types/org_list_voices_params.py">params</a>) -> <a href="./src/cozmoai/types/org_list_voices_response.py">OrgListVoicesResponse</a></code>

## Agents

Types:

```python
from cozmoai.types.org import (
    Agent,
    AgentsThinkingSound,
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

- <code title="post /org/{org_id}/agents">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/agent_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent.py">Agent</a></code>
- <code title="get /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">retrieve</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agent.py">Agent</a></code>
- <code title="patch /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">update</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agent_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent.py">Agent</a></code>
- <code title="get /org/{org_id}/agents">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/agent_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">delete</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agent_delete_response.py">AgentDeleteResponse</a></code>

### Tools

Types:

```python
from cozmoai.types.org.agents import AgentTool
```

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
)
```

Methods:

- <code title="get /org/{org_id}/calls">client.org.calls.<a href="./src/cozmoai/resources/org/calls.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/call_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/call_list_response.py">CallListResponse</a></code>
- <code title="get /org/{org_id}/calls/{call_id}">client.org.calls.<a href="./src/cozmoai/resources/org/calls.py">get_details</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_get_details_response.py">CallGetDetailsResponse</a></code>

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
from cozmoai.types.org import DeleteListResponse, ListResponse
```

### Prospects

Types:

```python
from cozmoai.types.org.lists import ListProspectOperationResponse
```

## OutcomeDefinitions

Types:

```python
from cozmoai.types.org import OutcomeDefinition
```

## PhoneNumbers

Types:

```python
from cozmoai.types.org import PaginationMetaTelephony, PhoneNumberResponse
```

## Prospects

Types:

```python
from cozmoai.types.org import ProspectResponse, ResponseError, TagResponseProspect
```

### Bulk

Types:

```python
from cozmoai.types.org.prospects import BulkOperationResponseProspects
```

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

## Tools

Types:

```python
from cozmoai.types.org import ParameterProp, ToolResponse
```

## Workflows

Types:

```python
from cozmoai.types.org import PaginationMetaWorkflows, WorkflowResponse, WorkflowListResponse
```

Methods:

- <code title="get /org/{org_id}/workflows/{workflow_id}">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows.py">retrieve</a>(workflow_id, \*, org_id) -> <a href="./src/cozmoai/types/org/workflow_response.py">WorkflowResponse</a></code>
- <code title="get /org/{org_id}/workflows">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/workflow_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/workflow_list_response.py">WorkflowListResponse</a></code>
