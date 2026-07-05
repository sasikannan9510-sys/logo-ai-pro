from google import genai
import os
from datetime import date

# Gemini Client
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

# Read client brief
with open("clients/client.txt", "r", encoding="utf-8") as f:
    client_brief = f.read()

# Create prompt
prompt = f"""
### # Industry

Professional Dog Grooming & Pet Spa

### # Brand Strategy

Calm • Trusted • Professional • Premium • Modern

### # Logo Style

Minimalist monoline dog silhouette with subtle bubbles, clean vector

### # Color Palette

Teal, Soft Blue, Sage Green, Charcoal, White

### # Typography

Modern geometric sans-serif (Avenir, Gotham, Manrope, or Montserrat)

### # Detailed AI Logo Prompt

**Modern minimalist vector logo for "The Dog Spa", elegant monoline dog silhouette with subtle soap bubbles, clean geometric lines, Scandinavian + Swiss design, calm, trustworthy, professional pet grooming brand, premium yet approachable, teal and soft blue palette with charcoal typography, flat vector, balanced composition, negative space, timeless, scalable, white background.**

### # Negative Prompt

**cartoon, mascot, bathtub, paw badge, clipart, cute puppy, realistic dog, 3D, gradient, shadow, neon, vintage, grunge, ornate, handwritten font, cluttered, low quality, watermark, mockup, photo**


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
filename = f"prompts/{today}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved: {filename}")
