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
Detailed AI Logo Prompt
Create an award-winning premium minimalist vector logo for "The Dog Spa", a modern professional dog grooming salon. Design an elegant continuous single-line monoline illustration of a calm dog profile facing right with smooth flowing curves, refined proportions, and a relaxed closed eye expressing trust, comfort, and relaxation. Integrate two or three subtle soap bubbles using negative space so the grooming service is instantly recognizable without using bathtubs or grooming tools. Use Scandinavian and Swiss-inspired design principles with geometric balance, generous white space, clean symmetry, and timeless simplicity. Apply a calming color palette featuring Soft Teal (#4FAFB0), Deep Charcoal (#2C3439), and white. Position a bold uppercase geometric sans-serif wordmark reading "THE DOG SPA" beneath the icon with balanced spacing and premium typography. Produce flat vector artwork with crisp line weights, optimized for storefront signage, embroidery, uniforms, vehicle graphics, packaging, social media, business cards, letterheads, and website branding. The logo should feel professional, trustworthy, hygienic, approachable, memorable, and scalable while maintaining a refined, luxury aesthetic without appearing exclusive or overly boutique.

Negative Prompt
cartoon, mascot, puppy illustration, realistic dog, watercolor, sketch texture, clipart, paw print, bone, bathtub, shampoo bottle, scissors, hair dryer, comb, ribbon, crown, heart, kennel, dog house, excessive bubbles, playful style, vintage badge, ornamental details, gradients, shadows, bevel, emboss, glossy effects, neon colors, busy composition, handwritten fonts, script fonts, serif fonts, distressed textures, 3D rendering, mockup, photography, low resolution, pixelated, cluttered layout

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
