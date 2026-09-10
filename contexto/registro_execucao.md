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
| Infraestrutura e modelo | Concluída | 100% | 2026-08-16 | Ambiente uv, diretórios, documentação, notebook inicial e modelo criados e validados |
| Unidade I — Mineração de Dados | Concluída | 100% | 2026-09-07 | Todos os materiais em Markdown e gabaritos separados foram validados e aprovados |
| Unidade II — Análise de Dados | Concluída | 100% | 2026-09-07 | Todos os materiais em Markdown e gabaritos separados foram validados e aprovados |
| Unidade III — Pré-processamento | Concluída | 100% | 2026-09-09 | Notebook de redução ampliado; materiais, gabaritos e pareceres validados |
| Unidade IV — Mineração de Padrões | Concluída | 100% | 2026-09-07 | Três notebooks, listas, gabaritos e pareceres validados |
| Unidade V — Classificação e Regressão | Não iniciada | 0% | — | — |
| Unidade VI — Análise de Grupos | Não iniciada | 0% | — | — |
| Unidade VII — Detecção de Outliers | Não iniciada | 0% | — | — |
| Projeto integrador e revisão final | Não iniciada | 0% | — | — |

## Controle dos notebooks

| Notebook | Conteúdo | Produção | Revisão técnica | Execução limpa | Revisão editorial |
|---|---|---|---|---|---|
| `00_apresentacao_e_ambiente.ipynb` | Apresentação e configuração | Concluída | Concluída | Aprovada | Concluída |
| `01_01_introducao_a_mineracao_de_dados.ipynb` | Introdução | Concluída | Concluída | Aprovada | Concluída |
| `01_02_processo_kdd.ipynb` | Processo KDD | Concluída | Concluída | Aprovada | Concluída |
| `02_01_tipos_e_descricao_de_dados.ipynb` | Tipos e estatística descritiva | Concluída | Concluída | Aprovada | Concluída |
| `02_02_visualizacao_de_dados.ipynb` | Visualização | Concluída | Concluída | Aprovada | Concluída |
| `02_03_similaridade_e_dissimilaridade.ipynb` | Medidas de proximidade | Concluída | Concluída | Aprovada | Concluída |
| `03_01_qualidade_limpeza_e_integracao.ipynb` | Qualidade e limpeza | Concluída | Concluída | Aprovada | Concluída |
| `03_02_transformacao_e_discretizacao.ipynb` | Transformação | Concluída | Concluída | Aprovada | Concluída |
| `03_03_reducao_de_dados.ipynb` | Redução de dados | Concluída | Concluída | Aprovada | Concluída |
| `04_01_itemsets_e_regras_de_associacao.ipynb` | Regras de associação | Concluída | Concluída | Aprovada | Concluída |
| `04_02_algoritmo_apriori.ipynb` | Apriori | Concluída | Concluída | Aprovada | Concluída |
| `04_03_avaliacao_e_padroes_sequenciais.ipynb` | Avaliação e sequências | Concluída | Concluída | Aprovada | Concluída |
| `05_01_processo_e_avaliacao_de_classificacao.ipynb` | Processo e métricas | Pendente | Pendente | Pendente | Pendente |
| `05_02_classificadores_bayesianos_e_knn.ipynb` | Naive Bayes e k-NN | Pendente | Pendente | Pendente | Pendente |
| `05_03_arvores_de_decisao.ipynb` | Árvores de decisão | Pendente | Pendente | Pendente | Pendente |
| `05_04_regressao_linear.ipynb` | Regressão linear | Pendente | Pendente | Pendente | Pendente |
| `06_01_fundamentos_e_kmeans.ipynb` | Fundamentos e k-means | Pendente | Pendente | Pendente | Pendente |
| `06_02_agrupamento_hierarquico_e_dbscan.ipynb` | Hierárquico e DBSCAN | Pendente | Pendente | Pendente | Pendente |
| `06_03_avaliacao_de_agrupamentos.ipynb` | Avaliação de grupos | Pendente | Pendente | Pendente | Pendente |
| `07_01_conceitos_e_metodos_estatisticos.ipynb` | Outliers e estatística | Pendente | Pendente | Pendente | Pendente |
| `07_02_proximidade_densidade_e_agrupamento.ipynb` | Métodos de detecção | Pendente | Pendente | Pendente | Pendente |

