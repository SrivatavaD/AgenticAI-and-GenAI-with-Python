# Voice assistant with structured tool use
import json
import os
import subprocess
from typing import Literal, Optional, TypedDict

from dotenv import load_dotenv
from google import genai
from google.genai import types
import requests
import speech_recognition as sr
from pydantic import BaseModel, Field

load_dotenv()

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)


def speak(speech: str):
    if not speech:
        return

    try:
        subprocess.run(["say", speech], check=False)
    except FileNotFoundError:
        print("Speech playback is unavailable on this system.")


def listen_for_speech(recognizer: sr.Recognizer, source: sr.Microphone) -> str | None:
    print("Speak Something...")
    audio = recognizer.listen(source)

    print("Processing Audio... (STT)")
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand the audio. Please try again.")
    except sr.RequestError as exc:
        print(f"Speech recognition service failed: {exc}")

    return None


def get_weather(city: str):
    city = city.strip()
    if not city:
        return "Please provide a city name."

    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as exc:
        return f"Weather service failed: {exc}"

    if response.status_code == 200:
        return f"The weather in {city} is {response.text.strip()}"
    
    return "Something went wrong"


available_tools = {
    "get_weather": get_weather,
}


SYSTEM_PROMPT = """
    You're a helpful voice assistant. The user's speech has been converted to text.
    Respond with one JSON object at a time using the requested schema.
    Use TOOL only when you need live weather information. After a tool result is
    provided in an OBSERVE message, produce the final OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - Keep PLAN content brief. Do not reveal hidden chain-of-thought.
    - The final OUTPUT is spoken aloud to the user.

    Output JSON Format:
    { "step": "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string" }

    Available Tools:
    - get_weather(city: str): Takes city name as an input string and returns the weather info about the city.
    
    Example:
    User: What is the weather of Delhi?
    Assistant: { "step": "TOOL", "tool": "get_weather", "input": "Delhi" }
    User: OBSERVE: {"tool": "get_weather", "input": "Delhi", "output": "The weather in Delhi is Clear +32 C"}
    Assistant: { "step": "OUTPUT", "content": "The current weather in Delhi is clear and 32 degrees Celsius." }
    
"""

class MyOutputFormat(BaseModel):
    step: Literal["PLAN", "OUTPUT", "TOOL"] = Field(..., description="The ID of the step.")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call.")
    input: Optional[str] = Field(None, description="The input params for the tool")


class GeminiOutputFormat(TypedDict, total=False):
    step: Literal["PLAN", "OUTPUT", "TOOL"]
    content: str
    tool: str
    input: str


message_history = []


def build_conversation(messages: list[dict[str, str]]) -> str:
    lines = []
    for message in messages:
        role = "Assistant" if message["role"] == "model" else "User"
        lines.append(f"{role}: {message['content']}")
    return "\n".join(lines)


def ask_gemini_for_step() -> MyOutputFormat:
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=build_conversation(message_history),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            response_schema=GeminiOutputFormat,
        ),
    )

    raw_result = response.text or "{}"
    message_history.append({"role": "model", "content": raw_result})
    return MyOutputFormat(**json.loads(raw_result))


def main():
    r = sr.Recognizer() # Speech to Text

    with sr.Microphone() as source: # Mic Access
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        while True:
            try:
                user_query = listen_for_speech(r, source)
                if not user_query:
                    continue

                message_history.append({ "role": "user", "content": user_query })

                while True:
                    parsed_result = ask_gemini_for_step()

                    if parsed_result.step == "TOOL":
                        tool_to_call = parsed_result.tool
                        tool_input = parsed_result.input or ""

                        if tool_to_call not in available_tools:
                            tool_response = f"Tool not available: {tool_to_call}"
                        else:
                            print(f"Tool: {tool_to_call} ({tool_input})")
                            tool_response = available_tools[tool_to_call](tool_input)

                        print(f"Tool result: {tool_response}")
                        message_history.append({ "role": "user", "content": "OBSERVE: " + json.dumps(
                            { "tool": tool_to_call, "input": tool_input, "output": tool_response}
                        ) })
                        continue

                    if parsed_result.step == "PLAN":
                        print("Plan:", parsed_result.content)
                        continue

                    if parsed_result.step == "OUTPUT":
                        output = parsed_result.content or ""
                        print("AI:", output)
                        speak(output)
                        break
            except (json.JSONDecodeError, ValueError) as exc:
                print(f"Could not parse Gemini response: {exc}")
            except Exception as exc:
                print(f"Gemini error: {exc}")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()
