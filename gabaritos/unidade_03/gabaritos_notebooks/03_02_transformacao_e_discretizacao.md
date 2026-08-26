# Gabarito — 03.02 Transformação e discretização

## U03-NB02-V01

`fit_transform` no teste aprende outra mediana, outra média, outro desvio e possivelmente outro conjunto de categorias. Assim, treino e teste passam a ocupar representações diferentes e o teste deixa de simular novos dados processados pelo sistema treinado. O correto é `fit_transform` no treino e apenas `transform` no teste.

**Rubrica:** identificar o novo ajuste (1 ponto), explicar a inconsistência de representação (1 ponto) e indicar o fluxo correto (1 ponto).

## U03-NB02-E01

```python
imputador = preprocessador.named_transformers_["num"].named_steps["imputacao"]
mediana_treino = imputador.statistics_[numericas.index("idade")]
mediana_teste = X_teste["idade"].median()

pd.Series({
    "mediana_aprendida_no_treino": mediana_treino,
    "mediana_observada_no_teste": mediana_teste,
})
```

Com a semente fixada, a mediana aprendida no treino deve ser usada para preencher tanto treino quanto teste. A mediana do teste pode ser comparada apenas para fins didáticos; usá-la na transformação permitiria que o conjunto reservado definisse o sistema.

**Rubrica:** acesso correto ao objeto ajustado (2 pontos), comparação (1 ponto) e justificativa de prevenção de vazamento (2 pontos).
