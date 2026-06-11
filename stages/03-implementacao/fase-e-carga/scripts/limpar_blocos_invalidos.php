<?php
/**
 * Fase E.4 — Limpeza de blocos Gutenberg inválidos nos artigos carregados.
 *
 * O conversor da Fase D preservava a tag de abertura original do legado
 * (TinyMCE) nos blocos wp:paragraph e wp:heading. Atributos como
 * style="padding-left|text-align", class="c0|p1" (paste do Google Docs),
 * id="yui_..." (Moodle), align="justify" e data-start/data-end (paste do
 * ChatGPT) fazem o Gutenberg marcar o bloco como "conteúdo inesperado ou
 * inválido" — a validação compara a tag externa com o que save() geraria
 * (um <p>/<hN> puro). Auditoria de 2026-06-11: 25 dos 139 artigos afetados.
 *
 * O que faz, FORA de blocos wp:html/wp:freeform (raw, nunca tocados):
 *
 * 1. Remove TODO atributo data-* (lixo de paste: ChatGPT data-start/data-end,
 *    Google Sheets data-sheets-*) — em qualquer tag, externa ou interna.
 * 2. Desaninha <p><p ...>…</p></p> dentro de wp:paragraph (artefato de
 *    re-save no editor sobre bloco que já era inválido).
 * 3. Normaliza a tag de abertura do wp:paragraph para <p> puro. Alinhamento
 *    center/right (style ou align=) é PRESERVADO no formato canônico do bloco
 *    ({"align":"…"} + class has-text-align-…); left/justify e padding-left
 *    são descartados (sem equivalente nativo; curadoria refina — DP-7).
 * 4. Normaliza a tag de abertura do wp:heading: mantém apenas
 *    class="wp-block-heading…" e id="…"; descarta o resto.
 *
 * Idempotente: re-rodar sobre conteúdo já limpo não altera nada.
 *
 * Uso (CLI, sem wp-cli):
 *   php limpar_blocos_invalidos.php RAIZ_WP              (dry-run)
 *   php limpar_blocos_invalidos.php RAIZ_WP --executar
 */

if ( PHP_SAPI !== 'cli' ) {
	exit( "somente CLI\n" );
}

[ , $raiz_wp ] = $argv + [ null, null ];
$executar = in_array( '--executar', $argv, true );

if ( ! $raiz_wp || ! is_file( $raiz_wp . '/wp-load.php' ) ) {
	exit( "uso: php limpar_blocos_invalidos.php RAIZ_WP [--executar]\n" );
}

$_SERVER['HTTP_HOST']   = 'localhost';
$_SERVER['REQUEST_URI'] = '/';
require $raiz_wp . '/wp-load.php';

// Roda como admin: sem unfiltered_html o kses mutila iframes nos wp:html.
$admins = get_users( [ 'role' => 'administrator', 'number' => 1 ] );
if ( ! $admins ) {
	exit( "nenhum administrador encontrado no destino\n" );
}
wp_set_current_user( $admins[0]->ID );

/**
 * Extrai alinhamento center/right de uma string de atributos HTML.
 */
function cgte_extrair_align( $attrs ) {
	if ( preg_match( '/style="[^"]*text-align:\s*(center|right)/i', $attrs, $m ) ) {
		return strtolower( $m[1] );
	}
	if ( preg_match( '/\balign="(center|right)"/i', $attrs, $m ) ) {
		return strtolower( $m[1] );
	}
	// forma canônica do Gutenberg (já limpa) — preserva na re-execução
	if ( preg_match( '/\bclass="has-text-align-(center|right)"/i', $attrs, $m ) ) {
		return strtolower( $m[1] );
	}
	return null;
}

/**
 * Limpa um segmento de block markup (já sem os trechos wp:html/freeform).
 */
