# Unidade I — Exercícios conceituais

**Tema:** Mineração de Dados e processo KDD  
**Objetivos avaliados:** distinguir dados, informação, padrões e conhecimento; reconhecer tarefas de mineração; formular problemas; descrever as etapas do KDD; analisar riscos e critérios de sucesso.  
**Tempo estimado:** 90 minutos  
**Instruções:** responda com suas próprias palavras, justifique as decisões e explicite qualquer hipótese adotada. Quando houver mais de uma resposta defensável, a qualidade da justificativa será parte da avaliação.

## Fundamentos

1. Uma rede de supermercados armazena data, horário, produtos e valor de cada compra. Diferencie, nesse contexto:

   a. dado;
   b. informação;
   c. padrão;
   d. conhecimento útil para uma decisão.

   Apresente um exemplo específico para cada conceito e mostre como eles se relacionam.

2. Explique por que mineração de dados não é sinônimo de descoberta de conhecimento em bases de dados (KDD). Em sua resposta, indique o que pode dar errado quando uma equipe se concentra somente no treinamento de um algoritmo.

3. Classifique cada pergunta como tarefa de **classificação**, **regressão**, **agrupamento**, **associação** ou **detecção de outliers**. Identifique também a saída esperada.

   a. Qual será o consumo de energia de uma residência no próximo mês?  
   b. Esta mensagem é legítima ou tentativa de fraude?  
   c. Quais produtos aparecem frequentemente na mesma compra?  
   d. Que perfis de uso surgem entre clientes sem categorias predefinidas?  
   e. Qual sensor apresenta comportamento incompatível com os demais?

4. Classificação e regressão são frequentemente descritas como tarefas preditivas, enquanto agrupamento e associação são descritas como tarefas descritivas. Explique essa distinção e apresente uma situação em que ela não seja suficiente para caracterizar todo o problema.

5. O mesmo conjunto Iris pode ser usado em classificação, agrupamento, regressão e detecção de outliers. Formule uma pergunta para cada uma dessas quatro tarefas e identifique entrada e saída.

## Processo KDD

6. Organize as seguintes ações em um processo coerente de descoberta de conhecimento. Em seguida, explique por que a ordem não deve ser interpretada como uma sequência rígida e irreversível.

   - avaliar se o resultado atende à decisão;
   - compreender o problema;
   - comunicar o conhecimento;
   - selecionar e compreender os dados;
   - aplicar um método de mineração;
   - limpar e transformar os dados.

7. Uma universidade deseja “usar inteligência artificial para reduzir evasão”. Reescreva essa intenção como um problema operacional mais preciso. Sua formulação deve incluir:

   - decisão que será apoiada;
   - unidade de análise;
   - horizonte temporal;
   - tarefa de mineração candidata;
   - saída esperada;
   - pelo menos um critério de sucesso técnico e um institucional.

8. Para o problema de evasão da questão anterior, proponha cinco atributos que poderiam estar disponíveis no momento da previsão. Para cada atributo, informe:

   - significado;
   - momento em que se torna disponível;
   - possível problema de qualidade;
   - risco ético ou de interpretação, quando pertinente.

9. Considere um conjunto em que somente 5% dos exemplos pertencem à classe positiva. Um sistema que sempre prevê a classe negativa alcança 95% de acurácia.

   a. Por que esse valor não demonstra utilidade?  
   b. Que informação adicional seria necessária para escolher métricas adequadas?  
   c. Proponha um modelo de referência mais informativo que a previsão constante.

10. Explique o conceito de vazamento de dados. Depois, avalie os atributos abaixo em um sistema que prevê, no início do semestre, quais estudantes abandonarão uma disciplina até o final do período:

    a. média das disciplinas cursadas em semestres anteriores;  
    b. número de faltas acumuladas até o final do semestre atual;  
    c. curso e período do estudante;  
    d. registro administrativo da data de abandono.

    Indique quais atributos causam vazamento para esse uso e justifique.

## Aplicação e reflexão crítica

11. Um modelo identifica forte associação entre a compra de protetor solar e a compra de água. Liste pelo menos quatro explicações possíveis para o padrão. Explique por que a associação, isoladamente, não permite concluir que um produto causa a compra do outro.

12. Uma prefeitura pretende agrupar bairros para orientar políticas públicas. Analise o projeto sob quatro dimensões:

    - representatividade dos dados;
    - escolha dos atributos e da medida de similaridade;
    - interpretação dos grupos;
    - impacto sobre diferentes populações.

    Para cada dimensão, formule uma pergunta de controle que deveria ser respondida antes do uso do resultado.

13. Compare os custos de falso positivo e falso negativo em dois cenários:

    a. detecção de uma transação possivelmente fraudulenta;  
    b. priorização de uma inspeção preventiva em equipamento industrial.

    Mostre por que o mesmo limiar de decisão não deve ser escolhido automaticamente nos dois casos.

14. Escolha uma aplicação de mineração de dados em educação, saúde, indústria, meio ambiente ou comércio. Produza um plano de uma página contendo:

    - pergunta e decisão apoiada;
    - população e unidade de análise;
    - tarefa de mineração;
    - dados necessários e sua origem;
    - etapas do KDD e entregas verificáveis;
    - estratégia de avaliação;
    - riscos de privacidade, viés ou uso indevido;
    - plano inicial de comunicação e monitoramento.

## Desafio opcional

15. Compare KDD, mineração de dados, aprendizado de máquina e ciência de dados. Construa um diagrama próprio mostrando sobreposições e diferenças. Não existe uma única representação universal: explicite as definições adotadas e cite ao menos duas fontes acadêmicas.
