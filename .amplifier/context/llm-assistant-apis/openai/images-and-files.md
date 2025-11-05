# Images & Files (OpenAI Responses)

**Images:** Send via content parts (URL or Base64) using `input_image` alongside `input_text`. **Files (PDFs):** Provide via `input_file` content, or upload to Files and reference by ID. Azure’s Responses guide shows both methods and clarifies that PDFs add both extracted text and page images to the context for vision‑capable models—behavior mirrored on OpenAI.

**File Search** (retrieval over vector stores) is a built‑in tool for the Responses workflow.
