
from openai import OpenAI
from dotenv import load_dotenv
import os
import sys
import requests

load_dotenv()

# Read Gemini API key and endpoint from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL = os.getenv(
    "GEMINI_BASE_URL",
    "https://generativelanguage.googleapis.com/v1beta/openai/",
)
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

if not GEMINI_API_KEY:
    sys.stderr.write("ERROR: Set GEMINI_API_KEY in your .env file or environment before running.\n")
    sys.exit(1)

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL,
)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"


def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model=GEMINI_MODEL,
        messages=[
            { "role": "user", "content": user_query }
        ]
    )
    print(f"🤖: {response.choices[0].message.content}")

main()