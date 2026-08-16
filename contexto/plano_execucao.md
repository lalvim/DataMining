# Plano de execução da disciplina de Mineração de Dados

## 1. Finalidade

Este plano orienta a produção integral da disciplina TM434 em Jupyter Notebooks, combinando explicações em Markdown, fórmulas em LaTeX, imagens, visualizações, exemplos executáveis e atividades práticas. O planejamento segue as sete unidades do conteúdo programático e considera uma carga total de 60 horas.

O livro-guia é **HAN, Jiawei; PEI, Jian; TONG, Hanghang. _Data Mining: Concepts and Techniques_. 4. ed. Elsevier, 2023**, disponível em `contexto/hanDataMiningConceptual.pdf`. O livro serve como referência conceitual; o texto dos notebooks deverá ser autoral, em português, com as fontes devidamente citadas.

## 2. Resultados esperados

Ao final da produção, o repositório deverá conter:

- notebooks didáticos executáveis para todas as unidades;
- exercícios guiados e propostos, com soluções separadas quando necessário;
- imagens e diagramas próprios ou com licença e atribuição adequadas;
- conjuntos de dados locais, pequenos e documentados, ou rotinas reprodutíveis de obtenção;
- ambiente Python reproduzível;
- índice geral da disciplina e referências;
- notebooks validados por execução completa, do início ao fim.

## 3. Estrutura prevista do repositório

```text
DataMining/
├── README.md
├── ambiente/
│   ├── requirements.txt
│   └── environment.yml
├── contexto/
│   ├── resumo_disciplina.md
│   ├── plano_execucao.md
│   ├── registro_execucao.md
│   ├── diretrizes_formatacao.md
│   ├── revisores/
│   │   ├── README.md
│   │   ├── modelo_parecer.md
│   │   └── pareceres/
│   └── hanDataMiningConceptual.pdf
├── notebooks/
│   ├── 00_apresentacao_e_ambiente.ipynb
│   ├── unidade_01/
│   ├── unidade_02/
│   ├── unidade_03/
│   ├── unidade_04/
│   ├── unidade_05/
│   ├── unidade_06/
│   └── unidade_07/
├── dados/
│   ├── brutos/
│   ├── processados/
│   └── README.md
├── imagens/
│   ├── fontes.md
│   └── unidades/
└── solucoes/
```

A estrutura poderá ser refinada durante a implementação, mas nomes, numeração e separação entre material didático, dados, imagens e soluções devem permanecer consistentes.

## 4. Estratégia pedagógica comum às unidades

Cada assunto será desenvolvido no ciclo:

1. **Motivação:** problema real, pergunta norteadora e resultado esperado.
2. **Fundamentação:** conceitos, notação, hipóteses e fórmulas.
3. **Exemplo manual:** cálculo pequeno, verificável sem biblioteca especializada.
4. **Implementação:** código Python progressivo e comentado.
5. **Aplicação:** experimento com dados e interpretação do resultado.
6. **Verificação:** perguntas rápidas e exercícios.
7. **Síntese:** principais conclusões, limitações e referências.

Bibliotecas-base previstas: Python, NumPy, pandas, SciPy, Matplotlib, Seaborn, scikit-learn e, para regras de associação, mlxtend. Toda dependência usada deverá constar no arquivo de ambiente com versão compatível.

## 5. Distribuição da carga horária

| Unidade | Tema | Horas previstas | Quantidade inicial de notebooks |
|---|---|---:|---:|
| I | Mineração de Dados | 6 h | 2 |
| II | Análise de Dados | 10 h | 3 |
| III | Pré-processamento de Dados | 8 h | 3 |
| IV | Mineração de Padrões | 8 h | 3 |
| V | Classificação e Regressão | 12 h | 4 |
| VI | Análise de Grupos | 10 h | 3 |
| VII | Detecção de Outliers | 6 h | 2 |
| **Total** |  | **60 h** | **20** |

A quantidade de notebooks é uma estimativa. Um notebook deverá ser dividido quando sua leitura ou execução se tornar longa demais, sem alterar a carga ou os objetivos da unidade.

## 6. Etapa inicial — infraestrutura e modelo didático

Antes da Unidade I:

