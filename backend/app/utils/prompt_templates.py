def explain_prompt(context, question):
    return f"""
You are RebootAI, an expert developer assistant.

Code Context:
{context}

Question:
{question}

Explain in simple English.
"""

def debug_prompt(error):
    return f"""
You are RebootAI Debug Tutor.

Error:
{error}

Explain root cause and solution step by step.
"""