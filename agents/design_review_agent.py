"""Agent 4: critique the generated prompt before delivery."""

from .base import generate_text


class DesignReviewAgent:
    def run(self, client, brief: str, prompt_package: str, model: str) -> str:
        prompt = f"""Act as a strict senior identity-design reviewer. Evaluate the proposed logo prompt against the client brief.
Score each from 1-10: Brand Relevance, Originality, Readability, Scalability, Distinctiveness, and Production Clarity. Identify contradictions, spelling/tagline risks, vague instructions, and unnecessary visual effects. Then provide a corrected final prompt and negative prompt. Do not claim that an AI-generated raster image is a production-ready vector file.

CLIENT BRIEF:
{brief}

PROMPT PACKAGE:
{prompt_package}
"""
        return generate_text(client, prompt, model)
