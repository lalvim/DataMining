# Unidade IV — Gabarito dos exercícios conceituais

## U04-C01
Transação é o evento; item é um elemento; itemset é um conjunto; regra relaciona antecedentes e consequentes disjuntos. Binário perde quantidade, ordem, preço e possivelmente tempo. **Critério:** quatro definições e duas perdas.

## U04-C02
Suporte conjunto $=30/100=0,30$; confiança A→B $=30/40=0,75$; B→A $=30/50=0,60$; *lift* $=0,75/0,50=0,60/0,40=1,50$. **Critério:** resultados e denominadores.

## U04-C03
Suporte usa a mesma união e *lift* equivale a $P(A,B)/(P(A)P(B))$, simétrico. Confiança usa $P(A)$ ou $P(B)$ no denominador. **Critério:** simetria e condicionamento.

## U04-C04
Se o consequente ocorre em 95% dos casos, confiança 90% produz *lift* $0,90/0,95\approx0,947$. O antecedente está associado a taxa menor que a base. **Critério:** exemplo coerente e interpretação.

## U04-C05
Suporte: prevalência conjunta; confiança: proporção condicional; *lift*: razão contra taxa-base; alavancagem: diferença absoluta contra independência; convicção: falhas esperadas versus observadas. **Critério:** distinção e pergunta de cada uma.

## U04-C06
As transações que contêm $Y$ formam subconjunto das que contêm $X$ quando $X\subseteq Y$; logo sua contagem e suporte não podem ser maiores. **Critério:** argumento por inclusão.

## U04-C07
`{A,B,C}` é infrequente. Nada se conclui sobre `{A,C}`, que não é superset de `{A,B}`. **Critério:** poda correta sem extrapolação.

## U04-C08
Candidatos: AB, AC, AD, BC, BD, CD. ABC e ABD podem ser podados por conter AB. **Critério:** seis pares e supersets corretos.

## U04-C09
Gerar uniões, podar por subconjuntos infrequentes, contar na base e reter por limiar. Candidato ainda precisa ser contado; frequente já atingiu o limiar. **Critério:** ordem e distinção.

## U04-C10
Limiar menor inclui todos os anteriores e possivelmente muitos novos, aumenta candidatos, memória e risco de coincidências, mas revela nichos. **Critério:** quatro efeitos e ausência de garantia de utilidade.

## U04-C11
Comparar conjuntos e suportes nos mesmos dados/limiar; incluir base vazia conforme contrato, itens nunca/frequentemente presentes, suportes no limiar, empates e itemsets de vários tamanhos. **Critério:** valores, identidades e casos-limite.

## U04-C12
Contagem, suporte, *lift*, alavancagem, estabilidade temporal, validação externa, redundância, novidade, custo, acionabilidade e riscos são aceitáveis. **Critério:** seis justificativas distintas.

## U04-C13
Seleção, sazonalidade, público e disponibilidade podem confundir. Um experimento randomizado elegível, com grupo controle e desfecho pré-definido, pode estimar efeito. **Critério:** confundimento e desenho causal.

## U04-C14
Itemset ignora ordem; sequência preserva. `⟨A,C⟩` ocorre na primeira e terceira, não na segunda. **Critério:** três classificações.

## U04-C15
Suporte $=3/5=0,60$. Cada entidade contribui no máximo uma vez para prevalência entre clientes. **Critério:** 60% e unidade do denominador.

## U04-C16
Resposta-modelo: sessão de 30 minutos; eventos simultâneos agrupados como itemset; lacuna máxima de 10 minutos. Restrições menores excluem ocorrências e tendem a reduzir suporte. **Critério:** regras explícitas e efeitos.
