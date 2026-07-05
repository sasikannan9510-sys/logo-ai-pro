From google import genai

Import os

From datetime import date



# Gemini Client

Client = genai.Client(

    Api_key=os.environ[“GEMINI_API_KEY”]

)



# Read client brief

With open(“clients/client.txt”, “r”, encoding=”utf-8”) as f:

    Client_brief = f.read()



# Create prompt

Prompt = f”””

It looks like a tool was triggered by mistake here — you don’t actually need an API key setup for your logo brief.

What I *can* do for you is turn your Thermabond brief into a **high-quality AI logo prompt system** (including multiple directions + negative prompts), so you can generate or guide a designer directly.

Below is a **clean, production-ready prompt package** based on your brief:

---

# **THERMABOND – MASTER AI LOGO PROMPT (WORDMARK / COMBINATION MARK)**

## **Core Prompt (Primary Direction)**

Create a premium, minimalist wordmark logo for **“Thermabond”**, a civil infrastructure pavement maintenance technology company operating in Australia.

The logo must communicate:

* Engineering credibility
* Industrial-grade reliability
* Government / council procurement trust level
* High-end infrastructure technology brand positioning
* Fortune 500-level restraint and simplicity

Design direction:

* Clean, precise, modern typographic wordmark or subtle combination mark
* Strong geometric sans-serif typography with custom refinements
* Subtle structural modification to one or two letters (optional but minimal) to create distinctiveness
* Balanced spacing, engineered kerning, high legibility
* No illustrative icon unless fully integrated into typography

The mark must feel:

* Industrial yet premium
* Technical but not mechanical cliché
* Stable, durable, and institutional

Avoid literal construction symbolism. No asphalt, roads, tools, or machinery imagery.

---

## **Optional Symbol Concept Direction (if combination mark is used)**

If a symbol is included, it must be:

* Extremely minimal geometric abstraction
* Derived from concepts of “bonding”, “thermal fusion”, or “material connection”
* Constructed from simple shapes or negative space
* Capable of working independently as a favicon and embroidery mark
* Must not resemble road/construction clichés

---

## **Typography Direction**

* Custom geometric sans-serif or modified grotesk typeface
* Inspired by Swiss / German engineering design systems
* Similar restraint level to:

  * enterprise infrastructure brands
  * industrial SaaS platforms
  * government contractors
* Heavy emphasis on clarity at small sizes (PPE embroidery safe)

---

## **Color Direction**

Primary system (must be optional for logo usability in mono):

* Navy: #1A1A2E (primary institutional tone)
* Amber: #FFC107 (accent only, not dominant)
* Flame Red: #FF5722 (secondary highlight only)

Logo must work perfectly in:

* 1-color navy
* 1-color black
* reversed white
* embroidery-safe flat version

No gradients, shadows, or effects.

---

## **Composition Requirements**

* Must scale from favicon to vehicle decal
* Must remain legible at embroidery size (chest logo / cap size)
* Must survive single-color reproduction on hi-vis fabric
* Must be visually balanced in horizontal lockup format

---

## **Brand Positioning Keywords (for AI weighting)**

Use these to guide style:

* infrastructure-grade
* municipal procurement
* civil engineering trust
* industrial precision
* enterprise minimalism
* engineered typography
* Swiss restraint
* durable systems identity

---

## **NEGATIVE PROMPT (IMPORTANT)**

Do NOT include:

* construction clichés (road cones, asphalt, machinery, tools)
* gradients, bevels, shadows, 3D effects
* overly decorative typography
* script fonts or humanist playful styles
* mascots or illustrative icons
* overly complex geometry
* thin strokes or hairlines
* noisy textures or visual effects
* logo styles resembling startups or consumer apps

---

## **3 DISTINCT LOGO DIRECTIONS (FOR GENERATION VARIANTS)**

### **Direction 1: Institutional Wordmark**

Pure wordmark, custom kerning, subtle letter engineering
Focus: government-level trust, procurement-ready identity

---

### **Direction 2: Engineered Typographic System**

Wordmark with slight structural modification (e.g. T or B)
Focus: engineered precision + subtle differentiation

---

### **Direction 3: Minimal Bond Mark Combination**

Wordmark + abstract geometric “bond” symbol
Focus: scalable icon for equipment, PPE, favicon

---

If you want, I can take this further and:

* generate **actual Midjourney / DALL·E prompts per direction**
* design a **logo grid system + spacing rules**
* or create a **mock “Fortune 500 style” brand sheet for Thermabond**

Just tell me.




Client Brief:



{client_brief}

“””



# Generate response

Response = client.models.generate_content(

    Model=”gemini-2.5-flash”,

    Contents=prompt,

)



# Create prompts folder

Os.makedirs(“prompts”, exist_ok=True)



# Save markdown file

Today = date.today().isoformat()

Filename = f”prompts/{today}.md”



With open(filename, “w”, encoding=”utf-8”) as f:

    f.write(response.text)



print(f”Saved: {filename}”)
















