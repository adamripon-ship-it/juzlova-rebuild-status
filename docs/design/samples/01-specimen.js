/* Jůzlová — Phase 1 specimen motion + language switcher.
   Progressive enhancement: the page is complete without it.
   Rules: ≥ 600 ms, ease-out, no bounce; every effect is off under prefers-reduced-motion. */
(function () {
  'use strict';
  var params = new URLSearchParams(location.search);
  var capture = navigator.webdriver || params.get('static') === '1';   // headless captures: final state, no motion
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches || capture;
  document.documentElement.classList.add('js');
  if (capture) document.documentElement.classList.add('capture');
  var I18N = window.I18N || {};
  var lang = new URLSearchParams(location.search).get('lang') || document.documentElement.lang || 'cs';
  if (!I18N[lang]) lang = 'cs';
  var STAMP_DATE = '2026-09-17';

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function t(k) { var d = I18N[lang] || {}; return d[k]; }

  /* ── 0. Language: swap every data-i18n text, rebuild the marquee, keep the URL in sync ── */
  var VB = { 'sil-potato': '0 0 1024 768', 'sil-wheat': '0 0 1024 768', 'sil-vanilla': '0 0 1024 768', 'sil-cocoa': '0 0 1024 768', 'sil-sugarcane': '0 0 768 1024', 'sil-beans': '0 0 1024 683' };
  function buildMarquee() {
    var track = document.querySelector('[data-marquee]'), d = I18N[lang];
    if (!track || !d || !d.products) return;
    var icons = ['sil-potato', 'sil-wheat', 'sil-vanilla', 'sil-cocoa', 'sil-sugarcane'];
    var items = d.products.map(function (p, i) {
      return '<span class="item">' + esc(p.name) + ' <b>' + esc(p.price) + '</b><svg viewBox="' + VB[icons[i]] + '"><use href="#' + icons[i] + '"/></svg></span>';
    });
    items.push('<span class="item">' + esc(d.ticker_pickup) + '<svg viewBox="' + VB['sil-beans'] + '"><use href="#sil-beans"/></svg></span>');
    var html = items.join('');
    track.innerHTML = html + html;                       // two copies = seamless -50% loop
  }
  function applyLang() {
    var d = I18N[lang]; if (!d) return;
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var k = el.dataset.i18n;
      if (/^recipe_\d$/.test(k)) { var i = +k.split('_')[1] - 1; if (d.recipes && d.recipes[i]) el.textContent = d.recipes[i]; return; }
      if (d[k] != null) el.textContent = d[k];
    });
    document.querySelectorAll('[data-i18n-ph]').forEach(function (el) { var k = el.dataset.i18nPh; if (d[k]) { el.placeholder = d[k]; el.setAttribute('aria-label', d[k]); } });
    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) { var k = el.dataset.i18nAria; if (d[k]) el.setAttribute('aria-label', d[k]); });
    var h = document.querySelector('[data-i18n-h1]');
    if (h && d.h1_main) h.innerHTML = esc(d.h1_main).replace(/(\d+)/, '<span class="num">$1</span>');
    document.querySelectorAll('.langs-sw button').forEach(function (b) { b.classList.toggle('on', b.dataset.lang === lang); });
    buildMarquee();
    var stamp = document.querySelector('[data-stamp]'); if (stamp) stamp.textContent = STAMP_DATE + ' · ' + lang;
  }
  document.querySelectorAll('.langs-sw button').forEach(function (b) {
    b.addEventListener('click', function () {
      lang = b.dataset.lang; applyLang();
      var u = new URL(location.href); u.searchParams.set('lang', lang); history.replaceState(null, '', u);
    });
  });
  applyLang();

  /* ── 1. Vines: attach leaves to the actual stroke (petiole on the line, rotated to the tangent) ── */
  function attachLeaves(path) {
    var svg = path.ownerSVGElement, L = path.getTotalLength();
    var count = +path.dataset.leaves || 4, symbol = path.dataset.leaf || 'sil-leaf-single', size = +path.dataset.leafSize || 150;
    var sym = document.getElementById(symbol), vb = sym && (sym.getAttribute('viewBox') || '').split(/\s+/).map(Number);
    var ratio = vb && vb.length === 4 && vb[2] ? vb[3] / vb[2] : (+path.dataset.leafRatio || 0.6);
    var at = path.dataset.leafAt ? path.dataset.leafAt.split(',').map(parseFloat) : null;
    if (at) count = at.length;
    for (var i = 1; i <= count; i++) {
      var tt = at ? at[i - 1] * L : (i / (count + 1)) * L + (i % 2 ? -L * 0.03 : L * 0.03);
      var p = path.getPointAtLength(tt), q = path.getPointAtLength(Math.min(tt + 2, L));
      var tangent = Math.atan2(q.y - p.y, q.x - p.x) * 180 / Math.PI, side = i % 2 ? -1 : 1;
      var g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
      g.setAttribute('class', 'vine-leaf');
      g.setAttribute('transform', 'translate(' + p.x.toFixed(1) + ' ' + p.y.toFixed(1) + ') rotate(' + (tangent + side * 46).toFixed(1) + ')');
      var use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
      use.setAttribute('href', '#' + symbol);
      use.setAttribute('width', size); use.setAttribute('height', size * ratio);
      use.setAttribute('x', -size * 0.04); use.setAttribute('y', -(size * ratio) / 2);   // petiole (left-middle of the leaf) sits on the vine
      g.appendChild(use); svg.appendChild(g);
    }
  }
  document.querySelectorAll('path[data-vine]').forEach(attachLeaves);

  /* ── 1b. Wind: give every swaying element its own period and phase so nothing moves in lockstep ── */
  document.querySelectorAll('.art use, .vine-leaf use, .cutout img').forEach(function (el, i) {
    var big = el.closest('.art') !== null, dur = (big ? 8 : 5) + Math.random() * (big ? 5 : 3);
    el.style.setProperty('--dur', dur.toFixed(2) + 's');
    el.style.setProperty('--delay', (-Math.random() * dur).toFixed(2) + 's');
  });

  /* ── 2. Stroke-draw lengths ── */
  document.querySelectorAll('.draw path').forEach(function (p) { p.style.setProperty('--len', p.getTotalLength().toFixed(0)); });

  /* ── 3. Count-up numerals: from `data-from` (or 0) to `data-count`, 1.4 s, ease-out quart ── */
  function easeOutQuart(x) { return 1 - Math.pow(1 - x, 4); }
  function countUp(el) {
    var target = parseFloat(el.dataset.count), from = el.dataset.from != null ? parseFloat(el.dataset.from) : 0;
    if (reduced || isNaN(target)) { el.textContent = el.dataset.count; return; }
    var dur = 1400, t0 = null;
    function frame(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      el.textContent = Math.round(from + (target - from) * easeOutQuart(p));
      if (p < 1) requestAnimationFrame(frame); else el.textContent = el.dataset.count;
    }
    requestAnimationFrame(frame);
  }

  /* ── 4. Reveals with sibling stagger; numerals count when their block reveals ── */
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var el = e.target, parent = el.parentElement;
      var sibs = parent ? [].filter.call(parent.children, function (c) { return c.classList.contains('rv'); }) : [el];
      var idx = Math.max(sibs.indexOf(el), 0), delay = reduced ? 0 : idx * 90;
      el.style.transitionDelay = delay + 'ms';
      el.classList.add('is-in');
      el.querySelectorAll('.n[data-count]').forEach(function (n) { setTimeout(function () { countUp(n); }, delay); });
      io.unobserve(el);
    });
  }, { threshold: 0.18, rootMargin: '0px 0px -8% 0px' }) : null;
  document.querySelectorAll('.rv, .draw').forEach(function (el) {
    if (io && !reduced) io.observe(el); else { el.classList.add('is-in'); el.querySelectorAll('.n[data-count]').forEach(function (n) { n.textContent = n.dataset.count; }); }
  });

  /* ── 5. Parallax on silhouettes, cut-outs and bridging objects (fine pointers only) ── */
  if (!reduced && matchMedia('(pointer: fine)').matches) {
    var items = [].slice.call(document.querySelectorAll('.plx')), raf = 0;
    function tick() {
      raf = 0; var vh = innerHeight;
      items.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -vh || r.top > vh * 2) return;
        var c = (r.top + r.height / 2 - vh / 2) / vh, speed = parseFloat(el.dataset.speed) || 40;
        el.style.transform = 'translate3d(0,' + (-c * speed).toFixed(1) + 'px,0)' + (el.dataset.rotate ? ' rotate(' + el.dataset.rotate + ')' : '');
      });
    }
    addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(tick); }, { passive: true });
    addEventListener('resize', function () { if (!raf) raf = requestAnimationFrame(tick); });
    tick();
  }

  /* ── 6. Marquee pauses on hover and keyboard focus ── */
  document.querySelectorAll('.marquee').forEach(function (m) {
    ['mouseenter', 'focusin'].forEach(function (ev) { m.addEventListener(ev, function () { m.classList.add('is-paused'); }); });
    ['mouseleave', 'focusout'].forEach(function (ev) { m.addEventListener(ev, function () { m.classList.remove('is-paused'); }); });
  });

  /* ── 7. Call-back form: inline status in the current language, no page reload ── */
  var form = document.querySelector('form[data-callback]');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var tel = form.querySelector('input[type=tel]'), status = form.querySelector('[data-status]');
      var digits = (tel.value || '').replace(/\D/g, '');
      if (digits.length < 9) { status.textContent = t('form_err') || 'Check the phone number.'; status.className = 'form-status is-error'; tel.focus(); return; }
      status.textContent = t('form_ok') || 'Thank you.'; status.className = 'form-status is-ok';
    });
  }
})();
