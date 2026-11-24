#!/usr/bin/env python3
"""Build the static site for the wiki.

Reads the authored sources (wiki/articles, wiki/sources, the catalogue) and writes a flat site:
one page per article and per reading map, a home page, a search index, the stylesheet and script,
and a vendored KaTeX. Mathematics is rendered in the browser by the vendored KaTeX, so no page
needs the network.

Usage:
  python3 tools/preview.py                 # build into site/
  python3 tools/preview.py --out DIR       # build elsewhere
  python3 tools/preview.py --check         # fail if site/ is not what the sources build to
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
ARTICLES = WIKI / "articles"
SOURCES = WIKI / "sources"
STATIC = WIKI / "static"
CATALOG = WIKI / "src" / "content" / "catalog.json"
STRUCTURE = WIKI / "structure.json"
STYLE = WIKI / "STYLE.md"
DEFAULT_OUT = ROOT / "site"

# Fallback order used only if wiki/structure.json is missing; the structure file wins.
ORDER = [
    "hierarchical-lattice",
    "hierarchical-gibbs-measure",
    "renormalisation-group-map",
    "gaussian-renormalisation-group",
    "critical-exponents-from-rg",
    "corrections-to-scaling",
    "bleher-sinai-fixed-point",
    "hierarchical-vector-models",
    "hierarchical-phi4-truncations",
    "koch-wittwer-fixed-point",
    "abdesselam-global-trajectory",
    "hierarchical-percolation-rg",
    "hierarchical-and-euclidean-rg",
    "ultrametric-block-systems",
]

HEAD_RE = re.compile(r"^## (.+?) \{#(section-[a-z0-9-]+)\}\s*$")
ANCHOR_RE = re.compile(r'<a\s+id="tag-([0-9A-Z]{4})"\s+data-assertion="([a-z]+)"\s+data-title="([^"]+)"\s*></a>')
FIG_RE = re.compile(r'<div class="fig" data-fig="([a-z-]+)"(?: data-title="([^"]*)")?\s*></div>')
SIM_RE = re.compile(r'<div class="sim" data-sim="([a-z-]+)"(?: data-title="([^"]*)")?\s*></div>')

sys.path.insert(0, str(Path(__file__).resolve().parent))
import simulate  # noqa: E402


# ------------------------------------------------------------------ reading the sources

def split_front_matter(text: str):
    end = text.find("\n---\n", 4)
    return json.loads(text[4:end]), text[end + 5:]


def load_articles():
    out = {}
    for path in sorted(ARTICLES.glob("*.md")):
        meta, body = split_front_matter(path.read_text())
        meta["body"] = body
        out[meta["id"]] = meta
    order = [i for i in ORDER if i in out] + [i for i in out if i not in ORDER]
    return out, order


def load_structure(articles) -> dict:
    """Parts and reading paths, validated against the articles that exist."""
    data = json.loads(STRUCTURE.read_text())
    parts = data["parts"]
    seen = []
    for part in parts:
        if not part.get("articles"):
            raise SystemExit(f"structure: part {part['id']!r} has no articles")
        for aid in part["articles"]:
            if aid not in articles:
                raise SystemExit(f"structure: part {part['id']!r} names unknown article {aid!r}")
            seen.append(aid)
    missing = [a for a in articles if a not in seen]
    if missing:
        raise SystemExit(f"structure: articles not in any part: {missing}")
    if len(seen) != len(set(seen)):
        dupes = sorted({a for a in seen if seen.count(a) > 1})
        raise SystemExit(f"structure: article in more than one part: {dupes}")
    for path in data["paths"]:
        for aid in path["articles"]:
            if aid not in articles:
                raise SystemExit(f"structure: path {path['id']!r} names unknown article {aid!r}")
    return data


def load_maps():
    out = []
    if not SOURCES.is_dir():
        return out
    for path in sorted(SOURCES.glob("*.md")):
        text = path.read_text().strip("\n")
        title = text.splitlines()[0][2:].strip()
        out.append({"slug": path.stem, "title": title, "body": "\n".join(text.splitlines()[1:]).strip()})
    return out


NOTATION_RE = re.compile(r"^## Notation\s*$(.*?)(?=^## )", re.M | re.S)


def load_notation(articles) -> dict:
    """The notation table of wiki/STYLE.md, with each row's article resolved.

    The page is generated from STYLE.md rather than copied, so that the table has one home: a symbol
    added there appears on the page, and a row naming an article that does not exist fails the build.
    """
    m = NOTATION_RE.search(STYLE.read_text())
    if not m:
        sys.exit("STYLE.md has no '## Notation' section; the notation page is generated from it")
    rows, paras, para = [], {"lead": [], "note": []}, []
    state = "lead"

    def flush():
        nonlocal para
        if para:
            paras[state].append(" ".join(para))
            para = []

    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("|"):
            flush()
            state = "note"
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) != 3:
                sys.exit(f"a notation row of STYLE.md needs three columns (object, symbol, article): {line}")
            if cells[0] == "Object" or set(cells[0]) <= set("-: "):
                continue
            obj, symbol, aid = cells
            if aid not in articles:
                sys.exit(f"the notation table names '{aid}', which is not an article")
            rows.append((obj, symbol, aid))
        elif line.startswith(">"):
            continue  # notes to maintainers, kept in the source and not published
        elif line:
            para.append(line)
        else:
            flush()
    flush()
    if not rows:
        sys.exit("the notation table of STYLE.md is empty")
    return {"rows": rows,
            "lead": "".join(f"<p>{inline_md(p)}</p>" for p in paras["lead"]),
            "note": "".join(f"<p>{inline_md(p)}</p>" for p in paras["note"])}


# ------------------------------------------------------------------ transforming bodies

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


def rewrite_links(body: str, tag_owner: dict[str, str]) -> str:
    def art(m):
        target, frag = m.group(1), (m.group(2) or "")
        return f'href="{target}.html' + (f"#{frag}" if frag else "") + '"'
    body = re.sub(r'href="/articles/([a-z0-9-]+)/(?:#([a-z0-9-]+))?"', art, body)
    body = re.sub(r'href="/tag/([0-9A-Z]{4})/"',
                  lambda m: f'href="{tag_owner[m.group(1)]}.html#tag-{m.group(1)}"', body)
    body = re.sub(r'<a\s+data-wanted="[a-z0-9-]+">(.*?)</a>', r'<span class="wanted">\1</span>', body)
    return body


def markdown_links(body: str) -> str:
    """[text](target) as used by the reading maps."""
    def rep(m):
        label, target = m.group(1), m.group(2)
        t = re.fullmatch(r"/articles/([a-z0-9-]+)/(?:#(section-[a-z0-9-]+))?", target)
        href = f"{t.group(1)}.html" + (f"#{t.group(2)}" if t.group(2) else "") if t else target
        return f'<a href="{href}">{label}</a>'
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", rep, body)


def inline_md(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def map_body_to_html(body: str) -> str:
    blocks, para, table = [], [], []
    def flush():
        nonlocal para, table
        if table:
            head = [c.strip() for c in table[0].strip("|").split("|")]
            rows = [[c.strip() for c in r.strip("|").split("|")] for r in table[2:]]
            h = ["<table><thead><tr>"] + [f"<th>{inline_md(c)}</th>" for c in head] + ["</tr></thead><tbody>"]
            for r in rows:
                h.append("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in r) + "</tr>")
            h.append("</tbody></table>")
            blocks.append("".join(h)); table = []
        if para:
            blocks.append("<p>" + inline_md(" ".join(para)) + "</p>"); para = []
    for line in markdown_links(body).splitlines():
        if line.startswith("|"):
            if para: flush()
            table.append(line)
        elif not line.strip():
            flush()
        elif line.startswith("### "):
            flush(); blocks.append(f"<h3>{inline_md(line[4:])}</h3>")
        elif line.startswith("## "):
            flush(); blocks.append(f"<h2>{inline_md(line[3:])}</h2>")
        else:
            if table: flush()
            para.append(line.strip())
    flush()
    return "\n".join(blocks)


def add_heading_anchors(body: str) -> str:
    def rep(m):
        title, sid = m.group(1), m.group(2)
        return f'<h2 id="{sid}">{title}<a class="anchor" href="#{sid}" aria-label="link to this section">#</a></h2>'
    return re.sub(HEAD_RE.pattern.replace("^", "(?m)^"), rep, body)


def strip_html(text: str) -> str:
    text = re.sub(r"<script.*?</script>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


# ------------------------------------------------------------------ page shell

def shell(title: str, description: str, inner: str, sidebar: str, scripts: str = "") -> str:
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description[:200])}">
<link rel="stylesheet" href="assets/katex/katex.min.css">
<link rel="stylesheet" href="assets/site.css">
</head><body>
<div class="layout">
<aside class="sidebar">
{sidebar}
</aside>
<main>
{inner}
</main>
</div>
<script src="assets/katex/katex.min.js" defer></script>
<script src="assets/katex/contrib/auto-render.min.js" defer
  onload="renderMathInElement(document.querySelector('main'),{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:false,ignoredClasses:['sim']}});"></script>
<script src="assets/sim.js" defer></script>
<script src="assets/search.js" defer></script>
{scripts}
</body></html>"""


