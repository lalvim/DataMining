# Unidade IV — Gabarito completo dos exercícios conceituais

**Uso:** material de conferência separado da lista de exercícios. As respostas abaixo resolvem integralmente cada questão. Quando há mais de uma decisão possível, é apresentada uma solução-modelo explícita e são indicadas as condições que admitem alternativas.

## U04-C01

- **Item:** unidade elementar que pode ocorrer em uma compra, como `arroz` ou `leite`.
- **Transação:** evento observado, identificado e composto por itens. Uma compra pode ser representada por $t_1=\{arroz, feijao, leite\}$.
- **Itemset:** conjunto de um ou mais itens, independentemente de ordem. Por exemplo, $X=\{arroz, feijao\}$ é um itemset de tamanho 2.
- **Regra de associação:** implicação descritiva $X\rightarrow Y$, com $X\cap Y=\varnothing$, usada para avaliar se transações que contêm $X$ também tendem a conter $Y$. Ela não é uma implicação lógica nem uma afirmação causal.

Ao converter uma compra em presença binária, registra-se apenas se cada item ocorreu. Perdem-se quantidade — comprar uma ou dez unidades torna-se igual —, ordem de inclusão no carrinho, horário e intervalo entre eventos, preço pago, desconto, posição na loja ou página e, se não forem armazenados separadamente, contexto e identidade. Logo, a representação binária é adequada para coocorrência, mas não para consumo em quantidade ou jornada temporal.

**Critérios de correção:** definir os quatro conceitos, respeitar a disjunção da regra e explicar ao menos duas perdas da representação binária.

## U04-C02

Denotando o total por $N=100$:

$$
\operatorname{sup}(A)=\frac{40}{100}=0{,}40,\qquad
\operatorname{sup}(B)=\frac{50}{100}=0{,}50,
$$

$$
\operatorname{sup}(\{A,B\})=\frac{30}{100}=0{,}30.
$$

Para $A\rightarrow B$:

$$
\operatorname{conf}(A\rightarrow B)
=\frac{\operatorname{sup}(A,B)}{\operatorname{sup}(A)}
=\frac{0{,}30}{0{,}40}=0{,}75,
$$

$$
\operatorname{lift}(A\rightarrow B)
=\frac{0{,}75}{0{,}50}=1{,}50.
$$

Para $B\rightarrow A$:

$$
\operatorname{conf}(B\rightarrow A)
=\frac{0{,}30}{0{,}50}=0{,}60,
$$

$$
\operatorname{lift}(B\rightarrow A)
=\frac{0{,}60}{0{,}40}=1{,}50.
$$

Assim, o itemset conjunto aparece em 30% das compras. Entre compras com A, 75% têm B; entre compras com B, 60% têm A. O *lift* 1,5 indica que a coocorrência observada é 50% maior que a esperada sob independência na amostra. Isso não demonstra causalidade.

**Critérios de correção:** mostrar denominadores, obter suporte 0,30, confianças 0,75 e 0,60, dois *lifts* 1,50 e interpretar os valores.

## U04-C03

As duas regras usam o mesmo itemset conjunto, portanto:

$$
\operatorname{sup}(A\rightarrow B)
=\operatorname{sup}(B\rightarrow A)
=P(A\cap B).
$$

O *lift* também é simétrico:

$$
\operatorname{lift}(A\rightarrow B)
=\frac{P(A\cap B)}{P(A)P(B)}
=\operatorname{lift}(B\rightarrow A).
$$

A confiança é condicional e troca o denominador:

$$
\operatorname{conf}(A\rightarrow B)=\frac{P(A\cap B)}{P(A)},
\qquad
\operatorname{conf}(B\rightarrow A)=\frac{P(A\cap B)}{P(B)}.
$$

No exercício anterior, o suporte é 0,30 e o *lift* é 1,50 nas duas direções, mas as confianças são 0,75 e 0,60 porque $P(A)=0{,}40$ e $P(B)=0{,}50$. Elas só seriam iguais se os antecedentes tivessem o mesmo suporte.

**Critérios de correção:** demonstrar a simetria de suporte e *lift* e relacionar a diferença de confiança aos denominadores.

