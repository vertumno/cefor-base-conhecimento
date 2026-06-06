# Sistema de Ícones — Base de Conhecimento CEFOR/Ifes

> **Versão:** 1.0
> **Data:** 2026-06-06
> **Status:** Inventário documentado. Regra de seleção da trilha **em aberto** (ver §3.3).
> **Fase:** 2 — Design System
> **Escopo:** mapeia as 4 famílias de ícones geométricos do projeto e como cada uma é usada nos protótipos canônicos.
> **Referência cruzada:** [`sistema-cards-catalogo.md`](sistema-cards-catalogo.md) (família de artigos, mapeamento categoria→cor e grupo→ícone).

---

## Contexto

Todos os ícones do projeto compartilham uma mesma linguagem visual: formas geométricas no estilo **"blueprint nested"** (outline puro, sem preenchimento, com repetição da forma primária em camadas). A partir desse vocabulário de 8 formas primárias, o projeto compõe 4 famílias de ícones, cada uma com função distinta.

| Família | Pasta | Função | Composição |
|---|---|---|---|
| **Artigos** | `assets/icones_artigos/` | Ícone do **grupo de tópico** no card de artigo | 1 forma simples |
| **Trilha** | `assets/icones_trilha/` | Ícone da **trilha** (jornada de artigos) | 2 formas combinadas (aninhadas) |
| **Percurso** | `assets/icones_percursos/` | Ícone do **percurso** (conjunto de trilhas) | Ilustração numerada (1–6) |
| **Libras** | `assets/icon_libras/` | Toggle do accordion de vídeo em Libras | Símbolo de Libras (mãos) |

> A semântica das entidades (artigo ⊂ trilha ⊂ percurso) está em [`taxonomia.md §6`](../../01-fundacoes/output/taxonomia.md) e nas Decisões 18, 25–32 ([`_config/decisoes.md`](../../../_config/decisoes.md)).

---

## 1. As 8 formas primárias

O vocabulário base, compartilhado por todas as famílias. Cada forma é o ícone de um dos 8 grupos de tópico (ver [`sistema-cards-catalogo.md`](sistema-cards-catalogo.md)).

| Forma | Slug no nome do arquivo | Grupo de tópico associado |
|---|---|---|
| Círculo | `circulo` | Atividades e avaliação Moodle |
| Hexágono | `hexagono` | Recursos Moodle |
| Quadrado | `quadrado` | Gestão do AVA |
| Losango | `losango` | Inteligência Artificial |
| Triângulo | `triangulo` | Acessibilidade |
| Retângulo | `retangulo` | Pedagogia |
| Triângulo retângulo | `triangulo_retangulo` | Identidade institucional |
| Pentágono | `pentagono` | Conduta |

---

## 2. Família Artigos (`icones_artigos/`)

1 forma simples, em 2 variantes de cor (branco / preto). 16 arquivos.

- **Uso nos protótipos:** card de artigo (`.card-illust`), passos da trilha (`.seq-illust`), decoração da home.
- **Convenção de cor:** **branco** sobre fundo colorido (card no light mode); **preto** sobre fundo claro neutro.
- **Documentação completa:** [`sistema-cards-catalogo.md`](sistema-cards-catalogo.md).

---

## 3. Família Trilha (`icones_trilha/`)

### 3.1 Convenção de nome

Cada ícone de trilha combina **duas** das 8 formas primárias, aninhadas:

```
icone_trilha_<FORMA-A>_<FORMA-B>.png
```

Exemplos: `icone_trilha_circulo_hexagono.png`, `icone_trilha_quadrado_circulo.png`, `icone_trilha_triangulo_retangulo_circulo.png` (forma A = `triangulo_retangulo`, forma B = `circulo`).

A combinação de duas formas expressa visualmente que a trilha é uma entidade **composta** (uma jornada que reúne artigos de naturezas distintas), diferenciando-a do ícone de forma única do artigo.

- **Variante:** apenas uma (outline preto/escuro). Não há par branco/preto como na família de artigos.
- **Uso nos protótipos:** fundo do hero da página de trilha (`.hero-bg-icon`), card de trilha em listagens (`base-percurso.html`, `base-inicio-v5.html`, "outras trilhas" em `base-trilha.html`).

### 3.2 Inventário

**53 combinações válidas** em `icones_trilha/` + **10 descartadas** em `icones_trilha/nao-usar/`.

