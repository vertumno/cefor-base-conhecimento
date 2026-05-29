# Guia de teste — import do subset Fase D no DESTINO-LOCAL

Teste **reversível** da conversão SiteOrigin→Gutenberg: importa 5 artigos no
`C:\laragon\www\conhecimento`, valida no editor e no front-end, e desfaz tudo.

- **Banco:** `baseconhecimento2026` (MySQL 5.7.33 do Laragon, `root` sem senha).
- **Arquivo a importar:** `../subset-teste-5-artigos.xml` (5 artigos, já mapeados para `cgte_base`).
- **Rede de segurança:** `backup-banco-ANTES-import.sql` (snapshot já tirado em 2026-05-29).

## Os 5 artigos do subset e o que cada um valida

| post_id | Valida | Título |
|---|---|---|
| 378 | `[caption]` → `wp:image` com legenda | Medium: uma rede de textos colaborativa |
| 1663 | iframe YouTube → `wp:embed` | Como utilizar o aplicativo Moodle Mobile *(draft)* |
| 2901 | `<div>` por parágrafo → `wp:paragraph` | Tempo Ampliado no questionário do Moodle |
| 1271 | listas → `wp:list` + `wp:list-item` | O processo de programação da CGTE *(private)* |
| 2207 | callout estilizado → fallback `wp:html` | Cenário #1: Desafio da Comunicação Clara *(private)* |

## Passo 0 — Snapshot (já feito; refaça se quiser)

```sh
bash backup-banco.sh
```

## Passo 1 — Importar pelo wp-admin

1. Acesse o wp-admin do DESTINO-LOCAL (ex.: `http://conhecimento.test/wp-admin`).
2. **Ferramentas → Importar → WordPress** → *Instalar agora* (instala o plugin
   "WordPress Importer") → *Executar importador*.
3. *Escolher arquivo* → selecione `subset-teste-5-artigos.xml` → **Enviar arquivo e importar**.
4. **Atribuir autores:** mapeie para um usuário existente (ex.: seu admin). Não precisa criar.
5. **NÃO** marque "Download and import file attachments" — as imagens usam URL absoluta do
   legado-vivo (`conhecimento.cefor.ifes.edu.br`), que está no ar; resolvem sozinhas.
6. ⚠️ **DESMARQUE** o checkbox em *Content Options*: **"Change all imported URLs that
   currently link to the previous site so that they now link to this site"** (vem **marcado
   por padrão**). Se ficar marcado, o importer reescreve as URLs das imagens para o endereço
   local — e como os arquivos não estão locais, as imagens quebram. Desmarcado, as URLs do
   legado ficam intactas e as imagens carregam do legado-vivo.
7. **Submit**. Deve terminar com "Tudo pronto. Divirta-se!".

## Passo 2 — Verificar

No admin, menu lateral **Base de Conhecimento** (CPT `cgte_base`):

- Os 5 artigos aparecem (filtre por *Rascunhos* e *Privados* para ver 1663/1271/2207).
- **Abra #2901 e #378 no editor (Gutenberg).** Confirme:
  - os blocos aparecem como parágrafos, títulos, listas e imagem **editáveis**;
  - **nenhum** aviso amarelo "Este bloco contém conteúdo inesperado" / "Tentar
    recuperação em bloco". (Se aparecer, anote em qual artigo/bloco.)
- **#378:** a imagem do fluxo aparece com a legenda abaixo (bloco Imagem).
- **#1663:** o vídeo do YouTube aparece como bloco de incorporação.
- **#1271:** as listas estão como itens de lista editáveis.
- **#2207:** o callout (caixa amarela) aparece como bloco HTML — renderiza, mas
  não é editável bloco-a-bloco (esperado; a curadoria converte depois).
- **Front-end:** em cada artigo, *Visualizar* → o corpo renderiza sem shortcode cru.

## Passo 3 — Desfazer (voltar ao estado anterior)

```sh
bash restaurar-banco.sh
```

Isso remove os 5 posts importados e devolve o banco ao snapshot. Se preferir um reset
ainda mais radical (drop + recreate do banco), avise que eu preparo o comando.

## Se o teste for bem

Decidimos como conduzir a carga completa dos 139 (Fase E): mesmo fluxo de import, ou
script direto. A conversão (Fase D) estará validada de ponta a ponta.
