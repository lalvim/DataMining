# Adendo de revisão — fluxo visual do Apriori

**Data:** 2026-09-09  
**Decisão:** Aprovado

Foi acrescentada uma ilustração autoral e reproduzível da execução do Apriori. A imagem é gerada por código com a base sintética do notebook; a figura fornecida pelo usuário serviu somente para identificar a lacuna didática e não foi copiada, adaptada ou incorporada ao repositório.

A nova seção apresenta:

- suporte mínimo de 25%, equivalente a três das 12 transações;
- passagem de sete candidatos de tamanho 1 para cinco frequentes;
- geração e contagem dos dez pares obtidos a partir de cinco itens frequentes;
- geração inicial de quatro trios;
- justificativa individual da poda de três trios por subconjuntos infrequentes;
- contagem do único trio sobrevivente e sua entrada em `L3`;
- distinção entre poda estrutural antes da varredura e filtragem por suporte depois da contagem;
- condição de parada do algoritmo.

A composição usa gráficos de barras por nível e um painel textual de poda, diferente da diagramação e dos dados da referência apresentada. Estados também são escritos nos rótulos, evitando dependência exclusiva da cor. Asserções protegem todas as contagens narradas.

O notebook foi executado integralmente: 17 células, sete de código, duas figuras, identificadores únicos, atividades correspondentes aos gabaritos e nenhuma saída de erro.

**Achados obrigatórios:** nenhum.
