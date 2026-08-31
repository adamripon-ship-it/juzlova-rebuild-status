#!/usr/bin/env python3
"""Fail if any generated page points at a missing local file.

Walks every index.html outside archive/ and resolves src=, href=, and CSS
url() values that are not absolute or data URIs. Exit 0 means none missing.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_HREF = re.compile(r'(?:src|href)="([^"#?:]+?)"')
CSS_URL = re.compile(r"url\(([^)]+)\)")


def main() -> int:
    missing: set[str] = set()
    pages = 0
    for path in ROOT.rglob("index.html"):
        if "archive" in path.parts or ".git" in path.parts:
            continue
        pages += 1
        text = path.read_text(encoding="utf-8")
        refs = SRC_HREF.findall(text)
        refs.extend(u.strip("'\"") for u in CSS_URL.findall(text))
        for ref in refs:
            if ref.startswith(("http", "//", "mailto", "tel", "data:")):
                continue
            target = (path.parent / ref).resolve()
            if not target.exists() and not (target / "index.html").exists():
                missing.add(f"{path.relative_to(ROOT)} -> {ref}")
    print(f"pages {pages}")
    print(f"broken refs: {len(missing)}")
    for item in sorted(missing)[:20]:
        print(f"  {item}")
    if missing:
        print("verify_refs: FAIL", file=sys.stderr)
        return 1
    print("verify_refs: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
