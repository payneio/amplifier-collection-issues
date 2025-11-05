# Python Examples (Anthropic)

## Tool loop

```python
import anthropic, json
client = anthropic.Anthropic()

msg = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=800,
    tools=[{
        "name":"get_weather",
        "description":"Get weather for a city",
        "input_schema":{
            "type":"object",
            "properties":{"location":{"type":"string"}},
            "required":["location"]
        }
    }],
    messages=[{"role":"user","content":"Weather in SF today?"}],
)

responses = []
for block in msg.content:
    if block.type == "tool_use" and block.name == "get_weather":
        # run tool...
        tool_out = {"temp_c": 20, "desc":"Foggy"}
        responses.append({
            "role":"user",
            "content":[{
                "type":"tool_result",
                "tool_use_id": block.id,
                "content": json.dumps(tool_out),
            }],
        })

if responses:
    followup = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=800,
        messages=[{"role":"assistant","content": msg.content}] + responses,
    )
    print(followup.content[0].text)
```

See the Messages reference for exact `tool_use`/`tool_result` fields.

## Streaming

```python
from anthropic import Anthropic
client = Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-5",
    max_tokens=512,
    messages=[{"role":"user","content":"Stream a short response."}],
) as stream:
    for token in stream.text_stream:
        print(token, end="", flush=True)
```

SSE events and deltas are documented here.
