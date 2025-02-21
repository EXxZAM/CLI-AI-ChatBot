import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
    },
    json={
        "model": "deepseek/deepseek-chat:free",
        "messages": [{"role": "user", "content": "say who you are but keep it short."}],
    },
)

data = response.json()

print(data["choices"][0]["message"]["content"])
