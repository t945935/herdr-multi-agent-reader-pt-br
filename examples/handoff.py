"""Chapter 6: valida um registro explícito de passagem de trabalho, não uma afirmação narrativa do agente."""

import argparse
import hashlib
import json
from pathlib import Path


def validate(record, root):
    required = {"task_id", "from", "to", "completed", "next", "artifacts"}
    if not isinstance(record, dict) or not required <= record.keys():
        raise ValueError("Campos obrigatórios ausentes no handoff")
    if any(not isinstance(record[key], str) or not record[key].strip()
           for key in ["task_id", "from", "to", "completed", "next"]):
        raise ValueError("Os campos de texto do handoff não podem ficar vazios")
    if not isinstance(record["artifacts"], list) or not record["artifacts"]:
        raise ValueError("O handoff exige artefatos")
    root = Path(root).resolve()
    for artifact in record["artifacts"]:
        if not isinstance(artifact, dict) or set(artifact) != {"path", "sha256"}:
            raise ValueError("O artefato exige path e sha256")
        path = (root / artifact["path"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("O path do artefato deve indicar um arquivo dentro do projeto")
        if hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
            raise ValueError("O hash do artefato não corresponde")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    validate(json.loads(args.record.read_text()), args.root)
    print("Passagem de trabalho aceita")
