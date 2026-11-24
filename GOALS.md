# Goals

The objective, what counts as done, and the work queued after it. Written so that a chat with no
memory of the last one can pick the project up: read this, then [README.md](README.md),
[wiki/README.md](wiki/README.md) and [wiki/STYLE.md](wiki/STYLE.md), then run the checks.

## The objective

A wiki, in the style and file format of the PercLib wiki, giving a detailed and honest treatment of
the renormalisation group on hierarchical lattices: the block structure that makes decimation exact,
the recursion on block-spin laws, the fixed points, the exponents and their corrections, the models
that are not scalar spins, and the literature that establishes each of it.

Two things distinguish it from a set of notes. Statements are proved where the proof is short
enough to be complete, and attributed — to the work that establishes them, by work and not by
theorem number — where it is not. And the whole thing is checked: format, tags, links, formulas,
the browser code, the displayed identities, and the built site, by scripts in `tools/`.

## Current state

Fourteen articles in three parts, three reading maps, 52 tagged assertions, six interactive
simulations and five generated diagrams, and a built site committed under `site/`. The checks below
pass. The site is live at `https://tomhutchcroft.github.io/hierarchical-RG/`, served from the
Actions artifact whose root is `site/`.

This section ages. Trust the checks and `git log`, not this paragraph.

## Acceptance criteria

Every item below must pass before work is called finished. They are cheap; run them all.

```sh
python3 tools/check_wiki.py     # front matter, sections, tag ledger, links, citations, reading maps, structure
python3 tools/preview.py        # build site/ from the sources
python3 tools/check_site.py     # every local link, fragment and asset in site/
python3 tools/test_math.py      # render every formula through KaTeX (needs quickjs)
python3 tools/test_sim.py       # browser simulation code against the Python reference (needs quickjs)
python3 tools/numeric_checks.py # displayed identities against finite-block computation (needs numpy)
python3 tools/preview.py --check # site/ is exactly what the sources build to
```

`pip install --user numpy quickjs` provides the two dependencies; the site build itself needs only
the Python standard library. Commit `site/` whenever the sources change: Pages serves it, and
`--check` fails when it is stale.

Beyond the scripts:

- **Every article is in exactly one part** of `wiki/structure.json`, and each part's introduction
  says what it adds to the one before. The checker enforces the first half; the second is editorial.
- **No claim is invented.** A theorem attributed to a paper must be that paper's, at the level of
  its published abstract or review. Numbers from zbMATH are looked up, never guessed; where no
  record was found, say so.
- **Notation is the wiki's**, from the table in `wiki/STYLE.md`, not per-article variants.
- **Nothing needs the network to read**: KaTeX is vendored in `wiki/static/katex/`.
- **The site is reachable from the front page**: `start.html` and the part hubs link every article,
  and `check_site.py` checks it.

## The queue

In order. Each item names what finishes it.

### 1. The volume of the critical cluster (percolation depth)

Part 3 promises the non-mean-field regime and delivers one article; this is the largest
intellectual gap.

- A new article `hierarchical-cluster-volumes`, in part `beyond-spins` after
  `hierarchical-percolation-rg`: the exponent `δ` defined by the tail of `|K_0|`; why the two-point
  function is *not* the hard object here (it is known for every `0 < α < d`) while the volume is;
  the obstruction giving `δ ≥ (d+α)/(d−α)` above the triangle threshold; and what is conjectured
  versus proved.
- Sources already in the catalogue: `hutchcroft-hierarchical-2021` (Corollary 1.5),
  `hutchcroft-2025-volumes`. Add nothing to the catalogue without a zbMATH or DOI record.
- Prove what can be proved from the two-point exponent and the block identities; state the rest as
  attributed theorems with the argument sketched, and say which part is sketch.
- Done when: the article exists with its own tags, `hierarchical-percolation-rg` links to it, the
  part's introduction mentions it, and every check passes.

### 2. Notation page

- Generate `notation.html` from the notation table in `wiki/STYLE.md` (it is already a pipe table),
  with each symbol linking to one article that uses it.