## Controle dos exercícios e gabaritos

| Unidade | Conceituais `.md` | Múltipla escolha `.md` | Gabarito conceitual | Gabarito múltipla escolha | Gabaritos dos notebooks | Revisão |
|---|---|---|---|---|---|---|
| I — Mineração de Dados | Concluído | Concluída | Concluído | Concluído | Concluídos | Aprovada |
| II — Análise de Dados | Concluído | Concluída | Concluído | Concluído | Concluídos | Aprovada |
| III — Pré-processamento | Concluído | Concluída | Concluído | Concluído | Concluídos | Aprovada |
| IV — Mineração de Padrões | Concluído | Concluída | Concluído | Concluído | Concluídos | Aprovada |
| V — Classificação e Regressão | Pendente | Pendente | Pendente | Pendente | Pendente | Pendente |
| VI — Análise de Grupos | Pendente | Pendente | Pendente | Pendente | Pendente | Pendente |
| VII — Detecção de Outliers | Pendente | Pendente | Pendente | Pendente | Pendente | Pendente |

## Histórico

### 2026-09-09

- Reorganizado o notebook `03_03_reducao_de_dados.ipynb` em subseções explícitas de amostragem, agregação, seleção de atributos e extração de atributos, com finalidade, mecanismo, perdas e critérios de escolha.
- Implementada seleção supervisionada de 8 entre 30 atributos por filtro ANOVA, ajustado apenas no treino, tornando visível a preservação dos nomes das colunas originais e suas limitações.
- Explicada a redução de linhas por *clustering* como seleção de protótipos ou amostragem representativa, distinta de seleção e extração de atributos.
- Adicionado exemplo com K-means que resume 569 objetos em 12 grupos e escolhe a linha real mais próxima de cada centroide; diferenciados centroide sintético, representante real e amostragem dentro do grupo.
- Acrescentado quadro de decisão entre as formas de redução e esclarecida a possibilidade de combiná-las sem vazamento.
- Criada ilustração matricial comparando amostragem, agregação, seleção e extração, tornando visíveis as diferenças entre preservar linhas ou colunas e criar resumos ou dimensões.
- Criada projeção bidimensional dos agrupamentos, com símbolos distintos para as 569 observações, 12 centroides sintéticos e 12 linhas reais representantes, acompanhada de ressalva sobre a perda da projeção.
- Notebook reexecutado integralmente: 21 células, dez células de código, três figuras, identificadores únicos, atividades correspondentes aos gabaritos e nenhuma saída de erro.

### 2026-09-07

