# Gabarito — 03.01 Qualidade, limpeza e integração

## U03-NB01-V01

Marcar a idade impossível como ausente reconhece que não conhecemos o valor real. Preencher com a mediana fornece um valor operacional baseado no grupo, não uma observação recuperada da pessoa. A imputação pode reduzir variabilidade, alterar associações e ser inadequada se o mecanismo de ausência estiver relacionado a fatores não considerados.

**Rubrica:** distinguir validade de acurácia (1 ponto), interpretar imputação como estimativa (1 ponto) e indicar uma limitação estatística (1 ponto).

## U03-NB01-E01

Uma solução possível é:

```python
def ausencias_por_coluna(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.isna()
        .mean()
        .rename("proporcao_ausente")
        .to_frame()
        .sort_values("proporcao_ausente", ascending=False)
    )

sem_contrato = int(integrados["_merge"].eq("left_only").sum())
resultado = ausencias_por_coluna(clientes_brutos)
resultado.loc["clientes_sem_contrato", "proporcao_ausente"] = sem_contrato / len(integrados)
resultado
```

Na base bruta, `idade`, `email` e `mensalidade` têm uma ausência em oito linhas, isto é, 12,5% cada. Após a junção, um dos sete clientes limpos, cerca de 14,3%, não possui contrato correspondente. Essa segunda medida não é ausência de célula original; é falta de correspondência entre fontes e deve ser relatada separadamente.

**Rubrica:** cálculo por coluna (2 pontos), correspondência da junção (2 pontos) e duas interpretações corretas (2 pontos).
