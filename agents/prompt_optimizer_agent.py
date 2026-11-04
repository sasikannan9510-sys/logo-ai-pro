"""Agent 3: convert the selected direction into image-model prompts."""

from .base import generate_text


class PromptOptimizerAgent:
    def run(self, client, brief: str, strategy: str, concepts: str, model: str) -> str:
        prompt = f"""Act as a senior logo-prompt engineer. Choose the strongest concept based on brand relevance, originality, legibility, and scalability. Produce a production-ready prompt for Midjourney, Ideogram, or GPT Image.
Use this sequence: Client Description -> Brand Meaning -> Visual Concept -> Typography -> Symbol Integration -> Composition -> Production Constraints.
Default to premium minimalist, flat vector logo artwork unless the brief asks otherwise. Preserve exact brand spelling and exact tagline. Include explicit colour values when available. Do not ask the image model to create mockups unless requested.
Return exactly these sections: Selected Direction, Final Logo Prompt, Negative Prompt, and Production Notes. The final prompt must be one clean copy-paste paragraph. Exclude gradients, shadows, 3D, bevels, textures, mockups, stock icons, and extra text unless explicitly requested.

CLIENT BRIEF:
{brief}

BRAND STRATEGY:
{strategy}

CONCEPT DIRECTIONS:
{concepts}
"""
        return generate_text(client, prompt, model)
