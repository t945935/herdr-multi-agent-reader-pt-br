# Pacote executável para leitores

Execute todos os comandos a partir da raiz do projeto extraído. Importe os módulos por `examples.*`.

Os prompts do sistema de notas são `prompts/grades-developer.md` e `prompts/grades-qa.md`; `prompts/qa.md` é específico do site. Distribua tarefas em sua própria cópia de exercício para preservar intacta a versão de referência.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
.venv/bin/python -m examples.pipeline
```

| Capítulo | Ponto de entrada | Foco da aceitação |
| --- | --- | --- |
| 1 | `calculator.py` | Aritmética, divisão por zero e tipos |
| 2 | `grades.py` | Limites das notas, disciplinas ausentes e empates na classificação por competição |
| 3 | `../scripts/probe_herdr.py --live` | Executar, ler, aguardar e limpar um novo painel de shell |
| 4 | `../scripts/team.py` | Atribuições em etapas, IDs de tarefa exclusivos e aceitação de artefatos |
| 5 | `prompts/reviewer-a.md`, `reviewer-b.md` | Revisões independentes e decisão do Manager |
| 6 | `handoff.py` | Existência do arquivo, escopo do projeto e SHA-256 |
| 7 | `task_manager/` | CRUD, validação, páginas estáticas e persistência após reinício |
| 8 | `research.py` | Afirmações, fontes, citações e incerteza |
| 9 | `pipeline.py` | Códigos de saída, tempos limite, aceitação e interrupção em caso de falha |
| 10 | `queue.py` | Deduplicação, leases, recuperação, dead letters e concorrência |

Inicie o site:

```bash
.venv/bin/python -m uvicorn examples.task_manager.main:app --host 0.0.0.0 --port 8000
```

No WSL, abra `http://localhost:8000/` em um navegador do Windows. Os dados didáticos são gravados por padrão em `examples/data/tasks.db`; testes automatizados usam um diretório temporário e não alteram esse arquivo.

A fila em segundo plano é um exemplo finito de computação pura e não chama um modelo pago. A atribuição real a modelos é explícita em `scripts/team.py`; instale e autentique primeiro a CLI correspondente.