## U04-C04

Considere 1.000 transações:

- A ocorre em 100;
- B ocorre em 950;
- A e B ocorrem juntos em 90.

Então,

$$
\operatorname{conf}(A\rightarrow B)=\frac{90}{100}=0{,}90,
$$

mas a taxa-base de B é

$$
\operatorname{sup}(B)=\frac{950}{1000}=0{,}95.
$$

Logo,

$$
\operatorname{lift}(A\rightarrow B)=\frac{0{,}90}{0{,}95}
\approx0{,}947<1.
$$

Embora 90% pareça uma confiança alta, B ocorre em 95% da população. Entre as transações com A, a frequência de B é cinco pontos percentuais menor que a taxa-base. Assim, A está associado negativamente a B nesta amostra. O exemplo mostra por que confiança deve ser comparada à prevalência do consequente.

**Critérios de correção:** construir contagens ou probabilidades coerentes, calcular aproximadamente 0,947 e interpretar a taxa-base.

## U04-C05

Para a regra $X\rightarrow Y$:

| Medida | Fórmula | Pergunta respondida |
|---|---|---|
| Suporte | $P(X\cap Y)$ | Em que proporção de todas as transações X e Y aparecem juntos? |
| Confiança | $P(Y\mid X)=P(X\cap Y)/P(X)$ | Entre as transações com X, qual proporção também contém Y? |
| *Lift* | $P(Y\mid X)/P(Y)$ | Y é relativamente mais ou menos comum quando X ocorre do que em sua taxa-base? |
| Alavancagem | $P(X\cap Y)-P(X)P(Y)$ | Quantos pontos de proporção a coocorrência ganha ou perde em relação à independência? |
| Convicção | $(1-P(Y))/(1-P(Y\mid X))$ | Quão menos frequentes são as violações $X$ sem Y do que seriam sob independência? |

Exemplo com $P(X)=0{,}40$, $P(Y)=0{,}50$ e $P(X\cap Y)=0{,}30$:

$$
\operatorname{conf}=0{,}30/0{,}40=0{,}75,
\qquad \operatorname{lift}=0{,}75/0{,}50=1{,}50,
$$

$$
\operatorname{leverage}=0{,}30-(0{,}40\times0{,}50)=0{,}10,
$$

$$
\operatorname{conviction}=\frac{1-0{,}50}{1-0{,}75}=2.
$$

O suporte mostra volume; a confiança, acerto condicional; o *lift*, ganho relativo sobre a base; a alavancagem, ganho absoluto; e a convicção, redução relativa das violações. Nenhuma delas, isoladamente, mede causalidade ou utilidade econômica.

**Critérios de correção:** definir as cinco medidas, associar uma pergunta distinta a cada uma e não atribuir causalidade.

## U04-C06

Seja

$$
T(X)=\{t:\,X\subseteq t\}
$$

o conjunto de transações que contêm o itemset $X$. Se $X\subseteq Y$, toda transação que contém todos os itens de $Y$ necessariamente contém todos os itens de $X$. Portanto,

$$
T(Y)\subseteq T(X).
$$

Da inclusão segue $|T(Y)|\leq|T(X)|$. Dividindo ambas as contagens pelo mesmo número total $N$ de transações:

$$
\operatorname{sup}(Y)=\frac{|T(Y)|}{N}
\leq\frac{|T(X)|}{N}=\operatorname{sup}(X).
$$

Logo, o suporte é antimonótono em relação à inclusão: adicionar itens nunca aumenta o conjunto de transações que contém o padrão. Se $X$ já está abaixo do suporte mínimo, qualquer superconjunto $Y$ também estará.

**Critérios de correção:** definir os conjuntos de transações, demonstrar sua inclusão e derivar a desigualdade dos suportes.

## U04-C07

Como $\{A,B\}\subseteq\{A,B,C\}$, a propriedade antimonótona fornece

$$
\operatorname{sup}(A,B,C)\leq\operatorname{sup}(A,B).
$$

Se `{A,B}` está abaixo do suporte mínimo, `{A,B,C}` também está e pode ser podado sem contagem adicional.

