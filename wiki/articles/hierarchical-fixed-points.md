---
{
  "id": "hierarchical-fixed-points",
  "title": "The fixed points, and what is known about each",
  "subtitle": "An inventory of the fixed points of the hierarchical recursion, what they share, and what distinguishes them.",
  "kind": "theorem",
  "category": "Renormalisation group",
  "summary": "The recursion of a hierarchical model has few fixed points and they can be listed. There is the trivial law at the origin, a one-parameter Gaussian family of which the critical member is the standard normal, a nontrivial law whose existence is Bleher and Sinai's theorem and whose spectrum is known, and above criticality only degenerate laws on two points. At every fixed point with a finite nonzero variance the growth exponent is the same, theta = (d+alpha)/2, so the susceptibility exponent is alpha everywhere; what varies from one fixed point to another is the multiplier of the linearisation, hence the correlation-length exponent, and the subleading spectrum, hence the corrections. The article collects the statements, says which are proved and by which argument, and records the marginal cases in which two of the fixed points coalesce.",
  "context": [
    "The rescaled decimation map $\\mathcal R_{\\theta,b}$ on the class $\\mathcal E$ of symmetric laws with $0<\\int s^2<\\infty$ and an exponential moment; $\\theta_0=\\tfrac12(d+\\alpha)$, $b=\\beta J_1$, $\\lambda=L^{d+\\alpha}$, $m=L^d$.",
    "Couplings $J_k=JL^{-(d+\\alpha)k}$ with $0<\\alpha<d$, so the critical intensity is finite; $b_c=\\beta_cJ_1$.",
    "Throughout, $\\kappa=2\\theta-d$ and $\\nu=\\log L/\\log\\lambda_1$ are the exponents of the dictionary."
  ],
  "related": [
    "renormalisation-group-map",
    "gaussian-renormalisation-group",
    "gaussian-fixed-point-spectrum",
    "bleher-sinai-fixed-point",
    "koch-wittwer-fixed-point",
    "corrections-to-scaling",
    "hierarchical-two-marginalities"
  ],
  "sourceIds": ["bleher-sinai-1973", "bleher-sinai-1975", "gawedzki-kupiainen-1983", "koch-wittwer-1986"],
  "aliases": [
    "fixed points",
    "Gaussian fixed point",
    "nontrivial fixed point",
    "trivial fixed point",
    "universality",
    "relevant direction"
  ]
}
---

<p>The renormalisation group of a hierarchical model is one operator on laws on the line, and the theory of the model is the study of its orbits. This article is the inventory: what the fixed points are, which of them are proved to exist and by which argument, what they have in common, and what distinguishes them. It adds no analysis of its own beyond the assembling; every statement is proved or attributed in the article it links to, and the tables say which.</p>

<p>The organising fact is a division of labour that is easy to miss when the exponents are read off one fixed point at a time. <a href="/articles/renormalisation-group-map/#section-autonomous">The autonomy of the recursion</a> fixes one of the two numbers at <em>every</em> fixed point: the growth exponent is $\theta_0$ and the susceptibility exponent is $\alpha$, whatever the fixed point. The other number, the multiplier of the linearisation, is what the fixed point determines, and it is the only one that changes as the critical theory changes. So in this model the two-point exponent is universal across regimes and the correlation-length exponent is not — the opposite of the short-range intuition, where the borderline case $\alpha=2$ makes the two coincide. <a href="/articles/critical-exponents-from-rg/#section-dictionary">The dictionary</a> says why in general terms; this article says it fixed point by fixed point.</p>

## What counts as a fixed point {#section-definition}

