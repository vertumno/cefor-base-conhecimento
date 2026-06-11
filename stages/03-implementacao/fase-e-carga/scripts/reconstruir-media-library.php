<?php
/**
 * Fase E.1 — Reconstrói a Media Library a partir do WXR + uploads já copiados.
 *
 * Para cada <item> de attachment do WXR, localiza o arquivo correspondente em
 * wp-content/uploads (copiado na Fase C/E.1) e registra o anexo via
 * wp_insert_attachment + wp_generate_attachment_metadata, preservando título,
 * slug, datas, caption, descrição e alt. Grava a URL original do legado no
 * meta `_cgte_url_legada` (insumo da reescrita de URLs do corpo, Fase E.2).
 *
 * Idempotente: anexos cujo _wp_attached_file já existe na biblioteca são
 * pulados — pode rodar de novo após interrupção.
 *
 * Uso (CLI, sem wp-cli):
 *   php reconstruir-media-library.php RAIZ_WP CAMINHO_WXR           (dry-run)
 *   php -d memory_limit=2048M reconstruir-media-library.php RAIZ_WP CAMINHO_WXR --executar
 *
 * O memory_limit alto é necessário: o corpus legado tem PNGs enormes e o GD
 * aloca o bitmap inteiro ao gerar miniaturas (com 512M estoura por volta do
 * anexo 250).
 */

if ( PHP_SAPI !== 'cli' ) {
	exit( "somente CLI\n" );
}

[ , $raiz_wp, $caminho_wxr ] = $argv + [ null, null, null ];
$executar = in_array( '--executar', $argv, true );

if ( ! $raiz_wp || ! $caminho_wxr || ! is_file( $raiz_wp . '/wp-load.php' ) || ! is_file( $caminho_wxr ) ) {
	exit( "uso: php reconstruir-media-library.php RAIZ_WP CAMINHO_WXR [--executar]\n" );
}

// wp-load fora de HTTP precisa de um host para montar home_url.
$_SERVER['HTTP_HOST']   = 'localhost';
$_SERVER['REQUEST_URI'] = '/';
require $raiz_wp . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/image.php';
require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/file.php';

$raw = file_get_contents( $caminho_wxr );
$raw = substr( $raw, strpos( $raw, '<?xml' ) ); // WXR tem linhas em branco antes da declaração
$xml = simplexml_load_string( $raw );
if ( ! $xml ) {
	exit( "falha ao parsear o WXR\n" );
}

$uploads = wp_get_upload_dir();

// Anexos já registrados (idempotência).
global $wpdb;
$ja_registrados = array_flip(
	$wpdb->get_col( "SELECT meta_value FROM {$wpdb->postmeta} WHERE meta_key = '_wp_attached_file'" )
);

$marca      = '/wp-content/uploads/';
$criados    = 0;
$pulados    = 0;
$sem_arquivo = [];
$erros      = [];

foreach ( $xml->channel->item as $item ) {
	$wp = $item->children( 'http://wordpress.org/export/1.2/' );
	if ( 'attachment' !== (string) $wp->post_type ) {
		continue;
	}

	$url_legada = (string) $wp->attachment_url;
	$caminho    = (string) parse_url( $url_legada, PHP_URL_PATH );
	$pos        = strpos( $caminho, $marca );
	if ( false === $pos ) {
		$erros[] = "sem /wp-content/uploads/ na URL: $url_legada";
		continue;
	}
	$rel     = urldecode( substr( $caminho, $pos + strlen( $marca ) ) );
	$arquivo = $uploads['basedir'] . '/' . $rel;

	if ( isset( $ja_registrados[ $rel ] ) ) {
		$pulados++;
		continue;
	}
	if ( ! is_file( $arquivo ) ) {
		$sem_arquivo[] = $rel;
		continue;
	}

	if ( ! $executar ) {
		$criados++;
		continue;
	}

	$tipo    = wp_check_filetype( basename( $arquivo ) );
	$content = $item->children( 'http://purl.org/rss/1.0/modules/content/' );
	$excerpt = $item->children( 'http://wordpress.org/export/1.2/excerpt/' );

	$id = wp_insert_attachment(
		[
			'post_title'     => (string) $item->title ?: basename( $rel ),
			'post_name'      => (string) $wp->post_name,
			'post_content'   => (string) $content->encoded,
			'post_excerpt'   => (string) $excerpt->encoded,
			'post_date'      => (string) $wp->post_date,
			'post_date_gmt'  => (string) $wp->post_date_gmt,
			'post_mime_type' => $tipo['type'] ?: 'application/octet-stream',
			// Sem guid explícito o WP grava o permalink da página do anexo;
			// o padrão da Media Library é a URL do arquivo.
			'guid'           => $uploads['baseurl'] . '/' . $rel,
		],
		$arquivo,
		0,
		true
	);
	if ( is_wp_error( $id ) ) {
		$erros[] = "$rel: " . $id->get_error_message();
		continue;
	}

	wp_update_attachment_metadata( $id, wp_generate_attachment_metadata( $id, $arquivo ) );
	update_post_meta( $id, '_cgte_url_legada', esc_url_raw( $url_legada ) );

	// Alt text vem como postmeta no WXR.
	foreach ( $wp->postmeta as $meta ) {
		if ( '_wp_attachment_image_alt' === (string) $meta->meta_key ) {
			update_post_meta( $id, '_wp_attachment_image_alt', (string) $meta->meta_value );
		}
	}

	$criados++;
	if ( 0 === $criados % 50 ) {
		echo "  ... $criados anexos registrados\n";
	}
}

$modo = $executar ? 'EXECUTADO' : 'DRY-RUN (use --executar para gravar)';
echo "\n$modo\n";
echo 'Registrados' . ( $executar ? '' : ' (simulado)' ) . ": $criados\n";
echo "Pulados (já na biblioteca): $pulados\n";
echo 'Sem arquivo local: ' . count( $sem_arquivo ) . "\n";
foreach ( $sem_arquivo as $rel ) {
	echo "  FALTA  $rel\n";
}
foreach ( $erros as $erro ) {
	echo "  ERRO   $erro\n";
}
exit( $erros ? 2 : 0 );
