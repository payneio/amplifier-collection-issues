# Python Examples (Ollama via OpenAI‑compatible clients)

**Chat Completions‑style loop with tools (conceptual):**

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

tools=[{
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "Get weather for a city",
    "parameters": {
      "type": "object",
      "properties": {"city": {"type": "string"}},
      "required": ["city"],
    },
  },
}]

# First turn (model may request a tool)
r1 = client.chat.completions.create(
    model="llama3.1",
    messages=[{"role":"user","content":"Weather in Toronto?"}],
    tools=tools,
    stream=True,
)

tool_calls = []
for chunk in r1:
    # Inspect chunk.choices[0].delta.tool_calls for tool requests, then stop streaming & run tool.
    pass

# After you run the tool, return a role=tool message then ask again:
messages=[
  {"role":"user","content":"Weather in Toronto?"},
  {"role":"assistant","tool_calls":[{"id":"call_1","function":{"name":"get_weather","arguments":"{\"city\":\"Toronto\"}"}}]},
  {"role":"tool","tool_call_id":"call_1","content":"{\"temp_c\":20,\"desc\":\"Overcast\"}"},
]
r2 = client.chat.completions.create(model="llama3.1", messages=messages)
print(r2.choices[0].message.content)
```

See the Ollama blog and compatibility docs for up‑to‑date support details.
