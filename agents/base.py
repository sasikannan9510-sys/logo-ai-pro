"""Shared Gemini client helpers."""

import os
from google import genai


def create_client() -> genai.Client:
    """Create a Gemini client from GEMINI_API_KEY."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set. Add it to your environment; do not hard-code it.")
    return genai.Client(api_key=api_key)


def generate_text(client: genai.Client, prompt: str, model: str) -> str:
    """Run one text-generation step and validate the response."""
    response = client.models.generate_content(model=model, contents=prompt)
    text = (response.text or "").strip()
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text
