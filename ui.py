import streamlit as st
import subprocess
import webbrowser
from main import run_pipeline

st.title("🤖 AI Developer")

idea = st.text_input("Enter your idea:")

if st.button("Generate"):
    logs_box = st.empty()
    logs = ""

    app_path = None

    for step in run_pipeline(idea):
        if isinstance(step, dict) and "run_app" in step:
            app_path = step["run_app"]
        else:
            logs += str(step) + "\n\n"
            logs_box.code(logs)

    st.success("✅ Done!")

    if app_path:
        subprocess.Popen(["python", app_path])
        webbrowser.open("http://127.0.0.1:5000")