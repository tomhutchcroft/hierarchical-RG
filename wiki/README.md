# This wiki

This wiki treats the renormalisation group on hierarchical lattices: the block-spin
transformation, the exact recursion it satisfies there, the fixed points of that recursion, and
the exponents read off from them. It is eight articles and they are meant to be read in order,
though each stands alone.

The prose style is the PercLib wiki's
[style sheet](https://github.com/tomhutchcroft/perclib/blob/main/wiki/STYLE.md); the local
conventions and notation are in [STYLE.md](STYLE.md). The file format is PercLib's, described
below, so an article here can be moved there without conversion.

## Layout

```
wiki/
  STYLE.md               house style and notation
  README.md              this file
  articles/<id>.md       one article per file; the filename is the article id
  sources/<slug>.md      reading maps: a group of works and where the wiki uses them
  tags.json              the permanent ledger of assertion tags
  src/content/catalog.json   source catalogue (bibliography, by key)
tools/
  check_wiki.py          format, tag, link and citation checks
  preview.py             static preview of the articles
```

## File format

Front matter is JSON between `---` delimiters. It carries `id` (equal to the filename), `title`,
`subtitle`, `kind` (`definition`, `proposition`, `theorem`, `corollary` or `model`), `category`,
`summary`, `context` (an array of running notation and assumptions), `related` (article ids),
`sourceIds` (catalogue keys), and `aliases` (phrases search should match).

Then comes the lead: one to three paragraphs of bare text or `<p>…</p>`, separated by blank
lines, before the first heading.

Sections are introduced by `## Heading {#section-id}` and separated by blank lines; the file
ends with one newline. Section bodies keep their HTML, valid inside Markdown. Mathematics is
`$…$` inline and `<div class="math-display">$$…$$</div>` for a display.

An assertion anchor immediately precedes the statement it makes citable:

```html
<a id="tag-0A3F" data-assertion="theorem" data-title="Short assertion title"></a>
```

The four-character tag is reserved in `tags.json` before use and is never reused: to withdraw an
assertion, delete its anchor and mark the ledger entry `withdrawn`. A tag identifies a citable
statement, not every displayed calculation.

Collapsible blocks hold proofs and long computations:

```html
<p>Idea of the proof, visible by default.</p>
:::details Proof of the lower bound
<p>Every step of the proof.</p>
:::
```

The text after `:::details` is the summary and is mandatory. Nest by giving the outer fence more
colons. A link to an anchor inside a collapsed block opens it.

Links are `/articles/<id>/` for an article and `/tag/XXXX/` for an assertion, on the natural
phrase. A term whose article does not exist yet may be marked `<a data-wanted="id">phrase</a>`.
Citations are `[@key]` or `[@key, locator]`, resolved through the catalogue.

## Reading maps

`wiki/sources/<slug>.md` is a finding aid for a group of works: a title, a few paragraphs on what
the group did, a table with one row per work (what it establishes, where the wiki uses it), and a
statement of what is deliberately outside the map. The format is the PercLib reading-map format
and is deliberately small: `#` title, `##`/`###` headings, paragraphs, `https://` links, links to
articles of the form `/articles/<id>/` (optionally with a `#section-…` fragment), and simple pipe
tables. No raw HTML and no collapsibles. A map is a finding aid, not a claim of locator-level
accuracy: the wiki cites works by work, not by theorem number, unless a statement is quoted from
an abstract.

Current maps: `bleher-major-sinai.md`, `koch-wittwer.md` and `abdesselam.md`.

Catalogue entries carry a `zbl` field and its `zblUrl` where zbMATH Open has a record; the home
page of the site lists them. A work with no record shows a dash rather than a guessed number.

## Publishing

The site is built into `site/` and **committed**, because GitHub Pages publishing from the
branch is what a repository gets by default and it serves only what is in the tree. The root has
an `index.html` that redirects to `site/` and a `.nojekyll` file that stops Jekyll from
converting the sources to pages of its own. With *Settings -> Pages -> Deploy from a branch*,
branch `main`, folder `/`, the wiki is served at `<owner>.github.io/<repository>/`.

`.github/workflows/pages.yml` is the alternative, and is the better one once enabled: it runs
the checks, verifies that the committed `site/` is current (`preview.py --check`), and deploys
`site/` as the Pages artifact. Enable it with *Settings -> Pages -> Source: GitHub Actions*. Both
routes serve the same files, so switching does not change the site.

If `site/` is stale, both `preview.py --check` and the workflow fail; rebuild with
`python3 tools/preview.py` and commit.

Mathematics is rendered by the vendored KaTeX in `wiki/static/katex`, so pages need no network,
no CDN and no build-time TeX. The figures are two kinds: static SVG diagrams generated by
`tools/simulate.py`, and interactive simulations whose arithmetic lives in `wiki/static/sim.js`
and is tested by `tools/test_sim.py` against the Python reference in the same file.

## Checks

```sh
python3 tools/check_wiki.py          # front matter, sections, tags, links, citations, fences
python3 tools/check_wiki.py --strict # treat warnings (unused tags, plain-text citations) as failures
python3 tools/new_tag.py 2           # reserve assertion tags before using them
python3 tools/numeric_checks.py      # the displayed identities, on finite blocks
python3 tools/preview.py             # build site/ from the sources
python3 tools/check_site.py          # every local link, fragment and asset in site/
python3 tools/preview.py --check     # fail if site/ is not what the sources build to
python3 tools/test_sim.py            # the browser simulation code, in quickjs
```

The checker is a format check, not a mathematical one. It verifies that every tag is in the
ledger and used once, that every internal link resolves, that every citation key is in the
catalogue, that collapsible fences balance, and that the lead obeys its paragraph limit. The
PercLib build additionally renders mathematics at build time and joins compiled evidence; this
wiki has no Lean library behind it, so the formal-verification panels of the PercLib articles
have no counterpart here.
