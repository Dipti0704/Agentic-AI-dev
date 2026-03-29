import requests
import time
from config import OLLAMA_URL, OLLAMA_TIMEOUT, OLLAMA_RETRIES, TEMPERATURE, MAX_TOKENS, TOP_P

def call_ollama(prompt: str, model: str = "llama3") -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "num_predict": MAX_TOKENS,
        }
    }

    for attempt in range(1, OLLAMA_RETRIES + 1):
        try:
            print(f"Calling {model} (attempt {attempt})...")

            response = requests.post(
                OLLAMA_URL,
                json=payload,
                timeout=OLLAMA_TIMEOUT
            )

            if response.status_code != 200:
                raise Exception(f"HTTP {response.status_code}")

            data = response.json()

            if "response" not in data:
                raise Exception("Invalid response format")

            result = data["response"].strip()

            if not result:
                raise Exception("Empty response")

            return result

        except Exception as e:
            print(f"Error: {e}")
            if attempt < OLLAMA_RETRIES:
                time.sleep(2)

    return ""