<a id="tag-O9LJ" data-assertion="definition" data-title="The fixed points of the hierarchical recursion, and the four kinds that occur"></a>
<p>A <em>fixed point</em> is a law $\nu^*\in\mathcal E$ with $\mathcal R_{\theta,b}\nu^*=\nu^*$ for some $\theta$ and $b$, where $\mathcal E$ is the class of <a href="/articles/bleher-sinai-fixed-point/#section-setting">the fixed-point article</a>: symmetric, with $0&lt;\int s^2d\nu^*&lt;\infty$ and an exponential moment. Four kinds occur in this model, and nothing else is known to:</p>
<ol>
<li>the <em>trivial</em> fixed point $\delta_0$, the law of the block spin in the disordered phase, which is a fixed point only in the degenerate sense that its variance vanishes — it is the limit of every orbit with $b&lt;b_c$, and it lies on the boundary of $\mathcal E$ rather than in it;</li>
<li>the <em>Gaussian</em> fixed points $N(0,v_b)$, one for each $b&gt;0$, of which the critical member is $N(0,1)$ at $b=b_1^{(0)}$;</li>
<li>the <em>nontrivial</em> fixed point $\nu^*$ of the critical orbit, in $\mathcal E$ and not Gaussian when $\alpha&gt;d/2$;</li>
<li>the <em>degenerate</em> fixed points of the supercritical phase, $\delta_{+M}$ and $\delta_{-M}$, which are fixed points of the unrescaled map and lie outside $\mathcal E$ because their variance is of the order of the block rather than of the block's square root.</li>
</ol>
<p>"Fixed point" below means the second or third kind unless another is named, and the distinction between the four is the point of the inventory: only two of them can govern a critical theory.</p>

## The inventory {#section-inventory}

<p>The table is the article. Each row gives the fixed point, when it exists, whether its existence is a theorem and of what kind, the multiplier in the growth direction, the correlation-length exponent, and where the statement is proved.</p>
<table><thead><tr><th>Fixed point</th><th>Exists when</th><th>Status</th><th>Growth multiplier</th><th>$\nu$</th><th>Where</th></tr></thead>
<tbody>
<tr><td>$\delta_0$ (trivial)</td><td>always, as a limit</td><td>elementary; not in $\mathcal E$</td><td>&mdash;</td><td>&mdash;</td><td><a href="/articles/bleher-sinai-fixed-point/#section-statement">the trichotomy</a></td></tr>
<tr><td>$N(0,v_b)$</td><td>every $b&gt;0$</td><td>closed form</td><td>$\lambda/m=L^{\alpha}$</td><td>$1/\alpha$</td><td><a href="/tag/S8FR/">tag S8FR</a></td></tr>
<tr><td>$N(0,1)$ at $b_1^{(0)}$</td><td>critical member</td><td>closed form</td><td>$L^{\alpha}$</td><td>$1/\alpha$</td><td><a href="/articles/gaussian-renormalisation-group/#section-multiplier">the Gaussian article</a></td></tr>
<tr><td>$\nu^*$ (nontrivial)</td><td>$0&lt;\alpha&lt;d$</td><td>Bleher–Sinai; independently Koch–Wittwer for the $d=3$ scalar case</td><td>$\lambda_1&gt;1$, and $\lambda_1\neq L^{\alpha}$ for $\alpha&gt;d/2$</td><td>$\log L/\log\lambda_1$</td><td><a href="/tag/B7WD/">tag B7WD</a>, <a href="/tag/C2ZB/">tag C2ZB</a></td></tr>
<tr><td>$\delta_{\pm M}$</td><td>$b&gt;b_c$</td><td>degenerate; outside $\mathcal E$</td><td>&mdash;</td><td>&mdash;</td><td><a href="/articles/hierarchical-fixed-points/#section-degenerate">below</a></td></tr>
</tbody></table>
<p>Two remarks on the columns. The Gaussian row is one family rather than one point: for every $b$ the rescaled map has exactly one Gaussian fixed point, of variance $v_b=\frac{\lambda-m}{\lambda b(m-1)}$, and it is the critical one only at $b_1^{(0)}=\frac{\lambda-m}{\lambda(m-1)}$, where the variance is one and the multiplier is $L^{\alpha}$. And the nontrivial row's spectrum is part of its existence statement: the linearisation is compact on the signed measures of zero mass, its spectrum is a simple eigenvalue $\lambda_1&gt;1$ with the rest in a disk of radius $\rho&lt;1$, and complex pairs occur among the rest.</p>

## What is the same at every fixed point {#section-universal}

