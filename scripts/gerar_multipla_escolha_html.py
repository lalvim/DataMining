"""Converte a lista Markdown padronizada em formulário HTML sem respostas."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

QUESTION_RE = re.compile(r"^(\d+)\. \*\*([A-Z]\d{2}-M\d{2})\.\*\* (.+)$")
OPTION_RE = re.compile(r"^\s+([A-D])\.\s+(.+?)(?:\s{2})?$")


def parse_questions(source: str) -> list[dict[str, object]]:
    """Extrai questões e alternativas do Markdown adotado pelo projeto."""
    questions: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    for line in source.splitlines():
        question_match = QUESTION_RE.match(line)
        if question_match:
            current = {
                "number": int(question_match.group(1)),
                "id": question_match.group(2),
                "prompt": question_match.group(3),
                "options": [],
            }
            questions.append(current)
            continue
        option_match = OPTION_RE.match(line)
        if option_match and current is not None:
            options = current["options"]
            assert isinstance(options, list)
            options.append((option_match.group(1), option_match.group(2)))
    if not questions:
        raise ValueError("Nenhuma questão padronizada foi encontrada.")
    for question in questions:
        if len(question["options"]) != 4:
            raise ValueError(f"{question['id']} não possui quatro alternativas.")
    return questions


def render_html(title: str, questions: list[dict[str, object]]) -> str:
    """Gera HTML5 sem script, resposta ou transmissão de dados."""
    fields: list[str] = []
    for question in questions:
        question_id = str(question["id"])
        options_html = []
        for letter, text in question["options"]:
            input_id = f"{question_id}-{letter}"
            options_html.append(
                f'''        <div class="option">
          <input type="radio" id="{input_id}" name="{question_id}" value="{letter}">
          <label for="{input_id}"><strong>{letter}.</strong> {html.escape(text)}</label>
        </div>'''
            )
        fields.append(
            f'''    <fieldset id="{question_id}">
      <legend><span class="question-id">{question_id}</span> — {html.escape(str(question["prompt"]))}</legend>
{chr(10).join(options_html)}
    </fieldset>'''
        )
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{ color-scheme: light; font-family: system-ui, sans-serif; line-height: 1.5; }}
    body {{ max-width: 900px; margin: 0 auto; padding: 2rem 1rem 4rem; color: #172033; background: #fff; }}
    h1 {{ line-height: 1.2; }}
    .instructions {{ padding: 1rem; border-left: .35rem solid #0369a1; background: #f0f9ff; }}
    fieldset {{ margin: 1.5rem 0; padding: 1rem; border: 1px solid #94a3b8; border-radius: .5rem; }}
    legend {{ padding: 0 .4rem; font-weight: 650; }}
    .question-id {{ font-family: ui-monospace, monospace; color: #075985; }}
    .option {{ display: flex; gap: .65rem; align-items: baseline; margin: .7rem 0; }}
    input {{ inline-size: 1.15rem; block-size: 1.15rem; flex: 0 0 auto; }}
    label {{ cursor: pointer; }}
    input:focus-visible {{ outline: 3px solid #f59e0b; outline-offset: 3px; }}
    @media print {{ body {{ max-width: none; padding: 0; }} fieldset {{ break-inside: avoid; }} }}
  </style>
</head>
<body>
  <main>
    <h1>{html.escape(title)}</h1>
    <p class="instructions"><strong>Instruções:</strong> assinale uma alternativa por questão. Este arquivo não corrige nem envia respostas. O gabarito é distribuído separadamente.</p>
    <form>
{chr(10).join(fields)}
    </form>
  </main>
</body>
</html>
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    questions = parse_questions(args.source.read_text(encoding="utf-8"))
    args.destination.write_text(render_html(args.title, questions), encoding="utf-8")
    print(f"{args.destination}: {len(questions)} questões")


if __name__ == "__main__":
    main()
