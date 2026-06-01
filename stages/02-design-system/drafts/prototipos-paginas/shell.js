/* ============================================================
   SHELL COMPARTILHADO — CEFOR/Ifes
   Injeta o footer canônico (idêntico em todas as páginas) ao final
   do <body>. O header permanece inline em cada página para que a
   navegação primária não dependa de JavaScript.
   Estilos em shell.css.
   ============================================================ */
(function () {
  'use strict';

  var FOOTER = '' +
    '<footer class="site-footer">' +
      '<div class="footer-inner">' +
        '<div>' +
          '<div class="footer-brand">' +
            '<span class="footer-brand-mark" aria-hidden="true">' +
              '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
                '<path d="M8 8 L8 32 L20 36 L20 12 Z"/><path d="M32 8 L32 32 L20 36 L20 12 Z"/><path d="M8 8 L20 12 L32 8"/>' +
              '</svg>' +
            '</span>' +
            '<span class="footer-brand-text">Base de Conhecimento · CEFOR/Ifes</span>' +
          '</div>' +
          '<p class="footer-desc">Produzida pelo Centro de Referência em Formação e em EaD do Instituto Federal do Espírito Santo.</p>' +
          '<p class="footer-license">Conteúdo sob licença Creative Commons BY-NC-SA 4.0, salvo quando indicado.</p>' +
        '</div>' +
        '<div>' +
          '<h5>Navegar</h5>' +
          '<a href="base-percurso.html">Percursos</a>' +
          '<a href="base-trilha.html">Trilhas</a>' +
          '<a href="base-inicio.html">Todos os artigos</a>' +
          '<a href="#">Categorias</a>' +
          '<a href="#">Tópicos</a>' +
        '</div>' +
        '<div>' +
          '<h5>Sobre</h5>' +
          '<a href="#">O CEFOR</a>' +
          '<a href="#">Equipe editorial</a>' +
          '<a href="#">Como contribuir</a>' +
          '<a href="#">Acessibilidade do site</a>' +
        '</div>' +
        '<div>' +
          '<h5>Recursos</h5>' +
          '<a href="https://cefor.ifes.edu.br" target="_blank" rel="noopener">cefor.ifes.edu.br ↗</a>' +
          '<a href="#">ReLiCefor</a>' +
          '<a href="#">MOOC</a>' +
          '<a href="#">Feed RSS</a>' +
        '</div>' +
      '</div>' +
      '<div class="footer-bottom">' +
        '<span>© 2026 CEFOR · Instituto Federal do Espírito Santo</span>' +
        '<span>Base de Conhecimento · layout unificado</span>' +
      '</div>' +
    '</footer>';

  function build() {
    /* Evita duplicar caso algum footer inline ainda exista */
    if (document.querySelector('.site-footer')) return;
    document.body.insertAdjacentHTML('beforeend', FOOTER);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();
})();
