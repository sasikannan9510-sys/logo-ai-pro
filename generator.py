from google import genai
import os

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

prompt = """
Act as a senior logo designer.

Generate 10 modern logo design prompts.

For each prompt include:
- Company name
- Industry
- Style
- Color palette
- Typography
- Detailed AI image prompt
- Negative prompt
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)
