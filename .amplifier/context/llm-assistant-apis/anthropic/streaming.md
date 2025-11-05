# Streaming (Anthropic Messages)

The official SSE spec lists event types and order: `message_start` → `content_block_start` → `content_block_delta` (e.g., `text_delta`, `input_json_delta`, `thinking_delta`) → `content_block_stop` → `message_delta` → `message_stop`. Handle `ping` and potential `error` events like `overloaded_error`.

**Python SDK** supports sync/async streaming helpers; see the page for simple printing of streamed text.
