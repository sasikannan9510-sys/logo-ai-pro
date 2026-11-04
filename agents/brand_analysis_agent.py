"""Agent 1: extract brand strategy from a client brief."""

from .base import generate_text


class BrandAnalysisAgent:
    def run(self, client, brief: str, model: str) -> str:
        prompt = f"""Act as a senior brand strategist specializing in professional logo identity.
Analyze the client brief. Do not invent facts. Clearly distinguish supplied facts from reasonable creative recommendations.
Return concise sections for: Brand Summary, Industry, Target Audience, Brand Values, Desired Personality, Differentiation, Visual Opportunities, Risks and Clichés to Avoid, and 3 Core Design Priorities.

CLIENT BRIEF:
{brief}
"""
        return generate_text(client, prompt, model)
