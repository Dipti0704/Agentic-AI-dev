import streamlit as st
import subprocess
import webbrowser
from main import run_pipeline

st.set_page_config(page_title="AI Developer", layout="wide")

st.title("🤖 Autonomous AI Developer")

idea = st.text_input("Enter your project idea:")

if st.button("Generate Project"):
    if not idea:
        st.error("Please enter an idea")
    else:
        log_box = st.empty()
        logs = ""

        app_path = None
        entry = "/"

        for step in run_pipeline(idea):
            if isinstance(step, dict):
                app_path = step.get("run_app")
                entry = step.get("entry", "/")
            else:
                logs += str(step) + "\n\n"
                log_box.code(logs)

        st.success("✅ Project Generated!")

        if app_path:
            subprocess.Popen(["python", app_path])
            webbrowser.open(f"http://127.0.0.1:5000{entry}")