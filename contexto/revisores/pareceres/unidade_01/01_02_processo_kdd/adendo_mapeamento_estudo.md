# Adendo de revisão — mapeamento do estudo de caso ao KDD

**Notebook:** `01_02_processo_kdd.ipynb`  
**Data:** 2026-08-17  
**Estado:** Aprovado

## Alinhamento e didática

A nova seção relaciona explicitamente as seis etapas apresentadas no notebook ao estudo de evasão. A distinção entre etapa realizada, ilustrada, planejada e não realizada evita que geração sintética seja confundida com treinamento ou avaliação de modelo. A coluna sobre trabalho faltante conecta o exemplo introdutório às unidades posteriores.

## Exatidão técnica

Está correta a observação de que a função logística foi usada como mecanismo gerador do alvo, não como estimador ajustado aos dados. A discussão de iteração, vazamento, validação fora da amostra, baseline e monitoramento é consistente com o processo KDD.

## Reprodutibilidade

Notebook reexecutado integralmente com Python 3.11 por `uv run jupyter nbconvert --execute`: 13 células, IDs completos e nenhuma saída de erro.

**Decisão:** alteração aprovada para publicação, sem correções obrigatórias.
