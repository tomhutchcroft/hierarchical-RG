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
SITE_URL = "https://tomhutchcroft.github.io/hierarchical-RG/"

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
            if len(cells) != 4:
                sys.exit(f"a notation row of STYLE.md needs four columns (object, symbol, introduced in, also used in): {line}")
            if cells[0] == "Object" or set(cells[0]) <= set("-: "):
                continue
            obj, symbol, aid, also = cells
            for name in [aid] + [x.strip() for x in also.replace("\u2014", "").split(",") if x.strip()]:
                if name not in articles:
                    sys.exit(f"the notation table names '{name}', which is not an article")
            users = [x.strip() for x in also.replace("\u2014", "").split(",") if x.strip()]
            rows.append((obj, symbol, aid, users))
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
<a class="skip" href="#main">skip to content</a>
<div class="layout">
<aside class="sidebar" aria-label="site">
{sidebar}
</aside>
<main id="main">
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
        blocks.append(f'<nav class="sec" aria-label="part: {html.escape(part["title"])}">'
                      f'<h2><a href="part-{part["id"]}.html"{pcls}>'
                      f'{part["title"]}</a></h2><ol>{"".join(items)}</ol></nav>')
    mitems = []
    for m in maps:
        cls = ' class="active"' if "source-" + m["slug"] == active else ""
        mitems.append(f'<li><a href="source-{m["slug"]}.html"{cls}>{m["title"].split(":")[0]}</a></li>')
    index_items = [("start.html", "Start here"), ("assertions.html", "Assertions"),
                   ("notation.html", "Notation"), ("bibliography.html", "Bibliography"),
                   ("chronology.html", "Chronology"), ("figures.html", "Figures"),
                   ("open.html", "What is not known"), ("checks.html", "How it is checked"),
                   ("sections.html", "Sections"), ("all.html", "Single file")]
    idx = "".join(f'<li><a href="{href}"{" class=\"active\"" if href.split(".")[0] == active else ""}>{label}</a></li>'
                  for href, label in index_items)
    return f"""<a class="brand" href="index.html">Hierarchical RG<span>renormalisation on hierarchical lattices</span></a>
<form class="search" onsubmit="return false"><input id="q" type="search" placeholder="search  (press /)" aria-label="search the wiki"></form>
<ul class="search-results" id="results"></ul>
{''.join(blocks)}
<nav class="sec" aria-label="reading maps"><h2>Reading maps</h2><ul>{''.join(mitems)}</ul></nav>
<nav class="sec" aria-label="index"><h2>Index</h2><ul>{idx}</ul></nav>"""


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

    notation = load_notation(articles)
    symbols_of: dict[str, list[tuple[int, str]]] = {}
    for i, (obj, _symbol, aid, users) in enumerate(notation["rows"]):
        for name in [aid] + users:
            symbols_of.setdefault(name, []).append((i, obj))

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
            if name not in simulate.SIM_NOTES:
                sys.exit(f"{aid}: no interactive figure named {name!r}; the registered ones are {sorted(simulate.SIM_NOTES)}")
            title = m.group(2) or ""
            return (f'<div class="sim" data-sim="{name}">'
                    f'<div class="sim-title">{title}</div></div>')
        body = SIM_RE.sub(sim_slot, body)

        def fig_slot(match):
            name, title = match.group(1), match.group(2) or ""
            if name not in figs:
                sys.exit(f"{aid}: no figure named {name!r}; the figures are {sorted(figs)}")
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
        src_items = [src for src in catalog if src["id"] in set(meta.get("sourceIds", []))]
        sources_line = (
            '<p class="meta">Sources: '
            + ", ".join(f'<a href="bibliography.html#work-{src["id"]}">{src["shortName"]}, {src["year"]}</a>'
                        for src in src_items)
            + '.</p>') if src_items else ""
        strip_items = symbols_of.get(aid, [])
        notation_strip = (
            '<p class="meta">Notation in this article: '
            + ", ".join(f'<a href="notation.html#sym-{i + 1}">{obj}</a>' for i, obj in strip_items)
            + '.</p>') if strip_items else ""
        inner = f"""<p class="crumbs"><a href="index.html">Home</a> /
<a href="part-{part['id']}.html">{part['title']}</a> / {meta['title']}</p>
<h1>{meta['title']}</h1>
<p class="subtitle">{meta['subtitle']}</p>
<p class="meta">{meta['kind']} &middot; part {parts.index(part) + 1} &middot; {len(heads)} sections &middot;
{n_assert} tagged assertions &middot; <span class="tag">{aid}</span></p>
{lead}
<details class="toc" open><summary>On this page</summary><ol>{toc}</ol></details>
{rest}
{sources_line}
{linked_html}
{notation_strip}
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

    # ---- what is not known
    open_items = [
        ("Is the amplitude of the growth certified?", "critical-exponents-from-rg",
         "The exponent is <code>&alpha;</code> at criticality: the upper bound from the runaway argument, the lower "
         "one from the divergence of the susceptibility. What is not proved is the amplitude — that the normalised "
         "variance stays bounded away from zero — which needs a pointwise upper bound on the two-point function at "
         "criticality, a theorem for the percolation class on the same lattice and not for the spin model."),
        ("Is the threshold a matter of monotonicity?", "hierarchical-magnetised-phase",
         "FKG gives the architecture of the phase diagram and one nearly empty bound on the order parameter; the "
         "location of the threshold is the trichotomy's, which is external."),
        ("What does the free energy do at the Ising transition?", "hierarchical-free-energy",
         "The Gaussian case is computed in closed form, including the divergence of the curvature. For Ising spins no "
         "per-scale term is elementary and the curvature is computed nowhere."),
        ("Is the correlation-length exponent known in closed form?", "bleher-sinai-fixed-point",
         "The value is read off the leading eigenvalue of the linearisation; the eigenvalue is known through the "
         "expansion in the distance from the marginal exponent, not in closed form."),
        ("Can the logarithms at the upper critical dimension be got right everywhere?", "hierarchical-cluster-volume",
         "The volume exponent is known in every regime, including the order of the polylogarithmic correction at "
         "<code>d = 3&alpha;</code>, and that correction disagrees with the one predicted for the Euclidean model; what "
         "is not known is the corresponding statement for long-range percolation on <code>Z<sup>d</sup></code>."),
        ("What is &nu; for percolation above the triangle threshold?", "hierarchical-percolation-rg",
         "Below it the classical values hold and the two-point bound pins the exponents; above it the percolation "
         "analysis determines everything except the correlation-length exponent."),
        ("Which criterion holds at the marginal exponent for the scalar model?", "hierarchical-two-marginalities",
         "Bleher and Major decide the marginal exponent for the vector model and the percolation model has no "
         "transition there at all; for the scalar spin model this wiki records no criterion."),
        ("Is there an exact renormalisation group on the Euclidean lattice?", "hierarchical-and-euclidean-rg",
         "The decimation step produces interactions that depend on the shape of the boundary between blocks, so the "
         "recursion is no longer on one variable; the comparison article says what fails."),
    ]
    items = "".join(f'<li><strong>{title}</strong> &mdash; {text} See '
                    f'<a href="{aid}.html">{articles[aid]["title"]}</a>.</li>'
                    for title, aid, text in open_items)
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / What is not known</p>
<h1>What is not known</h1>
<p class="meta">{len(open_items)} open questions</p>
<p>A wiki that attributes its theorems should be as explicit about what it does not prove. This page
collects the places where the argument stops short of the statement, with the reason and the
article where the gap sits. Every item is either a question the wiki leaves open or a claim it
carries only on someone else's authority, and the distinction is made in the text of the articles
themselves, with the tags and the small print.</p>
<ol class="paths">{items}</ol>
<p>The other direction is worth stating too. Everything marked as a theorem, proposition or corollary
in the <a href="assertions.html">assertions index</a> is proved in the article that carries it, with
the hypotheses in the running text; the attributions are to works, not to theorem numbers, and the
<a href="figures.html">figures page</a> says which of the computations are checked by a script.</p>"""
    (out / "open.html").write_text(
        page_shell("What is not known — Hierarchical RG", "The open questions, and where they sit.",
                   inner, "open"))

    # ---- how it is checked
    checks = [
        ("<code>check_wiki.py</code>", "the sources",
         "front matter, the section structure, the tag ledger, internal links and section fragments, "
         "citation keys, the reading maps and the partition of the articles into parts"),
        ("<code>preview.py</code>", "the site",
         "builds the site from the sources, and refuses an unknown figure or simulation name rather than "
         "silently dropping it"),
        ("<code>check_site.py</code>", "the links",
         "every local <code>href</code>, <code>src</code> and stylesheet <code>url()</code> in the built "
         "site, including fragments"),
        ("<code>test_math.py</code>", "the formulas",
         "renders every formula through KaTeX with errors fatal, so an unsupported macro fails the build "
         "instead of a reader's page"),
        ("<code>test_sim.py</code>", "the browser code",
         "loads the simulation script in quickjs and compares it against the Python reference, bit for "
         "bit where the arithmetic is deterministic"),
        ("<code>numeric_checks.py</code>", "the displayed identities",
         "assertions of the articles against direct computation on finite blocks: eigenvalues, "
         "thresholds, sums, laws and bounds"),
        ("<code>preview.py --check</code>", "the commit",
         "the site in the repository is exactly what the sources build to, so a stale page cannot be "
         "published"),
    ]
    rows = "".join(f"<tr><td>{tool}</td><td>{what}</td><td>{detail}</td></tr>" for tool, what, detail in checks)
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / How it is checked</p>
<h1>How this wiki is checked</h1>
<p class="meta">seven checks, all of them cheap enough to run on every change</p>
<p>A claim is worth what its checks are worth, so here is what is checked and with what. The scripts
are in the repository under <code>tools/</code>; none of them needs the network, and the site build
itself needs only the Python standard library.</p>
<table><thead><tr><th>Script</th><th>Checks</th><th>What that means</th></tr></thead>
<tbody>{rows}</tbody></table>
<p>Two limits are worth stating. The checks establish that the statements are internally consistent
with the computations and that the site is well formed; they do not establish that a proof is
correct, which is a reader's job. And nothing here renders a page in a browser: the formulas are
checked through KaTeX and the browser code through quickjs, but how a page looks is not verified by
any script.</p>"""
    (out / "checks.html").write_text(
        page_shell("How it is checked — Hierarchical RG", "The checks, and what they do not cover.",
                   inner, "checks"))

    # ---- bibliography
    by_id = {s["id"]: s for s in catalog}
    brow = []
    for source in catalog:
        users = cited_in.get(source["id"], [])
        links = ", ".join(f'<a href="{a}.html">{articles[a]["title"]}</a>' for a in users) or "&mdash;"
        zbl = f'<a href="{source["zblUrl"]}">{source["zbl"]}</a>' if source.get("zbl") else "—"
        brow.append(f'<tr id="work-{source["id"]}"><td>{source["shortName"]}</td>'
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

    # ---- figures and simulations
    def shown_in(marker):
        users = [a for a in order if f'{marker}="' in articles[a]["body"]]
        return ", ".join(f'<a href="{a}.html">{articles[a]["title"]}</a>' for a in users) or "&mdash;"

    fcards = []
    for name, svg in figs.items():
        note, checked = simulate.FIGURE_NOTES.get(name, ("", ""))
        fcards.append(f"""<div class="card part"><span class="kind">figure</span>
