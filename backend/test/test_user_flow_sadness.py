import requests

BASE_URL = "http://127.0.0.1:8000"

payload = {
    "mood": "sadness",
    "voice": "male",
    "background": "rain",
    "answers": "",
    "tokens": []  # Leave empty to trigger GPT script generation
}

response = requests.post(f"{BASE_URL}/generate", json=payload)

print("Status:", response.status_code)
print("Response:", response.json())
