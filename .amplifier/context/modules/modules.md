# Amplifier Modules

## 🏗️ Module Types Reference

| Module Type      | Purpose                 | Contract                                                       | Examples                                        | Key Principle                                                      |
| ---------------- | ----------------------- | -------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------ |
| **Provider**     | LLM backends            | `ChatRequest → ChatResponse`                                   | anthropic, openai, azure, ollama, mock          | Preserve all content types (text, tool calls, thinking, reasoning) |
| **Tool**         | Agent capabilities      | `execute(input) → ToolResult`                                  | filesystem, bash, web, search, task             | Non-interference - failures can't crash kernel                     |
| **Orchestrator** | Execution strategy      | `execute(prompt, context, providers, tools, hooks) → response` | basic, streaming, events                        | Pure policy - swap to change behavior                              |
| **Context**      | Memory management       | `add/get/compact messages`                                     | simple (in-memory), persistent (file)           | Deterministic compaction with events                               |
| **Hook**         | Observability & control | `__call__(event, data) → HookResult`                           | logging, backup, redaction, approval, scheduler | Non-blocking - never delay primary flow                            |
| **Agent**        | Config overlay          | Partial mount plan                                             | User-defined personas                           | Sub-session delegation with isolated context                       |

