# Discovery and inquiry measurement

Implemented from the existing published product facts, 18 September 2026.

## Customer-facing changes

- All four languages retain their existing URLs and factual product copy.
- Product offers enumerate every visible pack/price, including pudding 1 kg / 60 Kč and 400 g / 30 Kč. No blanket InStock assertion is made without live inventory.
- Product pages link to their existing associated recipes. No untested recipes or new ingredient claims have been invented.
- Organization markup uses valid types, with no self-serving aggregate rating. Brand and organization use distinct IDs. Global artificial WebPage/Recipe modification dates are removed. Existing visible review-profile links remain.
- Source-generated multilingual sitemaps, llms crosslinks and robots policy include regression checks.

## Measurement

The existing real GA measurement ID must be present at runtime. Analytics and optional attribution activate only after the existing analytics consent is accepted; form/contact permission alone does not activate them. No GA ID means no attribution collection or events. Nothing in this change makes a form submission a sale.

`ai_referral`: recognized incoming assistant referrer. `contact_click`: telephone/email action, no contact details included. `generate_lead`: accepted, persisted contact/B2B/callback with server-issued lead ID; newsletters/honeypots/failures have no lead ID. The client suppresses repeats of an already emitted ID. A server create-if-absent record suppresses duplicate saves and notifications for identical retry submissions, including across Cloud Run instances. A changed inquiry gets a distinct ID. Without browser UUID support the older behavior remains (no cross-request idempotency); disabling the submit button still prevents immediate double clicks.

First/last observed source and canonical landing path are held in consented per-tab session storage for at most 30 minutes of attribution validity. Unknown/direct traffic is not labelled AI. Only allowlisted source labels and a canonical path enter an inquiry record. Raw referrer URLs, URL queries and customer form details are not passed in custom analytics events. GA page URLs omit query strings and referrers are reduced to origin. Review enhanced-measurement settings in GA separately if automatic form/outbound events are enabled.

The inquiry ID and consented source summary are included in the existing owner notification and durable inquiry record. Match that ID to a confirmed order in an offline ledger. Keep customer records private; analytics receives an opaque ID, not names, emails, telephone numbers or inquiry text. Deduplicate orders by order ID, record refunds and use a consistent VAT basis. Do not report quotes as revenue. The supplied reporting template and report_orders.py distinguish observed and self-reported attribution.

Persistence precedes notification. A repeat of an already-stored submission returns stored_existing rather than resending email. If the process failed after saving but before notification, the durable inquiry remains recoverable; this change does not add a background notification queue. Monitor stored-only/failed delivery logs and reconcile the private contacts store with the inbox.

## Deployment

The production workflow now fails explicitly when deployment variables are absent. It tests attribution/markup, sets SITE_REVISION, and smoke-tests the custom domain against the expected revision and exact discovery files. The smoke check reads all 119 canonical page URLs; it never submits customer forms.

The separate candidate-preview service has PREVIEW_READ_ONLY=1: write APIs return 403, llms hit logging is disabled, and HTML gets X-Robots-Tag noindex/nofollow. No production inquiry or rating writes are performed by preview tests. Preview is intentionally unsuitable for sending real orders.

Commands:

```
python3 scripts/build_site.py
python3 scripts/verify_refs.py
python3 scripts/verify_sitemaps.py
python3 scripts/verify_structured_data.py
python3 -m unittest discover -s tests -p 'test_*.py'
node tests/measurement.test.cjs
python3 scripts/wayback_archive.py --check
```

A real revision/API response and passing smoke checks prove a deployment, not search indexing or a traffic lift. Validate GA events in the owner's analytics property after release; preserve consent. No purchases are emitted automatically because there is no online checkout.
