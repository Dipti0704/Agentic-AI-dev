from agents.planner import planner_agent
from agents.architect import architect_agent
from agents.coder import coder_agent
from tools.executor import run_code
from agents.debugger import debug_agent
from config import MAX_DEBUG_TRIES
import json
import os


# ✅ create unique output folder
def create_output_folder():
    base = "output"
    if not os.path.exists(base):
        os.makedirs(base)
        return base

    i = 1
    while True:
        new_path = f"{base}_{i}"
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            return new_path
        i += 1


def clean_json(raw: str) -> str:
    lines = raw.strip().splitlines()
    return "\n".join([l for l in lines if not l.strip().startswith("```")])


def run_pipeline(idea):
    # ✅ always create new folder
    OUTPUT_DIR = create_output_folder()

    yield f"📁 Output folder created: {OUTPUT_DIR}"

    yield "🤖 AI Developer Started..."

    if not idea.strip():
        yield "❌ Empty input"
        return

    # ── Planning ─────────────────────
    yield "🧠 Planning..."
    tasks = planner_agent(idea)

    if not tasks:
        yield "❌ Planner failed"
        return

    yield f"📋 Tasks:\n{tasks}"

    # ── Architecture ────────────────
    yield "🏗️ Designing architecture..."
    architecture_raw = architect_agent(tasks)

    yield f"📐 Architecture:\n{architecture_raw}"

    try:
        architecture = json.loads(clean_json(architecture_raw))
        files = architecture["files"]
    except Exception as e:
        yield f"❌ JSON Parse Failed: {e}"
        return

    # ── Code Generation ─────────────
    yield "💻 Generating code..."
    generated_files = []

    for file in files:
        path = file["path"]
        desc = file["description"]

        yield f"🔨 Generating {path}..."

        code = coder_agent(architecture_raw, path, desc, OUTPUT_DIR)
        generated_files.append(os.path.join(OUTPUT_DIR, path))

    # ── Find main app ───────────────
    main_file_path = os.path.join(OUTPUT_DIR, "app.py")

    if not os.path.exists(main_file_path):
        yield "❌ app.py not found in output folder"
        return

    yield f"✅ Main file found: {main_file_path}"

    # ── Execution + Debug ───────────
    yield "▶️ Running generated app..."

    with open(main_file_path, "r") as f:
        current_code = f.read()

    for i in range(MAX_DEBUG_TRIES):
        yield f"▶️ Run Attempt {i+1}"

        output, error = run_code(current_code)

        if not error:
            yield f"✅ Success:\n{output}"
            yield "🎉 Project Generated Successfully!"

            # return folder path also
            yield {"run_app": main_file_path}
            return

        yield f"❌ Error:\n{error}"

        if i == MAX_DEBUG_TRIES - 1:
            yield "🚨 Max retries reached"
            return

        yield "🔧 Debugging..."

        fixed_code = debug_agent(error, current_code)

        if not fixed_code:
            yield "❌ Debugger failed"
            return

        current_code = fixed_code

        with open(main_file_path, "w") as f:
            f.write(current_code)