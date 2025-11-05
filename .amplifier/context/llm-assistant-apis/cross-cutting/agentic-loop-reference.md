# Agentic Loop Reference (All Providers)

The core loop is the same everywhere:

1. Send user+context to the model with **tools enabled**.
2. If the model requests a tool, **run it** and **return the result** to the model.
3. Repeat until no more tool calls are returned, then show the final assistant message.

### Canonical shapes

- **OpenAI/Azure Responses API**: The model returns outputs that may include `function_call` items. You reply with one or more `{"type":"function_call_output","call_id":"...","output":"..."}` items and **chain** the next request by setting `previous_response_id` to the prior response. Azure’s Responses how‑to shows this end‑to‑end, including `previous_response_id`.

- **Anthropic Messages**: When tools are provided, the model emits `tool_use` blocks. You execute the tool and return a `tool_result` block referencing the tool’s `id`. The API reference shows the exact fields and a worked example.

### Parallel / multiple tool requests

Models may ask for multiple tools in one turn. The Responses schema includes a top‑level `parallel_tool_calls` field and per‑output `function_call` items; handle them independently and return a `function_call_output` for each. (Property is visible in typical Responses outputs.)

### Loop stop conditions

- No tool calls in the latest model output.
- Model explicitly answers the user’s question.
- Safety refusal or system policy requires stopping.
