# Unidade III — Exercícios conceituais

**Tema:** qualidade, limpeza, integração, transformação, discretização e redução de dados  
**Objetivos avaliados:** diagnosticar problemas de qualidade; justificar tratamentos; construir fluxos sem vazamento; comparar transformações e formas de redução.  
**Tempo estimado:** 120 minutos  
**Instruções:** justifique todas as decisões. Quando houver cálculo, apresente o procedimento e interprete o resultado.

## Qualidade, limpeza e integração

1. **U03-C01.** Para uma base hospitalar, diferencie completude, validade, consistência, unicidade, atualidade e acurácia. Dê um exemplo de falha em cada dimensão e explique por que um valor válido pode ser inexato.

2. **U03-C02.** Uma coluna de renda possui 30% de ausências. Compare exclusão de linhas, imputação pela mediana e modelagem da ausência. Indique hipóteses, riscos e diagnósticos necessários antes da escolha.

3. **U03-C03.** Explique por que remover duplicatas usando todas as colunas pode falhar na identificação de uma mesma pessoa e por que usar apenas o nome também é perigoso. Proponha um procedimento auditável de resolução de entidades.

4. **U03-C04.** As tabelas `clientes` e `contratos` deveriam ter uma linha por cliente. Que verificações devem anteceder uma junção? Explique como uma junção muitos-para-muitos inesperada altera contagens e somas.

5. **U03-C05.** Proponha um relatório antes/depois para uma limpeza de dados. Inclua ao menos seis indicadores e explique por que a redução do número de problemas detectados não prova acurácia.

## Transformação e discretização

6. **U03-C06.** Normalize por min–max os valores `10, 20, 40` para `[0,1]`. Em seguida, aplique os mesmos limites ao novo valor 50. Interprete o resultado.

7. **U03-C07.** Um atributo tem média 80 e desvio-padrão 10. Calcule o escore padronizado de 65. Explique o que a padronização altera e o que ela não permite concluir sobre a forma da distribuição.

8. **U03-C08.** Compare codificação ordinal e *one-hot* para escolaridade (`fundamental`, `médio`, `superior`) e município. Justifique a representação de cada atributo e discuta categorias novas.

9. **U03-C09.** Para os valores `1, 2, 3, 4, 5, 20`, compare conceitualmente quatro intervalos por largura igual e por frequência aproximadamente igual. Discuta intervalos vazios, limites dependentes da amostra e perda de informação.

10. **U03-C10.** Descreva dois exemplos distintos de vazamento no pré-processamento: um causado pelo conjunto de teste e outro por uma variável disponível apenas depois do evento previsto. Proponha como impedir cada um.

11. **U03-C11.** Escreva a ordem correta de um fluxo com partição treino/teste, imputação, padronização, codificação, ajuste de modelo e avaliação. Indique em quais dados cada `fit` pode ocorrer.

## Redução de dados

12. **U03-C12.** Diferencie amostragem, agregação, seleção de atributos e extração de atributos. Para cada estratégia, dê uma finalidade e uma informação que pode ser perdida.

13. **U03-C13.** Uma amostra estratificada preservou a proporção da classe-alvo. Explique por que isso não garante representatividade geográfica, temporal ou demográfica.

14. **U03-C14.** Explique por que a PCA é sensível à escala, o significado de variância explicada acumulada e por que preservar 95% da variância não garante preservar 95% da capacidade preditiva.

15. **U03-C15.** Uma base tem 40 atributos. Uma PCA com 8 componentes preserva 92% da variância e produz RMSE de reconstrução 0,28 no espaço padronizado. Calcule a fração da dimensionalidade mantida e proponha critérios adicionais para decidir se a representação deve ser adotada.

## Desafio opcional

16. **U03-C16.** Projete um experimento que compare um pipeline correto a outro com imputação e escala ajustadas antes da validação cruzada. Declare hipótese, dados, métrica, repetições, controles e interpretação esperada sem assumir antecipadamente que a diferença será grande.