Nada pode ser concluído sobre `{A,C}` apenas a partir de `{A,B}`, pois `{A,C}` não é superconjunto de `{A,B}`. Ele pode ser frequente ou infrequente. Por exemplo, se A e C aparecem juntos em 80% das transações e A e B em 5%, `{A,C}` é frequente para limiar 20%, embora `{A,B}` não seja.

**Critérios de correção:** podar `{A,B,C}`, não podar `{A,C}` sem evidência e justificar pela relação de inclusão.

## U04-C08

Com $L_1=\{A,B,C,D\}$, todos os pares possíveis são:

$$
C_2=\{AB, AC, AD, BC, BD, CD\}.
$$

Há $\binom{4}{2}=6$ candidatos. Se `AB` for infrequente, qualquer candidato de tamanho 3 que o contenha deve ser podado. Os trios possíveis são `ABC`, `ABD`, `ACD` e `BCD`; portanto, `ABC` e `ABD` são podados por conterem `AB`. Não se pode podar `ACD` ou `BCD` por esse motivo.

Além disso, um trio só deve chegar à contagem se todos os seus subconjuntos de tamanho 2 forem frequentes. Assim, mesmo `ACD` seria podado se, por exemplo, `CD` fosse infrequente.

**Critérios de correção:** listar seis pares, quatro trios e identificar exatamente `ABC` e `ABD` como podáveis devido a `AB`.

## U04-C09

O Apriori trabalha por níveis de tamanho:

1. **Inicialização:** conte cada item e retenha em $L_1$ apenas os que atingem o suporte mínimo.
2. **Geração:** una itemsets compatíveis de $L_{k-1}$ para formar candidatos de tamanho $k$, produzindo $C_k$.
3. **Poda:** remova de $C_k$ qualquer candidato que possua ao menos um subconjunto de tamanho $k-1$ ausente de $L_{k-1}$.
4. **Contagem:** percorra as transações e conte somente os candidatos sobreviventes.
5. **Retenção:** forme $L_k$ com candidatos cujo suporte atinge o limiar.
6. **Repetição:** aumente $k$ e continue até $L_k$ ficar vazio; então nenhum itemset maior pode ser frequente.

Um **candidato** é uma hipótese que passou pela geração e talvez pela poda, mas ainda não teve frequência suficiente comprovada. Um **itemset frequente** já foi contado e alcançou o suporte mínimo. Por exemplo, para limiar 25%, `ABC` pode estar em $C_3$; se aparecer em apenas 10% das transações, não entra em $L_3$.

**Critérios de correção:** apresentar geração, poda, contagem e retenção na ordem e distinguir claramente $C_k$ de $L_k$.

## U04-C10

Reduzir suporte mínimo de 20% para 5% tem os seguintes efeitos esperados:

- **Cobertura:** todo itemset com suporte de pelo menos 20% continua frequente, e passam a entrar os situados entre 5% e 20%.
- **Custo:** mais itemsets sobrevivem em cada nível, gerando mais candidatos maiores; aumentam contagens, memória, tempo e volume de resultados.
- **Coincidências:** padrões baseados em poucas ocorrências tornam-se mais sensíveis ao acaso, a erros e a múltiplas comparações.
- **Nichos:** associações restritas a segmentos pequenos ou produtos raros podem aparecer, algo impossível com limiar de 20%.

O número exato de novos padrões depende da base. Limiar menor não garante explosão nem utilidade: se nenhum itemset tiver suporte entre 5% e 20%, o resultado não muda; se muitos itens raros coocorrerem, pode crescer drasticamente. Padrões de baixo suporte devem ser acompanhados por contagem absoluta, estabilidade em outra amostra e relevância contextual.

**Critérios de correção:** discutir os quatro efeitos, reconhecer dependência dos dados e não confundir maior cobertura com maior utilidade.

## U04-C11

Uma validação reproduzível pode usar a base pequena:

```python
transacoes = [
    {"A", "B"},
    {"A", "B"},
    {"A"},
    {"B"},
]
```