- criar a árvore de diretórios;
- definir as versões de Python e das bibliotecas;
- criar `00_apresentacao_e_ambiente.ipynb` com instruções de instalação e teste;
- criar um notebook-modelo com a estrutura definida nas diretrizes;
- escolher conjuntos de dados que possam reaparecer em diferentes unidades;
- configurar validação automatizada dos notebooks;
- atualizar o README com a ordem de estudo.

**Critério de conclusão:** ambiente recriado do zero e notebook de apresentação executado sem erros.

## 7. Execução por unidade

### Unidade I — Mineração de Dados

**Carga prevista:** 6 horas  
**Referência principal no livro:** Capítulo 1, especialmente seções 1.1–1.7.

**Objetivos de aprendizagem**

- distinguir dados, informação, padrão e conhecimento;
- explicar mineração de dados e sua posição no processo de KDD;
- reconhecer tarefas descritivas e preditivas;
- relacionar aplicações reais às tarefas adequadas;
- discutir qualidade, privacidade, viés e uso responsável.

**Notebooks previstos**

1. `01_01_introducao_a_mineracao_de_dados.ipynb`
   - definição e evolução da área;
   - tipos de conhecimento e tarefas;
   - exemplos em ciência, comércio, indústria e setor público;
   - pequena exploração executável de um conjunto de dados.
2. `01_02_processo_kdd.ipynb`
   - etapas do KDD e sua natureza iterativa;
   - relação entre KDD, mineração de dados, aprendizado de máquina e ciência de dados;
   - estudo de caso percorrendo todas as etapas;
   - diagrama autoral do processo.

**Atividade integradora:** formular um problema de mineração de dados, identificar tarefa, dados necessários, métrica de sucesso, riscos e etapas do KDD.

**Critério de conclusão:** notebooks executáveis, diagrama legível, estudo de caso completo e atividade com critérios de correção.

### Unidade II — Análise de Dados

**Carga prevista:** 10 horas  
**Referência principal no livro:** Capítulo 2, seções 2.1–2.3; Apêndice A quando necessário.

**Objetivos de aprendizagem**

- identificar atributos nominais, binários, ordinais e numéricos;
- calcular e interpretar medidas de posição, dispersão, covariância e correlação;
- selecionar visualizações coerentes com o tipo de variável;
- calcular similaridade e dissimilaridade para diferentes tipos de dados.

**Notebooks previstos**

1. `02_01_tipos_e_descricao_de_dados.ipynb`
   - objetos, atributos, matrizes de dados;
   - escalas de mensuração;
   - média, mediana, moda, quantis, variância e desvio-padrão;
   - fórmulas e cálculos manuais comparados com NumPy/pandas.
2. `02_02_visualizacao_de_dados.ipynb`
   - histogramas, boxplots, barras, dispersão, mapas de calor e gráficos multivariados;
   - escolha, leitura e crítica de gráficos;
   - acessibilidade de cores e prevenção de distorções visuais.
3. `02_03_similaridade_e_dissimilaridade.ipynb`
   - matriz de proximidade;
   - distâncias Euclidiana, Manhattan e Minkowski;
   - similaridade do cosseno, Jaccard e atributos binários/ordinais;
   - efeito da escala e comparação prática entre métricas.

**Atividade integradora:** análise exploratória documentada, incluindo tipagem dos atributos, estatísticas, visualizações, proximidades e conclusões.

**Critério de conclusão:** resultados manuais e computacionais conferem; gráficos possuem título, eixos, unidades e interpretação; atividade contempla dados mistos.

### Unidade III — Pré-processamento de Dados

**Carga prevista:** 8 horas  
**Referência principal no livro:** Capítulo 2, seções 2.4–2.6.

**Objetivos de aprendizagem**

- diagnosticar problemas de qualidade;
- tratar valores ausentes, ruído, duplicidade e inconsistências;
- integrar, transformar e codificar atributos;
- aplicar amostragem, redução de dimensionalidade e discretização sem vazamento de dados.

**Notebooks previstos**

1. `03_01_qualidade_limpeza_e_integracao.ipynb`
   - dimensões de qualidade;
   - ausências, duplicatas, conflitos e ruído;
   - junções e resolução básica de entidades;
   - relatório antes/depois da limpeza.
2. `03_02_transformacao_e_discretizacao.ipynb`
   - normalização, padronização e transformações;
   - codificação de categorias;
   - discretização por largura, frequência e critérios supervisionados;
   - pipelines para evitar vazamento.
