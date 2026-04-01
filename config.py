# ── Model Configuration ────────────────────────────────────────────
MODEL_PLANNER   = "llama3"
MODEL_ARCHITECT = "llama3"
MODEL_CODER     = "llama3"
MODEL_DEBUGGER  = "llama3"

# ── Ollama Settings ────────────────────────────────────────────────
OLLAMA_URL      = "http://localhost:11434/api/generate"
OLLAMA_TIMEOUT  = 180
OLLAMA_RETRIES  = 3

# ── Generation Settings ────────────────────────────────────────────
TEMPERATURE     = 0.2
MAX_TOKENS      = 2048
TOP_P           = 0.9

# ── Executor Settings ──────────────────────────────────────────────
RUN_TIMEOUT     = 15
MAX_DEBUG_TRIES = 3

# ── Project Settings ───────────────────────────────────────────────
OUTPUT_DIR      = "."
MAIN_FILE       = "output/app.py"