- Auditado e reescrito integralmente o gabarito dos 16 exercícios conceituais da Unidade IV; respostas antes resumidas passaram a incluir fórmulas, cálculos, demonstrações, exemplos, resultados esperados e protocolos completos.
- Detalhados, entre outros pontos, as cinco métricas de regras, a validação do Apriori, o experimento causal e as decisões temporais em padrões sequenciais; os 16 identificadores e critérios de correção foram validados.
- Reescrito integralmente o gabarito dos 16 exercícios conceituais da Unidade III, substituindo indicações de procedimento por respostas completas, cálculos, exemplos numéricos, código e decisões-modelo.
- Acrescentados exemplos de solução para todas as questões abertas e mantidos critérios de correção após cada resposta; correspondência dos 16 identificadores novamente validada.
- Convertidas para Markdown as listas de múltipla escolha das Unidades I, II, III e IV; os quatro arquivos HTML deixaram de fazer parte do material.
- Preservados 60 identificadores e 240 alternativas nas quatro listas, mantendo correspondência integral com os gabaritos separados.
- Atualizados plano, diretrizes, roteiro de estudo e protocolos de revisão para tornar `multipla_escolha.md` o formato obrigatório das unidades atuais e futuras.
- Substituídos os quatro pareceres de HTML por pareceres de formatação Markdown e removido o gerador HTML que se tornou obsoleto.
- Produzidos os três notebooks da Unidade IV: itemsets e regras de associação; algoritmo Apriori; avaliação de regras e padrões sequenciais.
- Demonstradas representação transacional, matriz *one-hot*, métricas de suporte, confiança, *lift*, leverage e conviction, com cálculo manual e interpretação sem atribuição causal.
- Implementado um Apriori didático com geração e poda por nível, auditoria de candidatos e verificação exata contra `mlxtend.apriori`.
- Analisado o efeito do suporte mínimo sobre itemsets frequentes e candidatos avaliados; criada figura comparativa com quatro limiares.
- Introduzidos padrões sequenciais, ocorrência como subsequência e suporte por entidade; criada figura com quatro padrões de jornada.
- Criadas 16 questões conceituais e 15 questões objetivas em Markdown, todas com identificadores e gabaritos comentados separados.
- Criados gabaritos para as sete atividades dos notebooks, com soluções, resultados esperados e rubricas.
- Emitidos sete pareceres especializados e uma consolidação para cada notebook, além de quatro pareceres das listas: 28 arquivos de revisão aprovados sem achados obrigatórios.
- Ambiente auditado com `uv sync --frozen`: 109 pacotes conferidos pelo lockfile.
- Reexecutadas 40 células, incluindo 15 de código, sem saídas de erro e com identificadores de célula únicos.
- Validada a correspondência completa dos identificadores: 16 conceituais, 15 de múltipla escolha e sete atividades internas.
- Validada a lista objetiva em Markdown com 15 questões, 60 alternativas e nenhum gabarito embutido; as duas figuras foram renderizadas e inspecionadas.

### 2026-09-02

- Incluída, antes da síntese do notebook `02_03_similaridade_e_dissimilaridade.ipynb`, a seção “Como escolher uma medida de proximidade”.
- Criada tabela comparativa de Euclidiana, Manhattan, Minkowski, cosseno, Jaccard e Gower, com situações de uso, exemplos e cuidados.
- Acrescentado roteiro de decisão sobre finalidade, tipos de atributos, invariâncias, ausências conjuntas, escala, casos especiais e validação.
- Reforçado que a escolha formaliza o significado de proximidade e pode alterar vizinhos, grupos e casos atípicos; não existe medida universalmente melhor.
- Incluída uma seção própria sobre Gower, com fórmula ponderada, contribuições para atributos numéricos, nominais, ordinais e binários, tratamento de ausências e limitações.
- Implementado exemplo didático com perfis mistos; a matriz resultou em 0,132 para Ana–Bruno, 0,917 para Ana–Carla e 0,973 para Bruno–Carla, confirmando o cálculo manual.
- Corrigida a fórmula da contribuição numérica na tabela de Gower: barras de valor absoluto passaram de caracteres `|`, interpretados como divisores da tabela Markdown, para `\lvert` e `\rvert` em LaTeX.
- Incluída ilustração geométrica dos caminhos Euclidiano e Manhattan para os mesmos dois pontos, com valores 5 e 7.
- Incluída decomposição visual da distância Manhattan antes e depois da padronização, evidenciando a dominação original da renda sobre a idade.
- Incluída figura de Gower com barras empilhadas das contribuições por atributo e mapa de calor da matriz final.
- Incluída figura 3D do cosseno com vetores originais e normalizados, evidenciando que A e B possuem magnitudes diferentes, mas a mesma direção e o mesmo ponto após normalização.
- Incluída figura de Jaccard com grade de presenças binárias e comparação entre interseção, união e ausência conjunta ignorada.
- Notebook reexecutado e figuras inspecionadas: 35 células, 12 células de código, cinco figuras, IDs únicos e nenhuma saída de erro.

