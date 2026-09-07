# Gabarito — 04.03 Avaliação de regras e padrões sequenciais

## U04-NB03-V01

Ao transformar uma jornada em uma cesta, perde-se a ordem dos eventos, a distância temporal entre eles e a posição ou repetição de cada ocorrência. Assim, `visita → busca → compra` torna-se apenas a coocorrência de três itens. Uma regra de associação obtida dessa cesta não autoriza afirmar que a visita ou a busca ocorreu antes da compra.

**Rubrica:** mencionar ordem (1 ponto), indicar ao menos outra informação perdida (1 ponto) e evitar interpretação temporal da regra de associação (1 ponto).

## U04-NB03-E01

Uma solução possível é acrescentar duas jornadas e adotar a regra de que eventos empatados preservam a ordem original do registro:

```python
jornadas_estendidas = jornadas + [
    ["visita", "busca", "produto", "compra"],
    ["visita", "produto", "carrinho", "abandono"],
]

padroes = [
    ("visita", "produto"),
    ("produto", "compra"),
    ("busca", "compra"),
    ("visita", "busca", "compra"),
]

pd.DataFrame({
    "padrao": [" → ".join(p) for p in padroes],
    "suporte_original": [suporte_sequencial(p, jornadas) for p in padroes],
    "suporte_estendido": [suporte_sequencial(p, jornadas_estendidas) for p in padroes],
})
```

Com essas jornadas, o denominador passa de 6 para 8. A primeira nova jornada contém os quatro padrões; a segunda contém apenas `visita → produto`. Repetições dentro de uma mesma jornada não devem contar mais de uma vez para o suporte por entidade. Outra extensão é válida se os dados, a regra de ordenação e os efeitos observados forem documentados.

**Rubrica (6 pontos):** duas jornadas válidas (1), regra para empates ou ordenação (1), recálculo reproduzível (2), interpretação do numerador e denominador (2).

## U04-NB03-E02

Não há uma única seleção correta. Uma entrega-modelo deve conter:

1. documentação da origem, unidade de análise e significado de cada item;
2. limpeza que preserve uma cópia dos dados brutos e trate identificadores, ausências e duplicatas;
3. pelo menos dois suportes mínimos, registrando o número de itemsets ou padrões encontrados;
4. no máximo cinco resultados finais, escolhidos com métricas adequadas — por exemplo, suporte, confiança, lift, leverage e conviction para regras;
5. verificação de estabilidade por período, segmento ou reamostragem;
6. hipótese de uso no domínio e explicitação de riscos, custos e limitações;
7. linguagem não causal: associação e precedência observada não provam efeito de uma ação.

Exemplo de quadro de decisão:

| Resultado | Frequência | Ganho sobre a base | Estabilidade | Uso proposto | Limitação |
|---|---:|---:|---|---|---|
| $X\rightarrow Y$ | suporte | lift/leverage | variação por período | organização de oferta | viés de exposição |
| $A\rightarrow B\rightarrow C$ | suporte sequencial | diferença entre grupos | presença em janelas | análise de jornada | intervalos ignorados |

Se houver escolha de limiares ou regras com base nos mesmos dados usados para reportar desempenho, a entrega deve reconhecer o caráter exploratório ou reservar dados/períodos para validação.

**Rubrica (10 pontos):** documentação e limpeza (2), dois limiares e rastreabilidade (2), até cinco resultados com métricas (2), estabilidade (2), aplicação e limitações causais/éticas (2).
