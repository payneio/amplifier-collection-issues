# Tool Use (Anthropic Messages)

Add a `tools` array (name/description/input_schema). When Claude wants a tool, it emits a `tool_use` block with an `id` and `input`. You run the tool and reply with a `tool_result` that references `tool_use_id`. The Messages API details the fields and a full example.

**Service headers:** Always send `anthropic-version`, and for File uploads use the beta header noted in Files API (when applicable).