Os resultados manuais são $sup(A)=3/4$, $sup(B)=3/4$ e $sup(AB)=2/4$. Com limiar 0,50, os três itemsets devem aparecer; com 0,5001, apenas A e B permanecem. A comparação deve:

1. converter a saída didática e a da biblioteca para o mesmo formato, como pares `(frozenset, suporte)`;
2. executar ambas nos mesmos dados e limiares;
3. exigir igualdade dos itemsets e comparar suportes com tolerância numérica;
4. registrar candidatos por nível apenas para a implementação didática, pois a biblioteca pode usar otimizações internas diferentes.

Exemplo de verificação:

```python
assert set(resultado_didatico) == set(resultado_biblioteca)
for itemset in resultado_didatico:
    assert abs(
        resultado_didatico[itemset] - resultado_biblioteca[itemset]
    ) < 1e-12
```

Casos-limite adicionais:

- base vazia: deve seguir contrato documentado, retornando vazio ou erro claro;
- transações vazias misturadas às demais: entram no denominador, mas não contêm item;
- item presente em todas as transações: suporte exatamente 1;
- itemset exatamente no limiar: deve ser incluído se a regra for `>=`;
- item nunca presente: não aparece nos frequentes;
- transações repetidas: contam como eventos distintos se esse for o significado dos dados;
- itemsets de tamanhos 1, 2 e 3: conferem geração e poda multinível.

**Critérios de correção:** definir base e valores esperados, comparar identidades e suportes, usar tolerância e incluir casos-limite com comportamento esperado.

## U04-C12

Seis critérios mínimos além de confiança alta são:

1. **Contagem absoluta:** uma regra apoiada em 4 casos é mais frágil que outra apoiada em 4.000, mesmo com a mesma confiança.
2. **Suporte:** mostra a parcela total da base coberta e ajuda a estimar alcance operacional.
3. **Ganho sobre a taxa-base:** *lift* ou alavancagem verificam se a confiança supera o que já seria esperado pela frequência do consequente.
4. **Estabilidade:** a regra deve reaparecer em outros períodos, amostras ou segmentos relevantes.
5. **Redundância e novidade:** regras equivalentes ou consequências já óbvias podem não acrescentar conhecimento.
6. **Acionabilidade:** antecedente e consequente precisam ser observáveis a tempo, e deve existir uma ação possível.

Também devem ser avaliados custos, benefício esperado, risco de intervenção, equidade, privacidade, explicações alternativas e validação externa. Uma solução concreta poderia exigir pelo menos 100 ocorrências, *lift* acima de 1,2, estabilidade em dois períodos e uma ação cujo benefício esperado supere custo e risco. Esses valores são apenas exemplo e devem ser definidos pelo domínio.

**Critérios de correção:** apresentar seis critérios distintos e explicar como cada um influencia investigação ou uso.

## U04-C13

Um *lift* 2 significa que, nos dados observados,

$$
P(compra\mid promocao)=2P(compra).
$$

Isso não prova efeito causal. A promoção pode ter sido oferecida justamente a clientes com maior intenção de compra; pode coincidir com feriados, maior estoque, publicidade ou redução geral de preço; clientes podem escolher ver promoções; e exposição e compra podem ser medidas de forma desigual. Esses fatores criam confundimento e seleção.

Uma solução-modelo é um experimento randomizado:

1. definir previamente clientes elegíveis e excluir casos em que a oferta seria inadequada;
2. sortear clientes elegíveis entre promoção e controle, preservando a unidade de randomização;
3. garantir que o controle não receba a promoção e monitorar contaminação;
4. definir antes o desfecho, por exemplo “realizou compra em até sete dias”, e uma janela comum;
5. calcular tamanho de amostra para um efeito mínimo relevante;
6. estimar por intenção de tratar a diferença de proporções
   $\hat p_{promocao}-\hat p_{controle}$, com intervalo de confiança;
7. relatar também receita, margem, cancelamentos e possíveis efeitos por grupo.

Se 12% do grupo promoção e 10% do controle comprarem, a estimativa causal de intenção de tratar será aumento absoluto de 2 pontos percentuais, sujeito à incerteza calculada — não o *lift* observacional original. Se houver interferência entre clientes, pode ser necessária randomização por loja ou região.

