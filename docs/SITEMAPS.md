# Sitemap maintenance

Run `python3 scripts/build_site.py`, then `python3 scripts/verify_sitemaps.py` and `python3 scripts/verify_refs.py`.

The master sitemap references four language sitemaps plus a separate optional text-resource sitemap. The resource sitemap preserves the six existing llms files, without treating them as Czech HTML pages or promising a ranking benefit. HTML coverage comes from the same stable page IDs as the page generator. Local Czech-only pages remain Czech-only. Hreflang matches each page, including self and x-default; image entries use existing assets.

Do not hand-edit generated XML or text. Keep the canonical www host, translated slugs, and trailing slash convention for HTML pages. File paths such as sitemap.xml and llms.txt have no trailing slash.

Optional `lastmod` comes from `scripts/content_dates.json`: language -> stable page ID -> YYYY-MM-DD. Record only an actual substantive content change confirmed by the editor. Unknown dates are omitted, not replaced with build or deployment time. Example shape: {"cs": {"home": "2026-09-17"}}. Use the actual stable ID and date; the example is not an instruction to date every page. Child sitemap timestamps are omitted until reliable file-change tracking exists.

The verifier independently inventories canonical HTML, excludes redirects/noindex/archive, checks exact coverage, language ownership, reciprocal alternate URLs, robots exclusions, local assets, resource links and XML limits. It runs in the build and deployment workflows. This validates local files; production HTTP status, WAF access and indexing still require post-deployment checks.

All changes in this patch are local and reviewable. Use the existing preview workflow first. The production workflow runs on main; do not use a main push as a preview. Roll back with a reverting commit and the existing deployment process, preserving later unrelated changes.
