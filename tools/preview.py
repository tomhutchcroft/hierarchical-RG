#!/usr/bin/env python3
"""Render a static preview of the wiki into wiki/preview/.

This is a reader for the authored sources, not the PercLib build: it renders the
article format (front matter, lead, sections, collapsible blocks, links, citation
keys) into HTML and loads KaTeX from a CDN for the mathematics. The PercLib build
renders mathematics at build time with node; this preview does not, so mathematics
needs the network the first time a page is opened.

Usage: python3 tools/preview.py
"""
from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
ARTICLES = WIKI / "articles"
SOURCES = WIKI / "sources"
CATALOG = WIKI / "src" / "content" / "catalog.json"
OUT = WIKI / "preview"

HEAD_RE = re.compile(r"^## (.+?) \{#(section-[a-z0-9-]+)\}\s*$")
ANCHOR_RE = re.compile(r'<a\s+id="tag-([0-9A-Z]{4})"\s+data-assertion="([a-z]+)"\s+data-title="([^"]+)"\s*></a>')

CSS = """
:root { --ink:#1a1a1a; --muted:#666; --rule:#ddd; --accent:#8a1c1c; }
* { box-sizing: border-box; }
body { margin:0; font: 17px/1.6 Georgia, 'Times New Roman', serif; color:var(--ink); background:#fbfaf7; }
main { max-width: 46rem; margin: 0 auto; padding: 3rem 1.25rem 6rem; }
header.site { border-bottom:1px solid var(--rule); margin-bottom:2rem; padding-bottom:.6rem;
  display:flex; justify-content:space-between; align-items:baseline; font-family: ui-sans-serif, system-ui, sans-serif; font-size:.85rem; }
header.site a { color: var(--ink); text-decoration:none; }
h1 { font-size:1.9rem; line-height:1.2; margin:.2rem 0 .3rem; }
.subtitle { color:var(--muted); font-style:italic; margin:0 0 1.6rem; }
h2 { font-size:1.2rem; margin:2.4rem 0 .6rem; padding-bottom:.25rem; border-bottom:1px solid var(--rule); }
a { color:var(--accent); }
.math-display { overflow-x:auto; margin:1rem 0; }
details { margin:1rem 0; border-left:2px solid var(--rule); padding:.1rem 0 .1rem 1rem; }
summary { cursor:pointer; color:var(--muted); font-family: ui-sans-serif, system-ui, sans-serif; font-size:.9rem; }
table { border-collapse:collapse; width:100%; font-size:.95rem; }
td, th { text-align:left; padding:.4rem .6rem; border-bottom:1px solid var(--rule); vertical-align:top; }
.meta { font-family: ui-sans-serif, system-ui, sans-serif; font-size:.82rem; color:var(--muted); }
.tag { font-family: ui-monospace, monospace; font-size:.75rem; color:var(--muted); }
.note { background:#fff6e5; border:1px solid #f0dcb4; padding:.7rem .9rem; font-size:.85rem;
  font-family: ui-sans-serif, system-ui, sans-serif; margin-bottom:2rem; }
"""

