from llm import call_ollama
from config import MODEL_PLANNER

def run():
    print("🤖 AI Developer System Started")

    idea = input("Enter your project idea: ")

    if not idea.strip():
        print("❌ Empty input")
        return

    print("\n🧠 Sending idea to LLM...\n")

    response = call_ollama(
        prompt=f"Break this idea into steps:\n{idea}",
        model=MODEL_PLANNER
    )

    if not response:
        print("❌ No response from LLM")
        return

    print("✅ LLM Response:\n")
    print(response)

if __name__ == "__main__":
    run()