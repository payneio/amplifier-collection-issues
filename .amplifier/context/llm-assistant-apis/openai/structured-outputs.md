# Structured Outputs (OpenAI)

Enable **schema‑constrained JSON** with `response_format` using `json_schema` and `strict: true`. This guarantees the model adheres to your schema, independent of tool use.

**When to choose:** Use a schema when you want deterministic output for downstream code; use function calls when you need to _do_ something.
