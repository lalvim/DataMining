# Adendo de revisão — padrão de explicação das métricas

**Data:** 2026-09-16  
**Decisão:** Aprovado

## Escopo

Revisão da explicação de suporte, confiança e *lift* após sua adequação ao padrão didático adotado no notebook 04.03.

## Verificações

- A regra $A\rightarrow B$ é apresentada e interpretada antes das métricas.
- Suporte, confiança e *lift* possuem subseções próprias com definição, fórmula, interpretação e exemplo.
- Um único exemplo de café e açúcar mantém coerência numérica entre as três explicações.
- A diferença entre proporção absoluta, probabilidade condicional e comparação relativa com a taxa-base está explícita.
- A distinção entre aumento relativo e pontos percentuais evita uma interpretação frequente, mas incorreta, do *lift*.
- O quadro comparativo registra corretamente que suporte e *lift* são simétricos, enquanto confiança é direcional.
- A aplicação a feijão→arroz apresenta contagens, suporte, confiança e *lift*, além da comparação com arroz→feijão.
- Os resultados narrados correspondem às saídas executadas: suporte 0,500, confianças 1,000 e 0,857 e *lift* 1,714 nas duas direções.
- As ressalvas amostrais e causais foram preservadas.
- O notebook foi executado integralmente: 12 células, quatro de código, identificadores únicos, atividades correspondentes aos gabaritos e nenhuma saída de erro.

## Conclusão

O notebook 04.01 agora segue o mesmo padrão de explicação progressiva do 04.03, mantendo precisão conceitual e coerência entre fórmulas, exemplos e código. Não há correções obrigatórias pendentes.
