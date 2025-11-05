# Security, Governance & Runtime Considerations

### Code Interpreter / Containers (OpenAI/Azure)

The **Code Interpreter** tool runs Python in a **sandboxed container**. Azure’s documentation covers container creation via tool config, session lifetime (active ~1 hour, **idle timeout ~20 minutes**), and supported file types (CSV, images, PDFs, etc.). Billing is separate from model tokens.

### PDFs as inputs (OpenAI/Azure)

PDF input extracts **text and page images** into the model context; be mindful of token costs and context limits when sending large documents.

### Streaming reliability signals (Anthropic)

Anthropic streams may include **`error` events** like `overloaded_error` during high load; handle these gracefully and implement retry/backoff.
