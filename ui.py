import streamlit as st
import subprocess
import os
import webbrowser

st.set_page_config(page_title="AI Developer", layout="wide")

st.title("🤖 Autonomous AI Developer")

idea = st.text_input("Enter your project idea:")

if st.button("Generate Project"):
    if not idea:
        st.error("Please enter an idea")
    else:
        st.info("Running AI pipeline...")

        # run main.py with input
        process = subprocess.Popen(
            ["python", "main.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        stdout, stderr = process.communicate(input=idea)

        st.subheader("📄 Output Logs")
        st.code(stdout if stdout else stderr)

        st.success("Project Generated!")

        if os.path.exists("output/app.py"):
            subprocess.Popen(["python", "output/app.py"])
            webbrowser.open("http://127.0.0.1:5000")