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
              '<img src="../../assets/logo/ID_base_branca.png" alt="" />' +
            '</span>' +
            '<span class="footer-brand-text">Base de Conhecimento · CEFOR/Ifes</span>' +
          '</div>' +
          '<p class="footer-desc">Produzida pelo Centro de Referência em Formação e em EaD do Instituto Federal do Espírito Santo.</p>' +
          '<p class="footer-license">Conteúdo sob licença Creative Commons BY-NC-SA 4.0, salvo quando indicado.</p>' +
        '</div>' +
        '<div>' +
          '<h5>Navegar</h5>' +
          '<a href="base-percursos.html">Percursos</a>' +
          '<a href="base-trilhas.html">Trilhas</a>' +
          '<a href="base-artigos.html">Todos os artigos</a>' +
          '<a href="base-categoria.html">Categorias</a>' +
          '<a href="base-topico.html">Tópicos</a>' +
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

  /* ----------------------------------------------------------------
     Navegação mobile — injeta o hambúrguer e controla o drawer.
     A nav primária já existe no HTML; aqui apenas a tornamos
     acessível no mobile. A classe .has-js liga o modo drawer no CSS;
     sem JS, shell.css mantém nav e busca empilhadas e visíveis.
     ---------------------------------------------------------------- */
  function enhanceHeader() {
    var header = document.querySelector('.site-header');
    if (!header) return;
    var inner = header.querySelector('.header-inner');
    var nav = header.querySelector('.nav');
    if (!inner || !nav || header.querySelector('.nav-toggle')) return;

    header.classList.add('has-js');
    if (!nav.id) nav.id = 'primary-nav';

    var toggle = document.createElement('button');
    toggle.className = 'nav-toggle';
    toggle.type = 'button';
    toggle.setAttribute('aria-label', 'Abrir menu de navegação');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', nav.id);
    toggle.innerHTML =
      '<svg class="icon-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>' +
      '<svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>';

    var brand = inner.querySelector('.brand');
    if (brand && brand.nextSibling) inner.insertBefore(toggle, brand.nextSibling);
    else inner.appendChild(toggle);

    function setOpen(open) {
      header.classList.toggle('menu-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Fechar menu de navegação' : 'Abrir menu de navegação');
    }

    toggle.addEventListener('click', function () {
      setOpen(!header.classList.contains('menu-open'));
    });
    /* fecha ao escolher um item */
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });
    /* fecha com Esc e devolve o foco ao botão */
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && header.classList.contains('menu-open')) {
        setOpen(false); toggle.focus();
      }
    });
  }

  function init() { build(); enhanceHeader(); }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
