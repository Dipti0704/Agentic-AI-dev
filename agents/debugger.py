from llm import call_ollama
from config import MODEL_DEBUGGER

def clean_code(raw: str) -> str:
    lines = raw.strip().splitlines()
    cleaned = [l for l in lines if not l.strip().startswith("```")]
    return "\n".join(cleaned)

def debug_agent(error: str, code: str) -> str:
    prompt = f"""You are an expert Python debugger.

Fix the code based on the error below.

Error:
{error}

Code:
{code}

Rules:
- Output ONLY corrected code
- No explanation
- No markdown
- Keep all functionality same
- Fix only the issue

Start with code directly.
"""

    raw = call_ollama(prompt, MODEL_DEBUGGER)

    if not raw:
        return code

    return clean_code(raw)