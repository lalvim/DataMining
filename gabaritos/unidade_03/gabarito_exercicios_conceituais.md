# Unidade III — Gabarito completo dos exercícios conceituais

**Uso:** material de conferência separado da lista de exercícios. As respostas abaixo são soluções-modelo completas. Quando o problema admite mais de uma decisão defensável, é apresentado um exemplo de solução e são explicitadas as condições que poderiam justificar outra escolha.

## U03-C01

As seis dimensões avaliam propriedades diferentes de uma base hospitalar:

| Dimensão | Significado | Exemplo de falha |
|---|---|---|
| Completude | Presença dos valores necessários | O campo `alergias` está vazio, embora seja necessário para prescrever um medicamento. |
| Validade | Conformidade com tipo, formato ou domínio permitido | A saturação de oxigênio foi registrada como 140%, fora do domínio físico esperado. |
| Consistência | Compatibilidade entre valores, registros ou fontes | O prontuário informa alta em 10/05, mas uma medicação aparece administrada durante a internação em 12/05. |
| Unicidade | Uma representação por entidade ou evento | A mesma pessoa possui dois prontuários porque um cadastro contém CPF pontuado e o outro, apenas dígitos. |
| Atualidade | Adequação do valor ao momento de uso | O endereço é formalmente válido, mas não é atualizado há oito anos e não serve para uma visita domiciliar. |
| Acurácia | Correspondência entre o registro e o estado real | A temperatura foi digitada como 36,8 °C, mas a leitura correta era 38,6 °C. |

Um valor pode ser válido e inexato porque validade verifica regras formais, não a verdade factual. `36,8` pertence ao domínio permitido para temperatura e tem tipo correto, portanto é válido; ainda assim, é inexato se a medição real era `38,6`. Do mesmo modo, idade 40 é válida para um adulto, mas inexata se a pessoa tem 37 anos.

**Critérios de correção:** definir as seis dimensões, dar um exemplo específico para cada uma e distinguir validade de acurácia.

## U03-C02

As três estratégias respondem a hipóteses diferentes:

| Estratégia | Quando pode ser razoável | Riscos principais |
|---|---|---|
| Excluir linhas | Quando a ausência é aproximadamente aleatória em relação ao desfecho e aos atributos relevantes, e a perda é pequena | Com 30% de ausência, elimina quase um terço da base, reduz precisão e pode excluir sistematicamente certos grupos |
| Imputar pela mediana | Quando se precisa de uma representação completa e a mediana do treino é uma aproximação operacional aceitável | Cria concentração artificial, reduz variabilidade, enfraquece relações e atribui o mesmo valor a casos diferentes |
| Modelar a ausência | Quando o fato de não informar renda pode carregar informação sobre cadastro, ocupação ou acesso | O indicador não recupera a renda real e pode capturar um processo operacional instável ou discriminatório |

Uma solução-modelo seria:

1. comparar classe-alvo, idade, região, ocupação, canal e período entre linhas com e sem renda;
2. investigar se a ausência decorre de falha técnica, recusa, não aplicabilidade ou política de cadastro;
3. verificar se a proporção de ausência muda no tempo e entre grupos;
4. manter as linhas, criar `renda_ausente` e imputar a mediana aprendida somente no treino;
5. comparar essa alternativa com exclusão e outro imputador por análise de sensibilidade;
6. avaliar desempenho global e por grupos, além das distribuições antes/depois.

Com 30% de ausência, eu não usaria exclusão como padrão sem forte evidência de aleatoriedade. Adotaria indicador + imputação como ponto de partida, deixando claro que os valores imputados são estimativas. Imputador e eventuais grupos usados no cálculo devem ser ajustados apenas no treino e reaplicados sem novo ajuste na validação e no teste.

**Critérios de correção:** comparar as três estratégias, explicitar hipóteses e riscos e apresentar diagnósticos e uma decisão condicional completa.

## U03-C03

Usar todas as colunas detecta apenas duplicatas exatas. A mesma pessoa pode aparecer como `MARIA DA SILVA` e `Maria Silva`, com telefone em outro formato, endereço antigo ou um campo ausente; essas linhas não serão iguais. Usar apenas nome cria o erro oposto: homônimos podem ser fundidos, enquanto abreviações, erros e mudanças de sobrenome podem impedir correspondências reais.

Exemplo de procedimento auditável:

