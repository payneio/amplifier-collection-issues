# OpenAI — Overview (Responses API + Tools)

- **Primary interface:** `/v1/responses` (stateful). Supports text, image, and file inputs; tool use; structured outputs; and typed streaming events.
- **Built‑in tools (via Agent/Responses stack):** web search, file search (vector stores), code interpreter, computer use, hosted MCP tool.
- **Streaming:** subscribe to events like `response.output_text.delta`.
- **State carry‑over:** use `previous_response_id` and feed any `function_call_output` items produced since the last turn. (Azure shows the exact shape; OpenAI is equivalent.)
