# Base de Conhecimento CEFOR/IFes

Workspace para o redesign da Base de Conhecimento do CEFOR. Cada stage corresponde a uma fase do projeto. O output de cada stage alimenta o proximo.

## Folder Map

```
Base-conhecimento-oficial/
├── CLAUDE.md              (voce esta aqui)
├── CONTEXT.md             (roteamento de tarefas)
├── setup/                 (onboarding do projeto)
├── _config/               (identidade do projeto, pilares, decisoes)
│   ├── projeto.md         (visao, equipe, premissas, plataforma)
│   ├── pilares.md         (os 11 pilares do sistema)
│   └── decisoes.md        (decisoes de consolidacao Fase 0 -> Fase 1)
├── stages/
│   ├── 00-benchmarking/   (Fase 0 -- pesquisa e benchmarking) [CONCLUIDA]
│   ├── 01-fundacoes/      (Fase 1 -- content system + taxonomia + descoberta)
│   ├── 02-design-system/  (Fase 2 -- visual, leitura, acessibilidade, interacao)
│   ├── 03-implementacao/  (Fase 3 -- tema WordPress + componentes + templates)
│   ├── 04-conteudo/       (Fase 4 -- producao e reescrita de artigos)
│   └── 05-lancamento/     (Fase 5 -- lancamento e operacao continua)
├── shared/                (recursos cross-stage: roadmap, ata, transcricao)
├── data/                  (dados brutos: inventario base antiga, URLs)
└── _archive/              (arquivos inativos: design-md)
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Rodar onboarding (configuracao do projeto) |
| `status` | Mostrar progresso do pipeline por fase |

## Routing

| Voce quer... | Va para |
|---|---|
| Ver em que fase o projeto esta | Digitar `status` |
| Trabalhar na Fase 1 (Fundacoes) | `stages/01-fundacoes/CONTEXT.md` |
| Trabalhar na Fase 2 (Design System) | `stages/02-design-system/CONTEXT.md` |
| Trabalhar na Fase 3 (Implementacao WP) | `stages/03-implementacao/CONTEXT.md` |
| Trabalhar na Fase 4 (Conteudo) | `stages/04-conteudo/CONTEXT.md` |
| Trabalhar na Fase 5 (Lancamento) | `stages/05-lancamento/CONTEXT.md` |
| Consultar decisoes da Fase 0 | `_config/decisoes.md` |
| Ver o roadmap geral | `shared/roadmap.md` |
| Consultar os 11 pilares | `_config/pilares.md` |
| Ver pesquisa de benchmarking | `stages/00-benchmarking/output/` |

## What to Load

| Task | Load These | Do NOT Load |
|---|---|---|
| Fase 1 work | `_config/decisoes.md`, `_config/pilares.md`, `stages/01-fundacoes/CONTEXT.md`, `stages/00-benchmarking/output/relatorio-comparativo.md` | stages/02-05, _archive/, data/ |
| Fase 2 work | `_config/pilares.md`, `stages/02-design-system/CONTEXT.md`, `stages/01-fundacoes/output/` | stages/00, 03-05, data/ |
| Fase 3 work | `stages/03-implementacao/CONTEXT.md`, `stages/01-fundacoes/output/`, `stages/02-design-system/output/` | stages/00, 04-05, data/ |
| Fase 4 work | `stages/04-conteudo/CONTEXT.md`, `stages/01-fundacoes/output/` | stages/00, 02-03, 05 |
| Quick reference | `_config/projeto.md` | Tudo o resto |

## Stage Handoffs

Cada stage escreve seus entregaveis na pasta `output/`. O proximo stage le de la. Se voce editar um arquivo de output entre stages, o proximo stage usa a versao editada.

Fluxo principal: 00 -> 01 -> 02 -> 03 -> 04 -> 05

Paralelismo possivel: Fase 4.1 (triagem) pode comecar junto com Fase 2/3.
