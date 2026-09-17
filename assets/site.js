/* Jůzlová.cz — motion + behaviour. Progressive enhancement: pages are complete without it.
   Rules: ease-out, no bounce, ≥ 450 ms; everything is off under prefers-reduced-motion. */
(function () {
  'use strict';
  var params = new URLSearchParams(location.search);
  var capture = params.get('static') === '1';                       // headless captures: final state, no motion
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches || capture;
  var root = document.documentElement;
  root.classList.add('js');
  if (capture) root.classList.add('capture');

  /* ── the wordmark writes itself once per session (not in captures, not for reduced motion) ── */
  try {
    if (!reduced && !sessionStorage.getItem('juzlova-logo')) { root.classList.add('logo-write'); sessionStorage.setItem('juzlova-logo', '1'); }
  } catch (e) {}

  /* ── header shadow once the page scrolls ── */
  var header = document.querySelector('header.site');
  function headerState() { if (header) header.classList.toggle('scrolled', window.scrollY > 24); }
  addEventListener('scroll', headerState, { passive: true });
  headerState();

  /* ── vines: attach leaves to the actual stroke (petiole on the line, rotated to the tangent) ── */
  var SVG_NS = 'http://www.w3.org/2000/svg';
  function attachLeaves(path) {
    var svg = path.ownerSVGElement, L = path.getTotalLength();
    if (!L) return;
    var count = +path.dataset.leaves || 4, symbol = path.dataset.leaf || 'sil-leaf-single', size = +path.dataset.leafSize || 150;
    var sprite = path.dataset.sprite || '';
    var ratio = +path.dataset.leafRatio || 0.65;
    var at = path.dataset.leafAt ? path.dataset.leafAt.split(',').map(parseFloat) : null;
    if (at) count = at.length;
    for (var i = 1; i <= count; i++) {
      var tt = at ? at[i - 1] * L : (i / (count + 1)) * L + (i % 2 ? -L * 0.03 : L * 0.03);
      var p = path.getPointAtLength(tt), q = path.getPointAtLength(Math.min(tt + 2, L));
      var tangent = Math.atan2(q.y - p.y, q.x - p.x) * 180 / Math.PI, side = i % 2 ? -1 : 1;
      var g = document.createElementNS(SVG_NS, 'g');
      g.setAttribute('class', 'vine-leaf');
      g.setAttribute('transform', 'translate(' + p.x.toFixed(1) + ' ' + p.y.toFixed(1) + ') rotate(' + (tangent + side * 46).toFixed(1) + ')');
      var use = document.createElementNS(SVG_NS, 'use');
      use.setAttribute('href', sprite + '#' + symbol);
      use.setAttribute('width', size); use.setAttribute('height', size * ratio);
      use.setAttribute('x', -size * 0.04); use.setAttribute('y', -(size * ratio) / 2);   // petiole (left-middle) sits on the vine
      g.appendChild(use); svg.appendChild(g);
    }
  }
  document.querySelectorAll('path[data-vine]').forEach(attachLeaves);

  /* ── wind: every swaying element gets its own period and phase ── */
  document.querySelectorAll('.art use, .vine-leaf use, .cutout img').forEach(function (el) {
    var big = el.closest('.art') !== null, dur = (big ? 8 : 5) + Math.random() * (big ? 5 : 3);
    el.style.setProperty('--dur', dur.toFixed(2) + 's');
    el.style.setProperty('--delay', (-Math.random() * dur).toFixed(2) + 's');
  });

  /* ── stroke-draw lengths ── */
  document.querySelectorAll('.draw path').forEach(function (p) {
    try { p.style.setProperty('--len', p.getTotalLength().toFixed(0)); } catch (e) {}
  });

  /* ── moving photos: the same picture, animated, inside the outline.
     Desktop: plays while the card is hovered. Touch: plays once when the card is centred/in view.
     Off for reduced motion, captures and data-saver; clips load only when first needed. ── */
  (function () {
    var saveData = navigator.connection && navigator.connection.saveData;
    if (reduced || saveData) return;
    var canHover = matchMedia('(hover: hover)').matches;
    var videos = [].slice.call(document.querySelectorAll('.shape video'));
    if (!videos.length) return;
    function shapeOf(v) { return v.closest('.shape'); }
    function start(v, loop) {
      v.loop = !!loop;
      if (v.preload === 'none') v.preload = 'auto';
      var p = v.play();
      if (p && p.catch) p.catch(function () {});
      shapeOf(v).classList.add('is-playing');
    }
    function stop(v) {
      shapeOf(v).classList.remove('is-playing');
      setTimeout(function () { if (!shapeOf(v).classList.contains('is-playing')) { v.pause(); try { v.currentTime = 0; } catch (e) {} } }, 700);
    }
    videos.forEach(function (v) {
      v.addEventListener('ended', function () { stop(v); });
      var host = v.closest('.shape-link') || v.closest('.obj-panel') || shapeOf(v);
      if (canHover) {
        host.addEventListener('mouseenter', function () { start(v, true); });
        host.addEventListener('mouseleave', function () { stop(v); });
        host.addEventListener('focusin', function () { start(v, true); });
        host.addEventListener('focusout', function () { stop(v); });
      }
    });
    // Touch (and the product panel on any device): play once when the card is the one in view.
    // Inside the phone shelf the centred card wins (thresholds alone are unreliable during snap scrolling).
    function playOnce(v) { if (!v.dataset.played) { v.dataset.played = '1'; start(v, false); } }
    function reset(v) { stop(v); v.dataset.played = ''; }
    function centred(stack) {
      var r = stack.getBoundingClientRect(), cx = r.left + r.width / 2, best = null, bd = 1e9;
      stack.querySelectorAll('.shape video').forEach(function (v) {
        var b = shapeOf(v).getBoundingClientRect(), d = Math.abs(b.left + b.width / 2 - cx);
        if (d < bd) { bd = d; best = v; }
      });
      return best;
    }
    if ('IntersectionObserver' in window) {
      var stacks = [].slice.call(document.querySelectorAll('.stack'));
      stacks.forEach(function (stack) {
        var inView = false, timer = 0;
        function update() {
          if (!inView || canHover) return;
          var best = centred(stack);
          stack.querySelectorAll('.shape video').forEach(function (v) { if (v !== best) reset(v); });
          if (best) playOnce(best);
        }
        new IntersectionObserver(function (es) {
          inView = es[0].isIntersecting && es[0].intersectionRatio >= 0.5;
          if (!inView) stack.querySelectorAll('.shape video').forEach(reset); else update();
        }, { threshold: [0, 0.5] }).observe(stack);
        stack.addEventListener('scroll', function () { clearTimeout(timer); timer = setTimeout(update, 150); }, { passive: true });
      });
      var loose = videos.filter(function (v) { return !v.closest('.stack'); });
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          var v = e.target.querySelector('video');
          if (!v) return;
          var inPanel = !!v.closest('.obj-panel');
          if (!canHover || inPanel) {
            if (e.isIntersecting && e.intersectionRatio >= 0.5) playOnce(v);
            else if (!e.isIntersecting) reset(v);
          }
        });
      }, { threshold: [0, 0.5] });
      loose.forEach(function (v) { io.observe(shapeOf(v)); });
    }
  })();

  /* ── hover lens rings: dash length = the outline's on-screen length (non-scaling stroke measures in px) ── */
  function sizeRings() {
    document.querySelectorAll('.ring use').forEach(function (u) {
      var id = (u.getAttribute('href') || '').slice(1), path = id && document.getElementById(id), box = u.closest('.ring');
      if (!path || !box) return;
      try {
        var r = box.getBoundingClientRect(), len = path.getTotalLength() * (r.width + r.height) / 2 * 1.08;
        box.style.setProperty('--len', len.toFixed(0));
      } catch (e) {}
    });
  }
  sizeRings();
  addEventListener('resize', sizeRings);

  /* ── count-up numerals: from data-from (or 0) to data-count, 1.4 s, ease-out quart ── */
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

  /* ── reveals with sibling stagger; numerals count when their block reveals ── */
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
    if (io && !reduced) io.observe(el);
    else { el.classList.add('is-in'); el.querySelectorAll('.n[data-count]').forEach(function (n) { n.textContent = n.dataset.count; }); }
  });

  /* ── parallax on silhouettes and cut-outs (fine pointers only) ── */
  if (!reduced && matchMedia('(pointer: fine)').matches) {
    var items = [].slice.call(document.querySelectorAll('.plx')), raf = 0;
    var tick = function () {
      raf = 0; var vh = innerHeight;
      items.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -vh || r.top > vh * 2) return;
        var c = (r.top + r.height / 2 - vh / 2) / vh, speed = parseFloat(el.dataset.speed) || 40;
        el.style.transform = 'translate3d(0,' + (-c * speed).toFixed(1) + 'px,0)' + (el.dataset.rotate ? ' rotate(' + el.dataset.rotate + ')' : '');
      });
    };
    if (items.length) {
      addEventListener('scroll', function () { if (!raf) raf = requestAnimationFrame(tick); }, { passive: true });
      addEventListener('resize', function () { if (!raf) raf = requestAnimationFrame(tick); });
      tick();
    }
  }

  /* ── marquee: pauses on hover and focus; the button pauses it for everyone else (WCAG 2.2.2) ── */
  document.querySelectorAll('.marquee').forEach(function (m) {
    var btn = m.querySelector('.marquee-toggle'), held = false;
    ['mouseenter', 'focusin'].forEach(function (ev) { m.addEventListener(ev, function () { m.classList.add('is-paused'); }); });
    ['mouseleave', 'focusout'].forEach(function (ev) { m.addEventListener(ev, function () { if (!held) m.classList.remove('is-paused'); }); });
    // a finger on the ticker pauses it, so a moving link can be tapped; it resumes a moment after release
    var touchTimer = 0;
    m.addEventListener('touchstart', function () { clearTimeout(touchTimer); m.classList.add('is-paused'); }, { passive: true });
    m.addEventListener('touchend', function () { touchTimer = setTimeout(function () { if (!held) m.classList.remove('is-paused'); }, 1500); }, { passive: true });
    if (btn) {
      btn.addEventListener('click', function () {
        held = !held;
        m.classList.toggle('is-paused', held);
        btn.setAttribute('aria-pressed', held ? 'true' : 'false');
        var label = btn.getAttribute(held ? 'data-play-label' : 'data-pause-label');
        if (label) btn.setAttribute('aria-label', label);
      });
    }
  });

  /* ── phone menu + products accordion ── */
  var menuBtn = document.querySelector('.menu-toggle');
  var navEl = document.querySelector('nav.main');
  var backdrop = document.querySelector('.nav-backdrop');
  var prodBtn = document.querySelector('.nav-products');
  var prodGroup = prodBtn ? prodBtn.closest('.navgroup') : null;
  function setMenu(open) {
    if (!navEl || !menuBtn) return;
    navEl.classList.toggle('is-open', open);
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    var label = menuBtn.getAttribute(open ? 'data-close-label' : 'data-open-label');
    if (label) menuBtn.setAttribute('aria-label', label);
    document.body.classList.toggle('nav-open', open);
    if (backdrop) { backdrop.classList.toggle('is-open', open); backdrop.hidden = !open; }
  }
  if (menuBtn) menuBtn.addEventListener('click', function () { setMenu(!navEl.classList.contains('is-open')); });
  if (backdrop) backdrop.addEventListener('click', function () { setMenu(false); });
  if (navEl) navEl.querySelectorAll('a').forEach(function (link) { link.addEventListener('click', function () { setMenu(false); }); });
  if (prodBtn && prodGroup) {
    prodBtn.addEventListener('click', function () {
      var open = !prodGroup.classList.contains('is-open');
      prodGroup.classList.toggle('is-open', open);
      prodBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      setMenu(false);
      if (prodGroup) { prodGroup.classList.remove('is-open'); if (prodBtn) prodBtn.setAttribute('aria-expanded', 'false'); }
    }
  });

  /* ── forms post to /api/contact (Turnstile + honeypot); also the footer call-back form ── */
  document.querySelectorAll('[data-contact-form]').forEach(function (form) {
    var statusEl = form.querySelector('[data-form-status]');
    var submitBtn = form.querySelector('[type="submit"]');
    var submitLabel = submitBtn ? (submitBtn.querySelector('span') || submitBtn) : null;
    var widgetId = null;
    var siteKey = (form.getAttribute('data-turnstile-key') || '').trim();

    var handleSetStatus = function (kind, text) {
      if (!statusEl) return;
      statusEl.hidden = !text;
      statusEl.textContent = text || '';
      statusEl.className = 'form-status' + (kind ? ' is-' + kind : '');
    };

    var handleLoadTurnstile = function (key) {
      var slot = form.querySelector('[data-turnstile-slot]');
      if (!slot || !key) return;
      var handleRender = function () {
        if (!window.turnstile || widgetId != null) return;
        var renderWidget = function () {
          if (widgetId != null) return;
          widgetId = window.turnstile.render(slot, {
            sitekey: key, action: 'contact', appearance: 'always', theme: 'light',
            language: form.getAttribute('data-lang') || 'cs'
          });
        };
        if (typeof window.turnstile.ready === 'function') { window.turnstile.ready(renderWidget); return; }
        renderWidget();
      };
      if (window.turnstile) { handleRender(); return; }
      var existing = document.querySelector('script[data-turnstile-api]');
      if (existing) { existing.addEventListener('load', handleRender); return; }
      var script = document.createElement('script');
      script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit';
      script.async = true;
      script.dataset.turnstileApi = '1';
      script.addEventListener('load', handleRender);
      document.head.appendChild(script);
    };

    fetch('/api/contact', { headers: { Accept: 'application/json' } })
      .then(function (res) { return res.ok ? res.json() : {}; })
      .then(function (data) {
        if (data && data.siteKey) siteKey = data.siteKey;
        if (siteKey) handleLoadTurnstile(siteKey);
      })
      .catch(function () { if (siteKey) handleLoadTurnstile(siteKey); });
    if (siteKey) handleLoadTurnstile(siteKey);

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.classList.contains('is-success')) return;
      var honey = form.querySelector('[name="bot-field"]');
      if (honey && honey.value) {
        form.classList.add('is-success');
        handleSetStatus('success', form.getAttribute('data-i18n-success') || '');
        return;
      }
      var token = '';
      if (siteKey && window.turnstile && widgetId != null) token = window.turnstile.getResponse(widgetId) || '';
      if (siteKey && !token) { handleSetStatus('error', form.getAttribute('data-i18n-captcha') || ''); return; }

      var products = [].slice.call(form.querySelectorAll('[name="product"]:checked')).map(function (c) { return c.value; });
      var buyerEl = form.querySelector('[name="buyer"]:checked') || form.querySelector('[name="buyer"]');
      var fulfillEl = form.querySelector('[name="fulfillment"]:checked');
      var consentEl = form.querySelector('[name="consent"]');
      var topicEl = form.querySelector('[name="topic"]');
      var formType = form.getAttribute('data-form-type') || 'contact';
      var val = function (name) { var el = form.querySelector('[name="' + name + '"]'); return el ? (el.value || '').trim() : ''; };
      var payload = {
        type: formType === 'callback' ? 'contact' : formType,
        name: val('name'), phone: val('phone'), email: val('email'), message: val('message'), quantity: val('quantity'),
        topic: topicEl ? (topicEl.value || '').trim() : '',
        fulfillment: fulfillEl ? fulfillEl.value : '',
        consent: consentEl && consentEl.checked ? 'yes' : '',
        buyer: buyerEl ? buyerEl.value : '',
        products: products,
        lang: form.getAttribute('data-lang') || 'cs',
        turnstileToken: token,
        honeypot: honey ? honey.value : ''
      };

      if (formType === 'newsletter') {
        if (!payload.email || !payload.consent) { handleSetStatus('error', form.getAttribute('data-i18n-need-contact') || form.getAttribute('data-i18n-error') || ''); return; }
      } else if (formType === 'b2b' && !payload.topic) {
        handleSetStatus('error', form.getAttribute('data-i18n-error') || ''); return;
      } else if (formType === 'callback') {
        var digits = payload.phone.replace(/\D/g, '');
        if (digits.length < 9 || !payload.name) {
          handleSetStatus('error', form.getAttribute('data-i18n-need-contact') || '');
          var telEl = form.querySelector('[name="phone"]'); if (telEl && digits.length < 9) telEl.focus();
          return;
        }
      } else if (!payload.phone && !payload.email) {
        handleSetStatus('error', form.getAttribute('data-i18n-need-contact') || form.getAttribute('data-i18n-error') || ''); return;
      }

      var defaultLabel = submitLabel ? submitLabel.textContent : '';
      if (submitBtn) { submitBtn.disabled = true; if (submitLabel) submitLabel.textContent = form.getAttribute('data-i18n-sending') || defaultLabel; }
      handleSetStatus('', '');

      fetch('/api/contact', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(payload) })
        .then(function (res) { return res.json().catch(function () { return {}; }).then(function (body) { return { ok: res.ok && body && body.ok, body: body }; }); })
        .then(function (result) {
          if (!result.ok) {
            var err = result.body && result.body.error;
            var errKey = err === 'captcha' ? 'data-i18n-captcha' : ((err === 'need_contact' || err === 'consent') ? 'data-i18n-need-contact' : 'data-i18n-error');
            handleSetStatus('error', form.getAttribute(errKey) || '');
            if (window.turnstile && widgetId != null) window.turnstile.reset(widgetId);
            return;
          }
          form.classList.add('is-success');
          form.reset();
          handleSetStatus('success', form.getAttribute('data-i18n-success') || '');
        })
        .catch(function () {
          handleSetStatus('error', form.getAttribute('data-i18n-error') || '');
          if (window.turnstile && widgetId != null) window.turnstile.reset(widgetId);
        })
        .then(function () {
          if (submitBtn && !form.classList.contains('is-success')) { submitBtn.disabled = false; if (submitLabel) submitLabel.textContent = defaultLabel; }
        });
    });
  });

  /* ── cocoa radar + nutrition bars: animate when in view ── */
  var cocoaBlocks = document.querySelectorAll('[data-cocoa-anim]');
  if (cocoaBlocks.length) {
    var handleCocoaOn = function (el) { el.classList.add('is-on'); };
    if (reduced || !('IntersectionObserver' in window)) cocoaBlocks.forEach(handleCocoaOn);
    else {
      var cocoaIo = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) { if (!entry.isIntersecting) return; handleCocoaOn(entry.target); cocoaIo.unobserve(entry.target); });
      }, { threshold: 0.22 });
      cocoaBlocks.forEach(function (el) { cocoaIo.observe(el); });
    }
  }

  /* ── recipe star ratings ── */
  document.querySelectorAll('[data-rating-slug]').forEach(function (box) {
    var slug = box.getAttribute('data-rating-slug');
    var api = box.getAttribute('data-api') || '/api/ratings';
    var countTpl = box.getAttribute('data-count-tpl') || '{n}';
    var thanks = box.getAttribute('data-thanks') || '';
    var already = box.getAttribute('data-already') || '';
    var errTxt = box.getAttribute('data-error') || '';
    var votedKey = 'juzlova-rated:' + slug;
    var stars = box.querySelectorAll('[data-stars]');
    var valueOut = box.querySelector('[data-rating-out]');
    var countOut = box.querySelector('[data-count-out]');
    var status = box.querySelector('.recipe-rating-status');
    var voted = false;
    try { voted = localStorage.getItem(votedKey) === '1'; } catch (e) { voted = false; }
    var handlePaint = function (value) {
      var rounded = Math.round(Number(value) || 0);
      stars.forEach(function (btn) { btn.classList.toggle('is-on', Number(btn.getAttribute('data-stars')) <= rounded); });
    };
    var handleShow = function (data) {
      if (!data) return;
      if (valueOut && data.ratingValue != null) valueOut.textContent = data.ratingValue;
      if (countOut && data.ratingCount != null) countOut.textContent = countTpl.replace('{n}', String(data.ratingCount));
      if (data.ratingValue != null) { box.setAttribute('data-rating-value', String(data.ratingValue)); handlePaint(data.ratingValue); }
    };
    var handleLock = function (msg, ok) {
      voted = true;
      box.classList.add('is-locked');
      stars.forEach(function (btn) { btn.disabled = true; });
      if (status && msg) { status.hidden = false; status.textContent = msg; status.classList.toggle('is-ok', !!ok); status.classList.toggle('is-err', !ok); }
      try { localStorage.setItem(votedKey, '1'); } catch (e) {}
    };
    handlePaint(box.getAttribute('data-rating-value'));
    if (voted) { box.classList.add('is-locked'); stars.forEach(function (btn) { btn.disabled = true; }); }
    fetch(api + '/' + encodeURIComponent(slug), { headers: { Accept: 'application/json' } })
      .then(function (res) { return res.ok ? res.json() : null; }).then(handleShow).catch(function () {});
    stars.forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (voted || box.classList.contains('is-busy')) return;
        var n = Number(btn.getAttribute('data-stars'));
        if (!n) return;
        box.classList.add('is-busy');
        handlePaint(n);
        fetch(api + '/' + encodeURIComponent(slug), { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify({ stars: n }) })
          .then(function (res) { return res.json().catch(function () { return {}; }).then(function (body) { return { ok: res.ok, body: body }; }); })
          .then(function (result) {
            box.classList.remove('is-busy');
            if (!result.ok) { handlePaint(box.getAttribute('data-rating-value')); if (status) { status.hidden = false; status.textContent = errTxt; status.classList.add('is-err'); } return; }
            handleShow(result.body);
            handleLock(result.body.already ? already : thanks, true);
          })
          .catch(function () { box.classList.remove('is-busy'); handlePaint(box.getAttribute('data-rating-value')); if (status) { status.hidden = false; status.textContent = errTxt; status.classList.add('is-err'); } });
      });
    });
  });

  /* ── recipes carousel (kept for pages that still render one) ── */
  document.querySelectorAll('[data-recipes-carousel]').forEach(function (rootEl) {
    var scroller = rootEl.querySelector('[data-carousel-scroller]');
    var track = rootEl.querySelector('.recipes-carousel-track');
    var prevBtn = rootEl.querySelector('[data-carousel-prev]');
    var nextBtn = rootEl.querySelector('[data-carousel-next]');
    var dotsEl = rootEl.querySelector('[data-carousel-dots]');
    var liveEl = rootEl.querySelector('[data-carousel-live]');
    if (!scroller || !track) return;
    var slides = [].slice.call(track.children);
    if (!slides.length) return;
    var statusTpl = rootEl.getAttribute('data-status') || '{current} / {total}: {name}';
    var gotoTpl = rootEl.getAttribute('data-goto') || '{n}: {name}';
    var current = 0, autoTimer = null, resumeTimer = null, isProgrammatic = false, userHeld = false, pointerInside = false;
    var name = function (slide) { return (slide.getAttribute('aria-label') || '').trim(); };
    var wrap = function (i) { var last = slides.length - 1; return i < 0 ? last : (i > last ? 0 : i); };
    var nearest = function () { var left = scroller.scrollLeft, best = 0, bestDist = Infinity; slides.forEach(function (s, i) { var d = Math.abs(s.offsetLeft - left); if (d < bestDist) { bestDist = d; best = i; } }); return best; };
    var paint = function (index, announce) {
      current = index;
      slides.forEach(function (slide, i) {
        var on = i === index; slide.setAttribute('aria-hidden', on ? 'false' : 'true');
        var link = slide.querySelector('a'); if (link) { if (on) link.removeAttribute('tabindex'); else link.setAttribute('tabindex', '-1'); }
      });
      if (dotsEl) [].slice.call(dotsEl.children).forEach(function (dot, i) { if (i === index) dot.setAttribute('aria-current', 'true'); else dot.removeAttribute('aria-current'); });
      var one = slides.length < 2; if (prevBtn) prevBtn.disabled = one; if (nextBtn) nextBtn.disabled = one;
      if (announce && liveEl) liveEl.textContent = statusTpl.replace('{current}', String(index + 1)).replace('{total}', String(slides.length)).replace('{name}', name(slides[index]));
    };
    var go = function (index, announce) {
      index = wrap(index); isProgrammatic = true;
      scroller.scrollTo({ left: slides[index].offsetLeft, behavior: reduced ? 'auto' : 'smooth' });
      paint(index, announce); setTimeout(function () { isProgrammatic = false; }, 450);
    };
    var stopAuto = function () { if (autoTimer) { clearInterval(autoTimer); autoTimer = null; } };
    var canAuto = function () { if (reduced || userHeld || pointerInside || document.hidden) return false; if (rootEl.matches(':focus-within')) return false; return slides.length > 1; };
    var startAuto = function () { stopAuto(); if (reduced || slides.length < 2) return; autoTimer = setInterval(function () { if (canAuto()) go(current + 1, false); }, 7000); };
    var userControl = function () { userHeld = true; stopAuto(); if (resumeTimer) clearTimeout(resumeTimer); resumeTimer = setTimeout(function () { userHeld = false; startAuto(); }, 12000); };
    if (dotsEl) slides.forEach(function (slide, i) {
      var dot = document.createElement('button'); dot.type = 'button'; dot.className = 'recipes-carousel-dot';
      dot.setAttribute('aria-label', gotoTpl.replace('{n}', String(i + 1)).replace('{name}', name(slide)));
      dot.addEventListener('click', function () { userControl(); go(i, true); }); dotsEl.appendChild(dot);
    });
    if (prevBtn) prevBtn.addEventListener('click', function () { userControl(); go(current - 1, true); });
    if (nextBtn) nextBtn.addEventListener('click', function () { userControl(); go(current + 1, true); });
    scroller.addEventListener('scroll', function () { paint(nearest(), false); if (!isProgrammatic) userControl(); }, { passive: true });
    rootEl.addEventListener('pointerenter', function () { pointerInside = true; });
    rootEl.addEventListener('pointerleave', function () { pointerInside = false; if (!userHeld) startAuto(); });
    rootEl.addEventListener('focusin', function () { pointerInside = true; });
    rootEl.addEventListener('focusout', function () { pointerInside = false; if (!userHeld) startAuto(); });
    document.addEventListener('visibilitychange', function () { if (document.hidden) stopAuto(); else if (!userHeld) startAuto(); });
    rootEl.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { e.preventDefault(); userControl(); go(current - 1, true); }
      if (e.key === 'ArrowRight') { e.preventDefault(); userControl(); go(current + 1, true); }
    });
    paint(0, false); startAuto();
  });

  /* ── Google Analytics: load gtag.js only after accept ── */
  var gaId = typeof window.__GA_MEASUREMENT_ID === 'string' ? window.__GA_MEASUREMENT_ID : '';
  var consentBar = document.querySelector('[data-consent-bar]');
  var gaLoaded = false;
  var CONSENT_KEY = 'juzlova-ga-consent';
  var gtagFn = function () { window.dataLayer = window.dataLayer || []; if (typeof window.gtag !== 'function') window.gtag = function () { window.dataLayer.push(arguments); }; return window.gtag; };
  var aiReferral = function (gtag) {
    if (!gaId || typeof gtag !== 'function') return;
    var ref = document.referrer || ''; if (!ref) return;
    var host = ''; try { host = new URL(ref).hostname.toLowerCase(); } catch (err) { return; }
    var sources = [['chatgpt.com', 'chatgpt'], ['chat.openai.com', 'chatgpt'], ['perplexity.ai', 'perplexity'], ['claude.ai', 'claude'], ['gemini.google.com', 'gemini'], ['copilot.microsoft.com', 'copilot']];
    var found = '';
    sources.forEach(function (pair) { if (found) return; if (host === pair[0] || host.slice(-(pair[0].length + 1)) === '.' + pair[0]) found = pair[1]; });
    if (found) gtag('event', 'ai_referral', { ai_source: found });
  };
  var hideConsent = function () { if (consentBar) { consentBar.hidden = true; consentBar.setAttribute('aria-hidden', 'true'); } };
  var showConsent = function () { if (consentBar) { consentBar.hidden = false; consentBar.removeAttribute('aria-hidden'); } };
  var loadGtag = function () {
    if (gaLoaded || !gaId) return; gaLoaded = true;
    var gtag = gtagFn();
    gtag('consent', 'update', { analytics_storage: 'granted' }); gtag('js', new Date()); gtag('config', gaId); aiReferral(gtag);
    var s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(gaId); document.head.appendChild(s);
  };
  if (!gaId) hideConsent();
  else {
    gtagFn();
    var stored = ''; try { stored = localStorage.getItem(CONSENT_KEY) || ''; } catch (e) {}
    if (stored === 'accept') { loadGtag(); hideConsent(); }
    else if (stored === 'essential') hideConsent();
    else showConsent();
    var acceptBtn = consentBar ? consentBar.querySelector('[data-consent-accept]') : null;
    var essentialBtn = consentBar ? consentBar.querySelector('[data-consent-essential]') : null;
    if (acceptBtn) acceptBtn.addEventListener('click', function () { try { localStorage.setItem(CONSENT_KEY, 'accept'); } catch (e) {} loadGtag(); hideConsent(); });
    if (essentialBtn) essentialBtn.addEventListener('click', function () { try { localStorage.setItem(CONSENT_KEY, 'essential'); } catch (e) {} hideConsent(); });
  }
})();
