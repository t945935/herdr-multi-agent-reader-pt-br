# Developer: contrato do sistema de notas

Leia primeiro os casos de notas em `examples/grades.py` e `tests/test_contracts.py`. Altere somente `examples/grades.py`; não modifique testes existentes, código do site nem inicie outros agentes.

Contrato: exatamente três disciplinas — English, History e Mathematics. Notas são valores finitos `int`/`float`; rejeite bool, strings, disciplinas ausentes ou extras e valores fora de 0–100. Média 60 corresponde à aprovação. Lista vazia de estudantes retorna lista vazia. Classifique pelos totais não arredondados com classificação por competição, preservando a ordem de entrada em empates; não modifique os dados de entrada.

Mantenha as interfaces `calculate_total`, `calculate_average`, `get_grade` e `rank_students`. Confira o contrato e corrija somente se necessário. Se já estiver conforme, preserve a implementação e relate as verificações em vez de reescrevê-la apenas para produzir um diff.

Execute `.venv/bin/python -m pytest -q tests/test_contracts.py -k 'ranking or scores'`. Registre o comando real, código de saída, arquivos alterados e itens não resolvidos em `reports/grade-developer.md`. Use o `task_id` e `completion_path` acrescentados pelo Manager no recibo de conclusão.
