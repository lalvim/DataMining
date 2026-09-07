# Gabarito — 04.02 Algoritmo Apriori

## U04-NB02-V01

Não. Pela propriedade antimonótona do suporte, todo superconjunto de um itemset tem suporte menor ou igual ao suporte desse itemset. Se o par já está abaixo do suporte mínimo, qualquer trio que o contenha também estará e pode ser podado sem ter seu suporte contado.

**Rubrica:** negar corretamente (1 ponto), enunciar a relação de suporte (1 ponto) e relacioná-la à poda (1 ponto).

## U04-NB02-E01

Uma ampliação possível da base é:

```python
novas_transacoes = transacoes + [
    {"pao", "cafe", "leite"},
    {"arroz", "cafe"},
    {"pao", "manteiga"},
    {"arroz", "feijao", "leite"},
]

linhas = []
for limiar in [0.20, 0.30]:
    frequentes, auditoria = apriori_didatico(novas_transacoes, limiar)
    linhas.append({
        "suporte_minimo": limiar,
        "itemsets_frequentes": len(frequentes),
        "candidatos_avaliados": int(auditoria["candidatos"].sum()),
        "maior_itemset": max(map(len, frequentes), default=0),
    })

pd.DataFrame(linhas)
```

Os valores exatos dependem das quatro transações acrescentadas. Uma resposta completa deve explicitar os novos dados, lembrar que cada ocorrência agora vale $1/16$ e mostrar que o aumento do suporte mínimo não pode aumentar o conjunto de itemsets frequentes. Também deve discutir que itens adicionados juntos podem alterar tanto a frequência individual quanto a coocorrência, mudando a fronteira de poda.

Para conferir a implementação, codifique `novas_transacoes` com `TransactionEncoder`, execute `mlxtend.frequent_patterns.apriori` nos mesmos limiares e compare os pares `(itemset, suporte)` com tolerância numérica.

**Rubrica (8 pontos):** quatro transações documentadas (1), execução em pelo menos quatro limiares (2), contagem de candidatos e frequentes (2), comparação com a biblioteca (2), interpretação da poda e do novo denominador (1).
