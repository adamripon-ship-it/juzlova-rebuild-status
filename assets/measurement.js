/* Consented, per-tab attribution. Never retain raw URLs, form text or contact details. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory;
  else root.JuzlovaMeasurement = factory(root);
}(typeof window !== 'undefined' ? window : this, function (win) {
  'use strict';
  var KEY = 'juzlova-attribution-v1';
  var active = false, state = null, gtag = null, sent = {};
  var sources = {
    'chatgpt.com': 'chatgpt', 'chat.openai.com': 'chatgpt', 'perplexity.ai': 'perplexity',
    'claude.ai': 'claude', 'gemini.google.com': 'gemini', 'copilot.microsoft.com': 'copilot',
    'google.com': 'organic_search', 'google.cz': 'organic_search', 'bing.com': 'organic_search',
    'search.seznam.cz': 'organic_search'
  };
  function sourceOf(ref) {
    if (!ref) return 'direct';
    try {
      var host = new URL(ref).hostname.toLowerCase();
      if (host === win.location.hostname || host === 'juzlova.cz' || host === 'www.juzlova.cz') return '';
      for (var domain in sources) {
        if (host === domain || host.endsWith('.' + domain)) return sources[domain];
      }
      return 'other_referral';
    } catch (_) { return 'unknown'; }
  }
  function safePath() {
    var canonical = win.document.querySelector('link[rel="canonical"]');
    try { return new URL(canonical ? canonical.href : win.location.origin + '/').pathname; }
    catch (_) { return '/'; }
  }
  function persist() { try { win.sessionStorage.setItem(KEY, JSON.stringify(state)); } catch (_) {} }
  function activate(fn) {
    if (active) return;
    active = true; gtag = fn;
    try { state = JSON.parse(win.sessionStorage.getItem(KEY)); } catch (_) {}
    var now = Date.now(), source = sourceOf(win.document.referrer);
    if (!state || !state.started_at || now - state.started_at > 1800000) {
      state = { first_source: source || 'direct', last_source: source || 'direct',
        landing_path: safePath(), started_at: now, sent_leads: [] };
    } else if (source && source !== 'direct') state.last_source = source;
    (state.sent_leads || []).forEach(function (id) { sent[id] = true; });
    persist();
    if (['chatgpt', 'perplexity', 'claude', 'gemini', 'copilot'].indexOf(source) >= 0)
      gtag('event', 'ai_referral', { ai_source: source });
  }
  function attribution() {
    if (!active || !state) return null;
    if (Date.now() - state.started_at > 1800000) return null;
    return { consent: true, first_source: state.first_source, last_source: state.last_source,
      landing_path: state.landing_path, language: win.document.documentElement.lang || 'cs' };
  }
  function lead(id, kind) {
    if (!active || !gtag || !/^lead_[a-f0-9]{32}$/.test(id || '') || kind === 'newsletter' || sent[id]) return;
    sent[id] = true; state.sent_leads = Object.keys(sent).slice(-100); persist();
    var data = attribution() || {};
    gtag('event', 'generate_lead', { lead_id: id, form_type: kind,
      language: win.document.documentElement.lang || 'cs',
      first_source: data.first_source || 'unknown', last_source: data.last_source || 'unknown' });
  }
  function contact(method) {
    if (active && gtag && ['phone', 'email'].indexOf(method) >= 0)
      gtag('event', 'contact_click', { contact_method: method });
  }
  return { activate: activate, attribution: attribution, lead: lead, contact: contact, sourceOf: sourceOf };
}));
