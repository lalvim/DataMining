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

## Roteiro de estudo

1. [Apresentação e ambiente](notebooks/00_apresentacao_e_ambiente.ipynb)
2. Unidade I — Mineração de Dados
   - [Introdução à mineração de dados](notebooks/unidade_01/01_01_introducao_a_mineracao_de_dados.ipynb)
   - [Processo KDD](notebooks/unidade_01/01_02_processo_kdd.ipynb)
   - [Exercícios conceituais](exercicios/unidade_01/exercicios_conceituais.md)
   - [Questões de múltipla escolha](exercicios/unidade_01/multipla_escolha.html)
3. Unidade II — Análise de Dados
   - [Tipos e descrição de dados](notebooks/unidade_02/02_01_tipos_e_descricao_de_dados.ipynb)
   - [Visualização de dados](notebooks/unidade_02/02_02_visualizacao_de_dados.ipynb)
   - [Similaridade e dissimilaridade](notebooks/unidade_02/02_03_similaridade_e_dissimilaridade.ipynb)
   - [Exercícios conceituais](exercicios/unidade_02/exercicios_conceituais.md)
   - [Questões de múltipla escolha](exercicios/unidade_02/multipla_escolha.html)
4. Unidade III — Pré-processamento de Dados
   - [Qualidade, limpeza e integração](notebooks/unidade_03/03_01_qualidade_limpeza_e_integracao.ipynb)
   - [Transformação e discretização](notebooks/unidade_03/03_02_transformacao_e_discretizacao.ipynb)
   - [Redução de dados](notebooks/unidade_03/03_03_reducao_de_dados.ipynb)
   - [Exercícios conceituais](exercicios/unidade_03/exercicios_conceituais.md)
   - [Questões de múltipla escolha](exercicios/unidade_03/multipla_escolha.html)

Os gabaritos ficam exclusivamente em `gabaritos/`, separados do material do estudante. Toda questão das listas e dos notebooks deve possuir resposta associada nessa pasta.

Os identificadores exibidos nas atividades, como `U02-NB01-E01`, permitem localizar diretamente a resposta-modelo e os critérios no gabarito correspondente.

As unidades seguintes serão adicionadas conforme o [plano de execução](contexto/plano_execucao.md). O andamento verificável está no [registro de execução](contexto/registro_execucao.md).
