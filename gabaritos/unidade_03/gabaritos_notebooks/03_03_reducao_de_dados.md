# Gabarito — 03.03 Redução de dados

## U03-NB03-V01

Escolher o número de componentes pelo resultado do teste transforma o teste em dado de seleção. A estimativa final fica otimista porque a configuração foi adaptada às particularidades desse conjunto. O número deve ser escolhido no treino, eventualmente por validação interna, e o teste deve ser usado apenas na avaliação final.

**Rubrica:** identificar adaptação ao teste (1 ponto), efeito sobre a estimativa (1 ponto) e fluxo correto (1 ponto).

## U03-NB03-E01

```python
linhas = []
for limiar in [0.80, 0.90, 0.95]:
    k = int(np.searchsorted(variancia_acumulada, limiar) + 1)
    pca = PCA(n_components=k).fit(X_treino_pad)
    reconstruido = pca.inverse_transform(pca.transform(X_teste_pad))
    rmse = np.sqrt(np.mean((X_teste_pad - reconstruido) ** 2))
    linhas.append({
        "limiar": limiar,
        "componentes": k,
        "compressao": k / X.shape[1],
        "rmse_teste": rmse,
    })

pd.DataFrame(linhas).round(3)
```

A resposta deve recomendar uma configuração com critério explícito. Por exemplo, 90% pode ser escolhido como compromisso se a redução adicional do RMSE em 95% não compensar mais componentes; outra decisão é aceitável se considerar desempenho futuro, custo e interpretabilidade. O teste serve aqui para comparar reconstrução no exercício; em uma seleção formal, a escolha deve usar validação interna e reservar um teste final.

**Rubrica:** cálculo dos três limiares (3 pontos), compressão e RMSE (2 pontos), recomendação justificada e ressalva sobre seleção (2 pontos).

## U03-NB03-E02

Não existe uma única base ou sequência universal. Uma entrega-modelo deve conter:

1. cópia imutável dos dados brutos e dicionário dos atributos;
2. função de diagnóstico com ausências, duplicatas, domínios e distribuições;
3. separação treino/teste antes de imputação, codificação, escala, discretização ou PCA;
4. `ColumnTransformer` ou estrutura equivalente, ajustada apenas no treino;
5. relatório antes/depois que não confunda validade com acurácia;
6. comparação entre duas formas de redução, por exemplo seleção de atributos e PCA, usando compressão, reconstrução, custo, estabilidade ou desempenho na tarefa;
7. justificativa da alternativa escolhida e discussão de informação perdida, vazamento, categorias novas, mudança temporal e representatividade.

Estrutura mínima do fluxo:

```python
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.25, random_state=RANDOM_STATE, stratify=y
)

preparo = ColumnTransformer([
    ("num", Pipeline([
        ("imputacao", SimpleImputer(strategy="median")),
        ("escala", StandardScaler()),
    ]), colunas_numericas),
    ("cat", OneHotEncoder(handle_unknown="ignore"), colunas_categoricas),
])

X_treino_pronto = preparo.fit_transform(X_treino)
X_teste_pronto = preparo.transform(X_teste)
```

As opções de redução também devem ser ajustadas no treino. Se houver modelo, ele deve ficar no mesmo pipeline durante a validação.

**Rubrica (10 pontos):** preservação e diagnóstico (2), separação e ausência de vazamento (2), transformações justificadas (2), comparação de redução com medidas (2), interpretação e limitações (2).