<h3><span class="tag">{name}</span></h3>
<p>{note}</p>
<div class="fig">{svg}</div>
<p class="meta">shown in {shown_in("data-fig=\"" + name)}<br>checked by: {checked}</p></div>""")
    scards = []
    for name in simulate.SIM_NOTES:
        note, checked = simulate.SIM_NOTES[name]
        scards.append(f"""<div class="card part"><span class="kind">interactive</span>
<h3><span class="tag">{name}</span></h3>
<p>{note}</p>
<p class="meta">shown in {shown_in("data-sim=\"" + name)}<br>checked by: {checked}</p></div>""")
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Figures</p>
<h1>Figures and simulations</h1>
<p class="meta">{len(figs)} generated figures, {len(simulate.SIM_NOTES)} interactive ones</p>
<p>Every figure and every interactive panel in the wiki, with what it computes, the articles that
show it, and what checks that the computation is right. The distinction in the last line is the one
this wiki cares about: a figure computed from the model can be checked by a script, and a schematic
cannot. The schematics are labelled as such rather than dressed up, and the rest say which test
would catch them being wrong.</p>
<h2>Generated figures</h2>
<div class="cards">{''.join(fcards)}</div>
<h2>Interactive figures</h2>
<div class="cards">{''.join(scards)}</div>"""
    (out / "figures.html").write_text(
        page_shell("Figures — Hierarchical RG", "Every figure and simulation, and what checks it.",
                   inner, "figures"))
    search_entries.append({"url": "figures.html", "title": "Figures and simulations",
                           "subtitle": f"{len(figs)} figures, {len(simulate.SIM_NOTES)} interactive",
                           "summary": "", "text": "figures simulations " + " ".join(
                               [simulate.FIGURE_NOTES.get(n, ("", ""))[0] for n in figs] +
                               [v[0] for v in simulate.SIM_NOTES.values()])})

    # ---- chronology
    chrono = sorted(catalog, key=lambda src: (src["year"], src["shortName"]))
    yrows = []
    for src in chrono:
        users = cited_in.get(src["id"], [])
        where = ", ".join(f'<a href="{a}.html">{articles[a]["title"]}</a>'
                          for a in sorted(users, key=order.index)) or "&mdash;"
        if src.get("zbl"):
            ref = f'<a href="{src["zblUrl"]}">Zbl {src["zbl"]}</a>'
        elif src.get("url"):
            ref = f'<a href="{src["url"]}">doi</a>'
        else:
            ref = "&mdash;"
        yrows.append(f'<tr><td class="num">{src["year"]}</td>'
                     f'<td>{src["shortName"]}, <em>{src["title"]}</em></td>'
                     f'<td>{ref}</td><td>{where}</td></tr>')
    years = sorted({src["year"] for src in catalog})
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Chronology</p>
<h1>Chronology</h1>
<p class="meta">{len(catalog)} works, {years[0]}&ndash;{years[-1]}</p>
<p>The works of the catalogue in the order they appeared, with the articles that cite each. The
bibliography answers the question "what is this work and where is it used"; this page answers the
other one, which is what was available at each stage of the subject. The layers are visible: the
model and its first analysis in the 1960s and 1970s, the correlation inequalities alongside them,
the renormalisation-group analysis of the hierarchical model in the 1980s, and the percolation
results of the last decade.</p>
<table><thead><tr><th>Year</th><th>Work</th><th>Record</th><th>Cited in</th></tr></thead>
<tbody>{''.join(yrows)}</tbody></table>"""
    (out / "chronology.html").write_text(
        page_shell("Chronology — Hierarchical RG", "The works of the wiki in the order they appeared.",
                   inner, "chronology"))
    search_entries.append({"url": "chronology.html", "title": "Chronology",
                           "subtitle": f"{len(catalog)} works in order",
                           "summary": "", "text": "chronology " + " ".join(
                               f"{src['year']} {src['author']} {src['title']}" for src in chrono)})

    # ---- notation
    def also_cell(users):
        return ", ".join(f'<a href="{u}.html">{articles[u]["title"]}</a>' for u in users) or "&mdash;"

    nrows = "".join(
        f'<tr id="sym-{i + 1}"><td>{symbol}</td><td>{obj}</td>'
        f'<td><a href="{aid}.html">{articles[aid]["title"]}</a></td>'
        f'<td>{also_cell(users)}</td></tr>'
        for i, (obj, symbol, aid, users) in enumerate(notation["rows"]))
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Notation</p>
<h1>Notation</h1>
<p class="meta">{len(notation["rows"])} symbols, one per object; each row is the target of the
notation line at the foot of the articles that use it</p>
{notation["lead"]}
<table><thead><tr><th>Symbol</th><th>Object</th><th>Introduced in</th><th>Also used in</th></tr></thead>
<tbody>{nrows}</tbody></table>
{notation["note"]}"""
    (out / "notation.html").write_text(
        page_shell("Notation — Hierarchical RG", "One symbol per object, and where each is introduced.",
                   inner, "notation"))
    search_entries.append({"url": "notation.html", "title": "Notation",
                           "subtitle": f"{len(notation['rows'])} symbols", "summary": "",
                           "text": " ".join(f"{obj} {articles[aid]['title']} "
                                            + " ".join(articles[u]["title"] for u in users)
                                            for obj, _symbol, aid, users in notation["rows"])})

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
names the article that introduces it; the <a href="chronology.html">chronology</a> puts the cited
works in the order they appeared; and the reading maps — for
<a href="source-bleher-major-sinai.html">Bleher, Major and Sinai</a>,
<a href="source-gawedzki-kupiainen.html">Gawedzki and Kupiainen</a>,
<a href="source-koch-wittwer.html">Koch and Wittwer</a>,
<a href="source-bauerschmidt-brydges-slade.html">Bauerschmidt, Brydges and Slade</a> and
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
    appendix = "".join(
        f'<tr><td>{symbol}</td><td>{obj}</td>'
        f'<td>{articles[aid]["title"]}</td></tr>'
        for obj, symbol, aid, _users in notation["rows"])
    inner = inner.replace(
        '<section class="whole" id="whole-', '<section class="whole" id="whole-', 1)
    inner += (f'<section class="whole" id="whole-notation"><h1>Notation</h1>'
              f'<p class="subtitle">One symbol per object, with the article that introduces it.</p>'
              f'<table><thead><tr><th>Symbol</th><th>Object</th><th>Introduced in</th></tr></thead>'
              f'<tbody>{appendix}</tbody></table></section>')
    (out / "all.html").write_text(
        page_shell("Hierarchical RG — single file", "The whole wiki in one page, with the notation.",
                   inner, "all"))
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
<li><a href="chronology.html">Chronology</a> <span class="meta">— the same works in the order they appeared</span></li>
<li><a href="figures.html">Figures</a> <span class="meta">— every figure and simulation, with what checks it</span></li>
<li><a href="all.html">Single file</a> <span class="meta">— the whole wiki in one page, for printing</span></li>
</ol>"""
    (out / "index.html").write_text(
        page_shell("Hierarchical RG — a wiki on the renormalisation group",
                   "A wiki on the renormalisation group on hierarchical lattices.", inner, "index"))

    # ---- sections index
    rows = []
    for aid in order:
        heads = re.findall(r'<h2 id="(section-[a-z0-9-]+)">(.*?)<a class="anchor"', rendered[aid])
        if not heads:
            continue
        items = "".join(f'<li><a href="{aid}.html#{sid}">{title}</a></li>' for sid, title in heads)
        rows.append(f'<h3><a href="{aid}.html">{articles[aid]["title"]}</a></h3><ol>{items}</ol>')
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Sections</p>
<h1>Every section</h1>
<p class="meta">{len(order)} articles, {sum(len(re.findall(r'<h2 id="section-', rendered[a])) for a in order)} sections</p>
<p>The tree of the wiki in one page: every article with its sections, for a reader who remembers a
heading and not where it lives. The <a href="assertions.html">assertions index</a> serves the same
purpose for statements and the <a href="all.html">single file</a> for reading end to end.</p>
{''.join(rows)}"""
    (out / "sections.html").write_text(
        page_shell("Every section — Hierarchical RG", "The tree of the wiki.", inner, "sections"))

    # ---- site-level files
    urls = "".join(f"<url><loc>{SITE_URL}{path.name}</loc></url>" for path in sorted(out.glob("*.html"))
                    if path.name != "404.html")
    (out / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>\n")
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n")
    inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Not found</p>
<h1>Not found</h1>
<p class="meta">404</p>
<p>There is no page at this address. The wiki is a flat set of pages with no server behind them, so
a link that points at a misspelling points at nothing.</p>
<p>Start from <a href="start.html">the argument</a>, look something up in the
<a href="assertions.html">assertions index</a> or the <a href="notation.html">notation page</a>, or
use the search box above: it matches titles, subtitles and the text of every page.</p>
<p>Every page of the wiki is listed on the <a href="index.html">home page</a>.</p>"""
    (out / "404.html").write_text(
        page_shell("Not found — Hierarchical RG", "No page at this address.", inner, "404"))

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
