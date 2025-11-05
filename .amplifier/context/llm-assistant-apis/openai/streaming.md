# Streaming (OpenAI Responses)

Use streaming to start rendering tokens as they’re generated. The Agents SDK docs show **raw response events** in Responses format (e.g., `response.created`, `response.output_text.delta`) and how to print deltas.

**Python skeleton:**

```python
from openai import OpenAI
client = OpenAI()

stream = client.responses.create(
    model="gpt-5-mini",
    input="Stream a short response, please.",
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```
