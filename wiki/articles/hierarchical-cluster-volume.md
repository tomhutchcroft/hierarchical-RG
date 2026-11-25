---
{
  "id": "hierarchical-cluster-volume",
  "title": "The volume of the critical cluster",
  "subtitle": "The exponent delta, its value in each range of the dimension, and why the two-point function does not give it.",
  "kind": "theorem",
  "category": "Percolation",
  "summary": "The two-point function at criticality controls connections between pairs of vertices; the volume of the cluster of a vertex is a different observable, and the exponents that govern it are not read off the two-point function. In hierarchical long-range percolation the volume exponent is known exactly in every regime: the tail of the cluster volume decays like n to the minus (d-alpha)/(d+alpha) below the upper critical dimension d = 3 alpha, like n to the minus one half above it, and with a specific polylogarithmic correction at the dimension itself. The triangle threshold is where the two behaviours meet, and the log correction there agrees with neither of the predictions for the Euclidean model.",
  "context": [
    "Long-range Bernoulli bond percolation on $\\mathbb H^d_L$: each pair $x\\neq y$ is joined with probability $1-\\exp(-\\beta\\lVert x-y\\rVert^{-d-\\alpha})$, with $0<\\alpha<d$.",
    "$\\beta_c$ is the critical intensity of the percolation article, $K$ the cluster of the origin, and $\\delta$ the exponent defined by $\\mathbb P_{\\beta_c}(\\lvert K\\rvert\\geq n)=n^{-1/\\delta+o(1)}$.",
    "The model is at its critical point throughout; nothing here is about the subcritical or supercritical phases."
  ],
  "related": [
    "hierarchical-percolation-rg",
    "critical-exponents-from-rg",
    "hierarchical-two-marginalities"
  ],
  "sourceIds": ["hutchcroft-2025-volumes"],
  "aliases": [
    "cluster volume",
    "cluster size distribution",
    "delta",
    "upper critical dimension",
    "polylogarithmic correction"
  ]
}
---

<p><a href="/articles/hierarchical-percolation-rg/#section-consequences">The percolation article</a> derives two exponents from the critical two-point function: it decays like the distance to the power $-(d-\alpha)$, so $\eta=2-\alpha$, and the block susceptibility grows like $L^{\alpha n}$, so $\kappa=\alpha$. Those are statements about pairs. The volume of a cluster is a statement about a set, and the two are related only through the scaling relations, which are not theorems about any particular model. This article is about the set.</p>

<p>The model is the hierarchical one throughout: pairs are joined with probability $1-\exp(-\beta\lVert x-y\rVert^{-d-\alpha})$, so the intensity of a bond depends on its level, and $\beta_c<\infty$ exactly when $\alpha<d$. The question is the tail of the volume of the cluster of the origin at $\beta_c$, and the answer is known in every regime, which is unusual enough to be worth a separate article: for the long-range model on the Euclidean lattice the corresponding statements are open.</p>

## The exponent {#section-definition}

<a id="tag-RQEG" data-assertion="definition" data-title="The volume exponent, and the upper critical dimension it turns at"></a>
<p>Write $\lvert K\rvert$ for the volume of the cluster of the origin, and define $\delta$ by</p>
<div class="math-display">$$\mathbb P_{\beta_c}\bigl(\lvert K\rvert\geq n\bigr)=n^{-1/\delta+o(1)},\qquad n\to\infty.$$</div>
<p>The <em>upper critical dimension</em> of the model is $d_c=3\alpha$: the value at which the triangle diagram of <a href="/articles/hierarchical-percolation-rg/#section-triangle">the percolation article</a> changes from convergent to divergent, and the value at which the volume exponent changes value.</p>
<p>The two thresholds of the percolation model should not be confused with the two marginal exponents of the spin model. The triangle threshold $3\alpha=d$ is a property of the percolation class alone; the summability threshold $\alpha=d$ decides whether the model is a Gibbs system at all, and the quartic threshold $\alpha=d/2$ is a property of the spin model's linearisation. In one dimension they read $\alpha=1/3$, $1$ and $1/2$. <a href="/articles/hierarchical-two-marginalities/">The article on the marginal exponents</a> sets the last two side by side; the first is this one.</p>

