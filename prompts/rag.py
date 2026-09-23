RAG_SYSTEM_PROMPT = """
You are a helpful AI assistant.

Rules:
- Use only the provided context
- Do not make up information
- If the answer is not in the context, say:
  'I do not have enough information.'
"""

RAG_TEMPLATE = """
CONTEXT:

{context}

QUESTION:

{question}

INSTRUCTIONS:

- Answer only using the context
- Be concise
- Cite relevant context sections if possible

ANSWER:
"""