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

Twenty-two articles in three parts, six reading paths, five reading maps, 84 tagged assertions,
eight generated figures, seven interactive ones, 42 works in the catalogue, and a built site of 131
pages under `site/`, with nine generated index pages beyond the articles and a page saying how the
wiki is checked. The checks below pass.

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

### 1. The pointwise rate, which is all that is left

The exponents of the Ising model on this lattice are settled: `κ = α` with `R_n = V_n/L^{(d+α)n}` bounded
away from zero and from infinity at criticality (`critical-exponents-from-rg`, section `lower`). What is
not proved is the per-pair statement behind it: `τ_∞(0,y) ≤ A L^{-(d-α)lev y}` and its finite-volume
counterpart on the top shell. Both are theorems for the percolation class on the same lattice; for Ising
spins the summed consequence is now proved and the pointwise one is not.

### 2. By value, next

- The energy's telescoping identity is now in the free-energy article, together with the trap it
  invites: the expected squared block sums are *not* the free variances, because a block inside a
  bigger block feels its siblings (1.4 per cent at `n = 2`). The energy needs the joint law of the
  children's sums, which is the same wall as the heat capacity. What would reopen both is a
  representation of that joint law cheaper than a vector of length `2m^k`.
- The one place where a computation is now known to be out of reach at this size: the Ising heat
  capacity. The free-energy article computes the Ising free energy to a few digits and certifies it
  from below, and shows that the derivatives are lost in the truncation near criticality. A method
  that carries the law at scale `k` more cheaply than a vector of length `2m^k` — a cumulant or
  Chebyshev representation, say — would reopen it.

## Done

- *The fixed points, and what is known about each* (`hierarchical-fixed-points`), the coda of part two:
  an inventory table of every fixed point of the recursion with its existence status, growth multiplier,
  `ν` and the article that proves it; the proposition that the growth exponent is `θ₀` at every fixed
  point, so `κ = α` everywhere while `ν` is what the fixed point determines; a table of the five methods
  that produce the rows and what each cannot do; the degenerate supercritical fixed points; the
  coalescence at `α = d/2`; and what is not a fixed point in each of the neighbouring classes.
- The amplitude (`tag-UJC1` now carries the two-sided theorem): a trapping argument, from a fifth submission,
  refereed here. In the small regime the uniform two-sided small-tilt expansion gives `R_n ≤ qR_{n-1}` with
  `q = (1+L^{-α})/2 < 1`, so a small value would decay for ever, making `log χ_n` have summable increments and
  the critical susceptibility bounded — contradicting sharpness. With the runaway argument for the upper bound,
  `0 < inf_n R_n ≤ sup_n R_n < ∞`, and the growth theorem's convergence hypothesis is no longer needed.
  Checked on the model's own laws: ratios `0.73–0.79` against `q = 0.854`.
- A second, independent route to the upper bound was reported to the swarm and refereed by me but not
  written up: reflection positivity of the hierarchical kernel, through the telescoping
  `f_R = sum_k (J_k - J_{k+1}) 1_{Λ_k} - J_1 delta_0` and the characters trivial on a block, gives
  Gaussian domination and an infrared bound, and the character weights then give an *explicit*
  constant, `K = (m-1)/(β_c(L^d - L^α))`. I verified the telescoping, the positive-semidefinite cross
  matrix and the weight arithmetic, but not the h-shifted reflection-positivity criterion, the Bochner
  step, or the limit `β ↑ β_c` — so the constant is not in the wiki. That chain, written out
  self-contained, is the cheapest way to put an explicit constant into the article.
- `κ = α` at criticality (`tag-UJC1` for the lower half, `tag-4QMQ` for the upper), from two submissions
  to a swarm run on this question. Both were refereed here before being written up: the two-child
  comparison's FKG-on-the-amplitude-quadrant and Riccati steps checked line by line, the recursion
  tested on the model's own laws over five intensities and three sizes (smallest margin `7e-4`), and
  the runaway argument's normalisations (`Q = L^{d-α} > 1`, summable deficits, positive product)
  checked by hand. The one external input, the mean-field lower bound for the susceptibility, is
  named in the article.
- The growth exponent reduced to two pointwise bounds (`tag-UTEB`), with the moment-monotonicity lemma
  (`tag-T8WS`) that the argument needs. The reduction came from a member of a swarm run on this
  question; it was refereed here — the lemma's Chebyshev step checked line by line and verified by
  exact enumeration, the two implications checked, the shell counts checked — and then written into
  the article in the wiki's own voice, with the percolation case noted as the one where both inputs
  are already theorems.
- The Ising free energy computed by the convolution recursion: one decimation step is a convolution
  because the tilt's matrix has eigenvalues `(m-1)/2` and `-1/2`; in the Fourier and log domains the
  recursion reproduces exact enumeration to `1.5e-16`, and since every per-scale term is nonnegative
  each table entry is a certified lower bound. The section then shows the method stopping — converged
  at twelve scales away from criticality, still moving in the fourth decimal at twenty near it — and
  says that this is why the Ising curvature is not computed in the wiki.
- The volume exponent as a picture (`volume-exponent`): `δ` against `α` in one dimension, mean field
  to the left of `d = 3α` and rising without bound to the right; the curve is cut where it leaves the
  frame rather than flattened on the axis.
- A table of what is proved on each side of the Euclidean comparison, six rows with sources, in
  `hierarchical-and-euclidean-rg`. The pattern is the argument: every row proved for the hierarchy and
  not for the lattice uses that a block has no boundary.
Sixteen increments in one session, of which three were content and the rest structure, checks and
navigation:

- *The free energy and its singularity*: the Gaussian per-scale terms in closed form, the uniform
  convergence of the series, and the divergence of the curvature with exponent `2 − d/α`. The
  quadrature check rejected my first closed form (wrong eigenvalue structure of the tilt) and the
  same check exposed a false claim that the series diverges at criticality.
- *The two marginal exponents*, and *the volume of the critical cluster*: the second corrects the
  percolation article, which had been calling a proved value a conjecture.
- Twelve structural increments: two generated documentation pages (what is not known, how it is
  checked), two reading paths, sitemap/robots/404, four checks (unknown figure names are now fatal;
  orphaned works; sourceIds cited in the text; catalogue hygiene), a sections index, a notation
  appendix in the printable edition, source lines per article, and landmarks with labels that
  `check_site.py` enforces.
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
