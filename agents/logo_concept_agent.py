"""Agent 2: develop distinct logo concept territories."""

from .base import generate_text


class LogoConceptAgent:
    def run(self, client, brief: str, strategy: str, model: str) -> str:
        prompt = f"""Act as an award-winning identity designer. Create exactly 3 meaningfully different logo concept directions from the brief and strategy.
For each direction include: Concept Name, Brand Meaning, Symbol Idea, Typography Direction, Composition, Suggested Palette, Why It Fits, and Practical Risks.
Avoid generic clip-art, predictable industry clichés, unnecessary detail, and concepts that are merely colour variations. Preserve the exact brand name and any supplied tagline.

CLIENT BRIEF:
{brief}

BRAND STRATEGY:
{strategy}
"""
        return generate_text(client, prompt, model)
