# Fase D — Conversão do conteúdo (HTML clássico → Gutenberg)

Converte o corpo dos 139 artigos `kbe_knowledgebase` do WXR da base antiga para
block markup Gutenberg (blocos core), de mínima fricção, sem reescrita (DP-7).

## Achado que corrige o roadmap

O roadmap (rev.3) assumia que o corpo estava **preso ao SiteOrigin Page Builder**.
A análise do WXR de 21/05 mostrou que **isso é falso para os artigos**: nenhum dos 139
usa SiteOrigin (`panels_data`/`[siteorigin_widget]` = 0). O corpo é **HTML clássico
TinyMCE** com parágrafos implícitos, UTF-8 válido. A conversão é, portanto, muito mais
simples do que o previsto.

## Pipeline

```
post_content (HTML clássico)
  → normalizar shortcodes  ([caption]→wp:image, [embed]/iframe→wp:embed YouTube,
                            [display-posts]/[libras]→wp:shortcode)  [placeholders atômicos]
  → wpautop                (insere <p> nos parágrafos implícitos)
  → tokenizar nível superior
  → mapear cada elemento   (p→paragraph, h1-6→heading, ul/ol→list+list-item,
                            img→image, hr→separator, blockquote→quote, pre→preformatted,
                            table→table, div-inline→paragraph, resto→html)
  → resolver placeholders
```

## Scripts (`scripts/`)

| Script | O que faz |
|---|---|
| `converter.py` | Módulo central. `html_para_blocos(post_content)` é a API. |
| `analisar_corpus.py <wxr>` | Caracteriza o corpus (status, tags, shortcodes, mídia). |
| `amostrar.py <wxr> [needle] [n]` | Mostra `post_content` cru de artigos. |
| `testar.py <wxr> [needle] [n]` | Mostra a conversão de artigos. |
| `qa.py <wxr>` | Varredura: distribuição de blocos, fallbacks, placeholders órfãos. |
| `gerar_wxr.py <entrada> <saida> [relatorio]` | Gera o WXR convertido + relatório. |

Requer Python 3 (testado em 3.14), só stdlib. O WXR de entrada tem ~12 linhas em branco
antes da declaração `<?xml` — todos os scripts cortam tudo antes de `<?xml`.

## Saída (`output/`)

- `basedeconhecimento-gutenberg-2026-05-29.xml` — WXR com os 139 corpos convertidos.
  **Preserva CDATA e toda a estrutura** (584 items, attachments, termos, postmeta,
  autores intactos) — substituição textual cirúrgica, sem reserializar.
- `relatorio-conversao.md` — distribuição de blocos + lista de artigos com fallback.

## Regenerar

```sh
cd scripts
python gerar_wxr.py \
  "C:/laragon/www/migracao-base-conhecimento/BASE ANTIGA - basedeconhecimento.wordpress.2026-05-21.xml" \
  ../output/basedeconhecimento-gutenberg-2026-05-29.xml \
  ../output/relatorio-conversao.md
```

## Validação feita

- XML de saída bem-formado; 584 items preservados; `post_types` idênticos à entrada.
- 139/139 artigos com blocos Gutenberg; 0 attachments tocados; 0 placeholders órfãos.
- Casos especiais conferidos contra artigos reais: `[caption]`, `[embed]`, iframe YouTube,
  `[display-posts]`, listas ordenadas/não-ordenadas, headings, divs-parágrafo.

## Limitações aceitas (DP-7 — "aceita imperfeição")

- 14 artigos têm trechos em `wp:html` (callouts estilizados, listas aninhadas/malformadas).
  Renderizam corretamente; a curadoria (Fase G) converte em blocos editoriais ao revisar.
- Sem reescrita de conteúdo. Mapeamento de eixos, subtítulos e blocos multimodais são Fase G.

## Próximo passo

Validar o import do WXR no DESTINO-LOCAL (`C:\laragon\www\conhecimento`) — confere se o
Gutenberg lê os blocos sem avisos de "recuperação". Depois alimenta a Fase E (carga).
