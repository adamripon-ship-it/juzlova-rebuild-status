#!/usr/bin/env python3
"""Add Cloudflare visitor counting and optional Google Analytics ID to HTML.

Tokens come from the server env only. Google's gtag.js is not loaded here —
the page waits for visitor consent before fetching it.
"""
import json
import os
import pathlib
import re

CF_TOKEN = (os.environ.get("CLOUDFLARE_WEB_ANALYTICS_TOKEN") or "").strip()
GA_ID = (
    os.environ.get("GOOGLE_ANALYTICS_MEASUREMENT_ID")
    or os.environ.get("GA_MEASUREMENT_ID")
    or ""
).strip()
ROOT = pathlib.Path("/usr/share/nginx/html")
CF_MARKER = "static.cloudflareinsights.com"
GA_MARKER = "__GA_MEASUREMENT_ID"
GA_ID_RE = re.compile(r"^G-[A-Z0-9]{4,20}$")


def cf_snippet(token):
    safe = (
        token.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return (
        '<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
        f'data-cf-beacon=\'{{"token":"{safe}"}}\'></script>'
    )


def ga_snippet(ga_id):
    if not GA_ID_RE.match(ga_id):
        return ""
    return (
        f"<script>window.__GA_MEASUREMENT_ID={json.dumps(ga_id)}</script>\n"
        "<script>window.dataLayer=window.dataLayer||[];"
        "function gtag(){dataLayer.push(arguments)}"
        "gtag('consent','default',{"
        "analytics_storage:'denied',"
        "ad_storage:'denied',"
        "ad_user_data:'denied',"
        "ad_personalization:'denied',"
        "wait_for_update:500"
        "})</script>"
    )


def main():
    snippets = []
    if CF_TOKEN:
        snippets.append((CF_MARKER, cf_snippet(CF_TOKEN)))
    ga = ga_snippet(GA_ID) if GA_ID else ""
    if ga:
        snippets.append((GA_MARKER, ga))
    if not snippets:
        return
    for path in ROOT.rglob("*.html"):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        added = []
        for marker, snip in snippets:
            if marker in text:
                continue
            added.append(snip)
        if not added:
            continue
        block = "\n".join(added) + "\n"
        if "</head>" in text:
            path.write_text(text.replace("</head>", block + "</head>", 1), encoding="utf-8")
        elif "</body>" in text:
            path.write_text(text.replace("</body>", block + "</body>", 1), encoding="utf-8")


if __name__ == "__main__":
    main()
