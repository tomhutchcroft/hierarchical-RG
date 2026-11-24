#!/usr/bin/env python3
"""Format, tag, link and citation checks for the wiki.

Usage: python3 tools/check_wiki.py [--strict]

Checks, in the manner of the PercLib wiki's build checks:
  * front matter is JSON, has the required keys, and its id matches the filename;
  * the lead has one to three paragraphs and no heading, anchor or collapsible block;
  * section headings have unique ids and bodies are separated by blank lines;
  * every assertion anchor has a four-character tag reserved in tags.json, a known kind,
    and is used exactly once;
  * collapsible fences balance, and each opens with a summary;
  * every internal link resolves (article, section fragment, assertion tag);
  * every citation key is in the source catalogue;
  * dollar signs are balanced in every paragraph and display.

The checks are structural: they do not verify the mathematics.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
ARTICLES = WIKI / "articles"
CATALOG = WIKI / "src" / "content" / "catalog.json"
LEDGER = WIKI / "tags.json"
SOURCES = WIKI / "sources"

KINDS = {"definition", "proposition", "theorem", "corollary", "model"}
REQUIRED = ["id", "title", "subtitle", "kind", "category", "summary", "context", "related", "sourceIds"]
TAG_RE = re.compile(r"^[0-9A-Z]{4}$")
ANCHOR_RE = re.compile(r'<a\s+id="tag-([0-9A-Z]{4})"\s+data-assertion="([a-z]+)"\s+data-title="([^"]+)"\s*></a>')
HEAD_RE = re.compile(r"^## (.+?) \{#(section-[a-z0-9-]+)\}\s*$")
LINK_RE = re.compile(r'href="(/articles/[^"#]*?/)(?:#(section-[a-z0-9-]+))?"')
TAGLINK_RE = re.compile(r'href="/tag/([0-9A-Z]{4})/"')
WANTED_RE = re.compile(r'<a\s+data-wanted="([a-z0-9-]+)"')
CITE_RE = re.compile(r"\[@([^\]\[]+)\]")

errors: list[str] = []
warnings: list[str] = []


def fail(where: str, msg: str) -> None:
    errors.append(f"{where}: {msg}")


def warn(where: str, msg: str) -> None:
    warnings.append(f"{where}: {msg}")


def split_front_matter(text: str, where: str):
    if not text.startswith("---\n"):
        fail(where, "does not start with front matter ---")
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        fail(where, "front matter is not closed by ---")
        return None, text
    raw = text[4:end]
    try:
        meta = json.loads(raw)
    except json.JSONDecodeError as exc:
        fail(where, f"front matter is not JSON: {exc}")
        return None, text[end + 5:]
    return meta, text[end + 5:]


def check_math(where: str, body: str) -> None:
    for i, block in enumerate(re.split(r"\n\s*\n", body)):
        if block.lstrip().startswith("::::") or block.lstrip().startswith(":::"):
            continue
        n = block.count("$") - 2 * block.count("$$") - block.count("\\$")
        if n % 2:
            fail(where, f"paragraph {i + 1}: odd number of $ delimiters")
        if re.search(r"\\\(|\\\[", block):
            fail(where, f"paragraph {i + 1}: uses \\( or \\[ delimiters")


def check_fences(where: str, body: str) -> None:
    stack: list[int] = []
    for lineno, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith(":"):
            continue
        m = re.match(r"^(:{3,})\s*(.*)$", stripped)
        if not m:
            continue
        colons, rest = len(m.group(1)), m.group(2).strip()
        if rest.startswith("details"):
            summary = rest[len("details"):].strip()
            if not summary:
                fail(where, f"line {lineno}: :::details without a summary")
            stack.append(colons)
        elif rest == "":
            if not stack:
                fail(where, f"line {lineno}: closing fence without an opening fence")
            else:
                if colons != stack[-1]:
                    fail(where, f"line {lineno}: closing fence has {colons} colons, expected {stack[-1]}")
                stack.pop()
        else:
            fail(where, f"line {lineno}: unknown collapsible directive {rest!r}")
    if stack:
        fail(where, f"{len(stack)} unclosed collapsible block(s)")


def check_lead(where: str, lead: str) -> None:
    if not lead.strip():
        fail(where, "no lead before the first section")
        return
    if ":::" in lead:
        fail(where, "lead contains a collapsible block")
    if "<a id=" in lead or "<h1" in lead or "<h2" in lead or "<h3" in lead:
        fail(where, "lead contains an anchor or a heading element")
    if re.search(r"^#+\s", lead, re.M):
        fail(where, "lead contains a heading")
    paragraphs = [p for p in re.split(r"\n\s*\n", lead.strip()) if p.strip()]
    if len(paragraphs) > 3:
        fail(where, f"lead has {len(paragraphs)} paragraphs, the limit is 3")


def check_maps(articles: dict[str, list[str]]) -> None:
    """Reading maps: a title, headings, paragraphs, https links, article links, pipe tables."""
    files = sorted(SOURCES.glob("*.md")) if SOURCES.is_dir() else []
    for path in files:
        where = f"sources/{path.name}"
        lines = path.read_text().splitlines()
        if not lines or not lines[0].startswith("# ") or lines[0].startswith("## "):
            fail(where, "does not start with a single '# ' title")
            continue
        if sum(1 for l in lines if l.startswith("# ") and not l.startswith("## ")) != 1:
            fail(where, "has more than one '# ' title")
        if ":::" in path.read_text():
            fail(where, "contains a collapsible block")
        for i, line in enumerate(lines, start=1):
            if line.startswith("####"):
                fail(where, f"line {i}: heading deeper than ###")
            if "<" in line or ">" in line:
                fail(where, f"line {i}: raw HTML; reading maps are plain Markdown")
        text = path.read_text()
        if (text.count("$") - 2 * text.count("$$")) % 2:
            fail(where, "unbalanced $ delimiters")
        for m in re.finditer(r"\]\((.*?)\)", text):
            target = m.group(1)
            if target.startswith("https://"):
                continue
            am = re.fullmatch(r"/articles/([a-z0-9-]+)/(?:#(section-[a-z0-9-]+))?", target)
            if not am:
                fail(where, f"link target {target!r} is neither https nor an article link")
            elif am.group(1) not in articles:
                fail(where, f"link to unknown article {am.group(1)!r}")
            elif am.group(2) and am.group(2) not in articles[am.group(1)]:
                fail(where, f"link to unknown section {am.group(1)}#{am.group(2)}")
        if not re.search(r"\]\(/articles/", text):
            fail(where, "no link into the wiki")
        # pipe tables: consistent column count per block
        block = []
        for i, line in enumerate(lines, start=1):
            if line.startswith("|"):
                block.append((i, line))
            else:
                if len(block) >= 2:
                    width = block[0][1].count("|")
                    for j, row in block:
                        if row.count("|") != width:
                            fail(where, f"line {j}: table row has {row.count('|') - 1} cells, header has {width - 1}")
                block = []
        if len(block) >= 2:
            width = block[0][1].count("|")
            for j, row in block:
                if row.count("|") != width:
                    fail(where, f"line {j}: table row has {row.count('|') - 1} cells, header has {width - 1}")
    if not files:
        warn("wiki/sources", "no reading maps")


def main() -> int:
    strict = "--strict" in sys.argv
    catalog = json.loads(CATALOG.read_text())
    keys = {s["id"] for s in catalog["sources"]}
    ledger = json.loads(LEDGER.read_text())
    reserved = {}
    for entry in ledger["tags"]:
        reserved[entry["tag"]] = entry["state"]

    files = sorted(ARTICLES.glob("*.md"))
    if not files:
        fail("wiki/articles", "no articles")
    meta_by_id = {}
    sections = {}
    anchors = {}
    bodies = {}

    for path in files:
        where = path.name
        text = path.read_text()
        meta, body = split_front_matter(text, where)
        if meta is None:
            continue
        for key in REQUIRED:
            if key not in meta:
                fail(where, f"front matter lacks {key!r}")
        aid = meta.get("id", "")
        if aid != path.stem:
            fail(where, f"id {aid!r} does not match the filename")
        if meta.get("kind") not in KINDS:
            fail(where, f"kind {meta.get('kind')!r} is not one of {sorted(KINDS)}")
        for src in meta.get("sourceIds", []):
            if src not in keys:
                fail(where, f"sourceId {src!r} is not in the catalogue")
        meta_by_id[aid] = meta
        bodies[aid] = body

        lines = body.splitlines()
        heads = [(i, HEAD_RE.match(l)) for i, l in enumerate(lines)]
        first = next((i for i, m in heads if m), None)
        lead = "\n".join(lines[:first]) if first is not None else body
        check_lead(where, lead)
        if first is None:
            fail(where, "no sections")
            continue
        check_fences(where, body)
        check_math(where, body)

        sec_ids = []
        for i, m in heads:
            if not m:
                if lines[i].startswith("## "):
                    fail(where, f"line {i + 1}: heading without a {{#section-...}} id")
                continue
            sid = m.group(2)
            if sid == "section-lead":
                fail(where, f"line {i + 1}: section id 'lead' is reserved")
            if sid in sec_ids:
                fail(where, f"line {i + 1}: repeated section id {sid!r}")
            sec_ids.append(sid)
        sections[aid] = sec_ids

        for m in ANCHOR_RE.finditer(body):
            tag, kind, title = m.group(1), m.group(2), m.group(3)
            if not TAG_RE.match(tag):
                fail(where, f"malformed tag {tag!r}")
            if kind not in KINDS:
                fail(where, f"tag {tag}: unknown assertion kind {kind!r}")
            if not title.strip():
                fail(where, f"tag {tag}: empty data-title")
            if tag in anchors:
                fail(where, f"tag {tag} is used twice (also in {anchors[tag][0]})")
            anchors[tag] = (where, kind, title)
            if reserved.get(tag) != "allocated":
                fail(where, f"tag {tag} is not reserved as allocated in tags.json")
        if body.count('<a id="tag-') != len(ANCHOR_RE.findall(body)):
            fail(where, "an assertion anchor does not have the required form")

    for aid, meta in meta_by_id.items():
        for rel in meta.get("related", []):
            if rel not in meta_by_id:
                fail(aid, f"related article {rel!r} does not exist")

    wanted: dict[str, list[str]] = {}
    for aid, body in bodies.items():
        where = aid
        for m in LINK_RE.finditer(body):
            target = m.group(1).strip("/").split("/")[-1]
            frag = m.group(2)
            if target not in meta_by_id:
                fail(where, f"link to unknown article {target!r}")
            elif frag and frag not in sections.get(target, []):
                fail(where, f"link to unknown section {target}#{frag}")
        for m in TAGLINK_RE.finditer(body):
            if m.group(1) not in anchors:
                fail(where, f"link to unknown assertion tag {m.group(1)}")
        for m in WANTED_RE.finditer(body):
            if m.group(1) in meta_by_id:
                warn(where, f"wanted article {m.group(1)!r} now exists")
        for m in CITE_RE.finditer(body):
            for part in m.group(1).split(";"):
                key = part.split(",")[0].strip()
                if key not in keys:
                    fail(where, f"citation key {key!r} is not in the catalogue")
        plain = re.findall(r"\[[A-Z][A-Za-z]+\d{2}[^\]]*\]", body)
        if plain:
            warn(where, f"plain-text citations {plain[:3]}")

    for aid, body in bodies.items():
        if not LINK_RE.search(body) and not TAGLINK_RE.search(body):
            warn(aid, "no inline link to another article or assertion")
        for m in re.finditer(r'<a href="/articles/([a-z0-9-]+)/', body):
            if m.group(1) == aid:
                warn(aid, "links to itself")

    check_maps(sections)

    unused = [t for t, s in reserved.items() if s == "allocated" and t not in anchors]
    if unused:
        warn("tags.json", f"{len(unused)} reserved tag(s) unused: {', '.join(sorted(unused))}")

    maps = len(list(SOURCES.glob("*.md"))) if SOURCES.is_dir() else 0
    print(f"articles: {len(meta_by_id)}   sections: {sum(len(v) for v in sections.values())}"
          f"   assertions: {len(anchors)}   reservations: {len(reserved)}   reading maps: {maps}")
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"FAIL  {e}")
    if errors:
        print(f"\n{len(errors)} failure(s)")
        return 1
    if strict and warnings:
        print(f"\n{len(warnings)} warning(s) treated as failures under --strict")
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
