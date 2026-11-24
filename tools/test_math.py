#!/usr/bin/env python3
"""Render every formula in the built pages through KaTeX, in quickjs.

This is the check that the mathematics actually renders: any unsupported macro shows up here
rather than as a red error in a reader's browser. Needs `pip install quickjs`.

Usage: python3 tools/test_math.py [--dir site]
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".scratch" / "pip"))
try:
    import quickjs
except ImportError:
    print("FAIL  quickjs is not installed; cannot check the mathematics")
    raise SystemExit(1)

DISPLAY = re.compile(r'<div class="math-display">\s*\$\$(.+?)\$\$\s*</div>', re.S)
INLINE = re.compile(r'(?<!\$)\$([^$]+?)\$(?!\$)')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="site")
    args = ap.parse_args()
    site = ROOT / args.dir
    pages = sorted(site.glob("*.html"))
    katex_js = (ROOT / "wiki/static/katex/katex.min.js").read_text()

    ctx = quickjs.Context()
    ctx.eval(katex_js + "\nvar K = (typeof katex !== 'undefined') ? katex : this.katex;")
    if not ctx.eval("typeof K === 'object' && typeof K.renderToString === 'function'"):
        print("FAIL  KaTeX did not load in the engine")
        return 1

    total, failures = 0, []
    for page in pages:
        text = page.read_text()
        pieces = [(m.group(1), True) for m in DISPLAY.finditer(text)]
        rest = DISPLAY.sub(" ", text)
        pieces += [(m.group(1), False) for m in INLINE.finditer(rest)]
        for tex, display in pieces:
            total += 1
            payload = json.dumps({"tex": html.unescape(tex), "display": display})
            try:
                ctx.eval(
                    "var __t = " + json.dumps(json.loads(payload)["tex"]) + ";" 
                    "var __d = " + ("true" if display else "false") + ";"
                    "var __err = null;"
                    "try { K.renderToString(__t, {displayMode: __d, throwOnError: true, strict: false}); }"
                    "catch (e) { __err = String(e.message || e); }"
                    "__err;"
                )
                err = ctx.eval("__err")
            except Exception as exc:                      # engine-level failure
                err = str(exc)
            if err:
                failures.append((page.name, tex.strip()[:110], str(err)[:160]))

    print(f"{total} formulas rendered from {len(pages)} pages")
    seen = set()
    for page, tex, err in failures:
        key = (tex, err)
        if key in seen:
            continue
        seen.add(key)
        print(f"FAIL  {page}: {err}\n      {tex}")
    if failures:
        print(f"\n{len(failures)} formula(s) do not render")
        return 1
    print("every formula renders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
