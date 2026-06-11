<?php
/**
 * Fase G — aplica o mapeamento de curadoria no destino.
 *
 * Lê `mapeamento-curadoria.json` (gerado por consolidar_mapeamento.py) e:
 *  1. Atribui cgte_tipo (1), cgte_categoria (1) e cgte_topico (0-4) a cada
 *     artigo classificado, por wp_id (conferindo o slug antes de tocar).
 *  2. Grava o meta cgte_subtitulo do artigo.
 *  3. Cria/atualiza os posts cgte_trilha (T1-T10) com cgte_artigos na ordem
 *     do mapa e cgte_subtitulo. Idempotente pelo meta _cgte_trilha_sigla.
 *  4. Cria/atualiza o cgte_percurso "Dominando o Moodle" (trilhas + artigos
 *     complementares + rotas de entrada). Idempotente pelo slug.
 *
 * Artigos com acao=nao-classificar são pulados e reportados (utilitários e
 * fora-da-base — decisão de arquivamento fica com a curadoria).
 *
 * Uso (CLI, sem wp-cli):
 *   php aplicar_curadoria.php RAIZ_WP MAPEAMENTO.json             (dry-run)
 *   php aplicar_curadoria.php RAIZ_WP MAPEAMENTO.json --executar
 */

if ( PHP_SAPI !== 'cli' ) {
	exit( "somente CLI\n" );
}

[ , $raiz_wp, $caminho_mapa ] = $argv + [ null, null, null ];
$executar = in_array( '--executar', $argv, true );

if ( ! $raiz_wp || ! $caminho_mapa || ! is_file( $raiz_wp . '/wp-load.php' ) || ! is_file( $caminho_mapa ) ) {
	exit( "uso: php aplicar_curadoria.php RAIZ_WP MAPEAMENTO.json [--executar]\n" );
}

$_SERVER['HTTP_HOST']   = 'localhost';
$_SERVER['REQUEST_URI'] = '/';
require $raiz_wp . '/wp-load.php';

if ( ! taxonomy_exists( 'cgte_tipo' ) || ! post_type_exists( 'cgte_trilha' ) ) {
	exit( "plugin cgte-estrutura precisa estar ativo no destino\n" );
}

$admins = get_users( [ 'role' => 'administrator', 'number' => 1 ] );
if ( ! $admins ) {
	exit( "nenhum administrador encontrado no destino\n" );
}
wp_set_current_user( $admins[0]->ID );

$mapa = json_decode( file_get_contents( $caminho_mapa ), true );
if ( ! $mapa ) {
	exit( "falha ao parsear o mapeamento\n" );
}

echo $executar ? "== EXECUTANDO ==\n" : "== DRY-RUN (use --executar para aplicar) ==\n";

/* ---------------------------------------------------------- helpers */

function term_id_ou_falha( string $taxonomia, string $campo, string $valor ): int {
	$term = get_term_by( $campo, $valor, $taxonomia );
	if ( ! $term ) {
		exit( "termo não encontrado: {$taxonomia} {$campo}={$valor}\n" );
	}
	return (int) $term->term_id;
}

/* ------------------------------------------------ 1+2. artigos */

$stats = [ 'classificados' => 0, 'pulados' => 0, 'erros' => 0 ];
$id_inv_para_wp = [];

foreach ( $mapa['artigos'] as $art ) {
	if ( null !== $art['id_inventario'] ) {
		$id_inv_para_wp[ $art['id_inventario'] ] = $art['wp_id'];
	}
}

foreach ( $mapa['artigos'] as $art ) {
	$post = get_post( $art['wp_id'] );
	if ( ! $post || 'cgte_base' !== $post->post_type || $post->post_name !== $art['slug'] ) {
		echo "ERRO: wp_id {$art['wp_id']} não confere (esperado slug {$art['slug']})\n";
		$stats['erros']++;
		continue;
	}

	if ( isset( $art['acao'] ) && 'nao-classificar' === $art['acao'] ) {
		echo "  pulado (não classificar): {$art['wp_id']} {$art['titulo']}\n";
		$stats['pulados']++;
		continue;
	}

	$tipo_id      = term_id_ou_falha( 'cgte_tipo', 'name', $art['tipo'] );
	$categoria_id = term_id_ou_falha( 'cgte_categoria', 'slug', $art['categoria'] );
	$topico_ids   = array_map(
		fn( $t ) => term_id_ou_falha( 'cgte_topico', 'name', $t ),
		$art['topicos']
	);

	if ( $executar ) {
		wp_set_object_terms( $art['wp_id'], [ $tipo_id ], 'cgte_tipo', false );
		wp_set_object_terms( $art['wp_id'], [ $categoria_id ], 'cgte_categoria', false );
		wp_set_object_terms( $art['wp_id'], $topico_ids, 'cgte_topico', false );
		update_post_meta( $art['wp_id'], 'cgte_subtitulo', $art['subtitulo'] );
	}
	$stats['classificados']++;
}

