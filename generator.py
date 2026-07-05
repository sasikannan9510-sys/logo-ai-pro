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
# Modern Grooming Salon Logo Design Brief

## Company Name

**The Dog Spa**

---

## Industry

**Professional Pet Grooming Salon / Dog Grooming & Wellness**

---

## Brand Strategy

The Dog Spa should position itself as a **modern, trusted, professional grooming salon** that offers premium-quality care without feeling overly luxurious or intimidating.

The identity should communicate:

* Trust
* Professionalism
* Calmness
* Cleanliness
* Compassion
* High-quality grooming
* Stress-free experience for dogs and owners

The brand should sit between:

* Boutique luxury grooming (too expensive/elitist ❌)
* Big-box chain grooming (generic/corporate ❌)

Instead, it should feel like:

> **"Your neighborhood premium grooming salon."**

---

# Logo Style

**Style Direction**

Modern Minimalist

Professional

Flat Vector

Scalable

Timeless

Elegant

Swiss-inspired simplicity

Balanced geometric composition

Negative space

Monoline illustration

Simple enough to embroider

Instantly recognizable

No unnecessary detail

---

## Icon Concept

Create an iconic symbol using:

* elegant dog outline
* continuous single-line drawing
* refined dog silhouette
* subtle soap bubbles
* negative space

Possible concepts:

### Concept A (Recommended)

Elegant side profile of a calm dog

2–3 floating bubbles

Smooth continuous line

Modern circular composition

---

### Concept B

Dog head inside a soft circular bubble

Minimal outlines

Balanced spacing

---

### Concept C

Dog silhouette forming part of a bubble

Negative space used creatively

Modern geometric appearance

---

Avoid:

* Bathtub
* Paw inside house
* Bones
* Cartoon dogs
* Cute puppy faces
* Grooming scissors
* Busy illustrations

The logo should feel like a premium service brand rather than a pet store.

---

# Color Palette

Primary

Soft Teal
**#5FAFA6**

Cool Blue
**#7CBBC4**

Muted Sage
**#A8C8B8**

Warm Gray
**#6F767D**

Off White
**#F7F8F7**

---

Accent

Deep Teal
**#2F6F73**

Charcoal
**#2C3439**

---

Color Psychology

Teal → cleanliness

Blue → trust

Green → calm

Gray → professionalism

White → hygiene

---

# Typography

Primary Typeface

Avenir Next

or

Montserrat

or

Manrope

or

Satoshi

or

General Sans

---

Style

Modern Sans Serif

Medium weight

Excellent readability

Balanced spacing

Minimal

Premium

Professional

Not playful

Not handwritten

Not script

---

Hierarchy

THE DOG

larger

SPA

slightly lighter weight

Well-kerned

Perfect horizontal alignment

---

# Detailed AI Logo Prompt

**Create a premium, modern minimalist vector logo for "The Dog Spa," a professional dog grooming salon. Design a refined continuous single-line outline of a calm dog profile combined with 2–3 subtle floating soap bubbles using elegant negative space. The icon should immediately communicate dog grooming while remaining sophisticated, clean, and timeless. Avoid cartoon styling and excessive detail. Use balanced geometric proportions inspired by Swiss graphic design principles, with crisp monoline strokes and excellent visual harmony. Pair the icon with a modern geometric sans-serif wordmark reading "The Dog Spa," using excellent kerning and balanced typography. Apply a calming color palette of soft teal (#5FAFA6), muted sage (#A8C8B8), cool blue (#7CBBC4), warm gray (#6F767D), and off-white (#F7F8F7). The design should be flat vector artwork with no gradients, fully scalable for storefront signage, embroidery, uniforms, packaging, business cards, vehicles, websites, and social media. Include full-color, one-color, black, white, and reversed variations. The overall feeling should communicate trust, professionalism, cleanliness, calmness, premium service, and a stress-free grooming experience without appearing overly luxurious or corporate. The logo should be iconic, memorable, award-winning, and timeless.**

---

# Negative Prompt

**cartoon, mascot logo, puppy eyes, smiling dog, realistic dog, furry texture, bathtub, shower, shampoo bottle, scissors, comb, bone, paw print, pet store aesthetic, veterinary symbols, clipart, childish, playful, kawaii, gradients, bevel, glossy effects, 3D rendering, shadows, metallic textures, neon colors, bright saturated colors, rainbow palette, vintage badge, ornate decoration, distressed texture, watercolor, sketch, low quality, pixelated, busy composition, cluttered layout, poor typography, decorative fonts, handwritten fonts, serif fonts, script fonts, stretched proportions, asymmetrical layout, AI artifacts, stock logo appearance, generic branding, unnecessary details, complex linework, background elements, mockups, photographic style.**


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