3. `03_03_reducao_de_dados.ipynb`
   - amostragem e agregação;
   - seleção de atributos;
   - PCA: intuição geométrica, fórmula e aplicação;
   - análise do compromisso entre compressão e perda de informação.

**Atividade integradora:** construir um pipeline reprodutível para um conjunto propositalmente problemático e justificar cada transformação.

**Critério de conclusão:** pipeline separa ajuste e transformação, não apresenta vazamento, preserva dados brutos e mede o efeito das decisões.

### Unidade IV — Mineração de Padrões

**Carga prevista:** 8 horas  
**Referência principal no livro:** Capítulo 4, seções 4.1–4.3; Capítulo 5, seção 5.4, para padrões sequenciais.

**Objetivos de aprendizagem**

- representar dados transacionais e sequenciais;
- definir itemsets frequentes e regras de associação;
- calcular suporte, confiança e lift;
- explicar e implementar as etapas essenciais do Apriori;
- avaliar relevância e limitações das regras encontradas.

**Notebooks previstos**

1. `04_01_itemsets_e_regras_de_associacao.ipynb`
   - cesta de compras e representação one-hot;
   - suporte, confiança, lift e exemplos manuais;
   - geração e filtragem de regras.
2. `04_02_algoritmo_apriori.ipynb`
   - propriedade antimonótona;
   - geração e poda de candidatos;
   - implementação didática e comparação com biblioteca;
   - impacto dos limiares no custo e nos resultados.
3. `04_03_avaliacao_e_padroes_sequenciais.ipynb`
   - regras fortes versus interessantes;
   - correlação e armadilhas interpretativas;
   - introdução a padrões de sequência;
   - estudo de caso aplicado.

**Atividade integradora:** minerar regras, selecionar um subconjunto útil e apresentar interpretação de negócio sem atribuir causalidade indevida.

**Critério de conclusão:** métricas validadas manualmente, Apriori explicado passo a passo e conclusões sustentadas pelos resultados.

### Unidade V — Classificação e Regressão

**Carga prevista:** 12 horas  
**Referência principal no livro:** Capítulo 6, seções 6.1–6.6. Para regressão, seção 6.5 e complemento conceitual específico.

**Objetivos de aprendizagem**

- formular problemas supervisionados;
- preparar partições de treino, validação e teste;
- explicar e aplicar Naive Bayes, k-NN e árvores de decisão;
- ajustar regressão linear simples e múltipla;
- selecionar métricas adequadas e comparar modelos de modo confiável.

**Notebooks previstos**

1. `05_01_processo_e_avaliacao_de_classificacao.ipynb`
   - fluxo supervisionado e baseline;
   - matriz de confusão, acurácia, precisão, revocação, F1, ROC e AUC;
   - validação cruzada, desbalanceamento e custo de erros.
2. `05_02_classificadores_bayesianos_e_knn.ipynb`
   - Teorema de Bayes e hipótese de independência;
   - exemplo manual de Naive Bayes;
   - k-NN, métricas de distância, escala e escolha de _k_;
   - comparação experimental.
3. `05_03_arvores_de_decisao.ipynb`
   - entropia, ganho de informação e índice Gini;
   - construção manual de uma divisão;
   - treinamento, visualização, poda e importância de atributos;
   - sobreajuste e interpretabilidade.
4. `05_04_regressao_linear.ipynb`
   - regressão simples e múltipla;
   - mínimos quadrados, resíduos e pressupostos;
   - MAE, MSE, RMSE e coeficiente de determinação;
   - diagnóstico e interpretação cautelosa dos coeficientes.

**Atividade integradora:** comparar pelo menos três classificadores sob o mesmo protocolo e desenvolver uma análise de regressão com diagnóstico de resíduos.

**Critério de conclusão:** ausência de vazamento, sementes fixadas, protocolo comparável, métricas interpretadas e limitações explicitadas.

### Unidade VI — Análise de Grupos

**Carga prevista:** 10 horas  
**Referência principal no livro:** Capítulo 8, seções 8.1–8.5; tópicos selecionados do Capítulo 9 se necessários.

**Objetivos de aprendizagem**

