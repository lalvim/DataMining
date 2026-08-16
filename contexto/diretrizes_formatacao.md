# Diretrizes de formatação e qualidade dos notebooks

## 1. Objetivo

Estas diretrizes definem o padrão editorial, visual e técnico do material da disciplina. Aplicam-se a todos os notebooks, imagens, fórmulas, trechos de código, dados e exercícios.

## 2. Idioma, tom e terminologia

- Escrever em português brasileiro, com linguagem clara, direta e acadêmica.
- Apresentar o termo em português e, na primeira ocorrência, o equivalente consagrado em inglês quando útil: “agrupamento (_clustering_)”.
- Preferir “conjunto de dados” a “dataset”, exceto em nomes de APIs.
- Distinguir algoritmo, modelo, estimador, atributo, variável-alvo, previsão e inferência.
- Não afirmar causalidade quando o resultado mostrar apenas associação ou correlação.
- Definir toda sigla na primeira ocorrência do notebook.
- Usar exemplos inclusivos e evitar atributos sensíveis sem justificativa pedagógica.

## 3. Estrutura obrigatória de cada notebook

Cada notebook deve seguir esta ordem geral:

1. Título e identificação da unidade.
2. Visão geral e pergunta norteadora.
3. Objetivos de aprendizagem.
4. Pré-requisitos.
5. Importações e configuração.
6. Conteúdo em seções curtas, alternando teoria e prática.
7. Exemplo guiado.
8. Aplicação com dados.
9. Exercícios ou verificação de aprendizagem.
10. Síntese.
11. Referências e fontes.

Modelo de abertura:

```markdown
# Unidade II — Análise de Dados
## Tipos e descrição de dados

**Carga estimada:** 3 horas  
**Pré-requisitos:** Python básico e noções de álgebra.

### Objetivos de aprendizagem

Ao concluir este notebook, você será capaz de:

- identificar tipos de atributos;
- selecionar medidas descritivas adequadas;
- interpretar os resultados no contexto do problema.
```

## 4. Hierarquia Markdown

- Usar exatamente um título de nível 1 (`#`) por notebook.
- Usar `##` para os blocos principais e `###` para subtópicos.
- Evitar níveis abaixo de `####`.
- Não simular títulos com texto em negrito.
- Manter uma linha em branco antes e depois de títulos, listas, tabelas, fórmulas e blocos de código.
- Preferir parágrafos curtos, com uma ideia central.
- Usar listas para sequências ou enumerações, não para fragmentar toda a explicação.
- Usar tabelas apenas quando facilitarem comparação ou consulta.

## 5. Fórmulas em LaTeX

Usar MathJax compatível com Jupyter:

- expressão em linha: `$x_i$`;
- expressão destacada: `$$ ... $$`;
- ambientes como `aligned` dentro de delimitadores destacados;
- comandos LaTeX padrão, evitando pacotes não suportados pelo MathJax.

Toda fórmula deve:

- ser precedida por uma motivação;
- ter símbolos definidos imediatamente antes ou depois;
- explicitar hipóteses relevantes;
- ser seguida por interpretação e, quando adequado, exemplo numérico.

Exemplo:

```markdown
A distância Euclidiana entre dois vetores $\mathbf{x},\mathbf{y}\in\mathbb{R}^d$ é

$$
d(\mathbf{x},\mathbf{y}) =
\sqrt{\sum_{j=1}^{d}(x_j-y_j)^2}.
$$

Nessa expressão, $d$ é o número de atributos e $x_j$ e $y_j$ são os valores do atributo $j$.
```

Convenções:

- escalares em itálico: `$x$`;
- vetores em negrito: `$\mathbf{x}$`;
- matrizes em maiúscula e negrito: `$\mathbf{X}$`;
- conjuntos em maiúscula caligráfica quando necessário: `$\mathcal{D}$`;
- funções e operadores com comandos próprios: `\log`, `\min`, `\arg\max`;
- decimais no código seguem ponto; no texto em português, vírgula.

## 6. Código Python

- Usar exclusivamente o **uv** para selecionar o Python, criar o `.venv`, resolver dependências e executar ferramentas.
- Declarar dependências diretas em `pyproject.toml` por meio de `uv add` ou `uv add --dev`.
- Versionar `.python-version`, `pyproject.toml` e `uv.lock`; não versionar `.venv`.
- Não executar `pip install`, `conda install`, `%pip` ou `!pip` nos notebooks.
- Executar comandos do projeto com `uv run`, por exemplo `uv run jupyter lab`.
- Seguir PEP 8 e usar nomes descritivos em `snake_case`.
- Organizar importações no início: biblioteca padrão, terceiros e módulos locais.
- Evitar `from modulo import *`.
- Não ocultar avisos globalmente sem justificar.
- Fixar sementes aleatórias e registrá-las em uma constante, por exemplo `RANDOM_STATE = 42`.
- Evitar números mágicos; nomear parâmetros importantes.
- Dividir células extensas por responsabilidade conceitual.
- Comentar o motivo de uma decisão, não traduzir literalmente cada linha.
- Usar funções quando um procedimento for repetido ou tiver lógica própria.
- Incluir docstrings e anotações de tipo em funções didáticas não triviais.
- Não usar caminhos absolutos. Resolver arquivos a partir da raiz do projeto ou de caminhos relativos documentados.
- Evitar downloads silenciosos durante a execução. Dados remotos devem ter instrução, licença, versão e alternativa local quando possível.
- Não incluir credenciais, tokens nem dados pessoais.

