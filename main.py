from agents.planner import planner_agent
from agents.architect import architect_agent
from agents.coder import coder_agent
from tools.executor import run_code
from config import MAIN_FILE
from agents.debugger import debug_agent
from config import MAX_DEBUG_TRIES
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

    
    # Step 4: Execution + Debug loop
    print("\n▶️ Running generated code...\n")

    if MAIN_FILE not in all_code:
        print(f"❌ {MAIN_FILE} not found")
        return

    current_code = all_code[MAIN_FILE]

    for i in range(MAX_DEBUG_TRIES):
        print(f"\n▶️ Run Attempt {i+1}/{MAX_DEBUG_TRIES}")

        output, error = run_code(current_code)

        if not error:
            print("✅ Success:\n", output)
            break

        print("❌ Error:\n", error)

        if i == MAX_DEBUG_TRIES - 1:
            print("🚨 Max retries reached. Fix manually.")
            break

        print("🔧 Debugging...")

        fixed_code = debug_agent(error, current_code)

        if not fixed_code:
            print("❌ Debugger failed")
            break

        current_code = fixed_code

        with open(MAIN_FILE, "w") as f:
            f.write(current_code)
            
if __name__ == "__main__":
    run()