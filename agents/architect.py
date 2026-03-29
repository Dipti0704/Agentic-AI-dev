from llm import call_ollama
from config import MODEL_ARCHITECT

def architect_agent(tasks: str) -> str:
    prompt = f"""You are a software architect.

Given the tasks below, output ONLY a valid JSON describing the project structure.

Rules:
- Output ONLY JSON (no explanation, no markdown)
- Each file must have "path" and "description"
- Keep it simple (3-5 files)
- Use Flask for backend
- Include requirements.txt
- Main file must be app.py

Tasks:
{tasks}

Output format:
{{
  "project_name": "todo_app",
  "files": [
    {{
      "path": "app.py",
      "description": "Flask server with API routes"
    }},
    {{
      "path": "templates/index.html",
      "description": "Frontend UI with fetch calls"
    }},
    {{
      "path": "requirements.txt",
      "description": "Dependencies"
    }}
  ]
}}
"""

    return call_ollama(prompt, MODEL_ARCHITECT)