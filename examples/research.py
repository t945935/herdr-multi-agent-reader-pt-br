"""Chapter 8: valida evidências que relacionam afirmações e fontes e produz um relatório auditável."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def validate(data):
    if not isinstance(data, dict) or not data.get("question"):
        raise ValueError("A pergunta de pesquisa é obrigatória")
    sources = data.get("sources", [])
    if not isinstance(sources, list) or not sources:
        raise ValueError("As fontes são obrigatórias")
    by_id = {}
    for source in sources:
        if not {"id", "url", "title", "accessed", "kind"} <= source.keys():
            raise ValueError("Fonte incompleta")
        parsed = urlparse(source["url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("A URL da fonte deve usar HTTP(S)")
        if source["id"] in by_id:
            raise ValueError("ID de fonte duplicado")
        by_id[source["id"]] = source
    claims = data.get("claims", [])
    if not claims:
        raise ValueError("As afirmações são obrigatórias")
    for claim in claims:
        if not claim.get("text") or claim.get("status") not in {"supported", "uncertain", "conflict"}:
            raise ValueError("Afirmação inválida")
        evidence = claim.get("evidence", [])
        if claim["status"] == "supported" and not evidence:
            raise ValueError("Afirmações sustentadas exigem evidências")
        for item in evidence:
            if item.get("source") not in by_id or not item.get("quote"):
                raise ValueError("A evidência exige uma fonte conhecida e uma citação")
    return by_id


def render(data):
    sources = validate(data)
    lines = ["# " + data["question"], "", "## Achados e evidências", ""]
    for claim in data["claims"]:
        lines.extend([f"### {claim['text']}", "", "Estado: " + claim["status"], ""])
        for evidence in claim.get("evidence", []):
            source = sources[evidence["source"]]
            lines.extend([f"> {evidence['quote']}", "", f"Fonte: [{source['title']}]({source['url']})", ""])
    lines.extend(["## Fontes", ""])
    for source in sources.values():
        lines.append(f"- {source['id']}：[{source['title']}]({source['url']})；{source['kind']}；acessada em {source['accessed']}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = render(json.loads(args.input.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report)
    print(args.output)