1. preservar as tabelas brutas e atribuir a cada linha um ID imutável de origem;
2. normalizar cópias dos campos: caixa, acentos e espaços do nome; dígitos de CPF e telefone; datas e endereços;
3. resolver correspondências determinísticas confiáveis, como CPF válido e igual;
4. criar pares candidatos por blocos, como mesmo mês de nascimento e prefixo de CEP;
5. combinar evidências de nome, nascimento, telefone, e-mail e endereço;
6. definir faixas prévias para correspondência automática, não correspondência e revisão manual;
7. não fundir automaticamente quando identificadores fortes entram em conflito;
8. guardar linhas de origem, regras, escore, versão, data e responsável pela decisão;
9. avaliar amostra rotulada de pares e não pares, medindo falsas fusões e duplicatas perdidas;
10. criar um ID mestre sem apagar os registros originais.

Assim, duas linhas com o mesmo CPF normalizado e nomes semelhantes podem receber o mesmo ID mestre. Duas pessoas chamadas José Santos, mas com datas de nascimento e telefones diferentes, permanecem separadas. Toda fusão pode ser explicada e desfeita.

**Critérios de correção:** explicar as falhas dos dois extremos e apresentar resolução em múltiplas etapas com rastreabilidade.

## U03-C04

Antes da junção, devem ser verificados:

1. existência, tipo e formato de `cliente_id` nas duas tabelas;
2. chaves ausentes ou inválidas;
3. unicidade de cada chave, pois a regra é uma linha por cliente;
4. contratos sem cliente e clientes sem contrato;
5. compatibilidade de datas, moeda e domínios;
6. cardinalidade e número de linhas esperados após a junção.

Em pandas:

```python
assert clientes["cliente_id"].notna().all()
assert contratos["cliente_id"].notna().all()
assert clientes["cliente_id"].is_unique
assert contratos["cliente_id"].is_unique

integrada = clientes.merge(
    contratos,
    on="cliente_id",
    how="left",
    validate="one_to_one",
    indicator=True,
)
```

Uma junção muitos-para-muitos gera todas as combinações da mesma chave. Se um cliente aparece duas vezes em `clientes` e três em `contratos`, surgem $2\times3=6$ linhas. Se os contratos valem R$ 100, R$ 200 e R$ 300, a soma verdadeira de R$ 600 aparece duas vezes e vira R$ 1.200. A contagem do cliente também pode subir de 1 para 6 se for feita por linhas. `validate="one_to_one"` transforma o erro silencioso em exceção e `indicator=True` permite auditar cobertura.

**Critérios de correção:** listar verificações de chave e cobertura, explicar o produto combinatório e demonstrar a inflação de uma contagem ou soma.

## U03-C05

Exemplo de relatório antes/depois para uma base inicialmente com 10.000 linhas:

| Indicador | Antes | Depois | Interpretação |
|---|---:|---:|---|
| Linhas | 10.000 | 9.850 | 150 duplicatas exatas removidas |
| Entidades únicas | 9.720 | 9.720 | Nenhuma entidade conhecida foi eliminada |
| Células ausentes | 2.400 | 0 | Valores tratados ou imputados, não recuperados |
| Linhas duplicadas | 150 | 0 | Segundo a chave e a regra documentadas |
| Idades fora de `[0, 120]` | 18 | 0 | Marcadas como ausentes antes da imputação |
| Altas anteriores à internação | 12 | 0 | Corrigidas na fonte ou isoladas para revisão |
| Clientes sem contrato | 83 | 83 | Falta de correspondência permanece visível |
| Mediana da renda | R$ 3.100 | R$ 3.100 | Centro preservado |
| Desvio-padrão da renda | R$ 2.050 | R$ 1.910 | Redução compatível com imputação |

O relatório deve registrar regras, código, versão dos dados, quantidade alterada por regra e amostras dos casos afetados. A diminuição das violações não prova acurácia porque mede conformidade com testes conhecidos. Uma idade impossível substituída pela mediana passa a ser completa e válida, mas não se torna a idade real. Erros plausíveis, como renda de R$ 5.000 no lugar de R$ 5.900, podem passar por todas as regras. Acurácia exige fonte confiável, nova medição ou auditoria amostral.

**Critérios de correção:** incluir pelo menos seis indicadores com antes/depois e explicar por que conformidade e imputação não comprovam verdade factual.

## U03-C06

A transformação é

$$
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}=\frac{x-10}{40-10}.
$$

Logo,

$$
10\mapsto0,\qquad
20\mapsto\frac{10}{30}=\frac13\approx0{,}333,\qquad
40\mapsto1.
$$

