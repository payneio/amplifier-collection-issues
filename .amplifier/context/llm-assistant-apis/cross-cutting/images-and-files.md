# Images & Files

### OpenAI/Azure (Responses API content parts)

You can mix `input_text` with `input_image` and `input_file` parts in a single user turn. The Azure Responses guide shows both image inputs (URL or Base64 as `input_image`) and PDF file input via `input_file`, with the system extracting **both the text and an image of each page** into context for vision‑capable models.

**File Search & Vector Stores (OpenAI built‑in tool):** The File Search tool lets models retrieve from uploaded files (vector & keyword search). You create vector stores, upload files, and attach them in Responses calls.

### Anthropic

- **Files API (beta):** Upload/host files and reference them from Messages; requires the header `anthropic-beta: files-api-2025-04-14`.
- **Images in Messages:** Images are passed as content blocks (base64 or URLs) alongside text; follow the Messages schema and model capabilities.