function cgte_limpar_segmento( $seg, &$stats ) {
	// 1. data-* em qualquer tag.
	$seg = preg_replace( '/\sdata-[\w-]+="[^"]*"/', '', $seg, -1, $n );
	$stats['data_attrs'] += $n;

	// 2 + 3. wp:paragraph — desaninhar e normalizar a tag externa.
	$seg = preg_replace_callback(
		'/<!--\s*wp:paragraph(\s+\{.*?\})?\s*-->(\s*)(.*?)(\s*)<!--\s*\/wp:paragraph\s*-->/s',
		function ( $m ) use ( &$stats ) {
			$json     = trim( (string) $m[1] );
			$body     = $m[3];
			$aninhado = false;

			if ( preg_match( '/^<p([^>]*)>\s*<p([^>]*)>(.*)<\/p>\s*<\/p>$/s', $body, $b ) ) {
				$aninhado = true;
				$attrs    = $b[1] . ' ' . $b[2];
				$inner    = $b[3];
			} elseif ( preg_match( '/^<p([^>]*)>(.*)<\/p>$/s', $body, $b ) ) {
				$attrs = $b[1];
				$inner = $b[2];
			} else {
				return $m[0]; // estrutura inesperada — não toca
			}

			if ( ! $aninhado && '' === trim( $attrs ) ) {
				return $m[0]; // já está limpo
			}

			if ( $aninhado ) {
				$stats['p_aninhado']++;
			}
			$align = cgte_extrair_align( $attrs );
			if ( '' !== trim( $attrs ) ) {
				$stats['p_attrs']++;
			}

			if ( $align ) {
				$dados          = $json ? json_decode( $json, true ) : [];
				$dados['align'] = $align;
				$json_novo      = ' ' . wp_json_encode( $dados, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
				$abertura       = '<p class="has-text-align-' . $align . '">';
				$stats['align_preservado']++;
			} else {
				$json_novo = $json ? ' ' . $json : '';
				$abertura  = '<p>';
			}

			return '<!-- wp:paragraph' . $json_novo . ' -->' . $m[2]
				. $abertura . $inner . '</p>'
				. $m[4] . '<!-- /wp:paragraph -->';
		},
		$seg
	);

	// 4. wp:heading — só class="wp-block-heading…" e id sobrevivem.
	$seg = preg_replace_callback(
		'/(<!--\s*wp:heading(?:\s+\{.*?\})?\s*-->\s*)<h([1-6])([^>]*)>/s',
		function ( $m ) use ( &$stats ) {
			$attrs = $m[3];
			$manter = '';
			if ( preg_match( '/\sclass="(wp-block-heading[^"]*)"/', $attrs, $c ) ) {
				$manter .= ' class="' . $c[1] . '"';
			}
			if ( preg_match( '/\sid="([^"]*)"/', $attrs, $i ) ) {
				$manter .= ' id="' . $i[1] . '"';
			}
			if ( $manter !== $attrs ) {
				$stats['h_attrs']++;
			}
			return $m[1] . '<h' . $m[2] . $manter . '>';
		},
		$seg
	);

	return $seg;
}

/**
 * Limpa o post_content inteiro preservando blocos wp:html/wp:freeform.
 */
function cgte_limpar_conteudo( $content, &$stats ) {
	$partes = preg_split(
		'/(<!--\s*wp:(?:html|freeform)\s*-->.*?<!--\s*\/wp:(?:html|freeform)\s*-->)/s',
		$content,
		-1,
		PREG_SPLIT_DELIM_CAPTURE
	);
	foreach ( $partes as $i => $seg ) {
		if ( preg_match( '/^<!--\s*wp:(html|freeform)/', $seg ) ) {
			continue;
		}
		$partes[ $i ] = cgte_limpar_segmento( $seg, $stats );
	}
	return implode( '', $partes );
}

global $wpdb;
$ids = $wpdb->get_col(
	"SELECT ID FROM {$wpdb->posts}
	 WHERE post_type = 'cgte_base'
	   AND post_status NOT IN ( 'inherit', 'auto-draft', 'trash' )
	 ORDER BY ID"
);

echo $executar ? "== EXECUTANDO ==\n" : "== DRY-RUN (use --executar para gravar) ==\n";

$alterados = 0;
$totais    = [ 'data_attrs' => 0, 'p_aninhado' => 0, 'p_attrs' => 0, 'h_attrs' => 0, 'align_preservado' => 0 ];

foreach ( $ids as $id ) {
	$post  = get_post( $id );
	$stats = [ 'data_attrs' => 0, 'p_aninhado' => 0, 'p_attrs' => 0, 'h_attrs' => 0, 'align_preservado' => 0 ];
	$novo  = cgte_limpar_conteudo( $post->post_content, $stats );

	if ( $novo === $post->post_content ) {
		continue;
	}
	$alterados++;
	foreach ( $stats as $k => $v ) {
		$totais[ $k ] += $v;
	}
	printf(
		"#%d %s\n    data-attrs:%d  p-aninhado:%d  p-attrs:%d  h-attrs:%d  align-preservado:%d\n",
		$id,
		mb_substr( $post->post_title, 0, 60 ),
		$stats['data_attrs'],
		$stats['p_aninhado'],
		$stats['p_attrs'],
		$stats['h_attrs'],
		$stats['align_preservado']
	);

	if ( $executar ) {
		$r = wp_update_post(
			[ 'ID' => $id, 'post_content' => $novo ],
			true
		);
		if ( is_wp_error( $r ) ) {
			echo "    ERRO: " . $r->get_error_message() . "\n";
		}
	}
}

echo "\nArtigos varridos: " . count( $ids ) . "\n";
echo "Artigos alterados: {$alterados}\n";
foreach ( $totais as $k => $v ) {
	echo "  {$k}: {$v}\n";
}
