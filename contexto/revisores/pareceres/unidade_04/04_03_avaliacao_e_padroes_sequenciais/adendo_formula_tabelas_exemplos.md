# Adendo de revisão — fórmulas, tabelas e exemplos

**Data:** 2026-09-16  
**Decisão:** Aprovado

## Escopo

Revisão da ligação didática entre as fórmulas de *leverage* e *conviction*, o código que produz as tabelas e os três exemplos interpretados.

## Verificações

- Foi criada uma seção própria antes do código, tornando explícito o início do exemplo aplicado.
- Cada coluna das duas tabelas possui fórmula e significado definidos.
- A passagem de probabilidades para contagens usa explicitamente as 12 transações do conjunto.
- A igualdade entre excesso de coocorrências e $N\times\operatorname{Leverage}$ está demonstrada.
- A igualdade entre *conviction* e a razão entre falhas esperadas e observadas está justificada pelo fator comum $N P(A)$.
- O texto esclarece por que contagens esperadas podem ser fracionárias.
- Os três exemplos identificam $P(A)$, $P(B)$ e $P(A\cap B)$ antes de substituir valores nas fórmulas.
- Cada resultado é relacionado à linha correspondente da Tabela 1 ou da Tabela 2.
- Os cálculos reproduzem as saídas: *leverage* 0,125 e aproximadamente 0,208; *conviction* 2,5, 3,5 e infinito.
- O notebook foi executado integralmente: 17 células, seis de código, uma figura, identificadores únicos, atividades correspondentes aos gabaritos e nenhuma saída de erro.

## Conclusão

A sequência fórmula → coluna da tabela → substituição numérica → interpretação está agora explícita e rastreável. Não há correções obrigatórias pendentes.