Descartadas (`nao-usar/`) e por quê:
- **Forma repetida** (`icone_trilha_2circulo`, `2hexagono`, `2losango`, `2pentagono`, `2quadrado`, `2retangulo`, `2triangulo`) — a mesma forma duas vezes não cria contraste visual de "composição".
- **Combinações redundantes com triângulo retângulo** (`triangulo_retangulo_triangulo`, `triangulo_triangulo_retangulo`, `triangulo_retangulo_triangulo_retangulo`) — ambíguas de ler e de nomear.

### 3.3 ⚠️ Regra de seleção — EM ABERTO

**Qual combinação de formas representa qual trilha ainda não está definida.** Nos protótipos as combinações foram escolhidas de forma ilustrativa (ex.: `icone_trilha_circulo_tringulo` no hero de exemplo), sem regra formal que ligue um par de formas a uma trilha específica.

Hipótese a validar (não decidida): forma A = grupo de tópico predominante da trilha; forma B = grupo secundário. Precisa de decisão de Elton + Juliana antes da Fase 3, e deve entrar no [`trilhas-percursos-mapa.md`](../../01-fundacoes/output/trilhas-percursos-mapa.md) (atribuir um ícone a cada trilha nomeada).

### 3.4 ⚠️ Inconsistência de grafia nos nomes de arquivo

Vários arquivos grafam "triângulo" como **`tringulo`** (sem o "a") e um como **`trigulo`**. Exemplos:
`icone_trilha_circulo_tringulo.png`, `icone_trilha_pentagono_trigulo_retangulo.png`, `icone_trilha_quadrado_tringulo.png`.

**Estes nomes são "load-bearing":** os protótipos referenciam o arquivo **com o typo** (ex.: `base-trilha.html` linha 307 usa `icone_trilha_circulo_tringulo.png`). Renomear para a grafia correta **quebra os protótipos** — qualquer correção precisa atualizar arquivo **e** referências no mesmo passo. Recomendação: padronizar a grafia (`triangulo`) na Fase 3, junto com a definição da regra de seleção (§3.3).

---

## 4. Família Percurso (`icones_percursos/`)

Ilustrações numeradas de 1 a 6 (`icone_percurso-1.png` … `icone_percurso-6.png`). 6 arquivos.

- **Variante:** uma só (decorativa, monocromática).
- **Uso nos protótipos:** fundo do hero da página de percurso (`.hero-bg-icon`), fundo dos cards de percurso na home (`.pc-bg`).
- **Atribuição percurso→número:** ilustrativa nos protótipos; como há poucos percursos na V1 (núcleo: "Dominando o Moodle"), a atribuição pode ser manual/curatorial, sem regra algorítmica. Confirmar na Fase 3.

---

## 5. Família Libras (`icon_libras/`)

Símbolo de Libras em 3 variantes de cor: `icon_libras_azul.png`, `icon_libras_branco.png`, `icon_libras_preto.png`.

- **Uso nos protótipos:** toggle do accordion de vídeo em Libras no artigo (`base-artigo.html`): `azul` em repouso (`.icon-libras-default`), `branco` em estado ativo (`.icon-libras-active`).
- **Origem:** Decisão 13 + Decisão 19 (Libras é o **primeiro** bloco multimodal do artigo).

---

## 6. Logo (`assets/logo/`)

Não é família de ícone geométrico, mas vive em `assets/`. Identidade da Base:
- `ID_base_verde.png` — logo sobre fundo claro.
- `ID_base_branca.png` — logo sobre fundo escuro/colorido.

---

## Pendências que decorrem deste documento

| Pendência | Bloqueia | Responsável |
|---|---|---|
| Definir regra de seleção trilha→ícone (§3.3) | Atribuição de ícone por trilha na Fase 3/4 | Elton + Juliana |
| Padronizar grafia `tringulo`→`triangulo` + atualizar refs (§3.4) | Limpeza técnica antes do tema WP | Fase 3 |
| Confirmar atribuição percurso→número (§4) | Página de percurso na Fase 3 | Elton + Juliana |

---

## Histórico de versões

| Versão | Data | Mudança | Por |
|---|---|---|---|
| 1.0 | 2026-06-06 | Inventário inicial das 4 famílias de ícones; flag da regra de seleção em aberto e da inconsistência de grafia | Elton |
