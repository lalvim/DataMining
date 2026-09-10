# Adendo de revisão — quatro formas de redução e representantes

**Data:** 2026-09-09  
**Decisão:** Aprovado

O notebook passou a apresentar subseções próprias para amostragem, agregação, seleção de atributos e extração de atributos. Cada subseção explicita o eixo reduzido, o resultado produzido, uma aplicação, as perdas e cuidados contra vazamento.

A seleção de atributos tornou-se observável em código: um filtro ANOVA ajustado somente no treino mantém 8 das 30 colunas e exibe seus nomes e estatísticas. O texto distingue filtros, métodos de busca e métodos embutidos, além de registrar as limitações da avaliação univariada.

A redução por agrupamento foi corretamente classificada como redução de objetos por prototipagem:

- K-means forma 12 grupos nas 569 linhas padronizadas;
- o alvo não participa do agrupamento;
- a linha real mais próxima de cada centroide é escolhida como representante;
- centroide sintético, representante real e amostragem dentro do grupo são distinguidos;
- ficam explícitas as limitações relativas a escala, distância, número de grupos, densidade, casos raros e fronteiras de classe.

O quadro final orienta a escolha entre reduzir linhas, granularidade ou colunas e esclarece que as técnicas podem ser combinadas. Uma ilustração matricial compara as quatro formas, e uma projeção distingue observações, centroides sintéticos e linhas reais representantes. Ambas possuem rótulos, formas distintas e interpretação textual. O notebook foi executado integralmente: 21 células, dez de código, três figuras, identificadores únicos e nenhuma saída de erro.

**Achados obrigatórios:** nenhum.
