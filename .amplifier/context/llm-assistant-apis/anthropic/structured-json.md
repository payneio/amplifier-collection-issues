# Structured JSON (Anthropic)

Claude can produce structured outputs, but the **preferred** way to get precise structures for downstream logic is to define **tools** with an `input_schema` (and optionally interpret tool results as your app’s outputs). Messages API documentation discusses tools for producing specific JSON structures.
