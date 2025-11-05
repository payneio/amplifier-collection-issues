# Images & Files (Azure OpenAI Responses)

- **Image input:** Add `input_image` with either a URL or Base64 data URL.
- **PDF input:** Use `input_file` with Base64 or upload to Files (purpose currently `assistants` as a workaround). Azure clarifies that models ingest both the **extracted text and a rasterized image of each page** into context.