Para o novo valor 50, mantendo os limites do treino:

$$
50\mapsto\frac{50-10}{40-10}=\frac43\approx1{,}333.
$$

O resultado maior que 1 não é erro: 50 está acima do máximo observado no ajuste. Não se devem recalcular limites no teste, pois isso muda a representação e causa vazamento. Recortar para 1 só é aceitável por decisão explícita de domínio, porque elimina a informação de que o valor excedeu o máximo de treino.

**Critérios de correção:** apresentar fórmula, quatro resultados e interpretar a extrapolação sem reajuste no teste.

## U03-C07

$$
z=\frac{x-\mu}{\sigma}=\frac{65-80}{10}=-1{,}5.
$$

O valor 65 está 1,5 desvio-padrão abaixo da média usada no ajuste. A padronização subtrai a média e divide pelo desvio-padrão; no conjunto de ajuste, a variável transformada terá média próxima de zero e desvio-padrão próximo de um.

Ela altera centro, unidade e escala, mas é linear e mantém a ordem dos valores. Não torna automaticamente a distribuição normal, simétrica ou livre de outliers. Uma distribuição originalmente assimétrica continua assimétrica após padronização. Também não se pode afirmar que $z=-1{,}5$ seja raro sem conhecer a distribuição ou assumir um modelo, como a normal.

**Critérios de correção:** calcular $-1{,}5$, interpretar a posição e distinguir escala de forma distributiva.

## U03-C08

Escolaridade possui ordem substantiva:

```text
fundamental < médio < superior
```

Uma codificação ordinal possível é `fundamental=0`, `médio=1`, `superior=2`. Ela preserva a ordem, mas impõe intervalos iguais entre níveis. Isso pode ser inadequado para regressão linear, k-NN ou k-means se os números forem tratados como distâncias. Se não se quiser assumir distância ou efeito monotônico, *one-hot* também é defensável:

```text
esc_fundamental  esc_medio  esc_superior
       1             0            0
       0             1            0
       0             0            1
```

Município é nominal. Codificar Curitiba, Londrina e Maringá como 0, 1 e 2 criaria ordem e distância sem significado; a representação comum é *one-hot*, com uma coluna booleana por município conhecido.

O codificador deve ser ajustado apenas no treino. `OneHotEncoder(handle_unknown="ignore")` representa um município novo com zeros nas colunas conhecidas; outra política é uma categoria `outros` definida previamente. Reajustar no teste muda o significado e a dimensão das colunas. Uma nova escolaridade, como `pós-graduação`, exige atualização controlada da ordem no próximo ciclo do modelo, e não um valor arbitrário durante a previsão.

**Critérios de correção:** representar concretamente os atributos, discutir a suposição de distância e definir política para categorias novas.

## U03-C09

Com quatro intervalos de largura igual, a amplitude é $20-1=19$ e a largura é $19/4=4{,}75$. Uma convenção possível é:

| Intervalo | Valores | Frequência |
|---|---|---:|
| $[1, 5{,}75)$ | 1, 2, 3, 4, 5 | 5 |
| $[5{,}75, 10{,}5)$ | nenhum | 0 |
| $[10{,}5, 15{,}25)$ | nenhum | 0 |
| $[15{,}25, 20]$ | 20 | 1 |

O extremo 20 amplia a faixa, deixa dois intervalos vazios e concentra quase todos os valores no primeiro.

Por frequência aproximadamente igual, quatro grupos não podem ter a mesma quantidade porque há seis observações. Com quartis interpolados, limites possíveis são 1, 2,25, 3,5, 4,75 e 20:

| Grupo | Valores | Frequência |
|---|---|---:|
| 1 | 1, 2 | 2 |
| 2 | 3 | 1 |
| 3 | 4 | 1 |
| 4 | 5, 20 | 2 |

Essa divisão equilibra contagens, mas coloca 5 e 20 na mesma categoria, ocultando diferença grande. Os limites dependem da amostra e mudam com novos dados. Empates podem impedir quatro grupos ou produzir limites repetidos. Nos dois métodos, valores distintos dentro do mesmo intervalo tornam-se indistinguíveis, causando perda de informação.

**Critérios de correção:** apresentar divisões concretas e discutir intervalos vazios, dependência amostral, empates e perda de variação interna.

## U03-C10