- Link it from the sidebar index and from `start.html`.
- Done when: the page lists every row of the table, the links resolve, and edits to `STYLE.md`
  change the page (the generator, not a copy).

### 3. Reading map for the percolation literature

- `wiki/sources/percolation.md`, in the format of the three existing maps: one row per work, what it
  establishes, where the wiki uses it; a section on what is deliberately outside; a "Records"
  section giving the date of the zbMATH consultation and crediting any review paraphrased
  (CC BY-SA 4.0).
- Works: `koval-meester-trapman-2012`, `hutchcroft-hierarchical-2021`, `hutchcroft-2022-bounds`,
  `hutchcroft-2025-volumes`, with `heydenreich-hofstad-sakai-2008` as background.
- Done when: the map is linked from the site and `check_wiki.py` passes its format checks.

### 4. Then, by value

- A percolation figure that is not a schematic: the cluster-size tail measured on a level-6 lattice,
  with the predicted power law and the crossover marked. It needs the sampling code to be testable
  the way `SIM.isingSweep` is (write it twice, compare bit for bit).
- A second look at part 2's entry points: whether `corrections-to-scaling` should precede
  `bleher-sinai-fixed-point` for a first-time reader, or whether the part needs a short bridge
  paragraph between the dictionary and the two rigorous fixed-point analyses.
- More literature maps (Gawędzki–Kupiainen; Bauerschmidt–Brydges–Slade) if a reader's question
  points there.

## How the repository works

Sources are authored; `site/` is generated, committed, and served. Nothing else is generated.

- `wiki/articles/<id>.md` — one article; the filename is the id. Front matter is JSON between `---`;
  the body is HTML-in-Markdown with `## Heading {#section-id}` sections, assertion anchors
  `<a id="tag-XXXX" data-assertion="theorem" data-title="..."></a>`, `:::details Summary` for
  collapsed proofs, `<div class="fig" data-fig="NAME">` and `<div class="sim" data-sim="NAME">` for
  figures and simulations.
- `wiki/sources/<slug>.md` — reading maps, plain Markdown, pipe tables, `/articles/<id>/` links.
- `wiki/structure.json` — the parts, their order, and the reading paths. Add an article here or the
  build refuses.
- `wiki/tags.json` — the permanent tag ledger. Reserve with `python3 tools/new_tag.py 3` before
  using a tag; entries are never removed or reused.
- `wiki/static/` — `site.css`, `sim.js`, `search.js`, and the vendored KaTeX. `tools/simulate.py`
  computes every figure's data and the Python twin of the browser arithmetic.

The pipeline: write the source, reserve tags, `preview.py`, the checks, commit the sources *and*
`site/`, push.

## Traps that have already cost time

- **Cross-article section links must emit `.html#section-x`.** A missing `#` produced 45 dead
  references once; `check_site.py` now catches it.
- **Pushing.** Push through the connector with a full commit id. If the person edited something in
  the browser first, the push is rejected as non-fast-forward: `github_fetch`, then
  `git rebase refs/remotes/omm/main`, then push. Do not force.
- **`.github/workflows/pages.yml`.** The connector's GitHub App lacks the `workflows` permission and
  cannot create or modify it. Do not try, and do not route around it; the file is live in the repo
  and changes to it are the person's to make.
- **Pages.** The site is served from the Actions artifact rooted at `site/`, so the front page is
  `site/index.html` and paths carry no `/site/` prefix. The CDN caches for ten minutes: a stale page
  after a deploy is a cache, not a failure — refetch with a query string.
- **`.scratch/`** is a cache (quickjs installs there for the tests) and is ignored; `site/` is not
  ignored and must be committed. Do not commit `wiki/preview/`.
- **Math.** `$...$` inline, `<div class="math-display">$$...$$</div>` for displays, and no bare `<`
  or `>` inside math (write `&lt;`, `&gt;`); `test_math.py` renders every formula with
  `throwOnError`, so an unsupported macro fails the build rather than a reader's page.

## Handing off

When an increment is finished, say what changed, what was checked and what was not, and what the
next queue item is. Update this file when the queue changes — it is the only durable memory of the
plan.