<a id="tag-NBGG" data-assertion="proposition" data-title="The growth exponent is theta_0 at every fixed point, so kappa is alpha everywhere"></a>
<p>Let $\nu^*\in\mathcal E$ be a fixed point of $\mathcal R_{\theta,b}$ with $\theta&gt;0$ and $b&gt;0$. Then $\theta=\theta_0=\tfrac12(d+\alpha)$, so $\kappa=2\theta_0-d=\alpha$ and $\eta=2-\alpha$ at every fixed point. Consequently the critical orbit has $\mathbb E[S_n^2]\asymp L^{(d+\alpha)n}$ whichever fixed point governs it, and the two-point exponent does not distinguish the Gaussian fixed point from the nontrivial one.</p>
:::details Proof
<p>By <a href="/articles/renormalisation-group-map/#section-autonomous">the autonomous form</a>, $\mathcal R_{\theta,b}$ is independent of the scale $n$ only at $\theta=\theta_0$: at any other exponent the map obtained by iterating $n$ scales carries the factor $L^{(\theta_0-\theta)n}$ in its argument, so it is a different map at each $n$. A fixed point of the rescaled map is by definition unchanged by one step, and the one step is the step of the model only at $\theta_0$; hence a fixed point with $0&lt;\int s^2&lt;\infty$ occurs only at $\theta_0$. The consequences for $\kappa$ and $\eta$ are the definitions of <a href="/articles/critical-exponents-from-rg/#section-exponents">the exponents</a>.</p>
:::
<p>The statement is the map article's autonomy read at a fixed point rather than along an orbit, and the reason to read it that way is the shape it gives the inventory: the growth direction is the same at every fixed point, so a fixed point can tell one only what the <em>multiplier</em> in that direction is — $L^{\alpha}$ at the Gaussian point and $\lambda_1$ at the nontrivial one. Equivalently, $\kappa$, $\eta$ and the order of the two-point function are mean-field in the sense of <a href="/articles/critical-exponents-from-rg/#section-dictionary">the dictionary</a> everywhere, while $\nu$ and everything the dictionary derives from it is not.</p>
<p>At the critical fixed point the growth statement can be sharpened to a two-sided bound, which is what <a href="/articles/critical-exponents-from-rg/#section-lower">the amplitude theorem</a> does: $0&lt;\inf_nR_n\leq\sup_nR_n&lt;\infty$ for $R_n=\mathbb E[S_n^2]/L^{(d+\alpha)n}$, so the rate is exactly $d+\alpha$ and the bound holds in both directions.</p>

## What changes from one fixed point to another {#section-differs}

<p>Everything the dictionary derives from $\nu$, and the corrections. Three things are worth naming separately.</p>
<p><em>The correlation-length exponent.</em> $\nu=\log L/\log\lambda_1$. At the Gaussian fixed point $\lambda_1=L^{\alpha}$ and $\nu=1/\alpha$; at the nontrivial one $\lambda_1$ is a different number, known through the expansion in the distance from the marginal exponent and not in closed form [@gawedzki-kupiainen-1983]. This is the exponent the fixed point determines, and above $\alpha=d/2$ it is the one that cannot be computed exactly.</p>
<p><em>The subleading spectrum, hence the corrections.</em> A perturbation in a direction of eigenvalue $\lambda$ is multiplied by $\lambda$ per scale, so it appears as a relative correction of order $\xi^{-\omega}$ with $\omega=-\log\lvert\lambda\rvert/\log L$; a complex pair turns the power into a power times a cosine of the logarithm of the length. <a href="/articles/corrections-to-scaling/">The corrections article</a> derives this from the spectral expansion, and the oscillatory corrections of the hierarchical model are a case of it.</p>
<p><em>The relevant directions.</em> The linearisation at the Gaussian fixed point is triangular in the even monomials with eigenvalues $\Lambda_{kk}=L^{d(1-k)+k\alpha}$, so the quadratic direction has $L^{\alpha}$ and the quartic $L^{2\alpha-d}$: the first is relevant for every $\alpha$, the second only above $\alpha=d/2$. <a href="/articles/gaussian-fixed-point-spectrum/">The spectrum article</a> proves this and derives the threshold from it. At the nontrivial fixed point the count of relevant directions is the same, which is why <a href="/articles/hierarchical-and-euclidean-rg/#section-status">the comparison article</a> can say that the structure of the linearisation transfers to the Euclidean theory even when the numbers do not.</p>

