# Adendo de revisão — escolha da medida de proximidade

**Data:** 2026-09-02  
**Material:** `notebooks/unidade_02/02_03_similaridade_e_dissimilaridade.ipynb`  
**Resultado:** aprovado

## Alteração verificada

Foi inserida, antes da síntese, uma seção comparativa sobre quando aplicar Euclidiana, Manhattan, Minkowski, cosseno, Jaccard e Gower, seguida por um roteiro de decisão.

## Parecer

- **Didática:** a seção transforma definições isoladas em um processo de escolha aplicável a novos problemas.
- **Exatidão:** são explicitados dependência de escala, condição $p\\geq1$, vetor nulo no cosseno, união vazia no Jaccard e tratamento por tipo no Gower.
- **Alinhamento:** a ampliação atende diretamente ao objetivo de escolher medidas para atributos numéricos, binários e mistos.
- **Nível acadêmico:** a decisão é vinculada ao significado substantivo, à análise de sensibilidade e à validação sem contaminação do teste.
- **Reprodutibilidade:** o notebook foi reexecutado com 16 células, cinco células de código, IDs únicos e nenhuma saída de erro.

Não foram identificados achados obrigatórios.
