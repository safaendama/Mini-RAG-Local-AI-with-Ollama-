import requests
import sys

# Configure UTF-8 output for Windows
sys.stdout.reconfigure(encoding="utf-8")

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen3:4b",
    "prompt": "Explain recursion in Python.",
    "stream": False
}

response = requests.post(url, json=data)
response.raise_for_status()

result = response.json()

print(result["response"])
