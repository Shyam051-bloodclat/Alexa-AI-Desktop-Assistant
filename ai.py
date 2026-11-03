from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_ai(prompt):

    try:

        response = client.models.generate_content(

            model="gemini-3.6-flash",

            contents=f"""
You are an AI laptop assistant.

Rules:

- Keep answers under 40 words.
- Never ask unnecessary follow-up questions.
- Be friendly.
- Answer directly.

User:
{prompt}
"""
        )

        print("Gemini:", response.text)

        if response.text:
            return response.text

        return "I couldn't generate a response."

    except Exception as e:

        print(e)

        return "Sorry, I couldn't connect to Gemini."