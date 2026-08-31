# Adendo de revisão — distribuições, `log1p` e `skew`

**Data:** 2026-08-31  
**Material:** `notebooks/unidade_03/03_02_transformacao_e_discretizacao.ipynb`  
**Resultado:** aprovado

## Alteração verificada

Foram acrescentadas explicações antes dos blocos de geração e transformação para justificar o uso de lognormal, Poisson, binomial, função logística, `log1p` e `skew`.

## Parecer

- **Didática:** cada função foi ligada ao tipo de atributo que simula ou à pergunta que ajuda a responder.
- **Exatidão:** os parâmetros da lognormal foram distinguidos das estatísticas na escala monetária; `binomial(1, p)` foi caracterizada como Bernoulli; `log1p` não foi apresentado como garantia de normalidade.
- **Interpretação:** sinal e magnitude de `skew` foram explicados sem impor limiar universal, e a saída de 2,26 para -0,06 foi interpretada no contexto da simulação.
- **Reprodutibilidade:** o notebook foi reexecutado com 15 células, cinco células de código, IDs únicos e nenhuma saída de erro.

Não foram identificados achados obrigatórios.
