# Structured Outputs (Schema‑constrained JSON)

### OpenAI / Azure

OpenAI introduced **Structured Outputs**: pass a JSON Schema in `response_format` (with `strict: true`) and the model will return outputs that conform to the schema. This is independent of tool calling and is supported in the Responses API.

Azure documents the same concept and guidance in its Structured Outputs guide.

### When to use tools vs. schema

- Use **tools** when the model needs to trigger side effects or query external systems.
- Use **schema outputs** when you only need reliable structured data back from the model without side effects.