**Critérios de correção:** explicar ao menos um confundidor e propor experimento com elegibilidade, aleatorização, controle, desfecho, janela e análise de efeito.

## U04-C14

Um **itemset frequente** é um conjunto não ordenado que aparece em proporção suficiente de transações. `{A,C}` ocorre tanto em uma cesta com A antes de C quanto com C antes de A, pois ordem não faz parte da representação.

Um **padrão sequencial** preserva ordem. O padrão $\langle A,C\rangle$ exige uma ocorrência de A anterior a uma ocorrência de C, sem exigir adjacência, salvo regra adicional.

- Em $\langle A,B,C,D\rangle$, ocorre: A está na posição 1 e C na 3.
- Em $\langle C,A,D\rangle$, não ocorre: não existe C depois do A.
- Em $\langle A,C,C\rangle$, ocorre: pode-se usar o A da posição 1 e qualquer C posterior.

Logo, ocorre na primeira e na terceira sequência, mas não na segunda.

**Critérios de correção:** distinguir conjunto de sequência e classificar corretamente os três casos com justificativa de posição.

## U04-C15

A unidade de análise é o cliente, não o número de ocorrências. Há cinco jornadas e três clientes contêm `busca→compra` ao menos uma vez. Portanto,

$$
\operatorname{sup}_{seq}(busca\rightarrow compra)
=\frac{3}{5}=0{,}60=60\%.
$$

O cliente que apresenta o padrão quatro vezes contribui apenas com 1 para o numerador, assim como os outros dois clientes que o apresentam. Formalmente, o numerador soma indicadores:

$$
\sum_{i=1}^{5}\mathbb{1}\{\text{a jornada }i\text{ contém o padrão}\}=3.
$$

Contar todas as repetições produziria $4+1+1=6$ ocorrências e a razão $6/5=120\%$, que não é uma prevalência por cliente. Frequência de ocorrências pode ser outra métrica válida, mas precisa de outro nome e denominador, como ocorrências por cliente ou por sessão.

**Critérios de correção:** calcular 3/5, explicar a contribuição binária por entidade e distinguir suporte de contagem de ocorrências.

## U04-C16

Uma política possível para jornadas digitais é:

1. **Janela temporal:** uma sessão termina após 30 minutos sem atividade. Um padrão não pode atravessar sessões.
2. **Eventos simultâneos:** eventos com o mesmo timestamp são agrupados em um itemset sem ordem interna. Um A e um C simultâneos não satisfazem o padrão estrito $\langle A,C\rangle$.
3. **Lacuna máxima:** entre eventos consecutivos correspondidos pelo padrão podem transcorrer no máximo 10 minutos.

Efeito de cada decisão:

- Reduzir a janela de sessão separa mais jornadas e elimina ocorrências que atravessavam pausas; em geral reduz o numerador de padrões longos. Se o denominador for número de sessões, ele também pode aumentar, tornando o efeito sobre o suporte ainda dependente da definição. Ampliar a janela faz o oposto e pode ligar eventos sem relação prática.
- Agrupar simultâneos evita inventar ordem quando o relógio não a distingue. Permitir qualquer desempate pode criar artificialmente `A→C` ou `C→A`; exigir ordem estrita exclui ambos. Para itemsets simultâneos, pode-se minerar o evento conjunto `{A,C}`.
- Diminuir a lacuna máxima remove correspondências distantes e tende a reduzir suporte; aumentá-la aceita mais ocorrências, mas pode relacionar eventos de contextos distintos.

Exemplo: em `A(10:00), B(10:04), C(10:12)`, $\langle A,C\rangle$ não atende lacuna máxima de 10 minutos, mas atende a 15 minutos. Em `A(10:00), C(10:00)`, não há precedência estrita sob agrupamento simultâneo. As regras devem ser definidas antes de comparar padrões e mantidas iguais entre grupos e períodos.

**Critérios de correção:** declarar regras operacionais para os três aspectos e explicar separadamente como cada uma muda ocorrência ou denominador.