def sidebar(articles, structure, maps, active: str) -> str:
    parts = structure["parts"]
    blocks = []
    for part in parts:
        items = []
        for n, aid in enumerate(part["articles"], start=1):
            cls = ' class="active"' if aid == active else ""
            items.append(f'<li><span class="num">{n}</span><a href="{aid}.html"{cls}>'
                         f'{articles[aid]["title"]}</a></li>')
        pcls = ' class="active"' if "part-" + part["id"] == active else ""
        blocks.append(f'<nav class="sec"><h2><a href="part-{part["id"]}.html"{pcls}>'
                      f'{part["title"]}</a></h2><ol>{"".join(items)}</ol></nav>')
    mitems = []
    for m in maps:
        cls = ' class="active"' if "source-" + m["slug"] == active else ""
        mitems.append(f'<li><a href="source-{m["slug"]}.html"{cls}>{m["title"].split(":")[0]}</a></li>')
    index_items = [("start.html", "Start here"), ("assertions.html", "Assertions"),
                   ("notation.html", "Notation"), ("bibliography.html", "Bibliography"),
                   ("all.html", "Single file")]
    idx = "".join(f'<li><a href="{href}"{" class=\"active\"" if href.split(".")[0] == active else ""}>{label}</a></li>'
                  for href, label in index_items)
    return f"""<a class="brand" href="index.html">Hierarchical RG<span>renormalisation on hierarchical lattices</span></a>
<form class="search" onsubmit="return false"><input id="q" type="search" placeholder="search  (press /)" aria-label="search the wiki"></form>
<ul class="search-results" id="results"></ul>
{''.join(blocks)}
<nav class="sec"><h2>Reading maps</h2><ul>{''.join(mitems)}</ul></nav>
<nav class="sec"><h2>Index</h2><ul>{idx}</ul></nav>"""


