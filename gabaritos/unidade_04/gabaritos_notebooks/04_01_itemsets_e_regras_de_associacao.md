# Gabarito — 04.01 Itemsets e regras de associação

## U04-NB01-V01

É possível. Considere uma regra com confiança de 90% cujo consequente apareça em 95% das transações. Nesse caso,

$$
\operatorname{lift}(X\rightarrow Y)=\frac{0{,}90}{0{,}95}\approx 0{,}947<1.
$$

A confiança é alta em termos absolutos, mas fica abaixo da frequência basal de $Y$. Conhecer $X$ reduz ligeiramente a chance de observar $Y$; portanto, a associação é negativa segundo o lift.

**Rubrica:** apresentar exemplo numericamente válido (1 ponto), comparar a confiança com o suporte do consequente (1 ponto) e interpretar corretamente o lift menor que 1 (1 ponto).

## U04-NB01-E01

Na base do notebook, `pao` aparece em 4 das 12 cestas, `leite` em 7 e ambos aparecem juntos em 3. Logo,

$$
\begin{aligned}
\operatorname{sup}(pao)&=4/12=0{,}3333,\\
\operatorname{sup}(leite)&=7/12=0{,}5833,\\
\operatorname{sup}(pao\cap leite)&=3/12=0{,}25,\\
\operatorname{conf}(pao\rightarrow leite)&=\frac{3/12}{4/12}=0{,}75,\\
\operatorname{conf}(leite\rightarrow pao)&=\frac{3/12}{7/12}=3/7\approx0{,}4286,\\
\operatorname{lift}&=\frac{0{,}75}{7/12}=\frac{3/7}{4/12}=9/7\approx1{,}2857.
\end{aligned}
$$

Código de conferência:

```python
def suporte(itemset, transacoes):
    alvo = set(itemset)
    return sum(alvo.issubset(t) for t in transacoes) / len(transacoes)

s_pao = suporte({"pao"}, transacoes)
s_leite = suporte({"leite"}, transacoes)
s_conjunto = suporte({"pao", "leite"}, transacoes)

resultado = {
    "suporte_conjunto": s_conjunto,
    "conf_pao_para_leite": s_conjunto / s_pao,
    "conf_leite_para_pao": s_conjunto / s_leite,
    "lift_pao_para_leite": (s_conjunto / s_pao) / s_leite,
    "lift_leite_para_pao": (s_conjunto / s_leite) / s_pao,
}
resultado
```

As confianças diferem porque usam antecedentes com frequências diferentes. O lift é simétrico para as duas direções, embora a confiança não seja. Como o lift é maior que 1, pão e leite aparecem juntos mais do que seria esperado sob independência; isso não demonstra causalidade.

**Rubrica (6 pontos):** suportes corretos (2), duas confianças corretas (2), lift e interpretação sem causalidade (2).
