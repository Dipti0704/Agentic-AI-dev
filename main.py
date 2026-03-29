from agents.planner import planner_agent
from agents.architect import architect_agent


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
    architecture = architect_agent(tasks)

    if not architecture:
        print("❌ Architect failed")
        return

    print("✅ Architecture:\n")
    print(architecture)

if __name__ == "__main__":
    run()