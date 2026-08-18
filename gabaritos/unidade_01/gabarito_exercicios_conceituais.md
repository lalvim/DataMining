# Unidade I — Gabarito dos exercícios conceituais

**Orientação:** respostas equivalentes, bem justificadas e coerentes com o contexto devem ser aceitas. Cada item vale integralmente quando contempla os elementos essenciais indicados.

## U01-C01 — Dado, informação, padrão e conhecimento

**Resposta-modelo:** dado: registro “compra 845, produto X, 18h42, R$ 20”; informação: total de vendas de X por horário; padrão: X e Y coocorrem persistentemente; conhecimento: após validação, a associação orienta uma exposição conjunta monitorada. A progressão acrescenta contexto, regularidade, validação e uso decisório.

**Critérios:** exemplo correto dos quatro níveis; relação entre eles; utilidade não confundida com mera correlação.

## U01-C02 — Mineração e KDD

**Resposta-modelo:** mineração é a etapa de descoberta de padrões/modelos; KDD inclui problema, seleção, compreensão, limpeza, transformação, mineração, avaliação e comunicação. Focar apenas no algoritmo pode produzir alvo inadequado, vazamento, dados enviesados, métrica inútil ou resultado sem ação válida.

**Critérios:** distinção de escopo e dois riscos concretos.

## U01-C03 — Tarefas

**Resposta:** a) regressão → consumo numérico; b) classificação → rótulo legítima/fraude; c) associação → itemsets/regras; d) agrupamento → grupos/perfis; e) detecção de outliers → escore ou alerta por sensor.

## U01-C04 — Preditivo e descritivo

**Resposta-modelo:** tarefas preditivas aprendem uma relação com alvo conhecido para novos casos; descritivas buscam estrutura sem alvo. A distinção é insuficiente quando, por exemplo, outliers usam rótulos, grupos são avaliados por rótulos externos ou padrões descritivos alimentam uma decisão preditiva.

## U01-C05 — Quatro usos do Iris

**Resposta possível:** classificação: medidas → espécie; agrupamento: medidas → grupos sem rótulo; regressão: demais medidas → comprimento da pétala; outliers: medidas → escore de anomalia. Devem estar explícitas pergunta, entrada e saída.

## U01-C06 — Ordem do KDD

**Resposta:** compreender problema → selecionar/compreender dados → limpar/transformar → minerar → avaliar/interpretar → comunicar conhecimento. É iterativo porque falhas de qualidade, baixa utilidade ou resultados inesperados exigem retorno.

## U01-C07 — Formulação de evasão

**Resposta possível:** “No início da oitava semana, priorizar estudantes ativos com risco de abandonar até o fim do semestre para oferta de apoio”. Unidade: matrícula aluno-disciplina; tarefa: classificação; saída: risco/rótulo; sucesso técnico: revocação sob capacidade fixa; institucional: aumento de permanência sem desigualdade entre grupos.

**Critérios:** seis elementos pedidos e ausência de solução centrada apenas no algoritmo.

## U01-C08 — Atributos

**Resposta possível:** histórico de aprovação, frequência disponível até a semana de corte, acessos ao AVA, carga matriculada e solicitações de apoio. Para cada um, aceitar análise coerente de disponibilidade temporal, ausências/erros e risco de proxy, vigilância ou interpretação causal.

## U01-C09 — Classe rara

**Resposta:** a previsão constante não encontra positivos. É necessário conhecer custo e capacidade, priorizando, por exemplo, precisão, revocação, F1 ou curva precisão-revocação. Baseline possível: regra simples baseada em um indicador disponível ou seleção aleatória da mesma quantidade de casos.

## U01-C10 — Vazamento

**Resposta:** vazamento usa informação indisponível no instante real ou derivada do alvo. a) válida se apenas semestres anteriores; b) vaza por usar o final do semestre; c) potencialmente válida, com análise ética; d) vaza diretamente.

## U01-C11 — Associação e causa

**Resposta possível:** estação quente, promoções, localização conjunta, perfil de cliente, viagem ou evento externo. Coocorrência não estabelece ordem temporal, mecanismo nem controle de confundidores.

## U01-C12 — Agrupamento de bairros

**Resposta esperada:** perguntas de controle sobre cobertura e atualização; relevância/escala dos atributos; estabilidade e validação dos grupos; risco de estigmatização e distribuição de recursos. Uma pergunta substantiva por dimensão.

## U01-C13 — Custos dos erros

**Resposta-modelo:** falso positivo em fraude bloqueia transação legítima; falso negativo permite perda. Em inspeção, falso positivo consome equipe/parada; falso negativo pode permitir falha grave. Limiar depende de prevalência, capacidade e custos, que diferem nos cenários.

## U01-C14 — Plano KDD

**Rubrica:** problema/decisão 20%; população e tarefa 15%; dados e disponibilidade 15%; etapas/entregas 20%; avaliação 15%; riscos, comunicação e monitoramento 15%.

## U01-C15 — Desafio

**Resposta-modelo:** KDD é processo de descoberta; mineração é sua etapa analítica; aprendizado de máquina fornece métodos que aprendem com dados; ciência de dados é prática mais ampla envolvendo aquisição, engenharia, análise, comunicação e produto. Aceitar outros diagramas se definições e duas fontes sustentarem as fronteiras.
