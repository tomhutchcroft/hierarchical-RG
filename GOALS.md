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

Nineteen articles in three parts, four reading paths, five reading maps, 75 tagged assertions,
seven interactive simulations, seven generated diagrams, and four generated index pages beyond the
bibliography and the assertions: notation (with where each symbol is used), chronology, figures, and
the single-file edition. 42 works in the catalogue; a built site of 109 pages under `site/`. The
checks below pass.

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

### 1. The one mathematical question still open in the wiki

The variance route gives `κ₊ ≤ α` unconditionally and pins the ratio of the two block-spin
fluctuations at criticality, but it cannot certify `κ = α`: the half of the sandwich that would do
so is an upper bound on the free block-spin variance, and the wiki has neither that bound nor a
proof that the free measures at `β_c` are the even mixture of the two extremal states. Everything
else that was open has been closed or attributed, so this is now the only place where the wiki's own
argument stops short of its own statement.

### 2. By value, next

- The free energy's singularity. The recursion gives `F_n → F` and convexity, and nothing in the wiki
  says what `F` does at `β_c`. The Gaussian case is computable in closed form from the per-scale
  terms of the recursion, so the singularity there is arithmetic; whether the Ising case can be said
  anything about beyond the attribution is an open editorial question.
- A second literature map is not needed; the catalogue is mapped in five groups, and the works
  outside them are cited individually.

### 3. The volume of the critical cluster (percolation depth), deferred

Part 3 promises the non-mean-field regime and delivers one article. Define the exponent from the
tail of the cluster volume, explain why the two-point function is not the hard object there, state
the obstruction giving the bound above the triangle threshold, and keep proved and attributed
sharply apart. Sources already in the catalogue.

## Done

- A reading map for Bauerschmidt, Brydges and Slade: the one book in the catalogue, with what the
  method is, what this wiki takes from it, and the boundary that matters — a book about the marginal
  dimension cannot decide the open questions about the hierarchical model, which is its setting.
- *The two marginal exponents* (`hierarchical-two-marginalities`), a synthesis article for part
  three: `α = d` is the threshold of the measure and `α = d/2` that of the map, the two coincide
  only at `α = 2`, `d = 4`, and the table says which criterion applies in each regime. Proved: the
  summability computation and the quartic eigenvalue crossing one. Attributed: Bleher and Major's
  criterion at the marginal exponent and its percolation counterpart, which disagree.
- Four generated index pages and one generated strip: a chronology of the cited works by year, a
  page documenting every figure and simulation with what checks it, per-article notation lines
  pointing at the rows of the notation table, and the earlier notation page extended with where each
  symbol is used. All generated from their sources, all linked from the sidebar.
- An exact widget for the magnetised phase: the three boundary conditions' block-spin laws side by
  side, enumerated, written twice and compared by `test_sim.py` to `3e-15`.
- `check_wiki.py` now warns when a `related` link is one-sided, and the 46 one-sided links in the
  data were made reciprocal.
- Every finite-volume plus state is magnetised at every positive intensity (`tag-LSTE`), which is why
  the transition is a statement about the limit; checked by enumeration at four intensities.
- A reading map for Gawedzki and Kupiainen: the five papers that build the local theory of the
  nontrivial fixed point, with the group's three boundaries stated — existence is not its subject,
  the analysis is local in `ε` or `1/N`, and the setting is the hierarchical approximation.
- Part two reordered and bridged: `corrections-to-scaling` now follows `bleher-sinai-fixed-point`,
  because it expands in the spectrum that article proves exists; the part's introduction says what
  the chain of articles is doing, and a bridge paragraph at the end of the exponent dictionary says
  which of its inputs are hypotheses and where they are supplied.
- The notation page says where each symbol is used, not only where it is introduced: a fourth column
  in the `STYLE.md` table, resolved by the generator, with the lists chosen by counting the LaTeX
  token in every article rather than from memory.
- A sampled cluster-size distribution for hierarchical percolation: 200 realisations on a 64-site
  block at three intensities, the pseudocritical one found by maximising the sampled mean finite
  cluster size, the predicted slope `n_s ∝ s^{-2d/(d+α)}` drawn as a guide and the block cutoff
  marked. The sampler is written twice — `percolation_clusters` in `simulate.py` and
  `SIM.percolationClusters` in `sim.js` share the uniform stream — and `test_sim.py` compares the
  cluster-size lists entry by entry over fifteen realisations.
- The variance route to `κ` (`critical-exponents-from-rg`, section `variance-route`): the GHS
  inequality makes the block-spin variance maximal at zero boundary field, so the boundary-field
  identity sandwiches the finite-size magnetisation between the two block-spin variances,
  `βC Var₊/L^{2θ₀n} ≤ M_n ≤ βC Var_free/L^{2θ₀n}`. Consequences, all unconditional: the plus
  block average concentrates at least like `L^{-(d-α)n/2}`, so `κ₊ ≤ α` at every intensity; the
  free one fluctuates at least `M_n` times mean field; and at criticality, given the growth
  theorem's hypothesis and continuity, a boundary field of size `B_n → 0` pins the block spin, with
  the ratio of the two fluctuations tending to zero. Checked: GHS monotonicity on eleven boundary
  fields at three intensities, the sandwich and both rate bounds.
- The block-average converse (`hierarchical-magnetised-phase`, section `block-average`): the plus
  state's block average *equals* its single-site magnetisation at every finite volume, because
  translations by `Λ_n` permute `Λ_n`, so it decreases to `M(β)`; every Gibbs measure's block
  average is bounded by `M` in modulus; and if `M = 0` the unique Gibbs measure is extremal, the
  limit of the block averages is translation invariant, invariant events are tail events, so the
  limit is the constant `0` — a nondegenerate limit therefore forces `M > 0`. Checked: the
  equivalence of the vertices, the identity, the monotonicity in the volume, the bound over seven
  boundary fields, and the variance identity to nine decimals by Gauss–Legendre quadrature.
- The magnetised phase (`hierarchical-magnetised-phase`): the FKG inequality plus a monotone heat-bath
  coupling gives the two extremal states, the sandwich of every Gibbs measure between them, and the
  equivalence of non-uniqueness with positivity of the order parameter `M(β)`; correlations under the
  plus state dominate `M²`, so a magnetised phase has infinite susceptibility; and `M ≤ tanh(βC)` is
  the only bound on the location that monotonicity gives, which is the article's argument that the
  threshold has to come from the recursion. Checked: domination on every upper set, monotonicity of
  the plus measure in the volume, the one-site Gibbs identity and the `tanh` bound, and positive
  correlations, all by exact enumeration in `numeric_checks.py`.
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
