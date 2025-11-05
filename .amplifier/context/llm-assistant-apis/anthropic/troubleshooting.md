# Troubleshooting (Anthropic)

- **Missing `max_tokens`:** It’s required—set it explicitly.
- **Streaming stalls or errors:** Handle `ping` and `error` events (e.g., `overloaded_error`) and retry with backoff.
- **Large context:** Prefer streaming and consider long‑context model options documented on the Models pages.
