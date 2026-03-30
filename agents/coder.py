from llm import call_ollama
from config import MODEL_CODER
import os
from config import OUTPUT_DIR

def clean_code(raw: str) -> str:
    lines = raw.strip().splitlines()

    cleaned = []
    started = False

    for line in lines:
        line_strip = line.strip()

        # skip markdown
        if line_strip.startswith("```"):
            continue

        # skip file labels like "app.py:"
        if line_strip.endswith(".py:") or line_strip.endswith(".js:"):
            continue

        # detect start of real code
        if not started:
            if line_strip.startswith((
                "import", "from", "#!", "#",
                "class", "def", "@",
                "<!DOCTYPE", "<html"
            )):
                started = True

        if started:
            cleaned.append(line)

    return "\n".join(cleaned)


def coder_agent(architecture: str, file_path: str, file_desc: str) -> str:
    prompt = f"""You are an expert developer.

Write COMPLETE code for ONE file.

File: {file_path}
Purpose: {file_desc}

Full architecture:
{architecture}

Rules:
- Output ONLY code
- No markdown
- No explanations
- No ``` 
- If Python → include full working code
- If HTML → full HTML with JS
- If requirements.txt → only package names

Start directly with code.
"""

    raw = call_ollama(prompt, MODEL_CODER)

    if not raw:
        return ""

    code = clean_code(raw)

    # Save file
    full_path = os.path.join(OUTPUT_DIR, file_path)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(code)

    return code