from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="AIの仕組みを一言で説明して",
)
print(response.text)