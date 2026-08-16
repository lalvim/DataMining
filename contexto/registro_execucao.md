# Registro de execução da disciplina

## Como atualizar este documento

Este arquivo registra o trabalho efetivamente realizado. Atualize-o sempre que uma entrega for iniciada, concluída, revisada ou bloqueada. Não marque uma unidade como concluída enquanto todos os seus notebooks não atenderem à definição de pronto do plano.

Estados permitidos:

- `Não iniciada`
- `Em andamento`
- `Em revisão`
- `Concluída`
- `Bloqueada`

## Visão geral

| Etapa | Estado | Progresso | Última atualização | Observação |
|---|---|---:|---|---|
| Infraestrutura e modelo | Não iniciada | 0% | — | — |
| Unidade I — Mineração de Dados | Não iniciada | 0% | — | — |
| Unidade II — Análise de Dados | Não iniciada | 0% | — | — |
| Unidade III — Pré-processamento | Não iniciada | 0% | — | — |
| Unidade IV — Mineração de Padrões | Não iniciada | 0% | — | — |
| Unidade V — Classificação e Regressão | Não iniciada | 0% | — | — |
| Unidade VI — Análise de Grupos | Não iniciada | 0% | — | — |
| Unidade VII — Detecção de Outliers | Não iniciada | 0% | — | — |
| Projeto integrador e revisão final | Não iniciada | 0% | — | — |

## Controle dos notebooks

| Notebook | Conteúdo | Produção | Revisão técnica | Execução limpa | Revisão editorial |
|---|---|---|---|---|---|
| `00_apresentacao_e_ambiente.ipynb` | Apresentação e configuração | Pendente | Pendente | Pendente | Pendente |
| `01_01_introducao_a_mineracao_de_dados.ipynb` | Introdução | Pendente | Pendente | Pendente | Pendente |
| `01_02_processo_kdd.ipynb` | Processo KDD | Pendente | Pendente | Pendente | Pendente |
| `02_01_tipos_e_descricao_de_dados.ipynb` | Tipos e estatística descritiva | Pendente | Pendente | Pendente | Pendente |
| `02_02_visualizacao_de_dados.ipynb` | Visualização | Pendente | Pendente | Pendente | Pendente |
| `02_03_similaridade_e_dissimilaridade.ipynb` | Medidas de proximidade | Pendente | Pendente | Pendente | Pendente |
| `03_01_qualidade_limpeza_e_integracao.ipynb` | Qualidade e limpeza | Pendente | Pendente | Pendente | Pendente |
| `03_02_transformacao_e_discretizacao.ipynb` | Transformação | Pendente | Pendente | Pendente | Pendente |
| `03_03_reducao_de_dados.ipynb` | Redução de dados | Pendente | Pendente | Pendente | Pendente |
| `04_01_itemsets_e_regras_de_associacao.ipynb` | Regras de associação | Pendente | Pendente | Pendente | Pendente |
| `04_02_algoritmo_apriori.ipynb` | Apriori | Pendente | Pendente | Pendente | Pendente |
| `04_03_avaliacao_e_padroes_sequenciais.ipynb` | Avaliação e sequências | Pendente | Pendente | Pendente | Pendente |
| `05_01_processo_e_avaliacao_de_classificacao.ipynb` | Processo e métricas | Pendente | Pendente | Pendente | Pendente |
| `05_02_classificadores_bayesianos_e_knn.ipynb` | Naive Bayes e k-NN | Pendente | Pendente | Pendente | Pendente |
| `05_03_arvores_de_decisao.ipynb` | Árvores de decisão | Pendente | Pendente | Pendente | Pendente |
| `05_04_regressao_linear.ipynb` | Regressão linear | Pendente | Pendente | Pendente | Pendente |
| `06_01_fundamentos_e_kmeans.ipynb` | Fundamentos e k-means | Pendente | Pendente | Pendente | Pendente |
| `06_02_agrupamento_hierarquico_e_dbscan.ipynb` | Hierárquico e DBSCAN | Pendente | Pendente | Pendente | Pendente |
| `06_03_avaliacao_de_agrupamentos.ipynb` | Avaliação de grupos | Pendente | Pendente | Pendente | Pendente |
| `07_01_conceitos_e_metodos_estatisticos.ipynb` | Outliers e estatística | Pendente | Pendente | Pendente | Pendente |
| `07_02_proximidade_densidade_e_agrupamento.ipynb` | Métodos de detecção | Pendente | Pendente | Pendente | Pendente |

## Histórico

### 2026-08-16

- Convertido o programa analítico de LaTeX para `contexto/resumo_disciplina.md`.
- Criado `contexto/plano_execucao.md`, organizado pelas sete unidades do conteúdo programático.
- Criado este registro de execução.
- Criado `contexto/diretrizes_formatacao.md` para padronizar os materiais.
- Inspecionado o sumário de `contexto/hanDataMiningConceptual.pdf` e mapeados os capítulos relevantes para cada unidade.
- Criada a pasta `contexto/revisores` com protocolos de didática, referências, alinhamento curricular, nível acadêmico, exatidão técnica, qualidade editorial/acessibilidade e reprodutibilidade.
- Criados um modelo padronizado de parecer e um checklist de consolidação das revisões.
- Adotado o `uv` como gerenciador exclusivo de Python, ambiente virtual e dependências.
- Criados `pyproject.toml`, `.python-version` e `uv.lock`; a resolução foi validada com Python 3.11.

## Decisões e alterações de escopo

| Data | Decisão | Motivo | Impacto |
|---|---|---|---|
| 2026-08-16 | Não incluir Data Warehouse como unidade | O tema está comentado no programa analítico atual | Mantidas sete unidades e 60 horas |
| 2026-08-16 | Usar o livro de Han, Pei e Tong, 4ª edição, como guia principal | É a edição disponível na pasta `contexto` | Referências do plano seguem capítulos da 4ª edição |
| 2026-08-16 | Adotar o uv para ambiente e pacotes | Unifica Python, `.venv`, dependências, lock e execução em uma única ferramenta | `pyproject.toml`, `.python-version` e `uv.lock` tornam-se a configuração oficial |

## Pendências e bloqueios

Nenhum bloqueio registrado. A configuração inicial e o lock do ambiente estão prontos; as próximas ações são instalar com `uv sync`, validar a execução e criar o notebook-modelo.
