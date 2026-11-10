# QA

Modifique somente `tests/`. Os testes devem seguir os requisitos, não enfraquecer a especificação para passar. Isole SQLite com `tmp_path` e inicie `TestClient` pelo lifespan da aplicação. Cubra CRUD, tipos, valores nulos, campos desconhecidos, dados ausentes e persistência após reinício. Execute os testes e registre comando, versão, código de saída e resumo das falhas.
