# Gabarito — 04.05 Avaliação responsável de regras

## U04-NB05-V01

A confiança 0,90 informa que 90% das ocorrências de $A$ são acompanhadas por $B$. Porém, $B$ também aparece em 90% da base completa. Conhecer $A$, portanto, não altera a probabilidade de $B$.

As três métricas que revelam a independência são:

- $\operatorname{lift}=0{,}90/0{,}90=1$;
- $\operatorname{leverage}=P(A\cap B)-P(A)P(B)=0$;
- $\operatorname{conviction}=P(\neg B)/P(\neg B\mid A)=1$.

Logo, a confiança é numericamente alta apenas porque o consequente é muito comum; a regra não acrescenta informação sobre ele.

**Rubrica (3 pontos):** reconhecer a taxa-base de $B$ (1), citar as três métricas e seus valores (1), concluir que $A$ não acrescenta informação (1).

## U04-NB05-E01

Nos dois casos, $N=1.000$ e o *lift* é 2.

No Caso 3:

$$N\times\operatorname{leverage}=1.000\times0{,}002=2.$$

Há 4 coocorrências observadas, 2 esperadas e, portanto, excesso absoluto de apenas 2. O antecedente ocorre 20 vezes: 4 são acompanhadas por $B$ e 16 violam a regra. A taxa de violação é $16/20=0{,}80$; confiança e *conviction* são 0,20 e 1,125.

No Caso 4:

$$N\times\operatorname{leverage}=1.000\times0{,}16=160.$$

Há 320 coocorrências observadas, 160 esperadas e excesso absoluto de 160. O antecedente ocorre 400 vezes: 320 são acompanhadas por $B$ e 80 violam a regra. Embora existam mais violações em número bruto, a taxa é $80/400=0{,}20$; confiança e *conviction* são 0,80 e 3.

Assim, o mesmo *lift* expressa o mesmo ganho relativo sobre a taxa-base, mas não o mesmo volume, impacto absoluto ou frequência de exceções. O Caso 4 tem muito mais alcance e consistência direcional. Isso não obriga a escolhê-lo: custos, valor de cada ocorrência, estabilidade e domínio ainda podem tornar uma regra rara relevante.

**Rubrica (6 pontos):** excessos 2 e 160 (2), violações e taxas 80% e 20% (2), explicação da insuficiência do *lift* e ressalva contextual (2).

## U04-NB05-E02

Não há uma única seleção correta. Uma solução completa deve apresentar:

1. origem, período, unidade de análise e significado dos itens;
2. preparação rastreável, preservando os dados brutos e tratando identificadores, ausências e duplicatas;
3. pelo menos duas combinações de suporte e confiança mínimos, com o número de itemsets e regras produzido em cada uma;
4. no máximo cinco regras finais, acompanhadas das contagens $n_{11}$ e $n_{10}$ e de suporte, confiança, *lift*, *leverage* e *conviction*;
5. conferência manual das cinco métricas para pelo menos uma regra;
6. análise de estabilidade por período, segmento ou reamostragem;
7. justificativa de utilidade, custos de acerto e erro, redundâncias e explicações alternativas;
8. linguagem não causal e, caso haja proposta de intervenção, indicação de que seu efeito exigiria desenho causal separado.

Exemplo de quadro de decisão:

| Regra | $n_{11}$ | $n_{10}$ | Suporte | Confiança | Lift | Leverage | Conviction | Estabilidade | Uso e limitação |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| $A\rightarrow B$ | valor | valor | valor | valor | valor | valor | valor | variação por período | hipótese de uso e possível explicação alternativa |

Uma regra rara com *lift* alto pode ser instável; uma regra com confiança alta pode apenas refletir a taxa-base; uma regra frequente pode ter associação negativa. A recomendação deve justificar conjuntamente as métricas e o contexto, sem calcular uma média arbitrária entre elas.

**Rubrica (10 pontos):** documentação e preparação (2), limiares e rastreabilidade (2), métricas, contagens e conferência manual (2), estabilidade (2), utilidade, limitações e cautela causal (2).
