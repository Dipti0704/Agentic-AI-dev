import os
from llm import call_ollama
from config import MODEL_CODER


def clean_code(raw: str) -> str:
    lines = raw.strip().splitlines()
    return "\n".join([l for l in lines if not l.strip().startswith("```")])


def coder_agent(architecture: str, file_path: str, file_desc: str, OUTPUT_DIR: str) -> str:
    prompt = f"""You are a senior full-stack developer.

Write COMPLETE production-level code for ONE file.

File: {file_path}
Purpose: {file_desc}

STRICT REQUIREMENTS:

GENERAL:
- Output ONLY code
- No markdown
- No explanations
- Fully working code (no placeholders)

IF app.py (Flask backend):
- MUST include:
  - Flask app initialization
  - Proper routing
  - "/" route MUST render index.html
  - At least 2-3 functional routes (CRUD or logic)
- Use realistic logic (NOT hello world)

- Add at top:
# ENTRY_POINT: /

IF HTML file:
- Create a MODERN UI:
  - Clean layout
  - Buttons, inputs, sections
  - Use CSS styling (not plain HTML)
  - Use JavaScript (fetch API) to connect backend
- Should look like a real app (not basic text)

IF requirements.txt:
- Include necessary dependencies:
  flask
  flask-cors

UI REQUIREMENTS:
- Must NOT be plain HTML
- Use:
  - colors
  - spacing
  - styled buttons
  - proper structure

IMPORTANT:
- NEVER return "Hello World"
- ALWAYS build a usable application

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