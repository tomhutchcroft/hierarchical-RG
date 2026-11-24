# Hierarchical RG

A wiki on the renormalisation group on hierarchical lattices: the block-spin transformation,
the exact recursion it satisfies there, its fixed points, and the critical exponents read off
from them.

The articles live in `wiki/articles/`, one topic each, in the format of the
[PercLib wiki](https://github.com/tomhutchcroft/perclib/tree/main/wiki): JSON front matter, a
lead of at most three paragraphs, `## Heading {#section-…}` sections, assertion anchors with
reserved four-character tags, collapsed proofs, and citations by catalogue key.

Start at [wiki/README.md](wiki/README.md) for the format and the checks, and
[wiki/STYLE.md](wiki/STYLE.md) for the house style and notation. The literature each article
draws on is mapped in `wiki/sources/`: one finding aid per group of works, listing what every
paper establishes and which article uses it.

## The articles

| Article | What it covers |
|---|---|
| [The hierarchical lattice](wiki/articles/hierarchical-lattice.md) | The ultrametric group, its blocks, and the child decomposition that makes decimation close |
| [Hierarchical spin systems and decimation](wiki/articles/hierarchical-gibbs-measure.md) | The long-range model, the exact decimation identity, the free energy recursion |
| [The renormalisation group map](wiki/articles/renormalisation-group-map.md) | The operator on block-spin laws, its scaling form, fixed points and the eigenvalue problem |
| [The Gaussian renormalisation group](wiki/articles/gaussian-renormalisation-group.md) | Exact closure on Gaussian laws, the critical coupling, the multiplier $L^\alpha$ |
| [Critical exponents from the renormalisation group](wiki/articles/critical-exponents-from-rg.md) | The exponent dictionary and the scaling relations |
| [The Bleher–Sinai fixed point](wiki/articles/bleher-sinai-fixed-point.md) | The non-Gaussian fixed point, its existence, and the crossover at $\alpha=d/2$ |
| [Renormalisation for hierarchical percolation](wiki/articles/hierarchical-percolation-rg.md) | The percolation recursion, the critical two-point exponent, the triangle threshold |
| [Hierarchical and Euclidean renormalisation](wiki/articles/hierarchical-and-euclidean-rg.md) | Why the recursion is exact here, what fails on $\mathbb Z^d$, and how the model is used anyway |
| [Hierarchical models with continuous symmetry](wiki/articles/hierarchical-vector-models.md) | Dyson's conjecture at the marginal exponent, the Thouless-like limit law, and the vector decimation |
| [The phi-fourth model and its truncations](wiki/articles/hierarchical-phi4-truncations.md) | The potential flow, the exact Gaussian truncation, and the low-temperature vector phase |
| [Koch and Wittwer's non-Gaussian fixed point](wiki/articles/koch-wittwer-fixed-point.md) | A certified fixed point at explicit parameters, with no small parameter |
| [Abdesselam's trajectory between two fixed points](wiki/articles/abdesselam-global-trajectory.md) | A whole orbit of the Euclidean renormalisation group, built from a one-dimensional iteration |

The site is published on GitHub Pages by `.github/workflows/pages.yml`; see
[wiki/README.md](wiki/README.md#publishing) for the one setting it needs.

## Checks

```sh
python3 tools/check_wiki.py       # format, tags, links, citations, fences
python3 tools/numeric_checks.py   # the displayed identities, checked on finite blocks
python3 tools/preview.py          # static preview in wiki/preview/
```

The numeric checks confirm the formulas the articles display (the variance recursion and its
closed form, the critical intensity, the multiplier $L^\alpha$, the block identity, the Ising
decimation identity and the triangle increment) against direct computation on blocks up to
$L^{12}$ vertices. They check identities, not theorems.
