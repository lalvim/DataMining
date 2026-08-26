# Unidade III — Gabarito dos exercícios conceituais

**Uso:** material separado do estudante. Respostas equivalentes, tecnicamente justificadas, são aceitáveis.

## U03-C01

Completude: campos preenchidos; validade: conformidade com formato/domínio; consistência: compatibilidade entre campos/fontes; unicidade: uma representação por entidade ou evento; atualidade: valor adequado ao período de uso; acurácia: proximidade do estado real. Exemplo válido e inexato: idade 40 dentro do domínio, quando a pessoa tem 37. **Critério:** definir as seis dimensões, exemplificar e separar validade de verdade factual.

## U03-C02

Excluir pode ser aceitável com pequena proporção e mecanismo aproximadamente aleatório, mas reduz amostra e pode enviesar. Mediana é robusta, porém reduz variabilidade e ignora relações. Modelar a ausência ou acrescentar indicador pode capturar informação do processo de coleta, sem transformar o ausente em valor conhecido. Devem-se comparar grupos com/sem renda, investigar motivo e tempo, medir sensibilidade e ajustar qualquer imputador apenas no treino. **Critério:** hipóteses, riscos e diagnósticos.

## U03-C03

Diferenças de grafia impedem duplicatas exatas; homônimos tornam nome insuficiente. Um fluxo defensável padroniza campos, cria candidatos, calcula evidências em múltiplos atributos, define limiares, revisa casos ambíguos, preserva IDs/fontes e avalia falsos pares e não pares. **Critério:** reconhecer ambos os erros e propor rastreabilidade.

## U03-C04

Verificar chave, tipo, domínio, ausências, duplicatas, cobertura e cardinalidade esperada. Em muitos-para-muitos, cada combinação de linhas correspondentes é produzida, multiplicando registros e podendo inflar somas. `validate` e `indicator` ajudam a auditar. **Critério:** explicar produto combinatório e controle.

## U03-C05

Indicadores possíveis: linhas, entidades únicas, ausências por coluna, duplicatas, violações de domínio, conflitos entre campos, correspondências de junção e distribuições. Regras detectam apenas problemas definidos; valores plausíveis ainda podem ser falsos. **Critério:** seis indicadores e limite epistêmico.

## U03-C06

Com mínimo 10 e máximo 40: `10→0`, `20→1/3`, `40→1`. Aplicando os limites aprendidos ao valor 50, $(50-10)/(40-10)=4/3\approx1,33$. Novos valores podem sair de `[0,1]`; não se devem recalcular limites no teste. **Critério:** cálculo e interpretação.

## U03-C07

$z=(65-80)/10=-1,5$. O valor está 1,5 desvio-padrão abaixo da média. Padronizar muda centro e escala, mas não garante normalidade, simetria nem ausência de outliers. **Critério:** resultado e limite.

## U03-C08

Escolaridade tem ordem substantiva e pode usar codificação ordinal se o algoritmo e a interpretação aceitarem essa estrutura; distâncias iguais entre níveis não devem ser presumidas. Município é nominal e convém *one-hot* ou outra representação nominal. Categorias novas precisam de política como ignorar, agrupar em "outros" ou refazer controladamente o vocabulário. **Critério:** significado e produção.

## U03-C09

Largura igual entre 1 e 20 cria intervalos de largura 4,75, deixando possivelmente intervalos centrais vazios; frequência tenta distribuir cerca de 1–2 valores por intervalo, com cortes concentrados entre 1 e 5 e um intervalo contendo 20. Quantis dependem fortemente da amostra e empates; ambos perdem ordem fina dentro dos intervalos. **Critério:** contraste e limitações, sem exigir limites únicos para quantis.

## U03-C10

Exemplo de contaminação pelo teste: calcular mediana ou escala em todos os dados antes de separar; impedir com pipeline ajustado em treino dentro de cada partição. Exemplo temporal: usar data de cancelamento para prever cancelamento; impedir definindo instante de previsão e usando apenas atributos disponíveis até ele. **Critério:** dois mecanismos distintos e controles apropriados.

## U03-C11

Separar treino/teste; ajustar imputador, codificador e escalonador somente no treino; transformar treino; ajustar modelo no treino transformado; transformar teste com os mesmos objetos; prever e avaliar uma vez no teste. Em validação cruzada, todos os `fit` ocorrem dentro de cada dobra de treino. **Critério:** ordem e escopo dos ajustes.

## U03-C12

Amostragem reduz linhas e pode perder subgrupos; agregação muda granularidade e perde variação individual; seleção mantém colunas originais e pode remover sinal complementar; extração cria atributos, como componentes, e perde interpretação/reconstrução perfeita. **Critério:** objeto reduzido, finalidade e perda para cada estratégia.

## U03-C13

Estratificar por alvo controla apenas sua distribuição. Regiões, datas ou grupos demográficos podem continuar ausentes ou distorcidos, especialmente se a coleta original for enviesada. Devem-se auditar margens e interseções relevantes e considerar desenho amostral. **Critério:** distinguir classe de representatividade multidimensional.

## U03-C14

Sem escala, atributos de maior variância/unidade dominam a covariância. Variância acumulada é a soma das proporções associadas aos componentes mantidos. PCA ignora o alvo; sinal preditivo pode estar em direção de baixa variância. **Critério:** escala, definição e diferença entre variância e utilidade.

## U03-C15

A fração mantida é $8/40=0,20$ ou 20%. Avaliar desempenho na tarefa com validação adequada, estabilidade, tempo/memória, RMSE por atributo, impacto em subgrupos e perda de interpretabilidade. **Critério:** 20% e ao menos três critérios adicionais.

## U03-C16 — Desafio

Uma proposta completa cria ou escolhe dados com ausências e escalas variadas, fixa as mesmas divisões repetidas, compara pipeline interno a pré-ajuste global, mede a mesma métrica e sua incerteza e registra tempo. A hipótese é que o fluxo global pode gerar estimativa otimista, mas o tamanho depende dos dados. **Critério:** controle pareado, repetições, incerteza e interpretação não determinista.