# ------------------------------------------------------------------ builders

def build(out: Path) -> dict:
    articles, _fallback = load_articles()
    structure = load_structure(articles)
    parts = structure["parts"]
    order = [aid for part in parts for aid in part["articles"]]
    part_of = {aid: part for part in parts for aid in part["articles"]}
    maps = load_maps()
    catalog = json.loads(CATALOG.read_text())["sources"]

    tag_owner = {}
    for aid, meta in articles.items():
        for m in ANCHOR_RE.finditer(meta["body"]):
            tag_owner[m.group(1)] = aid

    # reverse links and citations, for "linked from" and the bibliography
    linked_from: dict[str, list[str]] = {aid: [] for aid in articles}
    cited_in: dict[str, list[str]] = {}
    for aid, meta in articles.items():
        for target in set(re.findall(r'/articles/([a-z0-9-]+)/', meta["body"])):
            if target in linked_from and target != aid:
                linked_from[target].append(aid)
        for key in set(re.findall(r"\[@([a-z0-9-]+)", meta["body"])):
            cited_in.setdefault(key, []).append(aid)
    for v in linked_from.values():
        v.sort(key=order.index)

    out.mkdir(parents=True, exist_ok=True)
    sim_data = simulate.build()
    figs = simulate.figures()
    used_sims: dict[str, dict] = {}
    search_entries = []
    assertion_rows = []

    def page_shell(title, description, inner, active):
        return shell(title, description, inner, sidebar(articles, structure, maps, active))

    rendered: dict[str, str] = {}

    # ---- articles
    for aid in order:
        meta = articles[aid]
        part = part_of[aid]
        body = fences_to_details(meta["body"])
        body = rewrite_links(body, tag_owner)
        body = add_heading_anchors(body)

        def sim_slot(m):
            name = m.group(1)
            if name in sim_data:
                used_sims[name] = sim_data[name]
            title = m.group(2) or ""
            return (f'<div class="sim" data-sim="{name}">'
                    f'<div class="sim-title">{title}</div></div>')
        body = SIM_RE.sub(sim_slot, body)

        def fig_slot(match):
            name, title = match.group(1), match.group(2) or ""
            if name not in figs:
                return ""
            caption = f"<figcaption>{title}</figcaption>" if title else ""
            return f'<figure class="fig">{figs[name]}{caption}</figure>'
        body = FIG_RE.sub(fig_slot, body)

        heads = re.findall(r'<h2 id="(section-[a-z0-9-]+)">(.*?)<a class="anchor"', body)
        toc = "".join(f'<li><a href="#{sid}">{title}</a></li>' for sid, title in heads)
        n_assert = len(ANCHOR_RE.findall(meta["body"]))
        n = order.index(aid)

        def pager_link(target, direction):
            label = "previous" if direction < 0 else "next"
            if part_of[target] is not part:
                label += " part"
            return (f'<a href="{target}.html"><span class="dir">{label}</span>'
                    f'{articles[target]["title"]}</a>')
        prev_link = pager_link(order[n - 1], -1) if n > 0 else "<span></span>"
        next_link = pager_link(order[n + 1], +1) if n + 1 < len(order) else "<span></span>"

        sources = linked_from.get(aid, [])
        linked_html = ""
        if sources:
            linked_html = ('<p class="meta">Linked from: ' +
                           ", ".join(f'<a href="{b}.html">{articles[b]["title"]}</a>' for b in sources) +
                           '</p>')

        lead, sep, rest = body.partition("<h2")
        rest = sep + rest if sep else ""
        inner = f"""<p class="crumbs"><a href="index.html">Home</a> /
<a href="part-{part['id']}.html">{part['title']}</a> / {meta['title']}</p>
<h1>{meta['title']}</h1>
<p class="subtitle">{meta['subtitle']}</p>
<p class="meta">{meta['kind']} &middot; part {parts.index(part) + 1} &middot; {len(heads)} sections &middot;
{n_assert} tagged assertions &middot; <span class="tag">{aid}</span></p>
{lead}
<details class="toc" open><summary>On this page</summary><ol>{toc}</ol></details>
{rest}
{linked_html}
<div class="pager">{prev_link}{next_link}</div>
<a class="top" href="#">back to top</a>"""
        (out / f"{aid}.html").write_text(
            page_shell(f"{meta['title']} — Hierarchical RG", meta["summary"], inner, aid))
        rendered[aid] = body
        search_entries.append({"url": f"{aid}.html", "title": meta["title"], "subtitle": meta["subtitle"],
                               "summary": meta["summary"], "text": strip_html(body)[:4000]})

    # ---- part hubs
    for i, part in enumerate(parts):
        items = "".join(
            f'<div class="card"><span class="kind">{len(ANCHOR_RE.findall(articles[a]["body"]))} '
            f'tagged assertions</span><h3><a href="{a}.html">{articles[a]["title"]}</a></h3>'
            f'<p class="sub">{articles[a]["subtitle"]}</p><p class="sum">{articles[a]["summary"]}</p></div>'
            for a in part["articles"])
        nxt = ""
        if i + 1 < len(parts):
            nxt = (f'<div class="pager"><span></span><a href="part-{parts[i + 1]["id"]}.html">'
                   f'<span class="dir">next part</span>{parts[i + 1]["title"]}</a></div>')
        inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Part {i + 1}</p>
