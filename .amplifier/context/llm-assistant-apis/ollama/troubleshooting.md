# Troubleshooting (Ollama)

- **No `responses` endpoint:** Use `/v1/chat/completions` in the OpenAI‑compat layer unless your version documents more.
- **Tool call + message together missing:** By design, some builds convert JSON output into `tool_calls` and clear content—split into two operations.
- **Streaming quirks:** Behavior can differ by model/build; see current issues for streaming tool calls.
