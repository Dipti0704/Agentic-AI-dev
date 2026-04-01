from llm import call_ollama
from config import MODEL_PLANNER

def planner_agent(user_input):
    prompt = f"""You are a senior software engineer planning a coding project.

Given the project idea below, output ONLY a numbered list of concrete technical tasks.

Rules:
- Each task must be a specific coding action
- Do NOT give explanations
- Do NOT use bullet points
- Output ONLY numbered list
- Include frontend, backend, and UI tasks
- Ensure app is fully usable

Project Idea: {user_input}

Example:
1. Create Flask app in app.py
2. Add SQLite database connection
3. Implement GET /todos route
4. Implement POST /todos route

"""

    return call_ollama(prompt, MODEL_PLANNER)