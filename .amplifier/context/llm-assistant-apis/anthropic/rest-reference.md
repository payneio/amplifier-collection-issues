# REST Reference Cheatsheet (Anthropic)

- Base URL: `https://api.anthropic.com/v1/messages`
- Headers: `x-api-key: <key>`, `anthropic-version: 2023-06-01` (or current)
- Streaming: `stream: true` (SSE)
- Tools: define in `tools`; model emits `tool_use`, you return `tool_result`.

See the Messages API reference for all fields and enums.
