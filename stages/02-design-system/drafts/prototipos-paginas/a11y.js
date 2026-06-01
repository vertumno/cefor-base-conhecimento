/* ============================================================
   COMPONENTE DE ACESSIBILIDADE — CEFOR/Ifes (canônico, compartilhado)
   Injeta o painel flutuante (A−/A+, alto contraste, fonte para
   dislexia, tema) e o widget VLibras; gerencia os estados com
   persistência em localStorage.

   Requisitos na página:
     · a11y.css carregado;
     · body com font-size: calc(16px * var(--font-scale)) para A−/A+.
   ============================================================ */
(function () {
  'use strict';

  var root = document.documentElement;
  var LS = window.localStorage;
  var MIN = 0.8, MAX = 1.4, STEP = 0.1;

  function clamp(v) { return Math.max(MIN, Math.min(MAX, Math.round(v * 100) / 100)); }

  var svg = {
    a11y: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="7.5" r="1.4" fill="currentColor" stroke="none"/><path d="M7 10.5h10"/><path d="M12 10.5V18"/><path d="m12 13.5-3 4.5"/><path d="m12 13.5 3 4.5"/></svg>',
    contrast: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2v20"/><path d="M12 2a10 10 0 0 1 0 20"/></svg>',
    dyslexic: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 7 4 4 20 4 20 7"/><line x1="9" y1="20" x2="15" y2="20"/><line x1="12" y1="4" x2="12" y2="20"/></svg>',
    moon: '<svg class="a11y-icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
    sun: '<svg class="a11y-icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>',
    vlibras: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="16" cy="4" r="1"/><path d="m18 19 1-7-5.87.94"/><path d="m5 8 1 7 5.87-.94"/><path d="M12.93 17.52L9.5 21l-1-4"/><path d="m7 13 1.5 6 3.5-2"/></svg>'
  };

  /* Aplica estados persistidos imediatamente (antes de pintar o painel) */
  if (LS.getItem('cefor-theme') === 'dark') root.setAttribute('data-theme', 'dark');
  if (LS.getItem('cefor-contrast') === 'high') root.setAttribute('data-contrast', 'high');
  if (LS.getItem('cefor-dyslexic') === 'on') root.setAttribute('data-font', 'dyslexic');
  var savedFs = parseFloat(LS.getItem('cefor-font-scale'));
  if (!isNaN(savedFs)) root.style.setProperty('--font-scale', clamp(savedFs));

  function btn(bar, name) { return bar.querySelector('[data-a11y="' + name + '"]'); }
  function setPressed(bar, name, on) { var b = btn(bar, name); if (b) b.setAttribute('aria-pressed', String(on)); }
  function toggleThemeIcons(bar, dark) {
    var m = bar.querySelector('.a11y-icon-moon'), s = bar.querySelector('.a11y-icon-sun');
    if (m) m.style.display = dark ? 'none' : '';
    if (s) s.style.display = dark ? '' : 'none';
  }

  function stepFont(delta) {
    var cur = parseFloat(getComputedStyle(root).getPropertyValue('--font-scale')) || 1;
    var next = clamp(cur + delta);
    root.style.setProperty('--font-scale', next);
    LS.setItem('cefor-font-scale', next);
  }

  function build() {
    if (document.querySelector('.a11y-bar')) return;

    var bar = document.createElement('div');
    bar.className = 'a11y-bar';
    bar.setAttribute('role', 'toolbar');
    bar.setAttribute('aria-label', 'Preferências de leitura');
    bar.setAttribute('data-collapsed', 'true');
    bar.innerHTML =
      '<button class="a11y-trigger" type="button" aria-expanded="false" aria-label="Abrir preferências de leitura" title="Acessibilidade e tema">' + svg.a11y + '</button>' +
      '<div class="a11y-bar-controls">' +
        '<button type="button" data-a11y="font-dec" aria-label="Diminuir tamanho da fonte" title="Diminuir fonte">A&minus;</button>' +
        '<button type="button" data-a11y="font-inc" aria-label="Aumentar tamanho da fonte" title="Aumentar fonte">A+</button>' +
        '<div class="a11y-sep"></div>' +
        '<button type="button" data-a11y="contrast" aria-label="Alto contraste" title="Alto contraste" aria-pressed="false">' + svg.contrast + '</button>' +
        '<button type="button" data-a11y="dyslexic" aria-label="Fonte para dislexia" title="Fonte para dislexia" aria-pressed="false">' + svg.dyslexic + '</button>' +
        '<div class="a11y-sep"></div>' +
        '<button type="button" data-a11y="theme" aria-label="Alternar tema claro/escuro" title="Tema escuro" aria-pressed="false">' + svg.moon + svg.sun + '</button>' +
      '</div>';
    document.body.appendChild(bar);

    var vlibras = document.createElement('button');
    vlibras.className = 'vlibras-widget';
    vlibras.type = 'button';
    vlibras.setAttribute('aria-label', 'VLibras — Tradução para Libras');
    vlibras.setAttribute('title', 'VLibras');
    vlibras.innerHTML = svg.vlibras;
    document.body.appendChild(vlibras);

    /* expandir / contrair */
    var trigger = bar.querySelector('.a11y-trigger');
    trigger.addEventListener('click', function () {
      var collapsed = bar.getAttribute('data-collapsed') === 'true';
      bar.setAttribute('data-collapsed', String(!collapsed));
      trigger.setAttribute('aria-expanded', String(collapsed));
    });
    document.addEventListener('click', function (e) {
      if (bar.getAttribute('data-collapsed') === 'false' && !bar.contains(e.target)) {
        bar.setAttribute('data-collapsed', 'true');
        trigger.setAttribute('aria-expanded', 'false');
      }
    });

    /* tamanho da fonte */
    btn(bar, 'font-dec').addEventListener('click', function () { stepFont(-STEP); });
    btn(bar, 'font-inc').addEventListener('click', function () { stepFont(STEP); });

    /* alto contraste */
    btn(bar, 'contrast').addEventListener('click', function () {
      var on = root.getAttribute('data-contrast') === 'high';
      if (on) { root.removeAttribute('data-contrast'); LS.setItem('cefor-contrast', 'normal'); }
      else { root.setAttribute('data-contrast', 'high'); LS.setItem('cefor-contrast', 'high'); }
      setPressed(bar, 'contrast', !on);
    });

    /* fonte para dislexia */
    btn(bar, 'dyslexic').addEventListener('click', function () {
      var on = root.getAttribute('data-font') === 'dyslexic';
      if (on) { root.removeAttribute('data-font'); LS.setItem('cefor-dyslexic', 'off'); }
      else { root.setAttribute('data-font', 'dyslexic'); LS.setItem('cefor-dyslexic', 'on'); }
      setPressed(bar, 'dyslexic', !on);
    });

    /* tema claro / escuro */
    btn(bar, 'theme').addEventListener('click', function () {
      var dark = root.getAttribute('data-theme') === 'dark';
      if (dark) { root.removeAttribute('data-theme'); LS.setItem('cefor-theme', 'light'); }
      else { root.setAttribute('data-theme', 'dark'); LS.setItem('cefor-theme', 'dark'); }
      setPressed(bar, 'theme', !dark);
      toggleThemeIcons(bar, !dark);
    });

    /* sincroniza estado inicial dos botões */
    setPressed(bar, 'contrast', root.getAttribute('data-contrast') === 'high');
    setPressed(bar, 'dyslexic', root.getAttribute('data-font') === 'dyslexic');
    var dark = root.getAttribute('data-theme') === 'dark';
    setPressed(bar, 'theme', dark);
    toggleThemeIcons(bar, dark);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();
})();
