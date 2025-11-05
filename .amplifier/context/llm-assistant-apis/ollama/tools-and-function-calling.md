# Tools & Function Calling (Ollama)

Ollama’s tool format mirrors OpenAI function calling (`tools: [{type:"function", function:{...}}]`). After an assistant tool call, **append a `role: "tool"` message** with the result, then call chat again. See example implementations and community notes.

**Caveat:** Ollama’s streaming/tool semantics are still maturing; some versions may not stream full tool call details or may restrict mixed content + tool calls in the same chunk. Track current issues for your version.