KATEX = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});"></script>
"""


def split(text: str):
    end = text.find("\n---\n", 4)
    meta = json.loads(text[4:end])
    return meta, text[end + 5:]


def fences_to_details(body: str) -> str:
    out, stack = [], []
    for line in body.splitlines():
        m = re.match(r"^(:{3,})\s*(details\s+.*|[A-Za-z]*)\s*$", line.strip())
        if m and line.strip().startswith(":"):
            cols, rest = len(m.group(1)), m.group(2).strip()
            if rest.startswith("details"):
                summary = rest[len("details"):].strip()
                out.append(f"<details><summary>{summary}</summary><div class='collapsible-body'>")
                stack.append(cols)
                continue
            if rest == "" and stack:
                out.append("</div></details>")
                stack.pop()
                continue
        out.append(line)
    return "\n".join(out)


def rewrite_links(body: str, tag_owner: dict[str, str], ids: set[str]) -> str:
    def art(m):
        target, frag = m.group(1), (m.group(2) or "")
        return f'href="{target}.html{frag}"'
    body = re.sub(r'href="/articles/([a-z0-9-]+)/(?:#([a-z0-9-]+))?"', art, body)
    body = re.sub(r'href="/tag/([0-9A-Z]{4})/"',
                  lambda m: f'href="{tag_owner[m.group(1)]}.html#tag-{m.group(1)}"', body)
    return body


def inline(text: str, ids: set[str], tag_owner: dict[str, str]) -> str:
    """Inline Markdown of the reading-map format: links, emphasis, code."""
    out = []
    for line in text.splitlines():
        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                      lambda m: _link(m.group(1), m.group(2), ids, tag_owner), line)
        line = re.sub(r"`([^`]+)`", r"<code>\1</code>", line)
        line = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", line)
        line = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", line)
        out.append(line)
    return "\n".join(out)


def _link(label: str, target: str, ids: set[str], tag_owner: dict[str, str]) -> str:
    m = re.fullmatch(r"/articles/([a-z0-9-]+)/(?:#(section-[a-z0-9-]+))?", target)
    if m:
        frag = f"#{m.group(2)}" if m.group(2) else ""
        return f'<a href="{m.group(1)}.html{frag}">{label}</a>'
    return f'<a href="{target}">{label}</a>'


def render_map(text: str, ids: set[str], tag_owner: dict[str, str]) -> tuple[str, str]:
    """Returns (title, body html) for a reading map."""
    lines = text.splitlines()
    title = lines[0][2:].strip()
    blocks, para, table = [], [], []

    def flush():
        nonlocal para, table
        if table:
            head = [c.strip() for c in table[0].strip("|").split("|")]
            rows = [[c.strip() for c in r.strip("|").split("|")] for r in table[2:]]
            html = ["<table><thead><tr>"]
            html += [f"<th>{inline(c, ids, tag_owner)}</th>" for c in head]
            html.append("</tr></thead><tbody>")
            for r in rows:
                html.append("<tr>" + "".join(f"<td>{inline(c, ids, tag_owner)}</td>" for c in r) + "</tr>")
            html.append("</tbody></table>")
            blocks.append("".join(html))
            table = []
        if para:
            blocks.append("<p>" + inline(" ".join(para), ids, tag_owner) + "</p>")
            para = []

    for line in lines[1:]:
        if line.startswith("|"):
            if para:
                flush()
            table.append(line)
        elif not line.strip():
            flush()
        elif line.startswith("### "):
            flush(); blocks.append(f"<h3>{inline(line[4:], ids, tag_owner)}</h3>")
        elif line.startswith("## "):
            flush(); blocks.append(f"<h2>{inline(line[3:], ids, tag_owner)}</h2>")
        else:
            if table:
                flush()
            para.append(line.strip())
    flush()
    return title, "\n".join(blocks)


def source_row(s: dict) -> str:
    zbl = s.get("zbl") or ""
    link = (f"<a href=\"{s['zblUrl']}\">{zbl}</a>" if zbl else "<span class='meta'>-</span>")
    return (f"<tr><td>{s['shortName']}</td>"
            f"<td>{s['title']}<br><span class='meta'>{s['edition']}</span></td>"
            f"<td class='tag'>{link}</td></tr>")


def main() -> None:
    entries = []
    tag_owner: dict[str, str] = {}
    for path in sorted(ARTICLES.glob("*.md")):
        meta, body = split(path.read_text())
        meta["_body"] = body
        meta["_path"] = path
        entries.append(meta)
        for m in ANCHOR_RE.finditer(body):
            tag_owner[m.group(1)] = meta["id"]

    catalog = {s["id"]: s for s in json.loads(CATALOG.read_text())["sources"]}
    ids = {m["id"] for m in entries}
    OUT.mkdir(exist_ok=True)

    def page(title: str, inner: str) -> str:
        return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><style>{CSS}</style>{KATEX}</head>
<body><main>
<header class="site"><a href="index.html">Hierarchical RG</a>
<span>A wiki: unfinished, in draft</span></header>
{inner}
</main></body></html>"""

    for meta in entries:
        body = fences_to_details(meta["_body"])
        body = rewrite_links(body, tag_owner, ids)
        # Contents and section anchors
        parts, cur, heads = [], [], []
        for line in body.splitlines():
            m = HEAD_RE.match(line)
            if m:
                if cur or not parts:
                    parts.append("\n".join(cur))
                    cur = []
                heads.append((m.group(1), m.group(2)))
                cur.append(f'<h2 id="{m.group(2)}">{m.group(1)}</h2>')
            else:
                cur.append(line)
        parts.append("\n".join(cur))
        lead, sections = parts[0], parts[1:]
        toc = "".join(f'<li><a href="#{h[1]}">{h[0]}</a></li>' for h in heads)
        body_html = f"""<h1>{meta['title']}</h1>
<p class="subtitle">{meta['subtitle']}</p>
<p class="meta">{meta['kind']} &middot; {meta['category']} &middot; <span class="tag">{meta['id']}</span></p>
<div class="note">Preview generated from the sources by <code>tools/preview.py</code>. Mathematics
renders only if the KaTeX style sheet and script load from the network; the sources are the
authority.</div>
{lead}
<nav class="meta"><strong>Contents</strong><ol>{toc}</ol></nav>
{''.join(sections)}"""
        (OUT / f"{meta['id']}.html").write_text(page(meta["title"], body_html))
        print("wrote", f"{meta['id']}.html")

    map_links = []
    if SOURCES.is_dir():
        for path in sorted(SOURCES.glob("*.md")):
            mtitle, mbody = render_map(path.read_text(), ids, tag_owner)
            slug = path.stem
            (OUT / f"source-{slug}.html").write_text(page(mtitle, f"""<h1>{mtitle}</h1>
<p class="meta">Reading map &middot; <span class="tag">source-{slug}</span></p>
<div class="note">A reading map lists the works of a group, what each establishes, and where this
wiki uses it. It is a finding aid, not a source of formal status or of locator-level accuracy.</div>
{mbody}
<p class="meta"><a href="index.html">All articles</a></p>"""))
            print("wrote", f"source-{slug}.html")
            map_links.append(f"<li><a href=\"source-{slug}.html\">{mtitle}</a></li>")

    rows = "".join(
        f"<tr><td><a href=\"{m['id']}.html\">{m['title']}</a><br><span class='meta'>{m['subtitle']}</span></td>"
        f"<td>{m['summary']}</td></tr>" for m in entries)
    index = f"""<h1>Hierarchical renormalisation group</h1>
<p class="subtitle">Eight articles on the block-spin transformation, its exact recursion, its fixed points and their exponents.</p>
<div class="note">Preview generated from the sources by <code>tools/preview.py</code>. Mathematics
renders only if KaTeX loads from the network.</div>
<table><tbody>{rows}</tbody></table>
<h2 id="reading-maps">Reading maps</h2>
<ul>{''.join(map_links)}</ul>
<h2 id="sources">Sources cited</h2>
<table><thead><tr><th>Author</th><th>Work</th><th>zbMATH</th></tr></thead><tbody>{''.join(source_row(s) for s in catalog.values())}</tbody></table>"""
    (OUT / "index.html").write_text(page("Hierarchical RG", index))
    print("wrote index.html")

    # local link check
    bad = []
    for f in OUT.glob("*.html"):
        text = f.read_text()
        for target in re.findall(r'href="([a-z0-9-]+\.html)(#[^"]*)?"', text):
            if not (OUT / target[0]).exists():
                bad.append((f.name, target[0]))
    print("broken local links:", bad if bad else "none")


if __name__ == "__main__":
    main()
