# Agents

Types:

```python
from cozmoxai.types import (
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

- <code title="post /agents">client.agents.<a href="./src/cozmoxai/resources/agents.py">create</a>(\*\*<a href="src/cozmoxai/types/agent_create_params.py">params</a>) -> <a href="./src/cozmoxai/types/agent_response.py">AgentResponse</a></code>
- <code title="get /agents/{agent_id}">client.agents.<a href="./src/cozmoxai/resources/agents.py">retrieve</a>(agent_id) -> <a href="./src/cozmoxai/types/agent_response.py">AgentResponse</a></code>
- <code title="patch /agents/{agent_id}">client.agents.<a href="./src/cozmoxai/resources/agents.py">update</a>(agent_id, \*\*<a href="src/cozmoxai/types/agent_update_params.py">params</a>) -> <a href="./src/cozmoxai/types/agent_response.py">AgentResponse</a></code>
- <code title="get /agents">client.agents.<a href="./src/cozmoxai/resources/agents.py">list</a>(\*\*<a href="src/cozmoxai/types/agent_list_params.py">params</a>) -> <a href="./src/cozmoxai/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /agents/{agent_id}">client.agents.<a href="./src/cozmoxai/resources/agents.py">delete</a>(agent_id) -> <a href="./src/cozmoxai/types/agent_delete_response.py">AgentDeleteResponse</a></code>

# Calls

Types:

```python
from cozmoxai.types import CallRetrieveResponse, CallListResponse
```

Methods:

- <code title="get /calls/{call_id}">client.calls.<a href="./src/cozmoxai/resources/calls.py">retrieve</a>(call_id) -> <a href="./src/cozmoxai/types/call_retrieve_response.py">CallRetrieveResponse</a></code>
- <code title="get /calls">client.calls.<a href="./src/cozmoxai/resources/calls.py">list</a>(\*\*<a href="src/cozmoxai/types/call_list_params.py">params</a>) -> <a href="./src/cozmoxai/types/call_list_response.py">CallListResponse</a></code>

# Workflows

Types:

```python
from cozmoxai.types import WorkflowRetrieveResponse, WorkflowListResponse
```

Methods:

- <code title="get /workflows/{workflow_id}">client.workflows.<a href="./src/cozmoxai/resources/workflows.py">retrieve</a>(workflow_id) -> <a href="./src/cozmoxai/types/workflow_retrieve_response.py">WorkflowRetrieveResponse</a></code>
- <code title="get /workflows">client.workflows.<a href="./src/cozmoxai/resources/workflows.py">list</a>(\*\*<a href="src/cozmoxai/types/workflow_list_params.py">params</a>) -> <a href="./src/cozmoxai/types/workflow_list_response.py">WorkflowListResponse</a></code>

# Voices

Types:

```python
from cozmoxai.types import VoiceListResponse
```

Methods:

- <code title="get /voices">client.voices.<a href="./src/cozmoxai/resources/voices.py">list</a>(\*\*<a href="src/cozmoxai/types/voice_list_params.py">params</a>) -> <a href="./src/cozmoxai/types/voice_list_response.py">VoiceListResponse</a></code>