## Where two fixed points meet {#section-marginal}

<p>The inventory is not static: two of its rows coalesce at a value of the exponent, and the way they meet is what makes that value special.</p>
<p><em>$\alpha=d/2$.</em> As $\alpha\downarrow d/2$ the nontrivial fixed point approaches the Gaussian one and $\lambda_1\to L^{d/2}$; at the threshold the two coincide, the classical values hold with logarithmic corrections, and the corrections are logarithmic because the second eigenvalue tends to one [@bleher-sinai-1975] [@gawedzki-kupiainen-1983]. The threshold is therefore a bifurcation point of the inventory rather than a boundary between two unrelated regimes, which is why the $\varepsilon$-expansion is organised in $\alpha-d/2$.</p>
<p><em>$\alpha=d$.</em> Here the model stops being a Gibbs system for a level sequence that does not decay, as <a href="/articles/hierarchical-two-marginalities/">the article on the two thresholds</a> sets out, so the inventory itself is at stake rather than a row of it: there is no fixed point to have, because there is no model. The two marginal values are different in kind, and the table above is a table of fixed points of a model that exists.</p>

## Above criticality: only degenerate fixed points {#section-degenerate}

<a id="tag-9UT8" data-assertion="proposition" data-title="For b above b_c the rescaled map has no fixed point in the class, and the orbit concentrates on two points"></a>
<p>Let $b&gt;b_c$. Then $\mathcal R_{\theta,b}$ has no fixed point in $\mathcal E$, and the unrescaled orbit of the Ising initial law concentrates: the law of $S_n/m^n$ converges to the symmetric mixture $\tfrac12(\delta_{-M}+\delta_M)$, where $M=M(\beta)&gt;0$ is the spontaneous magnetisation.</p>
:::details Proof
<p>The concentration is part (ii) of <a href="/articles/bleher-sinai-fixed-point/#section-statement">the trichotomy</a>: the orbit has unbounded variance after rescaling, and in the limit the block spin per site is $\pm M$, the two signs being the two phases of <a href="/articles/hierarchical-magnetised-phase/">the magnetised-phase article</a>. For a fixed point in $\mathcal E$ to exist at $b&gt;b_c$ it would have to be fixed by $\mathcal R_{\theta_0,b}$ with a finite nonzero variance, and then the orbit of the Ising law would have to converge to it up to the relevant directions; but the orbit's variance per site grows like $m^{2n}$, so the rescaled variance diverges, and no limit in $\mathcal E$ exists. The only invariant laws of the unrescaled map consistent with concentration on $\pm M$ are $\delta_{\pm M}$ and their mixture, each of variance of order $m^{2n}$, which is outside $\mathcal E$.</p>
:::
<p>So the four kinds of the definition are exhaustive in the following sense: the rescaled map has fixed points in $\mathcal E$ only at $b\leq b_c$, and at $b=b_c$ the one it has is the nontrivial fixed point. That is the technical content of the phrase "the phase transition is the critical orbit": every other orbit runs to a fixed point that is either outside the class or on its boundary.</p>

## How each one is found {#section-methods}

<p>The inventory is short and the methods that produce it are not interchangeable, so it is worth recording which method gives which row and what each method can and cannot do.</p>
<table><thead><tr><th>Method</th><th>Gives</th><th>Cannot give</th></tr></thead>
<tbody>
<tr><td>closed form (variance recursion)</td><td>the Gaussian family, exactly</td><td>anything non-Gaussian: the recursion does not close</td></tr>
<tr><td>invariant cone, truncation, contraction</td><td>existence and attractivity of $\nu^*$, and the spectrum</td><td>the value of $\lambda_1$ except near $\alpha=d/2$</td></tr>
<tr><td>$\varepsilon$-expansion about $\alpha=d/2$</td><td>$\lambda_1$ and the normal form near the threshold</td><td>anything at a parameter where $\alpha-d/2$ is not small</td></tr>
<tr><td>Borel summation of the large-field region</td><td>existence without a small parameter, for the $d=3$ scalar case</td><td>the spectrum, which it takes from the general theory</td></tr>
<tr><td>reflection positivity and infrared bounds</td><td>bounds on the variance, with explicit constants</td><td>existence of a fixed point</td></tr>
</tbody></table>
<p>The third and fourth rows are two rigorous analyses of the same object by different means, and <a href="/articles/koch-wittwer-fixed-point/#section-statement">the Koch–Wittwer statement</a> is careful about which part of the theorem is theirs: existence and convergent expansions, with the eigenvalue statement supplied by the general theory.</p>

