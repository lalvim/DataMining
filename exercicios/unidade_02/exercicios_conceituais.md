# Unidade II — Exercícios conceituais

**Tema:** tipos, descrição, visualização e proximidade de dados  
**Objetivos avaliados:** classificar atributos; calcular e interpretar medidas descritivas; selecionar visualizações; calcular e justificar medidas de proximidade.  
**Tempo estimado:** 120 minutos  
**Instruções:** justifique as respostas, apresente os cálculos e declare arredondamentos. Um resultado numérico sem interpretação será considerado incompleto.

## Tipos e descrição

1. **U02-C01.** Classifique cada atributo como nominal, binário, ordinal ou numérico. Para os numéricos, indique se é discreto ou contínuo: CEP, temperatura em °C, número de compras, satisfação de uma a cinco estrelas, presença de doença e renda mensal. Indique uma operação inadequada para dois deles.

2. **U02-C02.** Considere os valores `2, 3, 3, 4, 8`.

   a. Calcule média, mediana, moda e amplitude.  
   b. Substitua 8 por 80 e recalcule média e mediana.  
   c. Explique qual medida foi mais robusta e por quê.

3. **U02-C03.** Para a amostra `1, 2, 3`, calcule manualmente a variância amostral e o desvio-padrão. Explique por que a variância não está na mesma unidade dos dados.

4. **U02-C04.** Duas turmas têm a mesma média de nota, mas desvios-padrão 0,8 e 2,4. Interprete a diferença. É possível concluir qual turma aprendeu mais? Justifique.

5. **U02-C05.** Explique a diferença entre covariância e correlação. O que acontece com cada uma se todos os valores de uma variável forem multiplicados por 100? Considere um fator positivo.

6. **U02-C06.** Dê um exemplo de duas variáveis com forte relação não linear e correlação de Pearson próxima de zero. Explique por que correlação não implica causalidade.

## Visualização

7. **U02-C07.** Escolha uma visualização inicial para cada pergunta e justifique:

   a. Como a duração de atendimentos se distribui?  
   b. Como o salário varia entre quatro cargos?  
   c. Há relação entre temperatura e consumo de energia?  
   d. Quantos estudantes existem por curso?

8. **U02-C08.** Um gráfico de barras compara 99% e 100%, mas o eixo começa em 98%. Explique o efeito perceptivo e proponha uma apresentação mais honesta. Em que tipo de gráfico iniciar em zero não é sempre obrigatório?

9. **U02-C09.** Um mapa de calor mostra correlação 0,92 entre duas variáveis. Liste quatro verificações que devem anteceder qualquer conclusão substantiva.

10. **U02-C10.** Refaça conceitualmente um gráfico que distingue grupos apenas por vermelho e verde. Proponha canais visuais e elementos textuais que melhorem a acessibilidade.

## Similaridade e dissimilaridade

11. **U02-C11.** Para $x=(1,2,3)$ e $y=(4,2,7)$, calcule as distâncias Manhattan e Euclidiana. Compare o significado das duas agregações.

12. **U02-C12.** Três pessoas têm `(idade, renda)` iguais a A = `(20, 2000)`, B = `(22, 8000)` e C = `(55, 8500)`. Explique por que a renda domina a distância Euclidiana sem padronização e como isso pode alterar o vizinho mais próximo.

13. **U02-C13.** Calcule a similaridade do cosseno entre $a=(1,2)$ e $b=(2,4)$. Depois compare com $c=(2,0)$. Explique por que vetores de magnitudes distintas podem ter similaridade 1.

14. **U02-C14.** As cestas A e B contêm, respectivamente, `{arroz, feijão, óleo}` e `{arroz, café, óleo, leite}`.

   a. Calcule interseção e união.  
   b. Calcule similaridade e distância de Jaccard.  
   c. Explique por que ausências conjuntas normalmente não contam nesse caso.

15. **U02-C15.** Construa uma medida de dissimilaridade para perfis contendo idade, escolaridade ordinal, município e cinco preferências binárias. Explique tratamento, escala, pesos e significado de uma distância pequena. Discuta pelo menos uma limitação.

## Desafio opcional

16. **U02-C16.** Investigue o fenômeno de concentração de distâncias em alta dimensionalidade. Proponha um experimento com dados aleatórios que compare a razão entre distância mínima e máxima à medida que o número de dimensões cresce. Declare hipótese, procedimento, gráfico e interpretação esperada.
