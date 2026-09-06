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

      var buyerEl = form.querySelector('[name="buyer"]:checked') || form.querySelector('[name="buyer"]')
      var fulfillEl = form.querySelector('[name="fulfillment"]:checked')
      var consentEl = form.querySelector('[name="consent"]')
      var topicEl = form.querySelector('[name="topic"]')
      var formType = form.getAttribute('data-form-type') || 'contact'
      var payload = {
        type: formType,
        name: ((form.querySelector('[name="name"]') || {}).value || '').trim(),
        phone: ((form.querySelector('[name="phone"]') || {}).value || '').trim(),
        email: ((form.querySelector('[name="email"]') || {}).value || '').trim(),
        message: ((form.querySelector('[name="message"]') || {}).value || '').trim(),
        quantity: ((form.querySelector('[name="quantity"]') || {}).value || '').trim(),
        topic: topicEl ? (topicEl.value || '').trim() : '',
        fulfillment: fulfillEl ? fulfillEl.value : '',
        consent: consentEl && consentEl.checked ? 'yes' : '',
        buyer: buyerEl ? buyerEl.value : '',
        products: products,
        lang: form.getAttribute('data-lang') || 'cs',
        turnstileToken: token,
        honeypot: honey ? honey.value : ''
      }

      if (formType === 'newsletter') {
        if (!payload.email || !payload.consent) {
          handleSetStatus('error', form.getAttribute('data-i18n-need-contact') || form.getAttribute('data-i18n-error') || '');
          return;
        }
      } else if (formType === 'b2b' && !payload.topic) {
        handleSetStatus('error', form.getAttribute('data-i18n-error') || '');
        return;
      } else if (!payload.phone && !payload.email) {
        handleSetStatus('error', form.getAttribute('data-i18n-need-contact') || form.getAttribute('data-i18n-error') || '');
        return;
      }

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
            var err = result.body && result.body.error
            var errKey = err === 'captcha'
              ? 'data-i18n-captcha'
              : ((err === 'need_contact' || err === 'consent') ? 'data-i18n-need-contact' : 'data-i18n-error');
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

  /* ── recipe star ratings ── */
  document.querySelectorAll('[data-rating-slug]').forEach(function (box) {
    var slug = box.getAttribute('data-rating-slug')
    var api = box.getAttribute('data-api') || '/api/ratings'
    var countTpl = box.getAttribute('data-count-tpl') || '{n}'
    var thanks = box.getAttribute('data-thanks') || ''
    var already = box.getAttribute('data-already') || ''
    var errTxt = box.getAttribute('data-error') || ''
    var votedKey = 'juzlova-rated:' + slug
    var stars = box.querySelectorAll('[data-stars]')
    var valueOut = box.querySelector('[data-rating-out]')
    var countOut = box.querySelector('[data-count-out]')
    var status = box.querySelector('.recipe-rating-status')
    var voted = false
    try { voted = localStorage.getItem(votedKey) === '1' } catch (e) { voted = false }

    var handlePaint = function (value) {
      var rounded = Math.round(Number(value) || 0)
      stars.forEach(function (btn) {
        var n = Number(btn.getAttribute('data-stars'))
        btn.classList.toggle('is-on', n <= rounded)
      })
    }

    var handleShow = function (data) {
      if (!data) return
      if (valueOut && data.ratingValue != null) valueOut.textContent = data.ratingValue
      if (countOut && data.ratingCount != null) {
        countOut.textContent = countTpl.replace('{n}', String(data.ratingCount))
      }
      if (data.ratingValue != null) {
        box.setAttribute('data-rating-value', String(data.ratingValue))
        handlePaint(data.ratingValue)
      }
    }

    var handleLock = function (msg, ok) {
      voted = true
      box.classList.add('is-locked')
      stars.forEach(function (btn) { btn.disabled = true })
      if (status && msg) {
        status.hidden = false
        status.textContent = msg
        status.classList.toggle('is-ok', !!ok)
        status.classList.toggle('is-err', !ok)
      }
      try { localStorage.setItem(votedKey, '1') } catch (e) {}
    }

    handlePaint(box.getAttribute('data-rating-value'))
    if (voted) {
      box.classList.add('is-locked')
      stars.forEach(function (btn) { btn.disabled = true })
    }

    fetch(api + '/' + encodeURIComponent(slug), { headers: { 'Accept': 'application/json' } })
      .then(function (res) { return res.ok ? res.json() : null })
      .then(handleShow)
      .catch(function () {})

    stars.forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (voted || box.classList.contains('is-busy')) return
        var n = Number(btn.getAttribute('data-stars'))
        if (!n) return
        box.classList.add('is-busy')
        handlePaint(n)
        fetch(api + '/' + encodeURIComponent(slug), {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify({ stars: n })
        })
          .then(function (res) {
            return res.json().catch(function () { return {} }).then(function (body) {
              return { ok: res.ok, body: body }
            })
          })
          .then(function (result) {
            box.classList.remove('is-busy')
            if (!result.ok) {
              handlePaint(box.getAttribute('data-rating-value'))
              if (status) {
                status.hidden = false
                status.textContent = errTxt
                status.classList.add('is-err')
              }
              return
            }
            handleShow(result.body)
            handleLock(result.body.already ? already : thanks, true)
          })
          .catch(function () {
            box.classList.remove('is-busy')
            handlePaint(box.getAttribute('data-rating-value'))
            if (status) {
              status.hidden = false
              status.textContent = errTxt
              status.classList.add('is-err')
            }
          })
      })
    })
  })

  /* ── homepage recipes carousel ── */
  document.querySelectorAll('[data-recipes-carousel]').forEach(function (root) {
    var scroller = root.querySelector('[data-carousel-scroller]')
    var track = root.querySelector('.recipes-carousel-track')
    var prevBtn = root.querySelector('[data-carousel-prev]')
    var nextBtn = root.querySelector('[data-carousel-next]')
    var dotsEl = root.querySelector('[data-carousel-dots]')
    var liveEl = root.querySelector('[data-carousel-live]')
    if (!scroller || !track) return

    var slides = [].slice.call(track.children)
    if (!slides.length) return

    var statusTpl = root.getAttribute('data-status') || '{current} / {total}: {name}'
    var gotoTpl = root.getAttribute('data-goto') || '{n}: {name}'
    var prefersReduce = matchMedia('(prefers-reduced-motion: reduce)').matches
    var current = 0
    var AUTO_MS = 7000
    var RESUME_MS = 12000
    var autoTimer = null
    var resumeTimer = null
    var isProgrammatic = false
    var userHeld = false
    var pointerInside = false

    var handleSlideName = function (slide) {
      return (slide.getAttribute('aria-label') || '').trim()
    }

    var handleWrap = function (index) {
      var last = slides.length - 1
      if (index < 0) return last
      if (index > last) return 0
      return index
    }

    var handleNearestIndex = function () {
      var left = scroller.scrollLeft
      var best = 0
      var bestDist = Infinity
      slides.forEach(function (slide, i) {
        var dist = Math.abs(slide.offsetLeft - left)
        if (dist < bestDist) {
          bestDist = dist
          best = i
        }
      })
      return best
    }

    var handlePaint = function (index, announce) {
      current = index
      slides.forEach(function (slide, i) {
        var isOn = i === index
        slide.setAttribute('aria-hidden', isOn ? 'false' : 'true')
        var link = slide.querySelector('a')
        if (link) {
          if (isOn) link.removeAttribute('tabindex')
          else link.setAttribute('tabindex', '-1')
        }
      })
      if (dotsEl) {
        [].slice.call(dotsEl.children).forEach(function (dot, i) {
          if (i === index) dot.setAttribute('aria-current', 'true')
          else dot.removeAttribute('aria-current')
        })
      }
      var oneSlide = slides.length < 2
      if (prevBtn) prevBtn.disabled = oneSlide
      if (nextBtn) nextBtn.disabled = oneSlide
      if (announce && liveEl) {
        liveEl.textContent = statusTpl
          .replace('{current}', String(index + 1))
          .replace('{total}', String(slides.length))
          .replace('{name}', handleSlideName(slides[index]))
      }
    }

    var handleGo = function (index, announce) {
      index = handleWrap(index)
      var slide = slides[index]
      isProgrammatic = true
      scroller.scrollTo({
        left: slide.offsetLeft,
        behavior: prefersReduce ? 'auto' : 'smooth'
      })
      handlePaint(index, announce)
      setTimeout(function () { isProgrammatic = false }, 450)
    }

    var handleStopAuto = function () {
      if (autoTimer) {
        clearInterval(autoTimer)
        autoTimer = null
      }
    }

    var handleCanAuto = function () {
      if (prefersReduce || userHeld || pointerInside || document.hidden) return false
      if (root.matches && root.matches(':focus-within')) return false
      return slides.length > 1
    }

    var handleStartAuto = function () {
      handleStopAuto()
      if (prefersReduce || slides.length < 2) return
      autoTimer = setInterval(function () {
        if (!handleCanAuto()) return
        handleGo(current + 1, false)
      }, AUTO_MS)
    }

    var handleUserControl = function () {
      userHeld = true
      handleStopAuto()
      if (resumeTimer) clearTimeout(resumeTimer)
      resumeTimer = setTimeout(function () {
        userHeld = false
        handleStartAuto()
      }, RESUME_MS)
    }

    if (dotsEl) {
      slides.forEach(function (slide, i) {
        var dot = document.createElement('button')
        dot.type = 'button'
        dot.className = 'recipes-carousel-dot'
        dot.setAttribute('aria-label', gotoTpl
          .replace('{n}', String(i + 1))
          .replace('{name}', handleSlideName(slide)))
        dot.addEventListener('click', function () {
          handleUserControl()
          handleGo(i, true)
        })
        dotsEl.appendChild(dot)
      })
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', function () {
        handleUserControl()
        handleGo(current - 1, true)
      })
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        handleUserControl()
        handleGo(current + 1, true)
      })
    }

    scroller.addEventListener('scroll', function () {
      handlePaint(handleNearestIndex(), false)
      if (!isProgrammatic) handleUserControl()
    }, { passive: true })

    scroller.addEventListener('wheel', function (e) {
      if (Math.abs(e.deltaX) >= Math.abs(e.deltaY) || e.shiftKey) {
        e.stopPropagation()
      }
    }, { passive: true })

    root.addEventListener('pointerenter', function () { pointerInside = true })
    root.addEventListener('pointerleave', function () {
      pointerInside = false
      if (!userHeld) handleStartAuto()
    })
    root.addEventListener('focusin', function () { pointerInside = true })
    root.addEventListener('focusout', function () {
      pointerInside = false
      if (!userHeld) handleStartAuto()
    })
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) handleStopAuto()
      else if (!userHeld) handleStartAuto()
    })

    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') {
        e.preventDefault()
        handleUserControl()
        handleGo(current - 1, true)
        return
      }
      if (e.key === 'ArrowRight') {
        e.preventDefault()
        handleUserControl()
        handleGo(current + 1, true)
      }
    })

    handlePaint(0, false)
    handleStartAuto()
  })

  /* ── language switcher: more panel (German tip via title/hover only — never blocks nav) ── */
  var handleBindLangs = function () {
    var root = document.querySelector('[data-langs]')
    if (!root) return
    var moreBtn = root.querySelector('[data-lang-more]')
    var panel = root.querySelector('[data-lang-panel]')
    var handleCloseMore = function () {
      if (!moreBtn || !panel) return
      moreBtn.setAttribute('aria-expanded', 'false')
      panel.hidden = true
    }
    if (moreBtn && panel) {
      moreBtn.addEventListener('click', function (e) {
        e.stopPropagation()
        var open = moreBtn.getAttribute('aria-expanded') === 'true'
        moreBtn.setAttribute('aria-expanded', open ? 'false' : 'true')
        panel.hidden = open
      })
      panel.addEventListener('click', function (e) { e.stopPropagation() })
    }
    document.addEventListener('click', function (e) {
      if (!root.contains(e.target)) handleCloseMore()
    })
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') handleCloseMore()
    })
  }
  handleBindLangs()

  /* ── Google Analytics: load gtag.js only after accept ── */
  var gaId = typeof window.__GA_MEASUREMENT_ID === 'string' ? window.__GA_MEASUREMENT_ID : ''
  var consentBar = document.querySelector('[data-consent-bar]')
  var gaLoaded = false
  var CONSENT_KEY = 'juzlova-ga-consent'

  var handleGtagFn = function () {
    window.dataLayer = window.dataLayer || []
    if (typeof window.gtag !== 'function') {
      window.gtag = function () { window.dataLayer.push(arguments) }
    }
    return window.gtag
  }

  var handleAiReferral = function (gtag) {
    if (!gaId || typeof gtag !== 'function') return
    var ref = document.referrer || ''
    if (!ref) return
    var host = ''
    try { host = new URL(ref).hostname.toLowerCase() } catch (err) { return }
    var sources = [
      ['chatgpt.com', 'chatgpt'],
      ['chat.openai.com', 'chatgpt'],
      ['perplexity.ai', 'perplexity'],
      ['claude.ai', 'claude'],
      ['gemini.google.com', 'gemini'],
      ['copilot.microsoft.com', 'copilot']
    ]
    var found = ''
    sources.forEach(function (pair) {
      if (found) return
      if (host === pair[0] || host.slice(-(pair[0].length + 1)) === '.' + pair[0]) {
        found = pair[1]
      }
    })
    if (!found) return
    gtag('event', 'ai_referral', { ai_source: found })
  }

  var handleHideConsent = function () {
    if (!consentBar) return
    consentBar.hidden = true
    consentBar.setAttribute('aria-hidden', 'true')
  }

  var handleShowConsent = function () {
    if (!consentBar) return
    consentBar.hidden = false
    consentBar.removeAttribute('aria-hidden')
  }

  var handleLoadGtag = function () {
    if (gaLoaded || !gaId) return
    gaLoaded = true
    var gtag = handleGtagFn()
    gtag('consent', 'update', { analytics_storage: 'granted' })
    gtag('js', new Date())
    gtag('config', gaId)
    handleAiReferral(gtag)
    var s = document.createElement('script')
    s.async = true
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(gaId)
    document.head.appendChild(s)
  }

  var handleConsentAccept = function () {
    try { localStorage.setItem(CONSENT_KEY, 'accept') } catch (e) {}
    handleLoadGtag()
    handleHideConsent()
  }

  var handleConsentEssential = function () {
    try { localStorage.setItem(CONSENT_KEY, 'essential') } catch (e) {}
    handleHideConsent()
  }

  if (!gaId) {
    handleHideConsent()
  } else {
    handleGtagFn()
    var stored = ''
    try { stored = localStorage.getItem(CONSENT_KEY) || '' } catch (e) {}
    if (stored === 'accept') {
      handleLoadGtag()
      handleHideConsent()
    } else if (stored === 'essential') {
      handleHideConsent()
    } else {
      handleShowConsent()
    }
    var acceptBtn = consentBar ? consentBar.querySelector('[data-consent-accept]') : null
    var essentialBtn = consentBar ? consentBar.querySelector('[data-consent-essential]') : null
    if (acceptBtn) acceptBtn.addEventListener('click', handleConsentAccept)
    if (essentialBtn) essentialBtn.addEventListener('click', handleConsentEssential)
  }
})();