## The value in each regime {#section-value}

<a id="tag-HLTX" data-assertion="theorem" data-title="The tail of the critical cluster volume in each range of the dimension"></a>
<p>Let $0&lt;\alpha&lt;d$ and let $\beta=\beta_c$. Then, up to constants that depend only on $d$ and $\alpha$,</p>
<div class="math-display">$$\mathbb P_{\beta_c}\bigl(\lvert K\rvert\geq n\bigr)\ \asymp\ \begin{cases}n^{-(d-\alpha)/(d+\alpha)}, & d&lt;3\alpha,\\ n^{-1/2}(\log n)^{1/4}, & d=3\alpha,\\ n^{-1/2}, & d&gt;3\alpha.\end{cases}$$</div>
<p>So $\delta=\dfrac{d+\alpha}{d-\alpha}$ below the upper critical dimension, $\delta=2$ above it, and at the dimension itself the power law is the mean-field one with a polylogarithmic correction of order $(\log n)^{1/4}$.</p>
<p>The estimates are due to Hutchcroft [@hutchcroft-2025-volumes], who proves them from precise estimates on the moments of all orders of the volume of the cluster of the origin inside a box; the same work identifies the correction at $d=3\alpha$ and shows that it is <em>not</em> the correction predicted for nearest-neighbour percolation on $\mathbb Z^6$, so the correspondence between the hierarchical model and the Euclidean model at the upper critical dimension is not exact even at the level of the logarithm. No proof is reproduced here: the article records what is known and where, and the mechanism of the proof is the moment analysis in the article cited.</p>
<p>Three features of the statement are worth separating. The exponent above the critical dimension is the mean-field value $2$, which is what <a href="/articles/hierarchical-percolation-rg/#section-triangle">the triangle computation</a> predicts, so the threshold is visible in the value of $\delta$ and not only in the diagram. Between the two regimes the exponent varies continuously, from $2$ at $d=3\alpha$ down to $1$ as $\alpha\downarrow d$: in the limit the cluster volume is as heavy-tailed as it can be, which is consistent with $\eta=2-\alpha\to1$ and with the susceptibility's divergence. And the singular case is the boundary: at $d=3\alpha$ the minus one half power is exactly the mean-field one, so the correction is the whole content of the statement there.</p>

## Why the volume is not the two-point function {#section-obstruction}

<p>The temptation is to read $\delta$ off the two-point function through the scaling relation $\delta=\frac{d+\eta}{d-\eta}$, which with $\eta=2-\alpha$ gives $\frac{d+2-\alpha}{d-2+\alpha}$ — not the value above. The relation that does hold in the mean-field regime is the one with $\kappa$: $\delta=\frac{d+\kappa}{d-\kappa}$ with $\kappa=\alpha$, which is $\frac{d+\alpha}{d-\alpha}$. So the two ways of computing give different answers unless $\eta=\kappa$, that is unless the two-point exponent and the growth exponent agree, which happens only in the mean-field regime. <a href="/articles/critical-exponents-from-rg/#section-dictionary">The dictionary</a> says exactly this: the relation $\delta=\frac{d+\kappa}{d-\kappa}$ follows from the scaling relations plus hyperscaling, and hyperscaling is the hypothesis that fails away from mean field.</p>
<p>That is the structural reason the volume needs its own analysis. The two-point function is a property of the connection probability between two points; the volume of the cluster of one point depends on how the connections arrange themselves into a connected set, which is a statement about the geometry of the cluster rather than about any pair. In the hierarchical model the two are linked by the block structure — a cluster inside a block either joins the sibling blocks through its connections or does not — but the link is an inequality, which is what <a href="/articles/hierarchical-percolation-rg/#section-recursion">the recursion inequalities</a> say, and an inequality cannot identify an exponent.</p>

## What else the analysis gives {#section-consequences}

