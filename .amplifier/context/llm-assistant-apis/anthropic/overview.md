# Anthropic — Overview (Messages API)

- **Primary interface:** `POST https://api.anthropic.com/v1/messages` (always include `anthropic-version` and your API key headers).
- **Models:** Latest Claude Sonnet 4.5 and Opus 4.1 series; model IDs include the snapshot date (e.g., `claude-sonnet-4-5-20250929`).
- **Tool use:** Native `tools` with `tool_use` and `tool_result` blocks—no OpenAI compatibility layer required.
- **Streaming:** SSE with `message_start`/`content_block_*`/`message_delta`/`message_stop`.
