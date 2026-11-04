# AI Logo Design Agent Pipeline

This is an additional logo-focused pipeline. It does not replace the existing `generator.py` or the scheduled workflow.

## Agents

1. Brand Analysis Agent — extracts brand strategy and priorities.
2. Logo Concept Agent — proposes three distinct concept directions.
3. Prompt Optimizer Agent — prepares a copy-ready image-generation prompt and negative prompt.
4. Design Review Agent — scores and critiques the prompt, then suggests corrections.

## Setup

Use Python 3.11 or newer and install the dependency:

```bash
python -m pip install -r requirements-logo-agent.txt
```

Set your Gemini key as an environment variable. Never put API keys in source files or commit them to GitHub.

Linux / macOS / Termux:

```bash
export GEMINI_API_KEY="YOUR_KEY"
```

PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_KEY"
```

## Run

Copy `clients/logo_brief.example.txt` to `clients/logo_brief.txt`, fill in the client details, then run:

```bash
python logo_generator.py
```

Optional custom brief and model:

```bash
python logo_generator.py --brief clients/my-client.txt --model gemini-2.5-flash
```

The report is written to `logo_outputs/YYYY-MM-DD-logo-design.md`.

## Notes

- This pipeline generates strategy, concepts, and prompts; it does not itself render an image or produce a verified vector file.
- Keep exact brand spelling and taglines in the brief and check all generated text manually.
- Existing daily prompt generation remains separate and unchanged.
