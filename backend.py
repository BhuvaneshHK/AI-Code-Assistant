from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def review_code(code):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=f"Review this code:\n\n{code}"
    )
    return response.text
