/* Jůzlová.cz — motion engine: inertial scroll, scroll-film hero, parallax, reveals. */
(function () {
  'use strict';
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── staggered reveal on scroll ── */
  var io = 'IntersectionObserver' in window
    ? new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) return;
          var el = e.target;
          var siblings = el.parentElement ? [].slice.call(el.parentElement.children).filter(function (c) { return c.classList && c.classList.contains('rv'); }) : [el];
          var idx = siblings.indexOf(el);
          el.style.transitionDelay = reduced ? '0s' : (Math.max(idx, 0) * 70) + 'ms';
          el.classList.add('in');
          io.unobserve(el);
        });
      }, { threshold: 0.12 })
    : null;
  document.querySelectorAll('.rv').forEach(function (el) {
    if (io && !reduced) io.observe(el); else el.classList.add('in');
  });

  /* ── header: transparent over hero, solid after ── */
  var header = document.querySelector('header.site');
  function headerState() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 40);
  }
  addEventListener('scroll', headerState, { passive: true });
  headerState();

  /* ── inertial smooth scroll (lenis-lite) ── */
  if (!reduced && matchMedia('(pointer: fine)').matches) {
    var current = window.scrollY, target = current, raf = null;
    function tick() {
      current += (target - current) * 0.11;
      if (Math.abs(target - current) < 0.5) { current = target; raf = null; }
      else raf = requestAnimationFrame(tick);
      window.scrollTo(0, current);
      drive();
    }
    addEventListener('wheel', function (e) {
      if (e.ctrlKey) return;
      e.preventDefault();
      target = Math.max(0, Math.min(target + e.deltaY, document.documentElement.scrollHeight - innerHeight));
      if (!raf) raf = requestAnimationFrame(tick);
    }, { passive: false });
    addEventListener('scroll', function () { if (!raf) { current = target = window.scrollY; } }, { passive: true });
  }

  /* ── scroll-film: pinned keyframe crossfade scrub ── */
  var film = document.querySelector('[data-film]');
  var frames = film ? [].slice.call(film.querySelectorAll('.frame')) : [];
  var lines = film ? [].slice.call(film.querySelectorAll('.filmline')) : [];
  function clamp(v) { return Math.min(Math.max(v, 0), 1); }
  function filmScrub() {
    if (!film || !frames.length) return;
    var rect = film.getBoundingClientRect();
    var total = rect.height - innerHeight;
    var p = total > 0 ? clamp(-rect.top / total) : 0;
    var n = frames.length;
    frames.forEach(function (f, i) {
      var start = i / n, end = (i + 1) / n;
      var local = clamp((p - start) / (end - start));
      var vis;
      if (i === 0) vis = p < end ? 1 : clamp(1 - (p - end) * n * 2);
      else vis = clamp((p - start) * n * 2);
      if (i < n - 1 && p > end) vis = clamp(1 - (p - end) * n * 2);
      f.style.opacity = vis;
      f.style.transform = 'scale(' + (1 + local * 0.09) + ')';
    });
    lines.forEach(function (l) {
      var a = parseFloat(l.getAttribute('data-in') || 0);
      var b = parseFloat(l.getAttribute('data-out') || 1);
      var mid = (a + b) / 2, span = (b - a) / 2;
      var vis = clamp(1 - Math.abs(p - mid) / span * 1.4);
      l.style.opacity = vis;
      l.style.transform = 'translateY(' + (1 - vis) * 26 + 'px)';
    });
  }

  /* ── parallax bands ── */
  var plx = [].slice.call(document.querySelectorAll('[data-plx]'));
  function parallax() {
    plx.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < 0 || r.top > innerHeight) return;
      var mid = r.top + r.height / 2 - innerHeight / 2;
      var img = el.querySelector('.plx-img');
      if (img) img.style.transform = 'translateY(' + mid * -0.12 + 'px) scale(1.18)';
    });
  }

  var driving = false;
  function drive() {
    if (reduced) return;
    filmScrub();
    parallax();
  }
  function onScroll() {
    if (driving) return;
    driving = true;
    requestAnimationFrame(function () { driving = false; drive(); });
  }
  if (!reduced) {
    addEventListener('scroll', onScroll, { passive: true });
    addEventListener('resize', onScroll);
    drive();
  } else if (frames.length) {
    frames.forEach(function (f, i) { f.style.opacity = i === 0 ? 1 : 0; });
    lines.forEach(function (l) { l.style.opacity = 1; l.style.position = 'relative'; });
  }
})();
