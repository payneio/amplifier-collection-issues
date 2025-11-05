# REST Reference Cheatsheet (Azure OpenAI)

- Base URL: `https://<RESOURCE>.openai.azure.com/openai/v1`
- Create Response: `POST /responses` (Auth via API Key header `api-key` **or** Microsoft Entra ID Bearer token)
- Retrieve Response: `GET /responses/{id}`
- Streaming: `POST /responses` with `stream: true` (SSE)

See the Azure Responses how‑to for full parameters, auth modes, and output shapes.
