const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const context = {module: {exports: {}}, URL};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname, '../assets/measurement.js'), 'utf8'), context);
const create = context.module.exports;
function fixture(ref = 'https://chatgpt.com/?private=secret', shared = {}) {
  const events = [];
  const win = { location: { hostname: 'www.juzlova.cz', origin: 'https://www.juzlova.cz' },
    document: { referrer: ref, documentElement: {lang: 'cs'},
      querySelector: () => ({ href: 'https://www.juzlova.cz/kakao-holandskeho-typu/' }) },
    sessionStorage: { getItem: k => shared[k] || null, setItem: (k, v) => shared[k] = v } };
  return {tracker: create(win), events, gtag: (...args) => events.push(args), shared};
}
const a = fixture();
assert.equal(a.tracker.attribution(), null);
a.tracker.lead('lead_'+'a'.repeat(32), 'contact'); a.tracker.contact('phone');
assert.equal(a.events.length, 0);
a.tracker.activate(a.gtag);
assert.equal(a.tracker.attribution().first_source, 'chatgpt');
assert(!JSON.stringify(a.shared).includes('private'));
assert.equal(a.tracker.sourceOf('https://chatgpt.com.attacker.test'), 'other_referral');
assert.equal(a.tracker.sourceOf('https://www.juzlova.cz/recepty/'), '');
a.tracker.lead('lead_'+'a'.repeat(32), 'contact');
a.tracker.lead('lead_'+'a'.repeat(32), 'contact');
a.tracker.lead('lead_'+'b'.repeat(32), 'newsletter');
a.tracker.lead(undefined, 'contact');
assert.equal(a.events.filter(x => x[1]==='generate_lead').length, 1);
const b = fixture('https://www.juzlova.cz/recepty/', a.shared); b.tracker.activate(b.gtag);
assert.equal(b.tracker.attribution().first_source, 'chatgpt');
b.tracker.lead('lead_'+'a'.repeat(32), 'contact');
assert.equal(b.events.filter(x => x[1]==='generate_lead').length, 0);
b.tracker.contact('email');
assert.equal(b.events.at(-1)[1], 'contact_click');
assert(!b.events.some(x => x[1]==='purchase'));
const c = fixture('', {}); c.tracker.activate(c.gtag);
assert.equal(c.tracker.attribution().first_source, 'direct');
console.log('PASS: consent, referral privacy, internal navigation, lead deduplication and microconversions');