### 2026-08-31

- Ampliado o notebook `03_02_transformacao_e_discretizacao.ipynb` com explicações sobre os papéis das distribuições lognormal, Poisson e binomial na geração dos dados sintéticos.
- Esclarecido que os parâmetros da lognormal descrevem a normal subjacente ao logaritmo, que $\lambda$ controla a contagem de Poisson e que `binomial(1, p)` realiza um ensaio de Bernoulli por cliente.
- Explicados a função logística usada apenas na simulação, o objetivo e os limites de `log1p` e a interpretação da assimetria calculada por `skew`.
- Incluída interpretação da saída: `skew` da renda passou de 2,26 na escala original para -0,06 após `log1p`, sem afirmar normalidade.
- Criada uma figura de três painéis para visualizar renda lognormal, contagens de Poisson e resultados binários gerados por `binomial(1, p)`.
- Criada uma comparação visual da renda antes e depois de `log1p`, com os valores de `skew` nos títulos e interpretação textual acessível.
- Notebook reexecutado integralmente: 20 células, sete células de código, duas figuras, IDs únicos e nenhuma saída de erro.

### 2026-08-26

- Produzidos os três notebooks da Unidade III: qualidade, limpeza e integração; transformação e discretização; e redução de dados.
- Demonstrados diagnóstico antes/depois, preservação de dados brutos, imputação, tratamento de duplicatas, integração com cardinalidade validada, escalonamento, codificação, discretização e pipelines sem vazamento.
- Desenvolvidas amostragem estratificada, agregação e PCA com fórmulas, variância acumulada, taxa de compressão e erro de reconstrução.
- Criadas 16 questões conceituais, 15 questões objetivas em HTML e gabaritos comentados separados.
- Criados gabaritos para as sete atividades dos notebooks, incluindo a atividade integradora, com soluções executáveis e rubricas.
- Emitidos e consolidados os sete pareceres especializados de cada notebook; listas e HTML também foram aprovados.
- Ambiente auditado com `uv sync --frozen`; executadas 40 células, incluindo 17 de código, sem saídas de erro e com IDs únicos.
- Validada correspondência completa dos identificadores: 16 conceituais, 15 objetivas e sete atividades internas.
- Validado o HTML com 15 grupos, 60 controles, 60 rótulos e nenhum script ou resposta embutida.

### 2026-08-19

- Criada uma figura vetorial autoral com cinco painéis para comparar visualmente classificação, regressão, agrupamento, associação e detecção de outliers no notebook `01_01_introducao_a_mineracao_de_dados.ipynb`.
- Acrescentadas legenda, descrição alternativa e ressalvas sobre separações conceituais, diferença entre classificação e agrupamento e interpretação de outliers.
- Registradas autoria, origem conceitual e licença da nova figura em `imagens/fontes.md`; notebook reexecutado com 13 células, IDs únicos e nenhuma saída de erro.
- Incluída, no estudo de caso do notebook `01_02_processo_kdd.ipynb`, uma exploração inicial com `DataFrame.describe()` e transposição da tabela para facilitar a leitura por atributo.
- Acrescentada a interpretação de contagem, média, desvio-padrão, quartis, extremos e da média do atributo binário `cancelou`.
- Explicado o objetivo da comparação entre tempo como cliente e cancelamento, incluindo pergunta exploratória, papéis das variáveis, leitura do *boxplot*, resultado esperado na simulação e limites causais e preditivos.
- Notebook reexecutado integralmente: 17 células, quatro células de código, IDs únicos e nenhuma saída de erro.

### 2026-08-17

