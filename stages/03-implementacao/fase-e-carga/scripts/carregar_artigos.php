<?php
/**
 * Fase E.2 — Carga dos 139 artigos no destino (kbe_knowledgebase → cgte_base).
 *
 * Lê o WXR CONVERTIDO da Fase D (corpos já em blocos Gutenberg) e insere cada
 * artigo como cgte_base via wp_insert_post, com qualquer status (DP-1):
 *
 * - Reescreve as URLs de mídia do legado (…conhecimento.cefor.ifes.edu.br/
 *   wp-content/uploads/…) para a Media Library local (Fase E.1 é pré-requisito).
 *   Links internos /base/{slug} NÃO são tocados — o redirect 301 do plugin
 *   v0.3.0 os resolve no domínio novo.
 * - Grava _cgte_slug_legado (alimenta o redirect de renomeados — Decisão 34)
 *   e _cgte_id_legado (rastreabilidade com o dump).
 * - Slugs reservados: o filtro wp_unique_post_slug do plugin cgte-estrutura
 *   age sozinho; o script reporta qualquer artigo cujo slug final mudou.
 * - Sem termos de taxonomia (atribuição é da curadoria, Fase G) e sem autor
 *   quando o login do legado não existe no destino (DP-9; criação de autores
 *   legítimos é a E.3).
 *
 * Idempotente: pula artigos cujo _cgte_id_legado já existe — pode re-rodar.
 *
 * Uso (CLI, sem wp-cli):
 *   php carregar_artigos.php RAIZ_WP WXR_CONVERTIDO            (dry-run)
 *   php carregar_artigos.php RAIZ_WP WXR_CONVERTIDO --executar
 */

if ( PHP_SAPI !== 'cli' ) {
	exit( "somente CLI\n" );
}

[ , $raiz_wp, $caminho_wxr ] = $argv + [ null, null, null ];
$executar = in_array( '--executar', $argv, true );

if ( ! $raiz_wp || ! $caminho_wxr || ! is_file( $raiz_wp . '/wp-load.php' ) || ! is_file( $caminho_wxr ) ) {
	exit( "uso: php carregar_artigos.php RAIZ_WP WXR_CONVERTIDO [--executar]\n" );
}

$_SERVER['HTTP_HOST']   = 'localhost';
$_SERVER['REQUEST_URI'] = '/';
require $raiz_wp . '/wp-load.php';

// Roda como admin: sem unfiltered_html o kses mutila os blocos wp:html
// com iframe (fallbacks da conversão).
$admins = get_users( [ 'role' => 'administrator', 'number' => 1 ] );
if ( ! $admins ) {
	exit( "nenhum administrador encontrado no destino\n" );
}
wp_set_current_user( $admins[0]->ID );

if ( ! function_exists( 'CGTE\\Estrutura\\Permalinks\\slugs_reservados' ) ) {
	exit( "plugin cgte-estrutura (>= 0.3.0) precisa estar ativo no destino\n" );
}

$raw = file_get_contents( $caminho_wxr );
$raw = substr( $raw, strpos( $raw, '<?xml' ) );
$xml = simplexml_load_string( $raw );
if ( ! $xml ) {
	exit( "falha ao parsear o WXR\n" );
}

$uploads_baseurl = wp_get_upload_dir()['baseurl'];

// IDs legados já carregados (idempotência).
global $wpdb;
$ja_carregados = array_flip(
	$wpdb->get_col( "SELECT meta_value FROM {$wpdb->postmeta} WHERE meta_key = '_cgte_id_legado'" )
);

$reservados   = CGTE\Estrutura\Permalinks\slugs_reservados();
$inseridos    = 0;
$pulados      = 0;
$reescritas   = 0;
$por_status   = [];
$renomeados   = [];
$criadores    = [];
$erros        = [];

foreach ( $xml->channel->item as $item ) {
	$wp = $item->children( 'http://wordpress.org/export/1.2/' );
	if ( 'kbe_knowledgebase' !== (string) $wp->post_type ) {
		continue;
	}

	$id_legado   = (string) $wp->post_id;
	$slug_legado = (string) $wp->post_name;
	$status      = (string) $wp->status;
	$titulo      = (string) $item->title;
	$dc          = $item->children( 'http://purl.org/dc/elements/1.1/' );
	$criador     = (string) $dc->creator;
	$conteudo    = (string) $item->children( 'http://purl.org/rss/1.0/modules/content/' )->encoded;
	$excerto     = (string) $item->children( 'http://wordpress.org/export/1.2/excerpt/' )->encoded;

	$criadores[ $criador ] = ( $criadores[ $criador ] ?? 0 ) + 1;
	$por_status[ $status ] = ( $por_status[ $status ] ?? 0 ) + 1;

	if ( isset( $ja_carregados[ $id_legado ] ) ) {
		$pulados++;
		continue;
	}

	// Mídia do legado → Media Library local (http e https).
	$antes    = $conteudo;
	$conteudo = preg_replace(
		'#https?://conhecimento\.cefor\.ifes\.edu\.br/wp-content/uploads/#',
		$uploads_baseurl . '/',
		$conteudo,
		-1,
		$qtd
	);
	$reescritas += $qtd;

	if ( in_array( $slug_legado, $reservados, true ) ) {
		$renomeados[ $slug_legado ] = '(colisão com slug reservado — será sufixado)';
	}

	if ( ! $executar ) {
		$inseridos++;
		continue;
	}

	$autor = $criador ? get_user_by( 'login', $criador ) : false;

	$post_id = wp_insert_post(
		[
			'post_type'      => 'cgte_base',
			'post_title'     => $titulo,
			'post_name'      => $slug_legado,
			'post_status'    => $status,
			'post_date'      => (string) $wp->post_date,
			'post_date_gmt'  => (string) $wp->post_date_gmt,
			'post_content'   => $conteudo,
			'post_excerpt'   => $excerto,
			'post_author'    => $autor ? $autor->ID : 0,
			'comment_status' => 'closed',
			'ping_status'    => 'closed',
		],
		true
	);
	if ( is_wp_error( $post_id ) ) {
		$erros[] = "#$id_legado $slug_legado: " . $post_id->get_error_message();
		continue;
	}

	update_post_meta( $post_id, '_cgte_slug_legado', $slug_legado );
	update_post_meta( $post_id, '_cgte_id_legado', $id_legado );

	$slug_final = get_post_field( 'post_name', $post_id );
	if ( $slug_final !== $slug_legado ) {
		$renomeados[ $slug_legado ] = "→ $slug_final";
	}

	$inseridos++;
	if ( 0 === $inseridos % 25 ) {
		echo "  ... $inseridos artigos\n";
	}
}

$modo = $executar ? 'EXECUTADO' : 'DRY-RUN (use --executar para gravar)';
echo "\n$modo\n";
echo 'Inseridos' . ( $executar ? '' : ' (simulado)' ) . ": $inseridos | Pulados (já carregados): $pulados\n";
echo "URLs de mídia reescritas: $reescritas\n";
echo 'Status: ' . json_encode( $por_status ) . "\n";
echo 'Autores do legado (E.3 decide quem criar): ' . json_encode( $criadores, JSON_UNESCAPED_UNICODE ) . "\n";
if ( $renomeados ) {
	echo "Slugs alterados na carga (redirect coberto por _cgte_slug_legado):\n";
	foreach ( $renomeados as $de => $para ) {
		echo "  $de $para\n";
	}
}
foreach ( $erros as $erro ) {
	echo "  ERRO  $erro\n";
}
exit( $erros ? 2 : 0 );