Uma célula deve produzir apenas saídas relevantes. Remover depuração, tabelas enormes e mensagens desnecessárias antes da publicação.

## 7. Relação entre texto, código e saída

Antes de cada bloco significativo de código, explicar:

- o objetivo da operação;
- as entradas utilizadas;
- o resultado esperado.

Depois da saída, interpretar:

- o que foi observado;
- o que isso responde;
- quais limitações ou próximos passos existem.

Não deixar gráficos, métricas ou tabelas sem comentário. Não antecipar resultados que dependem da execução sem indicar que se trata de uma expectativa.

## 8. Imagens, diagramas e gráficos

### Imagens e diagramas

- Preferir diagramas autorais e arquivos vetoriais (`.svg`) quando possível.
- Imagens raster devem ter resolução suficiente para leitura, sem ampliação artificial.
- Guardar arquivos em `imagens/unidades/` com nomes descritivos em minúsculas.
- Usar caminhos relativos e texto alternativo informativo.
- Incluir legenda, fonte e licença quando a imagem não for autoral.
- Registrar todas as fontes externas em `imagens/fontes.md`.
- Não copiar figuras do livro-guia; recriar apenas os conceitos em diagramas autorais e citar a referência conceitual.

Exemplo:

```markdown
![Etapas iterativas do processo KDD](../../imagens/unidades/unidade_01/processo_kdd.svg)

*Figura 1 — Etapas do processo KDD. Fonte: elaboração própria, baseada em Han, Pei e Tong (2023).*
```

### Gráficos gerados por código

- Usar tamanho e resolução consistentes.
- Informar título, rótulos dos eixos e unidades.
- Incluir legenda somente quando ela acrescentar informação.
- Preferir paletas acessíveis a pessoas com deficiência na percepção de cores.
- Não depender apenas da cor; combinar marcadores, linhas ou rótulos quando necessário.
- Evitar efeitos 3D e elementos decorativos sem função analítica.
- Manter escalas honestas e indicar transformações, cortes e agregações.

Configuração inicial sugerida:

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams.update({
    "figure.figsize": (9, 5),
    "figure.dpi": 120,
    "axes.titlesize": 14,
    "axes.labelsize": 11,
})
```

## 9. Dados e reprodutibilidade

- Documentar origem, versão, licença, data de acesso e significado dos atributos.
- Preservar dados originais em `dados/brutos/`; salvar derivados em `dados/processados/`.
- Não modificar silenciosamente o conjunto bruto.
- Registrar todas as transformações em código executável.
- Usar conjuntos pequenos o suficiente para execução em computador pessoal.
- Quando a aleatoriedade existir, fixar sementes para Python e bibliotecas relevantes.
- O notebook deve executar do início ao fim após reiniciar o kernel.
- Células não podem depender de execução fora de ordem.
- Resultados demorados devem informar tempo aproximado e oferecer uma alternativa reduzida.

## 10. Exercícios e soluções

Cada notebook deve conter ao menos:

- uma verificação conceitual breve;
- um exercício de aplicação ou interpretação;
- indicação clara do produto esperado.

Usar marcadores consistentes:

```markdown
> **Verifique seu entendimento:** explique por que a acurácia pode ser enganosa em dados desbalanceados.

> **Exercício:** implemente a comparação proposta e interprete duas métricas.
```

Soluções extensas devem ficar em `solucoes/` ou em versão separada do notebook. Quando houver código incompleto para o estudante, usar `# TODO:` em pontos específicos e executáveis sempre que possível.

### Listas obrigatórias por unidade

Além dos exercícios inseridos nos notebooks, toda unidade deve possuir:

```text
exercicios/unidade_XX/exercicios_conceituais.md
exercicios/unidade_XX/multipla_escolha.md
solucoes/unidade_XX/gabarito_multipla_escolha.md
```

#### Lista de exercícios conceituais

- Usar formato Markdown e um único título de nível 1.
- Informar unidade, objetivos avaliados, instruções e tempo estimado.
- Cobrir todos os objetivos de aprendizagem da unidade.
- Combinar definição, explicação, comparação, cálculo manual, interpretação e aplicação quando pertinentes.
- Organizar as questões em progressão de dificuldade.
- Evitar questões respondidas apenas pela cópia literal de uma frase do material.
- Indicar dados, fórmulas, arredondamento e produto esperado quando necessários.
- Identificar questões desafiadoras ou opcionais sem misturá-las ao núcleo obrigatório.

