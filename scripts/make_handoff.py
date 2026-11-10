#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
path = root / "examples/grades.py"
record = {
    "task_id": "grade-api-v1", "from": "developer", "to": "qa",
    "completed": "Contrato de notas e implementação de referência estão prontos", "next": "Execute testes de regressão para classificação e validação de entrada",
    "artifacts": [{"path": "examples/grades.py", "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}],
}
out = root / "reports/handoff.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(out)
