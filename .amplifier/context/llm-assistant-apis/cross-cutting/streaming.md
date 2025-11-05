# Streaming (SSE / Event Streams) Across Providers

### OpenAI (Responses API event names)

OpenAI’s agent/Responses streaming uses **typed events** like `response.created` and `response.output_text.delta`. The Agents SDK docs show how to subscribe and print token deltas from `ResponseTextDeltaEvent`.

### Anthropic (Messages SSE)

Anthropic streams **SSE events** in a fixed flow: `message_start` → a series of content blocks (`content_block_start` / `content_block_delta` / `content_block_stop`) → `message_delta` → `message_stop`. Docs also define pings and show structured deltas for tool inputs via `input_json_delta`.

### Azure OpenAI

Azure exposes the same Responses API streaming pattern as OpenAI. The Azure how‑to shows iterating the stream and checking for `response.output_text.delta`.

### Ollama

Ollama added **streaming tool calls** so you can stream text and get tool invocations in real time; see the May 28, 2025 announcement. (Implementation is still evolving—see notes in the Ollama provider section.)
