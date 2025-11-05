# Tools & Function Calling (Azure OpenAI Responses)

The Azure how‑to shows **function calling** and the **exact format** for returning results via `function_call_output`, plus **chaining** using `previous_response_id`.

```python
from openai import OpenAI
client = OpenAI(base_url="https://<RESOURCE>.openai.azure.com/openai/v1/",
                api_key="<AZURE_OPENAI_API_KEY>")

# First turn
r1 = client.responses.create(
    model="gpt-5",
    tools=[{
        "type":"function",
        "name":"get_weather",
        "description":"Get the weather for a location",
        "parameters":{"type":"object","properties":{"location":{"type":"string"}},"required":["location"]}
    }],
    input=[{"role":"user","content":"Weather in SF?"}],
)

tool_inputs = []
for out in r1.output:
    if out.type == "function_call" and out.name == "get_weather":
        tool_inputs.append({"type":"function_call_output","call_id": out.call_id,"output": '{"temperature":"70 F"}'})

# Second turn
r2 = client.responses.create(model="gpt-5",
                             previous_response_id=r1.id,
                             input=tool_inputs)
print(r2.output_text)
```
