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
You are a Senior UI/UX Designer and Creative Director specializing in premium website design.

Read the following client brief and generate a comprehensive professional Homepage Design Prompt.

The output must be structured exactly using the headings below.

# Company Name

# Industry

# Website Purpose

# Target Audience

# Brand Personality

# Design Direction

# Visual Identity

# Color Palette

# Typography

# Layout Structure

Include:
- Header / Navigation
- Hero Section
- Feature Sections
- Content Sections
- Call-to-Action
- Footer

# Grid System

# Spacing System

# Components

Include recommendations for:
- Buttons
- Cards
- Forms
- Icons
- Dividers

# Imagery Style

Describe the recommended illustration, photography, or abstract visual style.

# Interaction & Animation

Describe subtle hover effects, transitions, and micro-interactions.

# Mobile Responsive Design

Explain how the desktop layout should adapt to mobile.

# Design System

Include:
- Typography Scale
- Color Tokens
- Spacing Scale
- Border Radius
- Shadows
- Component Variants

# Detailed AI Homepage Design Prompt

Write one extremely detailed AI prompt suitable for generating a premium homepage design in tools such as Midjourney, GPT Image, Flux, Ideogram, or other AI design models.

The prompt should emphasize:

- Architectural
- Modern
- Premium
- Enterprise
- Typography-driven
- Swiss Grid
- Editorial Layout
- Large White Space
- Timeless Design
- Professional UI
- Pixel-perfect Layout
- Responsive Design
- Minimal Visual Language
- Clean Information Hierarchy

# Negative Prompt

Include everything that should be avoided, including:

- Generic SaaS landing pages
- AI robots
- Cryptocurrency style
- Neon gradients
- Marketing agency layouts
- Dashboard-heavy interfaces
- Excessive glassmorphism
- Busy backgrounds
- Stock AI imagery
- Cartoon illustrations
- Low-quality typography
- Visual clutter

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
