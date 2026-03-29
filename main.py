from agents.planner import planner_agent
from agents.architect import architect_agent
from agents.coder import coder_agent
from tools.executor import run_code
from config import MAIN_FILE
import json


def run():
    print("🤖 AI Developer System Started")

    idea = input("Enter your project idea: ")

    if not idea.strip():
        print("❌ Empty input")
        return

    print("\n🧠 Planning...\n")

    tasks = planner_agent(idea)

    if not tasks:
        print("❌ Planner failed")
        return

    print("✅ Tasks:\n")
    print(tasks)

# Step 2: Architecture
    print("\n🏗️ Designing...\n")
    architecture_raw = architect_agent(tasks)
    print(architecture_raw)

    try:
        architecture = json.loads(architecture_raw)
        files = architecture["files"]
    except:
        print("❌ Invalid JSON from architect")
        return

    # Step 3: Code generation
    print("\n💻 Coding...\n")
    all_code ={}

    for file in files:
        path = file["path"]
        desc = file["description"]

        print(f"Generating {path}...")
        code = coder_agent(architecture_raw, path, desc)
        all_code[path] = code

    # Step 4: Execution
    print("\n▶️ Running generated code...\n")

    if MAIN_FILE not in all_code:
        print(f"❌ {MAIN_FILE} not found")
        return

    output, error = run_code(all_code[MAIN_FILE])

    if error:
        print("❌ Error:\n", error)
    else:
        print("✅ Success:\n", output)

if __name__ == "__main__":
    run()