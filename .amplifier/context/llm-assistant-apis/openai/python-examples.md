# Python Examples (OpenAI Responses)

## Basic multi‑turn with a function tool

```python
from openai import OpenAI
client = OpenAI()

# 1) First turn: let the model decide to call our tool
resp1 = client.responses.create(
    model="gpt-5",
    tools=[{
        "type": "function",
        "name": "get_weather",
        "description": "Get the weather for a location",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
        },
    }],
    input=[{"role":"user","content":"What's the weather in San Francisco?"}],
)

tool_outputs = []
for out in resp1.output:
    if out.type == "function_call" and out.name == "get_weather":
        # 2) Run your function here (pseudo)
        result = {"temperature":"20 C","conditions":"Foggy"}
        tool_outputs.append({
            "type": "function_call_output",
            "call_id": out.call_id,
            "output": json.dumps(result),
        })

# 3) Second turn: return tool results and chain the context
resp2 = client.responses.create(
    model="gpt-5",
    previous_response_id=resp1.id,
    input=tool_outputs,
)
print(resp2.output_text)
```

(Shapes and chaining are illustrated in Azure’s Responses how‑to; OpenAI follows the same pattern.)

## Streaming tokens

```python
from openai import OpenAI
client = OpenAI()

for event in client.responses.create(
    model="gpt-5-mini",
    input="Stream a haiku about the ocean.",
    stream=True,
):
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```

Event names are documented in the Agents SDK streaming guide.
