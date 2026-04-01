import os
from llm import call_ollama
from config import MODEL_CODER


def clean_code(raw: str) -> str:
    lines = raw.strip().splitlines()
    return "\n".join([l for l in lines if not l.strip().startswith("```")])


def coder_agent(architecture: str, file_path: str, file_desc: str, OUTPUT_DIR: str) -> str:
    prompt = f"""You are an expert developer.

Write COMPLETE code for ONE file.

File: {file_path}
Purpose: {file_desc}

Rules:
- Output ONLY code
- No markdown
- No explanations
- Full working code

IMPORTANT:
- If Flask app (app.py):
  - MUST include a root route "/"
  - Use render_template if HTML exists
  - Add this comment at top:
    # ENTRY_POINT: /

- If frontend exists:
  - Place HTML inside templates folder

Start directly with code.
"""

    raw = call_ollama(prompt, MODEL_CODER)

    if not raw:
        return ""

    code = clean_code(raw)

    full_path = os.path.join(OUTPUT_DIR, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(code)

    return code