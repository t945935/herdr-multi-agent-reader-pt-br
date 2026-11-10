# Pacote de recursos para leitores Herdr — pt-BR

Versão: 1.0.0

Este pacote complementar contém exemplos executáveis, testes, prompts e instruções concisas para *Fluxos de Trabalho Confiáveis com Múltiplos Agentes no Herdr*. O texto pago do livro não está incluído.

## Instalação e testes

Use Python 3.12 a partir da raiz do projeto extraído:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
```

Resultado esperado: 42 testes aprovados. Os direitos e a licença específica da edição pt-BR estão descritos em `resource-manifest.json`; nenhuma licença open source geral é concedida.

Veja [`examples/README.md`](examples/README.md) para o mapeamento dos capítulos, inicialização do site e orientações para os exercícios. Veja [`CHANGELOG.md`](CHANGELOG.md) para o histórico da versão.
