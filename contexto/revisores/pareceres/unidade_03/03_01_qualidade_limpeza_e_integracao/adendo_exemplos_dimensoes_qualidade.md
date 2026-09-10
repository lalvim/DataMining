# Adendo de revisão — exemplos das dimensões de qualidade

**Data:** 2026-09-09  
**Decisão:** Aprovado

A tabela sintética foi auditada e passou a conter pelo menos um exemplo explícito de cada dimensão trabalhada:

| Dimensão | Exemplo identificável |
|---|---|
| Completude | cliente 102 com idade ausente |
| Validade | cliente 104 com idade 150 |
| Consistência | cliente 106 associado à combinação incompatível Olinda/PB |
| Unicidade | cliente 104 representado em duas linhas |
| Atualidade | cliente 107 com atualização em 2020-01-10 diante da referência 2026-01-01 |

Após o DataFrame bruto, uma célula Markdown aponta dimensão, registro e justificativa. Essa separação deixa o código responsável apenas pelos dados e o texto responsável pela explicação conceitual. As regras de domínio e a referência temporal estão declaradas antes do diagnóstico.

O fluxo posterior permanece coerente: a inconsistência cidade–UF, duplicidade e valores inválidos são tratados; o e-mail ausente e a informação desatualizada permanecem sinalizados porque não há base para inventá-los. A junção mantém sete clientes e identifica um sem contrato.

Foram adicionadas asserções para proteger as sete contagens antes e depois e a cardinalidade da junção. O notebook foi executado integralmente com 14 células, seis de código, identificadores únicos, atividades correspondentes aos gabaritos e nenhuma saída de erro.

**Achados obrigatórios:** nenhum.
