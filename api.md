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
    AgentResponse,
    BackgroundSoundConfig,
    ExtraConfig,
    GoodbyeConfig,
    GreetingConfig,
    LlmConfig,
    RoomDurationConfig,
    TranscriberConfig,
    VadConfig,
    VoiceConfig,
    AgentListResponse,
    AgentDeleteResponse,
)
```

Methods:

- <code title="post /org/{org_id}/agents">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/org/agent_create_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent_response.py">AgentResponse</a></code>
- <code title="get /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">retrieve</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agent_response.py">AgentResponse</a></code>
- <code title="patch /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">update</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/org/agent_update_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent_response.py">AgentResponse</a></code>
- <code title="get /org/{org_id}/agents">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/agent_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /org/{org_id}/agents/{agent_id}">client.org.agents.<a href="./src/cozmoai/resources/org/agents.py">delete</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/org/agent_delete_response.py">AgentDeleteResponse</a></code>

## Calls

Types:

```python
from cozmoai.types.org import CallRetrieveResponse, CallListResponse
```

Methods:

- <code title="get /org/{org_id}/calls/{call_id}">client.org.calls.<a href="./src/cozmoai/resources/org/calls.py">retrieve</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/org/call_retrieve_response.py">CallRetrieveResponse</a></code>
- <code title="get /org/{org_id}/calls">client.org.calls.<a href="./src/cozmoai/resources/org/calls.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/call_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/call_list_response.py">CallListResponse</a></code>

## Workflows

Types:

```python
from cozmoai.types.org import WorkflowRetrieveResponse, WorkflowListResponse
```

Methods:

- <code title="get /org/{org_id}/workflows/{workflow_id}">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows.py">retrieve</a>(workflow_id, \*, org_id) -> <a href="./src/cozmoai/types/org/workflow_retrieve_response.py">WorkflowRetrieveResponse</a></code>
- <code title="get /org/{org_id}/workflows">client.org.workflows.<a href="./src/cozmoai/resources/org/workflows.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/org/workflow_list_params.py">params</a>) -> <a href="./src/cozmoai/types/org/workflow_list_response.py">WorkflowListResponse</a></code>