<h1>{part['title']}</h1>
<p class="subtitle">{part['subtitle']}</p>
<p class="meta">part {i + 1} of {len(parts)} &middot; {len(part['articles'])} articles &middot;
<span class="tag">part-{part['id']}</span></p>
<p class="lead-para">{part['intro']}</p>
<div class="cards">{items}</div>
{nxt}"""
        (out / f"part-{part['id']}.html").write_text(
            page_shell(f"{part['title']} — Hierarchical RG", part["subtitle"], inner, f"part-{part['id']}"))
        search_entries.append({"url": f"part-{part['id']}.html", "title": part["title"],
                               "subtitle": "part " + str(i + 1), "summary": part["subtitle"],
                               "text": part["intro"]})

    # ---- reading maps
    for m in maps:
        page = "source-" + m["slug"]
        inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Reading maps / {html.escape(m['title'])}</p>
<h1>{html.escape(m['title'])}</h1>
<p class="meta">reading map &middot; <span class="tag">{page}</span></p>
{map_body_to_html(m['body'])}
<div class="pager"><a href="index.html"><span class="dir">back</span>Home</a><span></span></div>"""
        (out / f"{page}.html").write_text(
            page_shell(f"{m['title']} — Hierarchical RG", "A reading map for the wiki.", inner, page))
        search_entries.append({"url": f"{page}.html", "title": m["title"], "subtitle": "reading map",
                               "summary": "", "text": strip_html(map_body_to_html(m["body"]))[:4000]})

    # ---- assertions
    for aid in order:
        body = articles[aid]["body"]
        for m in ANCHOR_RE.finditer(body):
            tag, kind, title = m.group(1), m.group(2), m.group(3)
            chunk = body[m.end():]
            cut = min([x for x in (chunk.find('<a id="tag-'), chunk.find("<h2 ")) if x >= 0] or [len(chunk)])
            statement = fences_to_details(chunk[:cut].strip())
            statement = rewrite_links(statement, tag_owner)
            statement = re.sub(r"^<p>", "", statement)
            page = f"tag-{tag}"
            inner = f"""<p class="crumbs"><a href="index.html">Home</a> / <a href="assertions.html">Assertions</a> / {tag}</p>
<h1>{title}</h1>
<p class="meta">{kind} &middot; <span class="tag">{tag}</span> &middot; in
<a href="{aid}.html">{articles[aid]['title']}</a></p>
<div class="assertion">{statement}</div>
<p class="meta">The full context, including the running hypotheses and the proof, is in
<a href="{aid}.html#tag-{tag}">{articles[aid]['title']}</a>. To cite this assertion, link to
<span class="tag">tag-{tag}.html</span> or to the article anchor directly.</p>
<div class="pager"><a href="assertions.html"><span class="dir">index</span>All assertions</a>
<a href="{aid}.html#tag-{tag}"><span class="dir">context</span>{articles[aid]['title']}</a></div>"""
            (out / f"{page}.html").write_text(
                page_shell(f"{title} — Hierarchical RG", f"{kind}: {title}", inner, page))
            assertion_rows.append((tag, kind, title, aid))
            search_entries.append({"url": f"{page}.html", "title": title, "subtitle": f"{kind} {tag}",
                                   "summary": "", "text": strip_html(statement)[:1500]})

    rows = "".join(
        f'<tr><td class="num">{tag}</td><td>{kind}</td><td><a href="tag-{tag}.html">{title}</a></td>'
        f'<td><a href="{aid}.html">{articles[aid]["title"]}</a></td></tr>'
        for tag, kind, title, aid in assertion_rows)
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Assertions</p>
<h1>Assertions</h1>
<p class="meta">{len(assertion_rows)} tagged statements</p>
<p>Each assertion has a permanent four-character tag, reserved in the wiki's ledger and never
reused. The tag identifies a citable statement rather than a page, so a link to it survives the
article being edited around it.</p>
<table><thead><tr><th>Tag</th><th>Kind</th><th>Statement</th><th>Article</th></tr></thead>
<tbody>{rows}</tbody></table>"""
    (out / "assertions.html").write_text(
        page_shell("Assertions — Hierarchical RG", "Every tagged assertion in the wiki.", inner, "assertions"))

    # ---- bibliography
    by_id = {s["id"]: s for s in catalog}
    brow = []
    for source in catalog:
        users = cited_in.get(source["id"], [])
        links = ", ".join(f'<a href="{a}.html">{articles[a]["title"]}</a>' for a in users) or "&mdash;"
        zbl = f'<a href="{source["zblUrl"]}">{source["zbl"]}</a>' if source.get("zbl") else "—"
        brow.append(f'<tr><td>{source["shortName"]}</td>'
                    f'<td>{source["title"]}<br><span class="meta">{source["edition"]}</span></td>'
                    f'<td class="num">{zbl}</td><td>{links}</td></tr>')
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Bibliography</p>
<h1>Bibliography</h1>
<p class="meta">{len(catalog)} works, {sum(1 for s in catalog if s.get("zbl"))} with a zbMATH record</p>
<p>Every work the wiki cites, with the articles that cite it. The zbMATH number links to the
record; a dash means no record was found, and the work is cited by its published details.</p>
<table><thead><tr><th>Author</th><th>Work</th><th>Zbl</th><th>Cited in</th></tr></thead>
<tbody>{''.join(brow)}</tbody></table>"""
    (out / "bibliography.html").write_text(
        page_shell("Bibliography — Hierarchical RG", "The works the wiki cites, and where.", inner, "bibliography"))
    search_entries.append({"url": "bibliography.html", "title": "Bibliography", "subtitle": f"{len(catalog)} works",
                           "summary": "", "text": " ".join(s["title"] + " " + s["author"] for s in catalog)})

    # ---- notation
    notation = load_notation(articles)
    nrows = "".join(
        f'<tr><td>{symbol}</td><td>{obj}</td>'
        f'<td><a href="{aid}.html">{articles[aid]["title"]}</a></td></tr>'
        for obj, symbol, aid in notation["rows"])
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Notation</p>
<h1>Notation</h1>
<p class="meta">{len(notation["rows"])} symbols, one per object</p>
{notation["lead"]}
<table><thead><tr><th>Symbol</th><th>Object</th><th>Introduced in</th></tr></thead>
<tbody>{nrows}</tbody></table>
{notation["note"]}"""
    (out / "notation.html").write_text(
        page_shell("Notation — Hierarchical RG", "One symbol per object, and where each is introduced.",
                   inner, "notation"))
    search_entries.append({"url": "notation.html", "title": "Notation",
                           "subtitle": f"{len(notation['rows'])} symbols", "summary": "",
                           "text": " ".join(f"{obj} {articles[aid]['title']}"
                                            for obj, _symbol, aid in notation["rows"])})

    # ---- start here
    path_blocks = []
    for path in structure["paths"]:
        items = "".join(
            f'<li><a href="{a}.html">{articles[a]["title"]}</a> '
            f'<span class="meta">— {articles[a]["subtitle"]}</span></li>' for a in path["articles"])
        path_blocks.append(f'<h3>{path["title"]}</h3><p class="meta">{path["note"]}</p><ol>{items}</ol>')
    part_links = "".join(
        f'<li><a href="part-{part["id"]}.html">Part {i + 1}: {part["title"]}</a> '
        f'<span class="meta">— {part["subtitle"]}</span></li>' for i, part in enumerate(parts))
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Start here</p>
<h1>Start here</h1>
<p class="subtitle">What the wiki argues, and three ways through it.</p>
<p>On a hierarchical lattice the renormalisation group is not an approximation. A block has no
boundary: every pair of vertices in different children of a block sits at the same distance, so
the energy of a block is the sum of the energies of its children plus one interaction between
their sums. Decimation is therefore an identity, the state of the recursion is the law of one
number, and the critical behaviour is the behaviour of an orbit of a single map. Everything in
this wiki follows from that.</p>
<p>The argument has three moves. First, <a href="part-block-structure.html">the block structure</a>
and the identity it makes exact. Second, <a href="part-renormalisation-group.html">the map and its
fixed points</a>, including the one case solved in closed form and the two rigorous analyses of the
case that is not. Third, <a href="part-beyond-spins.html">the models that are not scalar spins</a>,
where the same mechanism produces percolation exponents, a free direction for vector spins, and the
obstruction that stops the argument on $\\mathbb Z^d$.</p>
<h2>The parts</h2>
<ol class="paths">{part_links}</ol>
<h2>Reading paths</h2>
{''.join(path_blocks)}
<h2>Beyond the articles</h2>
<p>The <a href="assertions.html">assertions index</a> lists every tagged statement, each with a
page of its own; the <a href="bibliography.html">bibliography</a> gives every work cited and the
articles citing it; the <a href="notation.html">notation page</a> fixes one symbol per object and
names the article that introduces it; and the reading maps — for
<a href="source-bleher-major-sinai.html">Bleher, Major and Sinai</a>,
<a href="source-koch-wittwer.html">Koch and Wittwer</a> and
<a href="source-abdesselam.html">Abdesselam</a> — say what each paper establishes and where the
wiki uses it.</p>"""
    (out / "start.html").write_text(
        page_shell("Start here — Hierarchical RG", "The argument of the wiki, and ways through it.", inner, "start"))
    search_entries.append({"url": "start.html", "title": "Start here",
                           "subtitle": "the argument of the wiki", "summary": "", "text":
                           "the block structure, the decimation identity, the renormalisation group map, "
                           "fixed points, exponents, percolation, vector models, phi-fourth, Euclidean comparison"})

    # ---- single-file edition
    def strip_sims(text):
        def note(m):
            title = m.group(2) or ""
            return (f'<p class="meta">[Interactive figure: {title} &mdash; on the web page]</p>'
                    if title else '<p class="meta">[Interactive figure &mdash; on the web page]</p>')
        return re.sub(r'<div class="sim" data-sim="[a-z-]+"(?: data-title="([^"]*)")?>(?:<div class="sim-title">(.*?)</div>)?</div>',
                      lambda m: f'<p class="meta">[Interactive figure{": " + m.group(2) if m.group(2) else ""} &mdash; on the web page]</p>',
                      text)
    contents = []
    for i, part in enumerate(parts):
        contents.append(f'<li><strong>Part {i + 1}: {part["title"]}</strong><ol>' +
                        "".join(f'<li><a href="#whole-{a}">{articles[a]["title"]}</a></li>'
                                for a in part["articles"]) + "</ol></li>")
    whole = []
    for aid in order:
        meta = articles[aid]
        body = strip_sims(rendered[aid])
        body = re.sub(r'<a class="anchor" href="#[^"]*" aria-label="link to this section">#</a>', "", body)
        whole.append(f'<section class="whole" id="whole-{aid}"><h1>{meta["title"]}</h1>'
                     f'<p class="subtitle">{meta["subtitle"]}</p>'
                     f'<p class="meta">{meta["kind"]} &middot; <a href="{aid}.html">separate page</a></p>'
                     f'{body}</section>')
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Single file</p>
<h1>Hierarchical RG</h1>
<p class="subtitle">The whole wiki in one page, for printing or reading offline.</p>
<p class="meta">{len(order)} articles &middot; {len(assertion_rows)} tagged assertions &middot; the pages
that are interactive or generated are linked from each article's separate page</p>
<details class="toc" open><summary>Contents</summary><ol>{''.join(contents)}</ol></details>
{''.join(whole)}"""
    (out / "all.html").write_text(
        page_shell("Hierarchical RG — single file", "The whole wiki in one page.", inner, "all"))
    search_entries.append({"url": "all.html", "title": "Single file edition",
                           "subtitle": f"all {len(order)} articles in one page", "summary": "",
                           "text": "single file printable edition"})

    # ---- home
    part_cards = []
    for i, part in enumerate(parts):
        arts = "".join(f'<li><a href="{a}.html">{articles[a]["title"]}</a> '
                       f'<span class="meta">{articles[a]["subtitle"]}</span></li>' for a in part["articles"])
        part_cards.append(f"""<div class="card part"><span class="kind">part {i + 1}</span>
