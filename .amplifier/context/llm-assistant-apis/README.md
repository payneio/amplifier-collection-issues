# LLM Assistant API Playbook (Providers: OpenAI, Azure OpenAI, Anthropic, Ollama)

**Last generated:** 2025-10-12

This package documents _current_ request/response shapes, streaming, tool use, and agentic loop patterns across the four providers your team targets. It’s organized as folders per provider with consistent sub‑docs, plus cross‑cutting guidance.

> Note: These docs paraphrase/condense vendor guidance and include canonical citations to the official sources so devs can double‑check fine details. When behavior differs between OpenAI and Azure OpenAI, we call it out explicitly.

## Structure

```
/
  README.md
  cross-cutting/
    agentic-loop-reference.md
    streaming.md
    images-and-files.md
    structured-outputs.md
    security-and-governance.md
    testing-and-observability.md
  openai/
    overview.md
    tools-and-function-calling.md
    streaming.md
    images-and-files.md
    structured-outputs.md
    python-examples.md
    rest-reference.md
    troubleshooting.md
  anthropic/
    overview.md
    tools-and-tool-use.md
    streaming.md
    images-and-files.md
    structured-json.md
    python-examples.md
    rest-reference.md
    troubleshooting.md
  azure-openai/
    overview.md
    tools-and-function-calling.md
    streaming.md
    images-and-files.md
    structured-outputs.md
    python-examples.md
    rest-reference.md
    troubleshooting.md
  ollama/
    overview.md
    tools-and-function-calling.md
    streaming.md
    python-examples.md
    rest-reference.md
    troubleshooting.md
```

### Where these links came from

We validated canonical doc entry points from the “LLM API Lookup” index you shared and then pulled details directly from vendor docs referenced throughout this package. fileciteturn1file1

---

## Quick links (official docs we cite throughout)

- **OpenAI**: Responses API / tools / file search / structured outputs / streaming event shapes (via Agents SDK).
- **Azure OpenAI**: Responses API how‑to (includes `previous_response_id`, Code Interpreter container + supported files, image & file input, event type names, region/model lists).
- **Anthropic**: Messages API (tools `tool_use`/`tool_result`), Streaming SSE event taxonomy, Files API (beta header).
- **Ollama**: OpenAI‑compat layer, tool calling + streaming blog, limitations.