echo "\nArtigos: {$stats['classificados']} classificados, {$stats['pulados']} pulados, {$stats['erros']} erros.\n";

/* ------------------------------------------------ 3. trilhas */

$trilha_post_ids = [];

foreach ( $mapa['trilhas'] as $sigla => $trilha ) {
	$artigo_ids = [];
	foreach ( $trilha['artigos'] as $id_inv ) {
		if ( ! isset( $id_inv_para_wp[ $id_inv ] ) ) {
			exit( "trilha {$sigla}: id de inventário {$id_inv} sem artigo no destino\n" );
		}
		$artigo_ids[] = $id_inv_para_wp[ $id_inv ];
	}

	$existentes = get_posts( [
		'post_type'      => 'cgte_trilha',
		'post_status'    => 'any',
		'posts_per_page' => 1,
		'meta_key'       => '_cgte_trilha_sigla',
		'meta_value'     => $sigla,
		'fields'         => 'ids',
	] );

	$dados = [
		'post_type'   => 'cgte_trilha',
		'post_title'  => $trilha['titulo'],
		'post_status' => $trilha['status'] ?? 'draft',
	];

	if ( $existentes ) {
		$dados['ID'] = $existentes[0];
		$acao        = 'atualizada';
	} else {
		$acao = 'criada';
	}

	if ( $executar ) {
		$trilha_id = wp_insert_post( $dados, true );
		if ( is_wp_error( $trilha_id ) ) {
			exit( "falha ao salvar trilha {$sigla}: " . $trilha_id->get_error_message() . "\n" );
		}
		update_post_meta( $trilha_id, '_cgte_trilha_sigla', $sigla );
		update_post_meta( $trilha_id, 'cgte_artigos', $artigo_ids );
		update_post_meta( $trilha_id, 'cgte_subtitulo', $trilha['subtitulo'] ?? '' );
		$trilha_post_ids[ $sigla ] = $trilha_id;
	} else {
		$trilha_post_ids[ $sigla ] = $existentes[0] ?? 0;
	}

	$n = count( $artigo_ids );
	echo "  trilha {$sigla} {$acao} [{$dados['post_status']}]: {$trilha['titulo']} ({$n} artigos)\n";
}

/* ------------------------------------------------ 4. percurso */

$p          = $mapa['percurso_v1'];
$slug_perc  = sanitize_title( $p['titulo'] );
$existentes = get_posts( [
	'post_type'      => 'cgte_percurso',
	'post_status'    => 'any',
	'posts_per_page' => 1,
	'name'           => $slug_perc,
	'fields'         => 'ids',
] );

$dados = [
	'post_type'   => 'cgte_percurso',
	'post_title'  => $p['titulo'],
	'post_status' => $p['status'] ?? 'draft',
];
if ( $existentes ) {
	$dados['ID'] = $existentes[0];
	$acao        = 'atualizado';
} else {
	$acao = 'criado';
}

if ( $executar ) {
	$percurso_id = wp_insert_post( $dados, true );
	if ( is_wp_error( $percurso_id ) ) {
		exit( 'falha ao salvar percurso: ' . $percurso_id->get_error_message() . "\n" );
	}
	$complementares = array_map( fn( $id_inv ) => $id_inv_para_wp[ $id_inv ], $p['complementares'] );
	update_post_meta( $percurso_id, 'cgte_trilhas', array_values( array_map( fn( $s ) => $trilha_post_ids[ $s ], $p['trilhas'] ) ) );
	update_post_meta( $percurso_id, 'cgte_artigos_complementares', $complementares );
	update_post_meta( $percurso_id, 'cgte_subtitulo', $p['subtitulo'] ?? '' );
	update_post_meta( $percurso_id, 'cgte_como_percorrer', $p['como_percorrer'] ?? [] );
	update_post_meta( $percurso_id, 'cgte_curadoria', $p['curadoria'] ?? '' );
	update_post_meta( $percurso_id, 'cgte_data_criacao', $p['data_criacao'] ?? '' );
}

echo "  percurso {$acao} [{$dados['post_status']}]: {$p['titulo']} (" . count( $p['trilhas'] ) . " trilhas + " . count( $p['complementares'] ) . " complementares)\n";

echo $executar ? "\nConcluído.\n" : "\nDry-run concluído — nada foi gravado.\n";
