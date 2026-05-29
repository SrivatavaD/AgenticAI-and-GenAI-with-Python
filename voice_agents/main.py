import os
import subprocess

from dotenv import load_dotenv
from google import genai
from google.genai import types
import speech_recognition as sr

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


def build_conversation(messages: list[dict[str, str]]) -> str:
    lines = []
    for message in messages:
        role = "User" if message["role"] == "user" else "Assistant"
        lines.append(f"{role}: {message['content']}")
    return "\n".join(lines)


def main():
    r = sr.Recognizer() # Speech to Text

    with sr.Microphone() as source: # Mic Access
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        SYSTEM_PROMPT = """
                You're an expert voice agent. You are given the transcript of what
                user has said using voice.
                You need to output as if you are a voice agent and whatever you speak
                will be converted back to audio and played back to user.
            """

        messages = []

        while True:
            try:
                stt = listen_for_speech(r, source)
                if not stt:
                    continue

                print("You Said:", stt)

                messages.append({ "role": "user", "content": stt })

                response = client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=build_conversation(messages),
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT
                    ),
                )

                ai_response = response.text or ""
                messages.append({ "role": "assistant", "content": ai_response })

                print("AI Response", ai_response)
                speak(ai_response)
            except Exception as exc:
                print(f"Gemini error: {exc}")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break


if __name__ == "__main__":
    main()
