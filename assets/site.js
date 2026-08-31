/* Jůzlová.cz — reveal-on-scroll + optional hero frame scrub (progressive enhancement). */
(function () {
  // Reveal on scroll
  var io = 'IntersectionObserver' in window
    ? new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
      }, { threshold: 0.12 })
    : null;
  document.querySelectorAll('.rv').forEach(function (el) {
    if (io) io.observe(el); else el.classList.add('in');
  });

  // Hero canvas scrub: plays a numbered JPG sequence by scroll progress.
  var scrub = document.querySelector('[data-scrub]');
  if (!scrub || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var canvas = scrub.querySelector('canvas');
  if (!canvas || !canvas.getContext) return;
  var count = parseInt(scrub.getAttribute('data-frames'), 10) || 0;
  var path = scrub.getAttribute('data-path'); // e.g. /assets/hero/frame_%04d.jpg
  if (!count || !path) return;

  var ctx = canvas.getContext('2d');
  var frames = new Array(count);
  var loaded = 0, current = -1;

  function src(i) { return path.replace('%04d', String(i + 1).padStart(4, '0')); }
  function draw(i) {
    var img = frames[i];
    if (!img || !img.complete || !img.naturalWidth) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var w = scrub.clientWidth, h = scrub.querySelector('.stage').clientHeight;
    if (canvas.width !== w * dpr) { canvas.width = w * dpr; canvas.height = h * dpr; }
    var s = Math.max((w * dpr) / img.naturalWidth, (h * dpr) / img.naturalHeight);
    var dw = img.naturalWidth * s, dh = img.naturalHeight * s;
    ctx.drawImage(img, (w * dpr - dw) / 2, (h * dpr - dh) / 2, dw, dh);
  }
  for (var i = 0; i < count; i++) {
    frames[i] = new Image();
    frames[i].onload = (function (n) { return function () { if (++loaded === 1) draw(0); }; })(i);
    frames[i].src = src(i);
  }
  var ticking = false;
  function onScroll() {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () {
      ticking = false;
      var rect = scrub.getBoundingClientRect();
      var total = rect.height - window.innerHeight;
      var p = total > 0 ? Math.min(Math.max(-rect.top / total, 0), 1) : 0;
      var idx = Math.min(count - 1, Math.round(p * (count - 1)));
      if (idx !== current) { current = idx; draw(idx); }
    });
  }
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', function () { current = -1; onScroll(); });
  onScroll();
})();
