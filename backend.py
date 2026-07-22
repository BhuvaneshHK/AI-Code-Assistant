from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

# Function which sends the input and prompt to Gemini and returns the output
def review_code(code):
    prompt = f"""
You are an expert code reviewer. Review the following code and structure your feedback into these sections:

1. Bugs — any errors, incorrect behavior, logical loopholes
2. Readability — naming, formatting, clarity
3. Performance — inefficiencies, mention performance time and ways to decrease it
4. Best Practices — style, conventions, structure

Code to review:
{code}
"""
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred while contacting Gemini: {e}"