## What is not a fixed point {#section-nonexamples}

<p><em>A law with heavy tails.</em> If the prior's density decays like $\lvert s\rvert^{-p}$ with $p$ large, the tilt is not normalisable for any $b&gt;0$, so the map is not defined on such a law and it can be neither a fixed point nor on an orbit. The class $\mathcal E$ is chosen to exclude it, and the exponential moment is what makes the tilt integrable.</p>

<p><em>The product measure at infinite temperature.</em> The prior $\mu_0$ is not a fixed point of the rescaled map: rescaling by $L^{-\theta_0}$ changes its variance. It is $\delta_0$, not $\mu_0$, that attracts the disordered phase.</p>

<p><em>The percolation recursion.</em> The percolation class has no one-variable fixed point, and that is structural rather than a gap in the analysis: the state of a block is the partition of its vertices into clusters, not the law of a number, so decimation acts on a much larger object [@hutchcroft-hierarchical-2021]. What survives is the growth of the cluster of the origin, which is <a href="/articles/hierarchical-percolation-rg/#section-consequences">fixed at exponent $\alpha$</a> by the same autonomy, and the exponents of the class are read off that rather than off a fixed law.</p>

<p><em>The Euclidean renormalisation group.</em> On $\mathbb Z^d$ the decimation step does not close on any finite-dimensional object, so there is no analogue of the table above: the fixed point exists as a point of an infinite-dimensional space and the statement of its existence is the content of the theory rather than a preliminary to it. <a href="/articles/hierarchical-and-euclidean-rg/">The comparison article</a> sets out what transfers and what does not.</p>

## What is not known {#section-open}

<p>Four things, in order of how much they would add. The <em>value</em> of $\lambda_1$ at the nontrivial fixed point is not known in closed form above $\alpha=d/2$; it is known near the threshold, which is what the $\varepsilon$-expansion computes. The <em>pointwise</em> two-point function at the critical fixed point is not proved to have the order $\lVert y\rVert^{-(d-\alpha)}$ for Ising spins, although the summed statement is now a theorem and for percolation the pointwise one is Hutchcroft's. The <em>subleading spectrum</em> is not classified: complex pairs occur, and the wiki records that as part of the spectrum statement without listing the structure. And the <em>field direction</em> is treated separately throughout, so the inventory above is of the zero-field map; a version with the field included would have a two-dimensional unstable manifold and would gain a column rather than a row.</p>

## History and attribution {#section-history}

<p>The transformation as an operator on laws, the Gaussian fixed points in closed form, and the existence, uniqueness and attractivity of the nontrivial fixed point are the work of Bleher and Sinai [@bleher-sinai-1973] [@bleher-sinai-1975], whose trichotomy of the orbit organises the inventory. The local analysis — the $\varepsilon$-expansion of the leading eigenvalue and the normal form of the unstable manifold — is Gawedzki and Kupiainen's [@gawedzki-kupiainen-1983]. The parameter-free construction for the three-dimensional scalar hierarchy, by Borel summation of the large-field region, is Koch and Wittwer's [@koch-wittwer-1986]. The organisation of this article is the wiki's own; the statements are those of the articles cited in each row.</p>

## References {#section-references}

<ul>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian fixed points of the block spin transformation. Hierarchical model approximation, <em>Comm. Math. Phys.</em> 89 (1983), 191&ndash;220.</li>
<li>H. Koch and P. Wittwer, A non-Gaussian renormalization group fixed point for hierarchical scalar lattice field theories, <em>Comm. Math. Phys.</em> 106 (1986), 495&ndash;532.</li>
</ul>
