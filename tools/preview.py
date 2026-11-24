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
DEFAULT_OUT = ROOT / "site"

# Reading order of the articles, from the lattice to the comparison.
ORDER = [
    "hierarchical-lattice",
    "hierarchical-gibbs-measure",
    "renormalisation-group-map",
    "gaussian-renormalisation-group",
    "critical-exponents-from-rg",
    "bleher-sinai-fixed-point",
    "hierarchical-vector-models",
    "hierarchical-phi4-truncations",
    "koch-wittwer-fixed-point",
    "abdesselam-global-trajectory",
    "hierarchical-percolation-rg",
    "hierarchical-and-euclidean-rg",
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


def load_maps():
    out = []
    if not SOURCES.is_dir():
        return out
    for path in sorted(SOURCES.glob("*.md")):
        text = path.read_text().strip("\n")
        title = text.splitlines()[0][2:].strip()
        out.append({"slug": path.stem, "title": title, "body": "\n".join(text.splitlines()[1:]).strip()})
    return out


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


def sidebar(articles, order, maps, active: str) -> str:
    items = []
    for n, aid in enumerate(order, start=1):
        cls = ' class="active"' if aid == active else ""
        items.append(f'<li><span class="num">{n}</span><a href="{aid}.html"{cls}>{articles[aid]["title"]}</a></li>')
    mitems = []
    for m in maps:
        cls = ' class="active"' if "source-" + m["slug"] == active else ""
        mitems.append(f'<li><a href="source-{m["slug"]}.html"{cls}>{m["title"].split(":")[0]}</a></li>')
    return f"""<a class="brand" href="index.html">Hierarchical RG<span>renormalisation on hierarchical lattices</span></a>
<form class="search" onsubmit="return false"><input id="q" type="search" placeholder="search  (press /)" aria-label="search the wiki"></form>
<ul class="search-results" id="results"></ul>
<nav class="sec"><h2>Articles</h2><ol>{''.join(items)}</ol></nav>
<nav class="sec"><h2>Reading maps</h2><ul>{''.join(mitems)}</ul></nav>
<nav class="sec"><h2>On this site</h2><ul>
<li><a href="index.html">Home</a></li>
<li><a href="index.html#bibliography">Bibliography</a></li>
</ul></nav>"""


# ------------------------------------------------------------------ builders

def build(out: Path) -> dict:
    articles, order = load_articles()
    maps = load_maps()
    catalog = json.loads(CATALOG.read_text())["sources"]
    by_id = {s["id"]: s for s in catalog}

    tag_owner = {}
    for aid, meta in articles.items():
        for m in ANCHOR_RE.finditer(meta["body"]):
            tag_owner[m.group(1)] = aid

    out.mkdir(parents=True, exist_ok=True)
    sim_data = simulate.build()
    figs = simulate.figures()
    used_sims: dict[str, dict] = {}
    search_entries = []

    # ---- articles
    for aid in order:
        meta = articles[aid]
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
        prev_link = (f'<a href="{order[n-1]}.html"><span class="dir">previous</span>{articles[order[n-1]]["title"]}</a>'
                     if n > 0 else "<span></span>")
        next_link = (f'<a href="{order[n+1]}.html"><span class="dir">next</span>{articles[order[n+1]]["title"]}</a>'
                     if n + 1 < len(order) else "<span></span>")
        lead, sep, rest = body.partition("<h2")
        rest = sep + rest if sep else ""
        inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Articles / {meta['title']}</p>
<h1>{meta['title']}</h1>
<p class="subtitle">{meta['subtitle']}</p>
<p class="meta">{meta['kind']} &middot; {meta['category']} &middot; {len(heads)} sections &middot;
{n_assert} tagged assertions &middot; <span class="tag">{aid}</span></p>
{lead}
<details class="toc" open><summary>On this page</summary><ol>{toc}</ol></details>
{rest}
<div class="pager">{prev_link}{next_link}</div>
<a class="top" href="#">back to top</a>"""
        (out / f"{aid}.html").write_text(
            shell(f"{meta['title']} — Hierarchical RG", meta["summary"], inner,
                  sidebar(articles, order, maps, aid)))
        search_entries.append({"url": f"{aid}.html", "title": meta["title"], "subtitle": meta["subtitle"],
                               "summary": meta["summary"], "text": strip_html(body)[:4000]})

    # ---- reading maps
    for m in maps:
        page = "source-" + m["slug"]
        inner = f"""<p class="crumbs"><a href="index.html">Home</a> / Reading maps / {html.escape(m['title'])}</p>
<h1>{html.escape(m['title'])}</h1>
<p class="meta">reading map &middot; <span class="tag">{page}</span></p>
{map_body_to_html(m['body'])}
<div class="pager"><a href="index.html"><span class="dir">back</span>Home</a><span></span></div>"""
        (out / f"{page}.html").write_text(
            shell(f"{m['title']} — Hierarchical RG", "A reading map for the wiki.", inner,
                  sidebar(articles, order, maps, page)))
        search_entries.append({"url": f"{page}.html", "title": m["title"], "subtitle": "reading map",
                               "summary": "", "text": strip_html(map_body_to_html(m["body"]))[:4000]})

    # ---- home
    cards = []
    for n, aid in enumerate(order, start=1):
        meta = articles[aid]
        cards.append(f"""<div class="card"><span class="kind">{meta['kind']} · {meta['category']}</span>
<h3><a href="{aid}.html">{meta['title']}</a></h3>
<p class="sub">{meta['subtitle']}</p>
<p class="sum">{meta['summary']}</p></div>""")
    map_cards = "".join(f'<li><a href="source-{m["slug"]}.html">{html.escape(m["title"])}</a></li>' for m in maps)
    def bib_row(source):
        zbl = f'<a href="{source["zblUrl"]}">{source["zbl"]}</a>' if source.get("zbl") else "—"
        return (f'<tr><td>{source["shortName"]}</td>'
                f'<td>{source["title"]}<br><span class="meta">{source["edition"]}</span></td>'
                f'<td class="num">{zbl}</td></tr>')

    bib = "".join(bib_row(source) for source in catalog)
    inner = f"""<h1>Hierarchical RG</h1>
<p class="subtitle">Twelve articles on the block-spin transformation, its exact recursion, its fixed points and their exponents.</p>
<p>The renormalisation group is exact on a hierarchical lattice: a block has no boundary, every
pair between two children carries one coupling, and one decimation step is an operation on the law
of a single number. This wiki develops that structure — the lattice, the recursion, the fixed
points, the exponents, the literature — with complete proofs where they are short and precise
attribution where they are not. Each article has a simulation or a worked computation attached
where one is illuminating.</p>
<h2 id="articles">The articles</h2>
<div class="cards">{''.join(cards)}</div>
<h2 id="maps">Reading maps</h2>
<p>One finding aid per group of works: what each paper establishes and where the wiki uses it.</p>
<ul>{map_cards}</ul>
<h2 id="bibliography">Bibliography</h2>
<p>{len(catalog)} works, with the zbMATH record where one exists.</p>
<table><thead><tr><th>Author</th><th>Work</th><th>Zbl</th></tr></thead><tbody>{bib}</tbody></table>"""
    (out / "index.html").write_text(
        shell("Hierarchical RG — a wiki on the renormalisation group", "A wiki on the renormalisation group on hierarchical lattices.",
              inner, sidebar(articles, order, maps, "index")))

    # ---- search index, simulation data, assets
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
            "sims": sorted(used_sims), "sources": len(catalog)}


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
