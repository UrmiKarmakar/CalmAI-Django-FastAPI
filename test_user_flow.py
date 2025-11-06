import requests

# Define the payload for this test
payload = {
    "mood": "tired",
    "voice": "female",
    "background": "ocean",
    "answers": "",
    "tokens": []
}

# Send the request to your FastAPI backend
try:
    response = requests.post("http://127.0.0.1:8000/generate", json=payload)
    print("Status:", response.status_code)
    print("Response:", response.json())
except Exception as e:
    print(" Request failed:", e)