**Vazamento pelo teste.** Antes da separação, calculam-se mediana da renda, média e desvio-padrão da idade na base completa. Esses parâmetros incorporam a distribuição dos exemplos que deveriam permanecer reservados. A avaliação já não simula dados desconhecidos. A prevenção é separar primeiro e manter imputador e escalonador dentro de um `Pipeline`, com `fit` apenas no treino. Em validação cruzada, o pipeline recebe novo `fit` dentro de cada dobra de treino.

**Variável posterior ao evento.** Para prever no início do mês quem cancelará até o fim dele, incluem-se `data_cancelamento`, `motivo_cancelamento` ou anotação de ligação feita após o cancelamento. Esses atributos revelam o desfecho, mas não existem no instante real da previsão. A prevenção é definir data de corte para cada exemplo e reconstruir todos os atributos como estavam nela. Para previsão em 1º de março, por exemplo, só entram informações disponíveis até 28 de fevereiro. Também se deve documentar latência das fontes e preferir validação temporal.

**Critérios de correção:** apresentar dois mecanismos distintos, explicar a contaminação e indicar um controle apropriado para cada caso.

## U03-C11

A ordem correta é:

1. definir atributos, alvo e instante da previsão;
2. separar treino e teste antes de aprender estatísticas dos atributos;
3. ajustar imputação, codificação e padronização somente no treino;
4. transformar o treino com esses objetos;
5. ajustar o modelo no treino transformado;
6. transformar o teste com os mesmos objetos, usando apenas `transform`;
7. gerar previsões no teste;
8. calcular as métricas no teste uma única vez para avaliação final.

```python
pipeline.fit(X_treino, y_treino)
previsoes = pipeline.predict(X_teste)
resultado = metrica(y_teste, previsoes)
```

O `fit` do pipeline aprende transformações e modelo no treino. O teste nunca recebe `fit`. Se houver hiperparâmetros, a seleção ocorre por validação interna usando apenas o treino. Em cada dobra, todos os componentes recebem `fit` somente na subdivisão de treino; depois, o pipeline escolhido pode ser reajustado no treino completo e avaliado no teste reservado.

**Critérios de correção:** apresentar a ordem completa e deixar inequívoco que teste e dobras de validação não ajustam componentes.

## U03-C12

| Estratégia | O que reduz | Finalidade | Informação que pode ser perdida |
|---|---|---|---|
| Amostragem | Linhas | Reduzir custo mantendo aproximação da população | Casos raros, subgrupos e precisão |
| Agregação | Linhas ou resolução | Resumir vendas diárias por mês | Ordem, variação individual e extremos |
| Seleção de atributos | Colunas originais | Remover atributos redundantes, caros ou irrelevantes | Sinal complementar e interações das colunas removidas |
| Extração de atributos | Dimensões, criando novas variáveis | Representar muitas colunas por componentes | Interpretação direta e reconstrução perfeita |

Exemplo: de um milhão de compras, escolher cem mil é amostragem; somar vendas por loja e mês é agregação; manter apenas `idade`, `renda` e `tempo_cliente` é seleção; substituir quarenta variáveis por oito componentes principais é extração. As estratégias atuam sobre objetos diferentes e preservam propriedades diferentes.

**Critérios de correção:** distinguir o objeto reduzido e fornecer finalidade e perda para as quatro estratégias.

## U03-C13

Estratificar pela classe-alvo garante apenas sua proporção. Por exemplo, população e amostra podem ter 20% de cancelamentos, mas a amostra pode conter sobretudo clientes do Sul, poucos registros do primeiro semestre e quase nenhum idoso. A seleção dentro de cada classe não controlou região, tempo ou idade; além disso, a base de origem já pode excluir grupos.

Devem-se comparar população e amostra nas margens de região, período, gênero, idade e outras dimensões, nos cruzamentos como classe × região, na cobertura de grupos raros e nas distribuições numéricas. Se necessário, pode-se estratificar por combinação controlada, usar amostragem temporal/geográfica, aplicar pesos ou coletar dados adicionais. Preservar margens separadas tampouco garante preservar suas interseções, e nenhum ajuste corrige automaticamente uma população de origem enviesada.

**Critérios de correção:** limitar a garantia ao alvo, dar exemplo multidimensional e propor auditoria ou desenho adicional.

## U03-C14

A PCA maximiza variância. Sem padronização, um atributo em reais com desvio de milhares pode dominar outro em escala de 0 a 10, mesmo que o segundo seja importante. A padronização torna as escalas comparáveis quando diferenças de unidade não devem definir importância.