Estrutura recomendada:

```markdown
# Unidade II — Exercícios conceituais

**Objetivos avaliados:** ...  
**Tempo estimado:** ...  
**Instruções:** justifique as respostas e apresente os cálculos.

## Fundamentos

1. [Questão]

## Aplicação e interpretação

2. [Questão]

## Desafio opcional

3. [Questão]
```

#### Lista de múltipla escolha

- Cada questão deve possuir enunciado autossuficiente e, preferencialmente, quatro alternativas (`A` a `D`).
- Deve existir uma única melhor resposta, salvo indicação explícita em contrário.
- Distratores devem ser plausíveis e baseados em erros conceituais frequentes.
- Evitar pistas gramaticais, alternativas sobrepostas, negações duplas e opções como “todas as anteriores”.
- Distribuir as alternativas corretas sem padrão previsível.
- Não tornar uma questão dependente da resposta de outra.
- Incluir questões de compreensão e aplicação, não apenas memorização.
- Não inserir respostas ou dicas no arquivo destinado aos estudantes.

#### Gabarito de múltipla escolha

- Ficar obrigatoriamente em `solucoes/`, separado da lista do estudante.
- Repetir o número da questão e indicar a alternativa correta.
- Fornecer justificativa breve e conceitual.
- Explicar o erro representado pelos distratores mais relevantes.
- Referenciar notebook, seção ou bibliografia para revisão quando útil.
- Passar por revisão de exatidão técnica e alinhamento antes da publicação.

## 11. Referências, autoria e direitos autorais

- Citar a fonte de conceitos, dados, imagens e implementações adaptadas.
- Adotar uma forma bibliográfica consistente em toda a disciplina.
- Incluir seção `## Referências` ao final de cada notebook.
- Referenciar o livro por capítulo e seção, sem reproduzir longos trechos ou figuras.
- Textos explicativos devem ser autorais, ainda que baseados na bibliografia.
- Código de terceiros deve respeitar a licença e ter atribuição próxima ao trecho adaptado.

Referência-padrão do livro-guia:

> HAN, Jiawei; PEI, Jian; TONG, Hanghang. _Data Mining: Concepts and Techniques_. 4. ed. Cambridge: Morgan Kaufmann/Elsevier, 2023.

## 12. Acessibilidade

- Fornecer texto alternativo significativo para imagens.
- Garantir contraste adequado e não codificar informação exclusivamente por cor.
- Evitar blocos longos em caixa alta e excesso de itálico.
- Usar títulos hierárquicos para facilitar navegação por leitores de tela.
- Explicar símbolos e siglas.
- Disponibilizar em texto os valores essenciais apresentados apenas visualmente.
- Usar linguagem clara e exemplos que não exijam conhecimento cultural desnecessário.

## 13. Qualidade técnica e validação

Antes de considerar um notebook pronto:

1. Sincronizar o ambiente com `uv sync --frozen`.
2. Reiniciar o kernel e limpar todas as saídas.
3. Executar todas as células na ordem usando uma ferramenta iniciada com `uv run`.
4. Confirmar ausência de erros e dependência de estado oculto.
5. Conferir fórmulas renderizadas, links e imagens.
6. Verificar se resultados numéricos sustentam a interpretação.
7. Revisar ortografia, terminologia e referências.
8. Conferir tempo e consumo de memória.
9. Validar que `pyproject.toml` e `uv.lock` contêm todas as dependências.
10. Registrar a validação em `contexto/registro_execucao.md`.

Ferramentas de validação poderão incluir execução via `jupyter nbconvert --execute`, limpeza controlada de metadados e verificação estática, desde que configuradas e documentadas no projeto.

## 14. Checklist editorial por notebook

- [ ] Um único título de nível 1.
- [ ] Objetivos e pré-requisitos explícitos.
- [ ] Termos e siglas definidos.
- [ ] Fórmulas motivadas, símbolos explicados e resultados interpretados.
- [ ] Código legível, reprodutível e sem caminhos absolutos.
- [ ] Sementes aleatórias fixadas.
- [ ] Gráficos legíveis, acessíveis e interpretados.
- [ ] Imagens com texto alternativo, legenda, fonte e licença.
- [ ] Dados documentados e transformações rastreáveis.
- [ ] Exercícios com instruções e produto esperado.
- [ ] Lista conceitual da unidade criada e alinhada aos objetivos.
- [ ] Lista de múltipla escolha criada sem exposição das respostas.
- [ ] Gabarito separado, comentado e tecnicamente revisado.
- [ ] Referências completas.
- [ ] Execução limpa concluída sem erros.
- [ ] Registro de execução atualizado.