- Ampliado o estudo de caso do notebook `01_02_processo_kdd.ipynb` com um mapeamento explícito entre o caso e as seis etapas do KDD.
- Diferenciadas etapas realizadas, ilustradas, planejadas e ainda não executadas no estudo.
- Esclarecido que a função logística gera os dados sintéticos e não representa um modelo treinado.
- Notebook reexecutado sem erros e alteração aprovada em adendo de revisão.

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
- Instalado o ambiente `.venv` por `uv sync`, com 109 pacotes, e validada a importação das bibliotecas-base.
- Criada a estrutura de diretórios para notebooks, dados, imagens, soluções e modelos.
- Criados `dados/README.md`, `imagens/fontes.md` e o notebook-modelo padronizado.
- Criado e executado sem erros `notebooks/00_apresentacao_e_ambiente.ipynb`.
- Produzidos e executados sem erros os dois notebooks da Unidade I: introdução à mineração de dados e processo KDD.
- Criado diagrama vetorial autoral e acessível do processo KDD.
- Emitidos e consolidados os sete pareceres de cada notebook da Unidade I; ambos foram aprovados para publicação sem achados obrigatórios.
- Tornadas obrigatórias, para cada unidade, uma lista conceitual em Markdown, uma lista de múltipla escolha e um gabarito comentado separado.
- Criadas as listas conceitual e de múltipla escolha da Unidade I, ambas com 15 questões.
- Criado gabarito separado da Unidade I, com justificativas das respostas e dos principais distratores.
- Listas e gabarito da Unidade I aprovados nas revisões de alinhamento e exatidão técnica.
- Produzidos os três notebooks da Unidade II: tipos e descrição, visualização e medidas de proximidade.
- Executadas 43 células da Unidade II, incluindo 14 células de código, sem saídas de erro e com IDs válidos.
- Criadas as listas da Unidade II: 16 exercícios conceituais, 15 questões objetivas e gabarito comentado separado.
- Listas da Unidade II aprovadas nas revisões de alinhamento e exatidão técnica.
- Emitidos 21 pareceres especializados para os três notebooks da Unidade II; todos foram aprovados sem achados obrigatórios.
- Consolidados os três notebooks da Unidade II como aprovados para publicação.
- Atualizada a diretriz: toda questão passa a exigir identificador e gabarito separado em `gabaritos/`; múltipla escolha do estudante passa a ser HTML.
- Migrados os gabaritos objetivos das Unidades I e II para a pasta exclusiva `gabaritos/`.
- Criados gabaritos conceituais com respostas-modelo e critérios para 15 questões da Unidade I e 16 da Unidade II.
- Criados gabaritos separados para todas as atividades dos cinco notebooks das Unidades I e II.
- Atribuídos identificadores estáveis às atividades e validada correspondência completa: 34 de 34 na Unidade I e 38 de 38 na Unidade II.
- Geradas listas de múltipla escolha HTML acessíveis para as Unidades I e II por conversor reutilizável.
- Validados 30 grupos de questões, 120 controles e 120 rótulos, sem scripts ou respostas embutidas.
- Gabaritos e HTML das Unidades I e II aprovados nas revisões de alinhamento, exatidão e acessibilidade.

## Decisões e alterações de escopo

| Data | Decisão | Motivo | Impacto |
|---|---|---|---|
| 2026-08-16 | Não incluir Data Warehouse como unidade | O tema está comentado no programa analítico atual | Mantidas sete unidades e 60 horas |
| 2026-08-16 | Usar o livro de Han, Pei e Tong, 4ª edição, como guia principal | É a edição disponível na pasta `contexto` | Referências do plano seguem capítulos da 4ª edição |
| 2026-08-16 | Adotar o uv para ambiente e pacotes | Unifica Python, `.venv`, dependências, lock e execução em uma única ferramenta | `pyproject.toml`, `.python-version` e `uv.lock` tornam-se a configuração oficial |

## Pendências e bloqueios

Nenhum bloqueio registrado. A próxima ação prevista é produzir a Unidade V, aplicando a política completa de gabaritos e revisões desde o início.
