from google import genai
import os
from datetime import date

# Gemini Client
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

# Read client brief
with open("clients/thermabond.txt", "r", encoding="utf-8") as f:
    client_brief = f.read()

# Create prompt
prompt = f"""
You are a senior brand identity designer.

Read the following client brief and generate a professional logo design prompt.

Include:

# Company Name
# Industry
# Brand Strategy
# Logo Style
# Color Palette
# Typography
# Detailed AI Logo Prompt
# Negative Prompt

Client Brief:

{client_brief}
"""

# Generate response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

# Create prompts folder
os.makedirs("prompts", exist_ok=True)

# Save markdown file
today = date.today().isoformat()
filename = f"prompts/{today}_thermabond.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved: {filename}")
