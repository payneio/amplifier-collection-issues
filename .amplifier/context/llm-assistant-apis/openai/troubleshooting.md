# Troubleshooting (OpenAI)

- **Tool loop stalls:** Make sure you’re returning **`function_call_output`** objects with the **matching `call_id`**, and include `previous_response_id` on the follow‑up call. (See Azure’s example—same shape on OpenAI.)
- **No stream deltas appearing:** Ensure `stream=True` and handle `response.output_text.delta` events as they arrive.
- **Retrieval returns nothing:** Confirm your vector store is attached and the File Search tool is enabled for the turn.
