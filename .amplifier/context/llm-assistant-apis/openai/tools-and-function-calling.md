# Tools & Function Calling (OpenAI)

## Defining tools

Use the **Tools** guide to define function tools (name/description/JSON schema parameters). The model will return `function_call` outputs when it wants you to run a tool.

**Built‑in hosted tools** available when using OpenAI’s Responses/Agent stack include WebSearch, FileSearch (vector stores), CodeInterpreter, ComputerTool, HostedMCPTool, ImageGenerationTool, LocalShellTool.

## Running tool calls & chaining

- Inspect `response.output` for `function_call` items.
- Execute your function and include a matching `{"type":"function_call_output","call_id": "<from model>", "output": "<json string or text>"}` in the **next** Responses call’s `input`.
- Include `previous_response_id` so the model has continuity across turns. (Example in Azure docs; shape is equivalent on OpenAI.)

## File Search / Vector Stores

Attach vector stores via File Search so the model can retrieve from your knowledge base; OpenAI handles chunking, embeddings, and hybrid search.
