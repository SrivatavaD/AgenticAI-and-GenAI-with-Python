from google import genai

client = genai.Client(
    api_key="AIzaSyA-Tink_sOkmwU7zO304tKRAGpBnzonT7Y"
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="how are you?",
)

print(response.text)