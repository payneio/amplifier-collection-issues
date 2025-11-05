# Testing & Observability

- **SSE inspection:** Log raw SSE event types. For OpenAI you’ll see `response.*` deltas; for Anthropic, the `message_*` and `content_block_*` flow.
- **Tool loop traces:** Record every tool request + the exact parameters the model produced, and the tool outputs you injected back.
- **Schema validation:** When using Structured Outputs, validate against your JSON Schema before using results.