<h3><a href="part-{part['id']}.html">{part['title']}</a></h3>
<p class="sub">{part['subtitle']}</p>
<ol class="mini">{arts}</ol></div>""")
    map_cards = "".join(f'<li><a href="source-{m["slug"]}.html">{html.escape(m["title"])}</a></li>' for m in maps)
    inner = f"""<h1>Hierarchical RG</h1>
<p class="subtitle">A wiki on the renormalisation group on hierarchical lattices: {len(order)} articles,
{len(figs)} figures, {len(assertion_rows)} tagged assertions.</p>
<p>The renormalisation group is exact on a hierarchical lattice. A block has no boundary, every
pair between two children carries one coupling, and a decimation step is an operation on the law
of a single number. This wiki develops that structure — the lattice, the recursion, the fixed
points, the exponents, the literature — with complete proofs where they are short and precise
attribution where they are not.</p>
<p><a href="start.html">Start here</a> for the argument and four reading paths, or go straight to
<a href="part-{parts[0]['id']}.html">part one</a>.</p>
<h2 id="parts">The three parts</h2>
<div class="cards">{''.join(part_cards)}</div>
<h2 id="maps">Reading maps</h2>
<p>One finding aid per group of works: what each paper establishes and where the wiki uses it.</p>
<ul>{map_cards}</ul>
<h2 id="index">Index</h2>
<ol class="paths">
<li><a href="assertions.html">Assertions</a> <span class="meta">— every tagged statement, with its own page</span></li>
<li><a href="notation.html">Notation</a> <span class="meta">— one symbol per object, and the article that introduces it</span></li>
<li><a href="bibliography.html">Bibliography</a> <span class="meta">— every work cited, with the articles citing it</span></li>
<li><a href="all.html">Single file</a> <span class="meta">— the whole wiki in one page, for printing</span></li>
</ol>"""
    (out / "index.html").write_text(
        page_shell("Hierarchical RG — a wiki on the renormalisation group",
                   "A wiki on the renormalisation group on hierarchical lattices.", inner, "index"))

    # ---- assets and search
    (out / "search-index.json").write_text(json.dumps(search_entries, ensure_ascii=False))
    if used_sims:
        blob = json.dumps(used_sims, ensure_ascii=False).replace("</", "<\\/")
        for path in out.glob("*.html"):
            text = path.read_text()
            if 'data-sim="' in text and "sim-data" not in text:
                text = text.replace("</main>", f'<script type="application/json" id="sim-data">{blob}</script>\n</main>')
                path.write_text(text)

    assets = out / "assets"
    if assets.exists():
        shutil.rmtree(assets)
    assets.mkdir(parents=True)
    for name in ("site.css", "sim.js", "search.js"):
        shutil.copy2(STATIC / name, assets / name)
    shutil.copytree(STATIC / "katex", assets / "katex")

    return {"articles": len(order), "maps": len(maps), "pages": len(list(out.glob("*.html"))),
            "sims": sorted(used_sims), "sources": len(catalog), "parts": len(parts),
            "assertions": len(assertion_rows)}


# ------------------------------------------------------------------ entry point

def differing(a: Path, b: Path) -> list[str]:
    problems = []
    fa = sorted(p.relative_to(a) for p in a.rglob("*") if p.is_file())
    fb = sorted(p.relative_to(b) for p in b.rglob("*") if p.is_file())
    if [str(x) for x in fa] != [str(x) for x in fb]:
        problems.append(f"file lists differ: {len(fa)} built, {len(fb)} committed")
    for rel in fa:
        if rel in fb and (a / rel).read_bytes() != (b / rel).read_bytes():
            problems.append(f"differs: {rel}")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--check", action="store_true", help="fail if the committed site is stale")
    args = ap.parse_args()

    if args.check:
        tmp = ROOT / ".scratch" / "build-check"
        if tmp.exists():
            shutil.rmtree(tmp)
        stats = build(tmp)
        problems = differing(tmp, DEFAULT_OUT)
        print(f"checked {stats['pages']} pages against site/")
        for p in problems[:20]:
            print("FAIL  " + p)
        if problems:
            print(f"\n{len(problems)} difference(s); run python3 tools/preview.py")
            return 1
        print("site/ is up to date")
        return 0

    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    stats = build(out)
    label = out.resolve().relative_to(ROOT) if out.resolve().is_relative_to(ROOT) else out
    print(f"wrote {stats['pages']} pages to {label}/ "
          f"({stats['articles']} articles, {stats['maps']} maps, simulations: {', '.join(stats['sims']) or 'none'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
