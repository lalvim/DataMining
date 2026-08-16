# Revisores do material didático

## Finalidade

Esta pasta reúne os protocolos dos revisores especializados da disciplina. Cada revisor analisa o mesmo notebook sob uma perspectiva diferente e registra evidências, problemas e recomendações sem reescrever silenciosamente o material.

Os pareceres devem ser salvos em:

```text
contexto/revisores/pareceres/<unidade>/<nome_do_notebook>/<especialidade>.md
```

Exemplo:

```text
contexto/revisores/pareceres/unidade_02/02_03_similaridade_e_dissimilaridade/didatica.md
```

## Especialidades

| Revisor | Arquivo | Pergunta central |
|---|---|---|
| Didática | `revisor_didatica.md` | O estudante consegue aprender seguindo a sequência proposta? |
| Referências | `revisor_referencias.md` | As fontes sustentam o conteúdo e estão corretamente atribuídas? |
| Alinhamento | `revisor_alinhamento.md` | O material atende à ementa, aos objetivos e ao plano da unidade? |
| Nível acadêmico | `revisor_nivel_academico.md` | A profundidade e o rigor são adequados a uma disciplina de graduação? |
| Exatidão técnica | `revisor_exatidao_tecnica.md` | Conceitos, fórmulas, código e interpretações estão corretos? |
| Qualidade editorial e acessibilidade | `revisor_editorial_acessibilidade.md` | O notebook segue o padrão visual, textual e de acessibilidade? |
| Reprodutibilidade | `revisor_reprodutibilidade.md` | O material pode ser executado e reproduzido em ambiente limpo? |

## Ordem recomendada de revisão

1. **Exatidão técnica** — elimina erros conceituais, matemáticos e computacionais.
2. **Referências** — verifica sustentação acadêmica, autoria e licenças.
3. **Alinhamento** — confere cobertura da unidade e evita desvios de escopo.
4. **Nível acadêmico** — calibra profundidade, pré-requisitos e exigência.
5. **Didática** — avalia progressão, exemplos, atividades e carga cognitiva.
6. **Editorial e acessibilidade** — uniformiza apresentação e acesso.
7. **Reprodutibilidade** — realiza a validação final em ambiente limpo.

Uma nova rodada deve ocorrer quando correções substanciais alterarem conteúdo, fórmulas, código, dados ou resultados.

## Regras comuns

Todo revisor deve:

- ler o notebook completo e as diretrizes aplicáveis antes de emitir o parecer;
- avaliar apenas sua especialidade, indicando problemas de outra área como encaminhamentos;
- citar a seção, célula, título, fórmula ou trecho que sustenta cada observação;
- distinguir erro comprovado, risco, sugestão e preferência editorial;
- propor correções executáveis e proporcionais ao problema;
- não aprovar conteúdo que não tenha sido efetivamente verificado;
- registrar quando um critério não se aplica;
- evitar elogios genéricos sem evidência;
- usar o modelo `modelo_parecer.md`;
- concluir com um dos estados padronizados.

## Estados do parecer

- **Aprovado:** não há correção obrigatória.
- **Aprovado com ressalvas:** há melhorias recomendadas, mas nenhuma impede o uso.
- **Correções obrigatórias:** existem problemas que impedem a aprovação.
- **Bloqueado:** faltam arquivos, fontes, execução ou informações indispensáveis à análise.

## Severidade dos achados

- **Crítica:** pode ensinar conteúdo incorreto, gerar resultado inválido, violar direitos ou impedir a execução.
- **Alta:** compromete objetivo de aprendizagem, rigor, interpretação ou parte importante da experiência.
- **Média:** reduz clareza, consistência, acessibilidade ou qualidade, sem invalidar o núcleo.
- **Baixa:** melhoria localizada de apresentação ou acabamento.

## Regra de aprovação final

Um notebook somente pode ser marcado como concluído em `contexto/registro_execucao.md` quando:

- nenhum parecer contiver achado crítico ou alto pendente;
- todos os revisores tiverem emitido um estado;
- as correções obrigatórias estiverem resolvidas ou formalmente justificadas;
- o revisor de reprodutibilidade confirmar a execução limpa;
- o responsável pela consolidação preencher `checklist_consolidacao.md`.