Variância explicada acumulada é a soma das proporções dos componentes mantidos. Se quatro componentes explicam 50%, 25%, 12% e 6%, o acumulado é $50+25+12+6=93\%$. Isso é a fração da variabilidade dos atributos capturada pelo subespaço; não é acurácia nem “informação” em sentido universal.

Preservar 95% da variância não garante 95% da capacidade preditiva porque a PCA ignora o alvo. Uma direção de baixa variância pode separar classes e ser descartada; uma de alta variância pode refletir ruído sem relação com o alvo. Deve-se comparar, com a mesma validação, pipeline sem PCA e pipelines com diferentes números de componentes.

**Critérios de correção:** explicar escala, definir acumulado e mostrar por que critério não supervisionado não garante desempenho supervisionado.

## U03-C15

$$
\frac{8}{40}=0{,}20=20\%.
$$

A representação mantém 20% das dimensões e reduz 80%. Preserva 92% da variância e tem RMSE 0,28 no espaço padronizado, mas esses números não bastam.

Uma decisão-modelo compararia:

1. desempenho e incerteza na tarefa final, com e sem PCA;
2. estabilidade entre dobras, períodos e amostras;
3. RMSE por atributo, pois 0,28 agregado pode ocultar variável mal reconstruída;
4. tempo, memória e latência;
5. impacto em subgrupos e casos raros;
6. necessidade de interpretar atributos originais;
7. comportamento sob mudança de distribuição.

Exemplo de conclusão: eu adotaria oito componentes se a métrica validada cair no máximo dentro de tolerância prévia, como 0,5 ponto percentual, nenhum subgrupo piorar materialmente e a economia computacional for relevante. Não adotaria apenas pelos 92% se explicação por atributo fosse requisito ou se 12 componentes melhorassem substancialmente a tarefa. A escolha ocorre no treino/validação, nunca no teste final.

**Critérios de correção:** calcular 20%, interpretar a redução de 80% e formular decisão com critérios mensuráveis adicionais.

## U03-C16 — Desafio

**Pergunta:** quanto imputação e escala ajustadas antes da validação cruzada alteram a estimativa de generalização em comparação com um pipeline ajustado dentro de cada dobra?

**Hipótese:** o pré-ajuste global usa informação das dobras de validação e pode produzir estimativa otimista. A diferença pode ser pequena, nula ou variar de sinal; a hipótese diz respeito à invalidade do protocolo, não a um efeito necessariamente grande.

**Dados:** usar classificação binária com, por exemplo, 2.000 linhas, dez atributos numéricos em escalas diferentes, 20% de positivos e 15% de células ausentes. Fixar sementes. Reservar ainda 20% como teste externo, que não participa dos ajustes ou comparações.

**Fluxo correto:** colocar `SimpleImputer(strategy="median")`, `StandardScaler` e regressão logística no mesmo `Pipeline`. Em cada dobra, todos são ajustados apenas na parte de treino.

**Fluxo com vazamento:** ajustar imputador e escalonador no conjunto de desenvolvimento completo antes de criar as dobras; transformar globalmente e validar apenas o classificador. Assim, medianas, médias e desvios incorporam cada futura dobra de validação.

**Repetições e controles:** usar `RepeatedStratifiedKFold` com 5 dobras e 10 repetições. Os métodos recebem exatamente as mesmas 50 divisões, o mesmo classificador, hiperparâmetros, sementes e linhas. A única diferença é onde o pré-processamento recebe `fit`.

**Métricas:** usar ROC-AUC como principal e balanced accuracy como complementar. Para cada divisão, calcular

$$
d_i=\operatorname{AUC}_{vazamento,i}-\operatorname{AUC}_{correto,i}.
$$

Relatar média, mediana, desvio-padrão e intervalo de confiança das diferenças pareadas, além de um gráfico dos 50 pares.

**Avaliação externa:** após selecionar o procedimento correto, ajustá-lo no desenvolvimento completo e avaliá-lo uma única vez no teste externo. O teste não escolhe o procedimento.

**Interpretação-modelo:** se a média de $d_i$ for 0,008, o fluxo contaminado superestimou a AUC em 0,8 ponto percentual neste experimento. Se a diferença ficar próxima de zero, não se conclui que o vazamento é aceitável; apenas que teve pouco efeito observável nessa base, modelo e tamanho. Convém repetir com outras taxas de ausência, tamanhos e mudanças de distribuição.

**Critérios de correção:** declarar hipótese sem garantir efeito grande, especificar dados e fluxos, usar divisões pareadas e repetidas, manter controles, medir incerteza e reservar teste externo.
