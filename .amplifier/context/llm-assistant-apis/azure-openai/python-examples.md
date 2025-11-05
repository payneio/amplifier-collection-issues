# Python Examples (Azure OpenAI Responses)

## Basic text

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://<RESOURCE>.openai.azure.com/openai/v1/",
    api_key="<AZURE_OPENAI_API_KEY>"
)
resp = client.responses.create(model="gpt-5-nano", input="This is a test.")
print(resp.output_text)
```

## Streaming tokens

```python
for event in client.responses.create(
    model="o4-mini",
    input="Stream a short response.",
    stream=True,
):
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```

## Code Interpreter (container)

```python
resp = client.responses.create(
    model="gpt-5",
    tools=[{"type":"code_interpreter","container":{"type":"auto"}}],
    instructions="When asked a math question, write & run Python to solve it.",
    input="3x + 11 = 14. Solve for x."
)
# See how‑to for supported files, container lifetime, and billing notes.
```

Container and supported files guidance (timeout, file list) is in the how‑to.
