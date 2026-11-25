#!/usr/bin/env python3
"""Check the built site: every local link and asset resolves, every fragment exists.

Usage: python3 tools/check_site.py [--dir site]
"""
from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)")


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.text = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for attr in ("href", "src"):
            if attr in a and a[attr]:
                self.links.append((attr, a[attr].strip()))


def parse(path: Path) -> Links:
    p = Links()
    p.text = path.read_text(errors="replace")
    p.feed(p.text)
    return p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="site")
    args = ap.parse_args()
    site = (ROOT / args.dir).resolve()
    if not site.is_dir():
        print(f"FAIL  {args.dir}/ does not exist; run python3 tools/preview.py")
        return 1

    pages = sorted(site.glob("*.html"))
    parsed = {p.name: parse(p) for p in pages}
    fails, checked = [], 0

    for page, info in parsed.items():
        for attr, target in info.links:
            if not target or EXTERNAL.match(target) or target.startswith("mailto:"):
                continue
            checked += 1
            path_part, _, frag = target.partition("#")
            path_part = path_part.split("?")[0]
            dest = (site / path_part).resolve() if path_part else (site / page)
            if not str(dest).startswith(str(site)):
                fails.append(f"{page}: link escapes the site: {target}")
                continue
            if not dest.exists():
                fails.append(f"{page}: missing target {target}")
                continue
            if frag:
                target_ids = parsed[dest.name].ids if dest.name in parsed else parse(dest).ids
                if frag not in target_ids:
                    fails.append(f"{page}: missing fragment {target}")

    # assets referenced from the stylesheet
    for css in site.rglob("*.css"):
        for m in re.finditer(r"url\(([^)]+)\)", css.read_text(errors="replace")):
            url = m.group(1).strip("'\"")
            if EXTERNAL.match(url):
                continue
            checked += 1
            if not (css.parent / url.split("?")[0]).exists():
                fails.append(f"{css.relative_to(site)}: missing asset {url}")

    # structure and accessibility: one main landmark, a skip link, labelled navigation
    for page, info in parsed.items():
        text = info.text
        if text.count("<main") != 1:
            fails.append(f"{page}: {text.count('<main')} main landmarks")
        if 'class="skip"' not in text:
            fails.append(f"{page}: no skip link")
        for m in re.finditer(r"<nav([^>]*)>", text):
            if "aria-label" not in m.group(1):
                fails.append(f"{page}: a nav element without an aria-label")
                break

    print(f"{len(pages)} pages, {checked} local links and assets checked")
    for f in fails[:25]:
        print("FAIL  " + f)
    if fails:
        print(f"\n{len(fails)} broken reference(s)")
        return 1
    print("every local link, fragment and asset resolves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
