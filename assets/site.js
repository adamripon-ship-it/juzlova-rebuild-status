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
    var last = lines.length - 1;
    lines.forEach(function (l, i) {
      var a = parseFloat(l.getAttribute('data-in') || 0);
      var b = parseFloat(l.getAttribute('data-out') || 1);
      // Trapezoid: hold the copy readable across its whole window, fading only
      // at the edges. The opening act is already visible at rest, and the
      // closing act stays up through the end of the film.
      var fade = Math.min(0.1, (b - a) * 0.4);
      var vis;
      if (p <= a) vis = i === 0 ? 1 : 0;
      else if (p >= b) vis = i === last ? 1 : 0;
      else vis = Math.min(i === 0 ? 1 : clamp((p - a) / fade),
                          i === last ? 1 : clamp((b - p) / fade));
      l.style.opacity = vis;
      l.style.transform = 'translateY(' + (1 - vis) * 26 + 'px)';
      // Acts are stacked on top of each other, so only the visible one may
      // take clicks — otherwise a faded act swallows the other's buttons.
      l.style.pointerEvents = vis > 0.5 ? 'auto' : 'none';
    });
    if (hint) hint.style.opacity = clamp(1 - p * 5);
  }

  /* scroll hint retires once the film is under way */
  var hint = film ? film.querySelector('.hint') : null;

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

  /* ── phone menu + products accordion ── */
  var menuBtn = document.querySelector('.menu-toggle')
  var navEl = document.querySelector('nav.main')
  var backdrop = document.querySelector('.nav-backdrop')
  var prodBtn = document.querySelector('.nav-products')
  var prodGroup = prodBtn ? prodBtn.closest('.navgroup') : null
  function setMenu(open) {
    if (!navEl || !menuBtn) return
    navEl.classList.toggle('is-open', open)
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false')
    var label = menuBtn.getAttribute(open ? 'data-close-label' : 'data-open-label')
    if (label) menuBtn.setAttribute('aria-label', label)
    document.body.classList.toggle('nav-open', open)
    if (backdrop) {
      backdrop.classList.toggle('is-open', open)
      backdrop.hidden = !open
    }
  }

  if (menuBtn) {
    menuBtn.addEventListener('click', function () {
      setMenu(!navEl.classList.contains('is-open'))
    })
  }
  if (backdrop) {
    backdrop.addEventListener('click', function () { setMenu(false) })
  }
  if (navEl) {
    navEl.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { setMenu(false) })
    })
  }
  if (prodBtn && prodGroup) {
    prodBtn.addEventListener('click', function () {
      var open = !prodGroup.classList.contains('is-open')
      prodGroup.classList.toggle('is-open', open)
      prodBtn.setAttribute('aria-expanded', open ? 'true' : 'false')
    })
  }
  addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      setMenu(false)
      if (prodGroup) {
        prodGroup.classList.remove('is-open')
        if (prodBtn) prodBtn.setAttribute('aria-expanded', 'false')
      }
    }
  })

  /* ── contact form posts to /api/contact (Turnstile + honeypot) ── */
  document.querySelectorAll('[data-contact-form]').forEach(function (form) {
    var statusEl = form.querySelector('[data-form-status]');
    var submitBtn = form.querySelector('[type="submit"]');
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
            sitekey: key,
            action: 'contact',
            appearance: 'always',
            theme: 'light',
            language: form.getAttribute('data-lang') || 'cs'
          });
        };
        if (typeof window.turnstile.ready === 'function') {
          window.turnstile.ready(renderWidget);
          return;
        }
        renderWidget();
      };

      if (window.turnstile) {
        handleRender();
        return;
      }

      var existing = document.querySelector('script[data-turnstile-api]');
      if (existing) {
        existing.addEventListener('load', handleRender);
        return;
      }

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
      .catch(function () {
        if (siteKey) handleLoadTurnstile(siteKey);
      });

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
      if (siteKey && window.turnstile && widgetId != null) {
        token = window.turnstile.getResponse(widgetId) || '';
      }
      if (siteKey && !token) {
        handleSetStatus('error', form.getAttribute('data-i18n-captcha') || '');
        return;
      }

      var products = [].slice.call(form.querySelectorAll('[name="product"]:checked')).map(function (c) {
        return c.value;
      });

      var payload = {
        name: ((form.querySelector('[name="name"]') || {}).value || '').trim(),
        phone: ((form.querySelector('[name="phone"]') || {}).value || '').trim(),
        email: ((form.querySelector('[name="email"]') || {}).value || '').trim(),
        message: ((form.querySelector('[name="message"]') || {}).value || '').trim(),
        products: products,
        lang: form.getAttribute('data-lang') || 'cs',
        turnstileToken: token,
        honeypot: honey ? honey.value : ''
      };

      var defaultLabel = submitBtn ? submitBtn.textContent : '';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = form.getAttribute('data-i18n-sending') || defaultLabel;
      }
      handleSetStatus('', '');

      fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (res) {
          return res.json().catch(function () { return {}; }).then(function (body) {
            return { ok: res.ok && body && body.ok, body: body };
          });
        })
        .then(function (result) {
          if (!result.ok) {
            var errKey = result.body && result.body.error === 'captcha'
              ? 'data-i18n-captcha'
              : 'data-i18n-error';
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
          if (submitBtn && !form.classList.contains('is-success')) {
            submitBtn.disabled = false;
            submitBtn.textContent = defaultLabel;
          }
        });
    });
  });

  /* ── cocoa radar + nutrition bars: animate when in view ── */
  var cocoaBlocks = document.querySelectorAll('[data-cocoa-anim]')
  if (cocoaBlocks.length) {
    var handleCocoaOn = function (el) { el.classList.add('is-on') }
    if (reduced || !('IntersectionObserver' in window)) {
      cocoaBlocks.forEach(handleCocoaOn)
    } else {
      var cocoaIo = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return
          handleCocoaOn(entry.target)
          cocoaIo.unobserve(entry.target)
        })
      }, { threshold: 0.22 })
      cocoaBlocks.forEach(function (el) { cocoaIo.observe(el) })
    }
  }
})();