<p>Two further statements from the same work are worth recording, because they are about the shape of the critical clusters rather than any exponent. Above the upper critical dimension, the sized-biased distribution of the volume of the cluster inside a box converges, under a suitable normalisation, to a chi-squared law; that is the hierarchical counterpart of the statement that the critical cluster is a random tree with a Gaussian volume in the mean-field regime. Below it, the decreasing list of cluster sizes in a box is tight in $\ell^p$ for exactly those $p$ greater than $2d/(d+\alpha)$, which says quantitatively how concentrated the volume is in a few large clusters. Both are stated here at the level of the published abstract, and neither is used elsewhere in the wiki.</p>

## Examples and non-examples {#section-examples}

<p><em>One dimension.</em> The regimes are $\alpha&lt;1/3$ and $\alpha&gt;1/3$, and the exponent passes from $2$ at $\alpha=1/3$ to $1$ as $\alpha\uparrow1$, the value at which the model stops being a Gibbs system. So in one dimension the exponent is never below $1$, and the tail is never lighter than $n^{-1}$.</p>

<p><em>The mean-field regime is not the whole of the easy case.</em> Above $d=3\alpha$ the volume exponent is the mean-field one, but the percolation article's <a href="/articles/hierarchical-percolation-rg/#section-triangle">triangle analysis</a> says that everything else is mean-field there too; the interest of the theorem is in the other direction, where the two-point function is still exact but the volume exponent is not the mean-field one.</p>

<p><em>Non-example: reading $\delta$ off the susceptibility.</em> The susceptibility at criticality diverges with exponent $\gamma=1$ in this model, and the naive relation $\gamma=\beta_{\mathrm{o}}(\delta-1)$ with $\beta_{\mathrm{o}}=\frac{1}{2}$ would give $\delta=3$; the true value below the critical dimension is $\frac{d+\alpha}{d-\alpha}$, which is $3$ only at $d=2\alpha$. So the relations do not fix the volume exponent: they relate it to exponents that the model does not have to obey in the same way.</p>

## Variants and generalisations {#section-variants}

<p><em>The Euclidean model.</em> The corresponding tail is not known for long-range percolation on $\mathbb Z^d$. What is known is the two-point function's upper bound, transported from the hierarchical lattice [@hutchcroft-2022-bounds], and the hierarchical result is the model in which the analysis can be completed rather than a step in a Euclidean proof.</p>

<p><em>The cluster-size distribution.</em> The theorem's content is about the tail of one cluster. The full distribution of cluster sizes, and the question of which sizes dominate at criticality, is the stronger statement behind the $\ell^p$ tightness recorded above; <a href="/articles/hierarchical-percolation-rg/">the percolation article</a> displays the distribution and its predicted slope on a block of sixty-four sites, which is an illustration of the same object at a scale where the exponent cannot be measured.</p>

## History and attribution {#section-history}

<p>The phase transition of long-range percolation on the hierarchical lattice, with a finite critical intensity exactly when $\alpha&lt;d$, is classical [@koval-meester-trapman-2012]. The critical two-point function and the triangle threshold in this model are Hutchcroft's [@hutchcroft-hierarchical-2021], and the volume of the critical cluster is the subject of his later analysis of critical cluster volumes [@hutchcroft-2025-volumes], which is where every statement of this article comes from. The upper bound on the critical two-point function that carries over to the Euclidean lattice is the same author's [@hutchcroft-2022-bounds].</p>

## References {#section-references}

<ul>
<li>T. Hutchcroft, The critical two-point function for long-range percolation on the hierarchical lattice, <em>Ann. Appl. Probab.</em> 34 (2024), no. 1B, 986&ndash;1002.</li>
<li>T. Hutchcroft, Sharp hierarchical upper bounds on the critical two-point function for long-range percolation on $\mathbb Z^d$, <em>J. Math. Phys.</em> 63 (2022), 113301.</li>
<li>T. Hutchcroft, Critical cluster volumes in hierarchical percolation, <em>Proc. Lond. Math. Soc.</em> (3) 130 (2025), e70023.</li>
<li>V. Koval, R. Meester and A. Trapman, Long-range percolation on the hierarchical lattice, <em>Electron. J. Probab.</em> 17 (2012), no. 57.</li>
</ul>
