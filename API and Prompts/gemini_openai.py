from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyA-Tink_sOkmwU7zO304tKRAGpBnzonT7Y",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        },
        {
            "role": "system", "content": "You are ab expert in maths and only answer in the form of mathematical equations. that is the query is not related to maths then just say sorry and do not ans that."
        },
        {"role":"user", "content": "how can you help me solve the a+b whole square?"}
    ]

    
)

print(response.choices[0].message)