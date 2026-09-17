# Gabarito — 04.04 Padrões sequenciais

## U04-NB04-V01

Ao transformar uma jornada em uma cesta, perde-se a ordem dos eventos, a distância temporal entre eles e a posição ou repetição de cada ocorrência. Assim, `visita → busca → compra` torna-se apenas a coocorrência de três itens. Uma regra de associação obtida dessa cesta não autoriza afirmar que visita ou busca ocorreu antes da compra.

**Rubrica:** mencionar ordem (1 ponto), indicar ao menos outra informação perdida (1) e evitar interpretação temporal da regra de associação (1).

## U04-NB04-E01

Uma solução possível é acrescentar duas jornadas e declarar que eventos com o mesmo instante preservam a ordem original do registro:

```python
jornadas_estendidas = {
    **jornadas,
    "C7": ["visita", "busca", "produto", "produto", "compra"],
    # Em C8, produto e busca empataram; a ordem original foi preservada.
    "C8": ["visita", "produto", "busca", "compra"],
}

pd.DataFrame({
    "padrao": [" → ".join(p) for p in padroes],
    "suporte_original": [
        sum(contem_subsequencia(s, p) for s in jornadas.values()) / len(jornadas)
        for p in padroes
    ],
    "suporte_estendido": [
        sum(contem_subsequencia(s, p) for s in jornadas_estendidas.values())
        / len(jornadas_estendidas)
        for p in padroes
    ],
})
```

As duas novas jornadas contêm os quatro padrões avaliados. O denominador passa de 6 para 8, produzindo:

| Padrão | Suporte original | Suporte estendido |
|---|---:|---:|
| visita → produto | $5/6\approx0{,}833$ | $7/8=0{,}875$ |
| produto → compra | $4/6\approx0{,}667$ | $6/8=0{,}750$ |
| busca → compra | $3/6=0{,}500$ | $5/8=0{,}625$ |
| visita → busca → compra | $2/6\approx0{,}333$ | $4/8=0{,}500$ |

A repetição de `produto` em C7 não aumenta o numerador mais de uma vez, pois o suporte é calculado por entidade. Outra solução é válida se as jornadas, a política de empates e os cálculos forem coerentes e documentados.

**Rubrica (7 pontos):** duas jornadas válidas (1), repetição tratada por entidade (1), regra de empate (1), recálculo reproduzível (2), interpretação de numerador e denominador (2).

## U04-NB04-E02

Não há uma única base ou seleção correta. Uma entrega-modelo deve conter:

1. identificação da entidade e do evento, além do período observado;
2. regra de ordenação por tempo e critério explícito para empates;
3. decisão sobre eventos repetidos, sessões, janelas e lacunas máximas;
4. pelo menos dois suportes mínimos e o número de padrões encontrado em cada caso;
5. no máximo cinco padrões finais, com numerador, denominador e suporte por entidade;
6. verificação de estabilidade por período, segmento ou reamostragem;
7. hipótese de uso e limitações, sem converter precedência observada em causalidade.

Exemplo de quadro de decisão:

| Padrão | Entidades com o padrão | Total de entidades | Suporte | Estabilidade | Uso proposto | Limitação |
|---|---:|---:|---:|---|---|---|
| $A\rightarrow B\rightarrow C$ | contagem | contagem | proporção | variação por período | análise de jornada | intervalos e confundidores ignorados |

Se os limiares e os padrões forem escolhidos nos mesmos dados usados para avaliar a qualidade, o relatório deve reconhecer o caráter exploratório ou reservar outro período para confirmação.

**Rubrica (10 pontos):** unidade e ordenação (2), empates/repetições/janelas (2), dois limiares e rastreabilidade (2), padrões com contagens e estabilidade (2), aplicação e ressalva causal (2).
