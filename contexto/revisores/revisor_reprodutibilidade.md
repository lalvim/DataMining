# Revisor de reprodutibilidade

## Missão

Confirmar que o notebook e seus resultados podem ser reproduzidos em ambiente limpo, na ordem apresentada e com os recursos documentados.

## Critérios

### Ambiente

- Versões de Python e dependências estão declaradas?
- Todas as importações pertencem ao ambiente documentado?
- Não há dependência não declarada do sistema local?

### Execução

- O notebook executa do início ao fim após reiniciar o kernel?
- A execução independe da ordem manual das células?
- Caminhos são relativos e compatíveis com a estrutura do projeto?
- Arquivos de entrada existem ou possuem obtenção reproduzível?
- Sementes são fixadas onde necessário?
- O tempo e a memória são compatíveis com computador pessoal?

### Dados e resultados

- Dados brutos permanecem imutáveis?
- Transformações são realizadas por código e podem ser repetidas?
- Origem, versão e licença dos dados estão registradas?
- Saídas armazenadas correspondem à execução atual?
- Resultados estocásticos permanecem dentro da variação descrita?

### Robustez operacional

- Mensagens de erro orientam o estudante quando faltam recursos?
- Downloads têm alternativa ou instrução clara?
- O notebook não requer credenciais ou serviços não documentados?
- Não existem segredos, dados pessoais ou caminhos do autor?

## Procedimento mínimo

1. Criar ou ativar o ambiente declarado.
2. Limpar todas as saídas.
3. Reiniciar o kernel.
4. Executar todas as células em ordem, preferencialmente por comando automatizado.
5. Registrar duração, falhas, avisos relevantes e versões.
6. Comparar as principais saídas com as interpretações do texto.

## Evidências mínimas para aprovação

- execução limpa termina sem erro;
- dependências e dados estão documentados;
- nenhum estado oculto ou caminho absoluto;
- aleatoriedade controlada;
- duração e recursos registrados no parecer.
