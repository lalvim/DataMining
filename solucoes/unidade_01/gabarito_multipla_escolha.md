# Unidade I — Gabarito comentado da múltipla escolha

**Uso:** material do docente e dos revisores. Distribuir separadamente da lista do estudante.  
**Referência principal:** notebooks `01_01_introducao_a_mineracao_de_dados.ipynb` e `01_02_processo_kdd.ipynb`.

## Resumo

| Questão | Resposta | Questão | Resposta | Questão | Resposta |
|---:|:---:|---:|:---:|---:|:---:|
| 1 | D | 6 | C | 11 | B |
| 2 | A | 7 | B | 12 | D |
| 3 | B | 8 | D | 13 | A |
| 4 | C | 9 | A | 14 | C |
| 5 | A | 10 | C | 15 | B |

## Justificativas

### 1. D

Conhecimento útil conecta um resultado validado a uma decisão e considera limites e monitoramento. A alternativa A é um dado; B é informação resumida; C é um padrão ainda não transformado em ação avaliada.

### 2. A

Mineração de dados é a etapa do KDD em que métodos buscam padrões ou modelos. As alternativas B e C reduzem indevidamente o KDD, e D inverte os conceitos.

### 3. B

A saída é um rótulo discreto entre duas classes conhecidas, portanto a tarefa é classificação. Regressão produziria valor contínuo; agrupamento não usaria os rótulos como alvo; associação buscaria coocorrências.

### 4. C

Regressão estima uma saída numérica contínua, como demanda. A corresponde a associação, B a detecção de outliers e D a classificação.

### 5. A

Agrupamento procura estruturas ou grupos sem rótulos predefinidos. B e C apresentam alvos conhecidos, enquanto D descreve a avaliação de uma regra de associação.

### 6. C

Uma observação incomum precisa ser investigada no contexto. Ela pode representar erro, novidade ou evento legítimo. As alternativas A e D confundem anomalia com erro ou fraude, e B impõe um requisito que não existe.

### 7. B

A sequência começa pela decisão, passa pela compreensão e preparação dos dados, aplica métodos e avalia e comunica o resultado. As demais alternativas escolhem métodos ou comunicam resultados antes de formular e verificar o problema.

### 8. D

O processo é iterativo porque avaliação, qualidade dos dados e interpretação podem exigir retorno a etapas anteriores. Repetir mecanicamente um algoritmo, manter atributos fixos ou omitir avaliação não caracteriza iteração do KDD.

### 9. A

A data final de cancelamento ainda não existe no instante da previsão e revela diretamente o desfecho. Isso produz vazamento e uma avaliação artificialmente otimista. Normalização, dimensionalidade e agrupamento não resolvem essa violação temporal.

### 10. C

Prever sempre a classe majoritária alcança alta acurácia sem encontrar casos positivos. Métricas e limiar devem refletir a decisão e os custos dos dois tipos de erro. Raridade não elimina a importância da classe nem exige trocar de tarefa.

### 11. B

Associação sustenta a afirmação de coocorrência nas condições observadas. Ela não estabelece mecanismo causal, invariância em outros contextos nem ausência de variáveis externas.

### 12. D

A alternativa D define saída, frequência e decisão apoiada. As demais começam por tecnologia ou algoritmo e não especificam uso, população, horizonte nem critério de sucesso.

### 13. A

Avaliação e interpretação confrontam métricas, erros, utilidade e limites com a decisão. B é preparação por transformação, C é integração de dados e D pertence à seleção e compreensão.

### 14. C

Uso responsável requer examinar representação, sensibilidade dos atributos, distribuição dos danos e comportamento após implantação. Mais atributos não removem viés, médias podem ocultar desigualdades e automatização não torna um resultado neutro.

### 15. B

A tarefa executada depende da informação fornecida ao algoritmo e da saída solicitada. Sem rótulos e buscando grupos, trata-se de agrupamento, ainda que os pesquisadores conheçam espécies para uma avaliação posterior. A natureza numérica dos atributos não define regressão.

## Distribuição das respostas

| Alternativa | Frequência |
|:---:|---:|
| A | 4 |
| B | 4 |
| C | 4 |
| D | 3 |

A distribuição evita um padrão dominante sem alterar a correção conceitual das questões.
