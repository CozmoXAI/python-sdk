# Agents

Types:

```python
from cozmoai.types import (
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

- <code title="post /org/{org_id}/agents">client.agents.<a href="./src/cozmoai/resources/agents.py">create</a>(org_id, \*\*<a href="src/cozmoai/types/agent_create_params.py">params</a>) -> <a href="./src/cozmoai/types/agent_response.py">AgentResponse</a></code>
- <code title="get /org/{org_id}/agents/{agent_id}">client.agents.<a href="./src/cozmoai/resources/agents.py">retrieve</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/agent_response.py">AgentResponse</a></code>
- <code title="patch /org/{org_id}/agents/{agent_id}">client.agents.<a href="./src/cozmoai/resources/agents.py">update</a>(agent_id, \*, org_id, \*\*<a href="src/cozmoai/types/agent_update_params.py">params</a>) -> <a href="./src/cozmoai/types/agent_response.py">AgentResponse</a></code>
- <code title="get /org/{org_id}/agents">client.agents.<a href="./src/cozmoai/resources/agents.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/agent_list_params.py">params</a>) -> <a href="./src/cozmoai/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /org/{org_id}/agents/{agent_id}">client.agents.<a href="./src/cozmoai/resources/agents.py">delete</a>(agent_id, \*, org_id) -> <a href="./src/cozmoai/types/agent_delete_response.py">AgentDeleteResponse</a></code>

# Calls

Types:

```python
from cozmoai.types import CallRetrieveResponse, CallListResponse
```

Methods:

- <code title="get /org/{org_id}/calls/{call_id}">client.calls.<a href="./src/cozmoai/resources/calls.py">retrieve</a>(call_id, \*, org_id) -> <a href="./src/cozmoai/types/call_retrieve_response.py">CallRetrieveResponse</a></code>
- <code title="get /org/{org_id}/calls">client.calls.<a href="./src/cozmoai/resources/calls.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/call_list_params.py">params</a>) -> <a href="./src/cozmoai/types/call_list_response.py">CallListResponse</a></code>

# Workflows

Types:

```python
from cozmoai.types import WorkflowRetrieveResponse, WorkflowListResponse
```

Methods:

- <code title="get /org/{org_id}/workflows/{workflow_id}">client.workflows.<a href="./src/cozmoai/resources/workflows.py">retrieve</a>(workflow_id, \*, org_id) -> <a href="./src/cozmoai/types/workflow_retrieve_response.py">WorkflowRetrieveResponse</a></code>
- <code title="get /org/{org_id}/workflows">client.workflows.<a href="./src/cozmoai/resources/workflows.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/workflow_list_params.py">params</a>) -> <a href="./src/cozmoai/types/workflow_list_response.py">WorkflowListResponse</a></code>

# Voices

Types:

```python
from cozmoai.types import VoiceListResponse
```

Methods:

- <code title="get /org/{org_id}/voices">client.voices.<a href="./src/cozmoai/resources/voices.py">list</a>(org_id, \*\*<a href="src/cozmoai/types/voice_list_params.py">params</a>) -> <a href="./src/cozmoai/types/voice_list_response.py">VoiceListResponse</a></code>
