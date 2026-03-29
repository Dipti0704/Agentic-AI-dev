from llm import call_ollama
from config import MODEL_CODER
import os

def clean_code(raw: str) -> str:
    lines = raw.strip().splitlines()
    cleaned = [l for l in lines if not l.strip().startswith("```")]
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
    os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else ".", exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

    return code