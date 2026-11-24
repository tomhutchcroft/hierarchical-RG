# Wiki style

This wiki follows the style of the PercLib wiki: its
[style sheet](https://github.com/tomhutchcroft/perclib/blob/main/wiki/STYLE.md) governs the
prose, and its [README](https://github.com/tomhutchcroft/perclib/blob/main/wiki/README.md)
governs the file format. What follows is the part of that style this wiki has to fix locally,
namely the shape of an article and the symbols it uses. Where the two disagree, the PercLib
style sheet wins; where it is silent, this file applies.

## Article shape

1. **Lead.** One to three paragraphs before the first heading, readable on their own: the
   object, the main statement informally, and where it sits. No heading, no anchor, no
   collapsible block.
2. **Sections, in this order as they apply:** Definitions and setting; Statement; Examples and
   non-examples; Idea of the proof; Proof; Consequences and applications; Variants and
   generalisations; History and attribution; References. Proof steps are paragraphs inside the
   Proof, never sections. A subtopic long enough to stand alone gets its own article and a
   one-paragraph summary with *Main article: […]*.
3. **Self-contained statements.** Every hypothesis of a statement is in the statement or in
   Definitions and setting. A statement read alone must be complete.
4. **Idea before proof, proof collapsed.** Each full proof follows a two-to-five-sentence idea
   and sits in `:::details <summary>`. A collapsed proof is complete: every step, nothing left
   to the reader. Long computations and one-use lemmas are collapsed too.
5. **Examples and non-examples** wherever a reader asks "for which models?".
6. **Attribute in the text**, naming results as the literature names them, and give the year in
   the lead and in History and attribution.
7. **Inline links** on the natural phrase, at first use in the lead and in each section, to
   `/articles/<id>/` or to an assertion's `/tag/XXXX/`. Never a bare tag as link text.
8. **No process language.** No inventories, interfaces, source files, Lean names, or sentences
   addressed to editors. State what is assumed; do not list what is not.
9. **Rhythm.** A paragraph carries an argument; lists are for parallel items. A paragraph does
   not close by restating itself. Bold only where a term is defined.

## Notation

One symbol per object across the wiki.

| Object | Symbol |
|---|---|
| hierarchical lattice | $\mathbb H=\mathbb H_L^d=\bigoplus_{i\ge1}(\mathbb Z/L\mathbb Z)^d$ |
| hierarchical scale, dimension, block volume | $L\ge2$ integer, $d\ge1$ integer, $m=L^d$ |
| block of radius $L^n$ at the origin | $\Lambda_n=\{x: x_i=0\text{ for }i>n\}$, $\lvert\Lambda_n\rvert=L^{dn}=m^n$ |
| distance, level | $\lVert x-y\rVert=L^{\max\{i:\,x_i\ne y_i\}}$, $\operatorname{lev}(x)$ for $x$ at distance $L^{\operatorname{lev}(x)}$ from $0$ |
| child of a block | a coset of $\Lambda_{n-1}$ in $\Lambda_n$; there are $m$ of them |
| coupling at level $k$, its decay ratio | $J_k=JL^{-(d+\alpha)k}$, $\lambda=L^{d+\alpha}$ |
| intensity, critical intensity | $\beta$, $\beta_c$ |
| spin, block spin | $\sigma_x\in\{\pm1\}$, $S_n=\sum_{x\in\Lambda_n}\sigma_x$ |
| law of the block spin, rescaled law | $\mu_n$, $\nu_n$ |
| renormalisation map, coupling argument | $\mathcal T_b$ (block sums), $\mathcal R_\theta$ (after rescaling by $L^{-\theta}$) |
| variance of the block spin | $v_n=\mathbb E_\beta[S_n^2]$, with $u_n=b_nv_n$ |
| block-spin growth, susceptibility growth | $\theta$ with $\mathbb E[S_n^2]\asymp L^{2\theta n}$; $\kappa=2\theta-d$ |
| relevant eigenvalue, correlation-length exponent | $\lambda_1>1$, $\nu=\log L/\log\lambda_1$ |
| exponents | $\eta$, $\gamma$, $\beta_{\mathrm{o}}$ (order parameter), $\delta$, $\alpha_{\mathrm{hy}}$ |
| free energy of a block | $F_n=m^{-n}\log Z_n$ |
| percolation | $\tau_\beta(x,y)$, $\chi(\beta)$, $K_x$ as in PercLib |

Two symbols collide with the literature and are resolved here once: $\beta$ is the intensity
(inverse temperature), never the order-parameter exponent, which is written $\beta_{\mathrm{o}}$;
and $\alpha$ is the kernel exponent, while the specific-heat exponent is written
$\alpha_{\mathrm{hy}}$.

## Citations

Cite a work by its key in the source catalogue (`src/content/catalog.json`): `[@key]`, or
`[@key, Theorem 1.1]` with the locator kept in the visible text. Several works go in one bracket
separated by `;`. Each article ends with a References section listing the works it cites. A key
missing from the catalogue fails the check; add the work there first.
