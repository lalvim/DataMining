# Unidade IV — Exercícios conceituais

**Tema:** itemsets, regras de associação, Apriori, avaliação e padrões sequenciais  
**Tempo estimado:** 120 minutos  
**Instruções:** apresente cálculos, denominadores e interpretação contextual. Não atribua causalidade a associações observacionais.

## Representação e métricas

1. **U04-C01.** Diferencie transação, item, itemset e regra de associação. Explique o que se perde ao representar compras apenas por presença binária.

2. **U04-C02.** Em 100 compras, A ocorre em 40, B em 50 e ambos em 30. Calcule suporte de `{A,B}`, confiança de `A→B` e `B→A` e *lift* das duas regras.

3. **U04-C03.** Explique por que regras inversas têm o mesmo suporte e *lift*, mas podem ter confianças diferentes.

4. **U04-C04.** Construa um exemplo em que uma regra tenha confiança de 90% e *lift* menor que 1. Interprete a taxa-base do consequente.

5. **U04-C05.** Compare suporte, confiança, *lift*, alavancagem e convicção. Indique uma pergunta respondida por cada medida.

## Apriori

6. **U04-C06.** Demonstre a propriedade antimonótona do suporte usando inclusão de conjuntos de transações.

7. **U04-C07.** Se `{A,B}` é infrequente, o que se conclui sobre `{A,B,C}`? Pode-se concluir algo sobre `{A,C}`? Justifique.

8. **U04-C08.** Com quatro itens frequentes de tamanho 1, liste os candidatos de tamanho 2. Se `{A,B}` for infrequente, indique candidatos de tamanho 3 que podem ser podados.

9. **U04-C09.** Descreva as etapas de geração, poda, contagem e retenção do Apriori. Diferencie candidato de itemset frequente.

10. **U04-C10.** Explique o efeito esperado de reduzir suporte mínimo de 20% para 5% sobre cobertura, custo, coincidências e padrões de nicho.

11. **U04-C11.** Proponha uma validação que compare uma implementação didática do Apriori a uma biblioteca, incluindo casos-limite.

## Avaliação e sequências

12. **U04-C12.** Liste seis critérios, além de confiança alta, para decidir se uma regra merece investigação ou uso.

13. **U04-C13.** Uma regra `promoção→compra` tem *lift* 2. Explique por que isso não demonstra que a promoção causou a compra e proponha um desenho para avaliar o efeito.

14. **U04-C14.** Diferencie itemset frequente de padrão sequencial. Verifique se `⟨A,C⟩` ocorre em `⟨A,B,C,D⟩`, `⟨C,A,D⟩` e `⟨A,C,C⟩`.

15. **U04-C15.** Em cinco jornadas, o padrão `busca→compra` ocorre ao menos uma vez em três clientes, sendo repetido quatro vezes em um deles. Calcule o suporte sequencial por cliente e explique por que as repetições não mudam o numerador.

16. **U04-C16.** Proponha regras para janela temporal, eventos simultâneos e lacuna máxima em uma análise de jornadas. Explique como cada decisão pode alterar o suporte.
