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

Seventeen articles in three parts, four reading paths, three reading maps, 62 tagged assertions,
six interactive simulations, six generated diagrams, a notation page generated from `STYLE.md`,
40 works in the catalogue, and a built site of 91 pages committed under `site/`. The checks below
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

**Priority: parts one and two first.** Percolation is not the priority. Build out the block
structure and the renormalisation group — and, within part three, the vector and phi-fourth
material — before returning to the percolation volume, which is item 2.

### 1. By value

- A percolation figure that is not a schematic: the cluster-size tail on a level-6 lattice with the
  predicted power law and the crossover marked, sampled by code written twice and compared bit for
  bit the way `SIM.isingSweep` is.
- A second look at part 2's entry order: whether `corrections-to-scaling` should precede
  `bleher-sinai-fixed-point`, or the part needs a bridge paragraph between the exponent dictionary
  and the two rigorous fixed-point analyses.
- More literature maps (Gawedzki–Kupiainen; Bauerschmidt–Brydges–Slade) if a reader's question
  points there.
- The notation page gives one article per symbol. A second column saying where each symbol is
  *used*, not only where it is introduced, would help a reader who arrives in the middle.
- Part one now has the infinite-volume limit, but the magnetised phase is only named there:
  the two boundary conditions ± and the spontaneous magnetisation of the hierarchical Ising model
  below the critical intensity are not proved anywhere in the wiki, only attributed. An article
  that states what the Bleher–Sinai analysis gives, and what the FKG argument gives cheaply, would
  close part one properly.

### 2. The volume of the critical cluster (percolation depth), deferred

Part 3 promises the non-mean-field regime and delivers one article. Define the exponent from the
tail of the cluster volume, explain why the two-point function is not the hard object there, state
the obstruction giving the bound above the triangle threshold, and keep proved and attributed
sharply apart. Sources already in the catalogue.

## Done

- The infinite-volume limit (`hierarchical-infinite-volume-limit`): the boundary field of a block is
  the same at every vertex and decays like `L^{-alpha n}`, while its sum over the block grows like
  `L^{(d-alpha)n}`, which is where the two ranges of the model part. The Gibbs conditional is
  Lipschitz in that field, so every limit point of the finite-volume measures is a Gibbs measure in
  the sense of Dobrushin, Lanford and Ruelle; limit points of the free-boundary measures are
  invariant under translations and coordinate-wise bijections, so their two-point function is
  radial. Checked: the closed form for the boundary field against direct summation, the Lipschitz
  bound, and the identity between the free-boundary conditional and the Gibbs conditional of the
  field, all in `numeric_checks.py`; the figure is rendered and looked at.
- The lattice's isometries (`hierarchical-symmetries`): translations and coordinate-wise bijections
  are isometries and act transitively on ordered pairs at each level, which supplies the three
  statements five articles were using as "by symmetry". A level-preserving bijection that is not an
  isometry, and the fact that the coordinates cannot be permuted, show the criterion has content.
  The five articles link to it where they lean on it.
- The notation page (`notation.html`): generated from the table in `wiki/STYLE.md`, each symbol
  linking to the article that introduces it, linked from the sidebar, `start.html` and `index.html`.
  A row naming a missing article fails the build, and lines starting with `>` are maintainer notes
  that stay out of the page.
- The spectrum at the Gaussian fixed point (`gaussian-fixed-point-spectrum`): the linearisation is
  triangular in the even monomials with eigenvalues `L^(d(1-k)+k alpha)`, which derives the quartic
  threshold `alpha = d/2`, the marginal case, and the upper critical dimension four. Checked
  numerically by finite-difference diagonalisation of the truncated map.

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
