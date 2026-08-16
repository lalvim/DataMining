# Mineração de Dados

Material didático em Jupyter Notebooks para a disciplina TM434 — Mineração de Dados.

## Ambiente com uv

O projeto usa o [uv](https://docs.astral.sh/uv/) para gerenciar a versão do Python, o ambiente virtual e todas as dependências.

Na raiz do repositório, prepare o ambiente e inicie o JupyterLab:

```bash
uv sync
uv run jupyter lab
```

O `uv sync` cria automaticamente o ambiente `.venv` e instala as versões resolvidas em `uv.lock`. O arquivo de lock deve ser versionado para que estudantes e revisores utilizem o mesmo conjunto de dependências.

Para adicionar uma dependência de execução:

```bash
uv add nome-do-pacote
```

Para adicionar uma ferramenta usada apenas no desenvolvimento ou na revisão:

```bash
uv add --dev nome-do-pacote
```

Evite instalar pacotes diretamente com `pip`, `conda` ou comandos `!pip` nos notebooks.
