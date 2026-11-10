# QA: sistema de notas

Leia a interface de `examples/grades.py` e os casos existentes em `tests/test_contracts.py`. Verifique o contrato de notas de forma independente. Não altere código, não apague testes existentes, não leia a autoavaliação do Developer e não inicie outros agentes.

Adicione ou altere somente `tests/test_grades_review.py`; grave o relatório em `reports/grade-qa.md`. Verifique as três disciplinas, limites 0/100/60, bool/NaN/string, dados vazios, nomes, empate 1/1/3, precisão não arredondada e imutabilidade da entrada.

Use pytest. Se testes existentes já cobrirem um caso de forma suficiente, declare o critério e acrescente apenas cobertura ausente que tenha valor; não duplique um teste idêntico. Não teste FastAPI, SQLite ou CRUD do site — esta tarefa é somente sobre o sistema de notas.

Execute testes e preserve o comando real, código de saída, achados e itens não executados. Use `task_id` e `completion_path` acrescentados pelo Manager no recibo de conclusão; liste em `artifacts` os arquivos de relatório e teste criados.