- explicar objetivos, requisitos e dificuldades do agrupamento;
- preparar dados e escolher funções de distância;
- comparar métodos particionais, hierárquicos e baseados em densidade;
- aplicar k-means, agrupamento hierárquico e DBSCAN;
- avaliar coesão, separação, estabilidade e utilidade dos grupos.

**Notebooks previstos**

1. `06_01_fundamentos_e_kmeans.ipynb`
   - conceitos, representação e preparação;
   - função objetivo do k-means;
   - atribuição/atualização passo a passo;
   - inicialização, escala, escolha de _k_ e limitações.
2. `06_02_agrupamento_hierarquico_e_dbscan.ipynb`
   - ligações simples, completa, média e Ward;
   - dendrogramas e cortes;
   - densidade, `eps`, `min_samples`, ruído e formas não convexas;
   - comparação visual e quantitativa.
3. `06_03_avaliacao_de_agrupamentos.ipynb`
   - medidas internas e externas;
   - silhouette, Davies–Bouldin, Rand ajustado;
   - estabilidade, interpretação e perfil dos grupos;
   - seleção responsável de uma solução.

**Atividade integradora:** comparar três famílias de algoritmos em dados sintéticos e reais, justificando pré-processamento, métrica e escolha final.

**Critério de conclusão:** algoritmos comparados sob condições documentadas, hiperparâmetros justificados e grupos interpretados sem tratá-los como verdades naturais.

### Unidade VII — Detecção de Outliers

**Carga prevista:** 6 horas  
**Referência principal no livro:** Capítulo 11, especialmente seções 11.1–11.5.

**Objetivos de aprendizagem**

- distinguir outliers globais, contextuais e coletivos;
- reconhecer causas, desafios e efeitos das anomalias;
- aplicar abordagens estatísticas, de proximidade, densidade e agrupamento;
- avaliar métodos quando rótulos são raros;
- decidir quando investigar, transformar ou manter uma observação anômala.

**Notebooks previstos**

1. `07_01_conceitos_e_metodos_estatisticos.ipynb`
   - tipos e causas de anomalias;
   - escore-z, intervalo interquartil e métodos robustos;
   - pressupostos, exemplos manuais e visualizações.
2. `07_02_proximidade_densidade_e_agrupamento.ipynb`
   - distância ao k-ésimo vizinho e LOF;
   - DBSCAN e isolamento de pontos;
   - comparação de métodos em diferentes geometrias;
   - avaliação, investigação e comunicação de alertas.

**Atividade integradora:** analisar um cenário de fraude, falha ou qualidade de dados, comparar métodos e produzir uma lista priorizada de observações para investigação.

**Critério de conclusão:** comparação considera escala, dimensionalidade e contaminação; decisões não removem automaticamente observações; limitações estão registradas.

## 8. Consolidação final

Após concluir as sete unidades:

- executar todos os notebooks em ambiente limpo e na ordem proposta;
- revisar links, caminhos relativos, imagens, fórmulas e referências;
- verificar consistência terminológica e visual;
- conferir cobertura de todos os itens da ementa;
- criar uma avaliação ou projeto final que percorra o KDD completo;
- produzir versão do estudante e, se aplicável, versão com soluções;
- atualizar `registro_execucao.md` e o README.

## 9. Definição de pronto para cada notebook

Um notebook somente será marcado como concluído quando:

- possuir objetivos e pré-requisitos explícitos;
- alternar explicação, fórmula, código e interpretação de forma coerente;
- executar sequencialmente em ambiente limpo, sem erros;
- não depender de estado oculto nem de caminhos absolutos;
- fixar sementes em operações aleatórias;
- incluir ao menos um exemplo e uma atividade;
- explicar os resultados exibidos, em vez de apenas gerar saídas;
- identificar fontes de dados, imagens e referências;
- cumprir `contexto/diretrizes_formatacao.md`;
- passar pelos revisores definidos em `contexto/revisores/README.md`;
- ter o checklist de consolidação aprovado.

## 10. Ordem de execução

1. Infraestrutura e notebook-modelo.
2. Unidade I.
3. Unidade II.
4. Unidade III.
5. Unidade IV.
6. Unidade V.
7. Unidade VI.
8. Unidade VII.
9. Projeto integrador e revisão final.

O arquivo `contexto/registro_execucao.md` é a fonte de verdade sobre o andamento. Ele deve ser atualizado na mesma alteração que criar, revisar ou validar qualquer entrega.
