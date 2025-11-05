# REST Reference Cheatsheet (OpenAI)

- Base URL: `https://api.openai.com/v1`
- Create Response: `POST /responses` (Authorization: `Bearer <API_KEY>`)
- Retrieve Response: `GET /responses/{id}`
- Files: `POST /files` (upload), `GET /files/{id}`
- Streaming: `POST /responses` with `stream: true` (SSE)

See the official Responses API reference for full fields, enums, and error types.
