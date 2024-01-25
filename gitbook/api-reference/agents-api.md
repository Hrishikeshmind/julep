# Agents API

## Agents

### List agents

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Create a new agent

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents" method="post" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Get a specific agent by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Update an agent

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}" method="put" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Delete an agent

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}" method="delete" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

*****

## Users

### List all users

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/users" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Create a new user

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/users" method="post" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Get a specific user by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/users/{user_id}" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Update a specific user by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/users/{user_id}" method="put" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Delete a specific user by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/users/{user_id}" method="delete" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

*****

## Sessions

### List sessions

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/sessions" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Create a new session

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/sessions" method="post" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Get a specific session by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/sessions/{session_id}" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Update a specific session by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/sessions/{session_id}" method="put" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Delete a specific session by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/sessions/{session_id}" method="delete" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

*****

## Chat

### Chat with an agent in a session

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/sessions/{session_id}/chat" method="post" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Get suggestions made by the agent based on the session

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/sessions/{session_id}/suggestions" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Get a session's chat history

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/sessions/{session_id}/history" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

*****

## Memories

### Get an agent's memories

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}/memories" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Delete a memory by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}/memories/{memory_id}" method="delete" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

*****

## Tools

### List all tools

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}/tools" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Create a new tool for agent

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}/tools" method="post" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Update a tool by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}/tools/{tool_id}" method="put" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Delete a tool by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}/tools/{tool_id}" method="delete" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

*****

## Docs

### Get all docs (for an agent or user)

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}/additional_info" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/users/{user_id}/additional_info" method="get" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Create a new doc (for agent or user)

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}/additional_info" method="post" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/users/{user_id}/additional_info" method="post" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

### Delete a doc by id

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/agents/{agent_id}/additional_info/{additional_info_id}" method="delete" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}

{% swagger src="../.gitbook/assets/agents-openapi.yaml" path="/users/{user_id}/additional_info/{additional_info_id}" method="delete" %}
[agents-openapi.yaml](<../.gitbook/assets/agents-openapi.yaml>)
{% endswagger %}
