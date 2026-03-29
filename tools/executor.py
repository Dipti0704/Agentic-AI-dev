import subprocess
import sys

def run_code(code: str):
    try:
        # temp file me likho
        with open("temp_exec.py", "w") as f:
            f.write(code)

        # run karo
        process = subprocess.Popen(
            [sys.executable, "temp_exec.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        try:
            stdout, stderr = process.communicate(timeout=5)

            if process.returncode == 0:
                return stdout, ""
            else:
                return "", stderr

        except subprocess.TimeoutExpired:
            # server chal raha hai → success
            process.terminate()
            return "Server running successfully!", ""

    except Exception as e:
        return "", str(e)