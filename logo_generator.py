"""CLI entry point for the AI logo-design agent pipeline."""

import argparse
from pathlib import Path
from datetime import date

from agents.pipeline import LogoDesignPipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a professional logo prompt package.")
    parser.add_argument("--brief", default="clients/logo_brief.txt", help="Path to the client brief text file.")
    parser.add_argument("--model", default="gemini-2.5-flash", help="Gemini model name.")
    args = parser.parse_args()

    brief_path = Path(args.brief)
    if not brief_path.is_file():
        raise SystemExit(f"Brief file not found: {brief_path}. Create it or pass --brief PATH.")

    brief = brief_path.read_text(encoding="utf-8")
    results = LogoDesignPipeline(model=args.model).run(brief)
    output_dir = Path("logo_outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{date.today().isoformat()}-logo-design.md"

    sections = [
        "# AI Logo Design Agent Output",
        f"\n**Model:** {args.model}",
        f"\n## 1. Brand Analysis\n\n{results['brand_analysis']}",
        f"\n## 2. Logo Concepts\n\n{results['logo_concepts']}",
        f"\n## 3. Optimized Prompt Package\n\n{results['optimized_prompt']}",
        f"\n## 4. Design Review\n\n{results['design_review']}",
    ]
    output_path.write_text("\n".join(sections) + "\n", encoding="utf-8")
    print(f"Saved logo design output: {output_path}")


if __name__ == "__main__":
    main()
