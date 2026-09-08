# Unidade III — Pré-processamento de Dados — Múltipla escolha

**Instruções:** assinale uma única alternativa por questão. Registre suas respostas sem consultar o gabarito, que é distribuído separadamente.

## U03-M01

Qual exemplo representa um valor válido, mas possivelmente inexato?

- [ ] **A.** Idade registrada como -4
- [ ] **B.** CEP com letras em um campo numérico
- [ ] **C.** Idade 40 para uma pessoa que na realidade tem 37
- [ ] **D.** Cliente sem identificador obrigatório

## U03-M02

Qual afirmação sobre imputação pela mediana é correta?

- [ ] **A.** Recupera o valor verdadeiro de cada observação
- [ ] **B.** Elimina qualquer viés causado por ausência
- [ ] **C.** Deve sempre ser calculada em toda a base
- [ ] **D.** Pode reduzir artificialmente a variabilidade

## U03-M03

O que `validate="one_to_one"` verifica em uma junção do pandas?

- [ ] **A.** Se as chaves são únicas em ambos os lados
- [ ] **B.** Se todas as colunas têm o mesmo tipo
- [ ] **C.** Se não existem valores ausentes
- [ ] **D.** Se as tabelas possuem o mesmo número de linhas

## U03-M04

Uma junção muitos-para-muitos inesperada pode:

- [ ] **A.** Padronizar automaticamente as chaves
- [ ] **B.** Multiplicar linhas e inflar somas
- [ ] **C.** Impedir qualquer correspondência
- [ ] **D.** Converter a junção em amostragem

## U03-M05

Qual prática preserva melhor a rastreabilidade da limpeza?

- [ ] **A.** Sobrescrever o arquivo bruto e guardar apenas o resultado
- [ ] **B.** Corrigir valores manualmente sem registrar a regra
- [ ] **C.** Preservar o bruto e produzir derivados por código versionado
- [ ] **D.** Remover todas as linhas incompletas

## U03-M06

Usando limites de treino 10 e 40, o min–max de um novo valor 50 é:

- [ ] **A.** 1,33 aproximadamente
- [ ] **B.** 1,00 exatamente
- [ ] **C.** 0,75 aproximadamente
- [ ] **D.** Impossível por definição

## U03-M07

Padronizar um atributo garante que:

- [ ] **A.** Seus valores fiquem entre zero e um
- [ ] **B.** Sua distribuição se torne normal
- [ ] **C.** Seus outliers sejam removidos
- [ ] **D.** No conjunto de ajuste, ele fique centrado e expresso em unidades de desvio-padrão

## U03-M08

Para um atributo nominal como município, qual representação evita impor ordem arbitrária?

- [ ] **A.** Substituir por ordem alfabética 1, 2, 3
- [ ] **B.** Codificação one-hot
- [ ] **C.** Usar a média dos nomes
- [ ] **D.** Aplicar logaritmo

## U03-M09

Em relação à discretização por quantis, é correto afirmar que:

- [ ] **A.** Seus intervalos sempre têm a mesma largura
- [ ] **B.** Ela não perde informação
- [ ] **C.** Busca frequências semelhantes e aprende limites da amostra
- [ ] **D.** Seus limites independem de valores repetidos

## U03-M10

Qual fluxo evita contaminação do teste?

- [ ] **A.** Ajustar escala em todos os dados e depois separar
- [ ] **B.** Separar, ajustar transformações no treino e apenas transformar o teste
- [ ] **C.** Ajustar um imputador diferente no teste
- [ ] **D.** Escolher transformações depois de observar a métrica final do teste

## U03-M11

Preservar a proporção da classe em uma amostra estratificada garante:

- [ ] **A.** Ausência de viés de coleta
- [ ] **B.** Representatividade em todos os atributos
- [ ] **C.** Igualdade de todas as estatísticas
- [ ] **D.** Apenas controle aproximado da distribuição usada na estratificação

## U03-M12

Qual alternativa descreve seleção de atributos?

- [ ] **A.** Manter um subconjunto das colunas originais
- [ ] **B.** Criar componentes como combinações das colunas
- [ ] **C.** Selecionar apenas algumas linhas
- [ ] **D.** Calcular médias mensais

## U03-M13

Antes da PCA, a padronização costuma ser importante porque:

- [ ] **A.** PCA exige entradas entre zero e um
- [ ] **B.** Ela transforma categorias em números
- [ ] **C.** A variância depende da escala e pode ser dominada por atributos de maior magnitude
- [ ] **D.** Ela faz os componentes usarem o alvo

## U03-M14

Preservar 95% da variância na PCA significa que:

- [ ] **A.** O modelo preservará exatamente 95% da acurácia
- [ ] **B.** A soma da variância explicada pelos componentes mantidos é 95% da variância considerada
- [ ] **C.** Apenas 5% das linhas foram removidas
- [ ] **D.** A reconstrução não tem erro

## U03-M15

Qual medida avalia diretamente a fidelidade de uma reconstrução PCA no espaço padronizado?

- [ ] **A.** Número de classes
- [ ] **B.** Taxa de ausências
- [ ] **C.** Cardinalidade da junção
- [ ] **D.** RMSE entre valores originais e reconstruídos


