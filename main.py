from agents.planner import planner_agent
from agents.architect import architect_agent
from agents.coder import coder_agent
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

    for file in files:
        path = file["path"]
        desc = file["description"]

        print(f"Generating {path}...")
        coder_agent(architecture_raw, path, desc)

    print("\n✅ Project Generated Successfully!")

if __name__ == "__main__":
    run()