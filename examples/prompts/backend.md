# Backend

Altere somente `examples/task_manager/main.py`. Inicialize as tabelas pelo lifespan do FastAPI; rejeite campos desconhecidos e coerção de tipos. POST bem-sucedido retorna 201, PATCH retorna 200, DELETE retorna 204; registros ausentes retornam 404 e entrada inválida retorna 422. Campos PATCH omitidos mantêm os valores atuais; `null` explícito é rejeitado; a descrição pode ser apagada. Não altere arquivos sob responsabilidade de Database.
