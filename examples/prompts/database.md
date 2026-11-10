# Database

Altere somente `examples/task_manager/db.py`. Forneça `init_db`, `get_tasks`, `get_task`, `create_task`, `update_task` e `delete_task`. Os testes podem substituir `DB_PATH`; sempre feche conexões, use transações para gravações e parâmetros SQL para valores. Gere nomes dinâmicos de coluna somente a partir de uma lista fixa de permissões. Retorne `None`/`False` para registros ausentes; não disfarce exceções de banco como lista vazia.
