---
{
  "id": "gaussian-fixed-point-spectrum",
  "title": "The spectrum at the Gaussian fixed point",
  "subtitle": "Why the quartic coupling is relevant above half the dimension, and what it is a computation of.",
  "kind": "theorem",
  "category": "Renormalisation group",
  "summary": "At the Gaussian fixed point the linearised decimation map is triangular in the basis of even monomials, and its diagonal entries are L^(d(1-k)+k alpha) for the monomial of degree 2k. The first entry is the variance multiplier; the second is the eigenvalue of the quartic coupling, which exceeds one exactly when alpha exceeds half the dimension. The relevance of the quartic term, the crossover at alpha = d/2 and the upper critical dimension four of the nearest-neighbour model are therefore one computation.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$; kernel exponent $0&lt;\\alpha&lt;d$; $\\theta_0=\\tfrac12(d+\\alpha)$.",
    "The Gaussian fixed point is the law $N(0,1)$ of the rescaled block spin, at the coupling $b^*=(1-mL^{-2\\theta_0})/(m-1)$.",
    "Perturbations are even polynomials of $s$ of degree at most $2K$, for a fixed $K$; the statement is finite-dimensional in $K$."
  ],
  "related": [
    "gaussian-renormalisation-group",
    "corrections-to-scaling",
    "hierarchical-phi4-truncations",
    "bleher-sinai-fixed-point",
    "hierarchical-two-marginalities",
    "hierarchical-fixed-points"
  ],
  "sourceIds": ["fisher-ma-nickel-1972", "gawedzki-kupiainen-1983", "bleher-sinai-1975", "bauerschmidt-brydges-slade-2019"],
  "aliases": [
    "Gaussian fixed point",
    "linearisation",
    "quartic coupling",
    "relevance",
    "upper critical dimension",
    "power counting"
  ]
}
---

<p>The <a href="/articles/gaussian-renormalisation-group/">Gaussian renormalisation group</a> computes one eigenvalue: the variance of the block spin is multiplied by $L^{\alpha}$ per scale at the critical point, and that gives $\nu=1/\alpha$. That is the first of a family. At the Gaussian fixed point the linearised map is triangular in the basis of even monomials, and the monomial $s^{2k}$ carries the eigenvalue</p>
<div class="math-display">$$\lambda_{2k}=L^{\,d(1-k)+k\alpha},$$</div>
<p>of which the variance direction is $k=1$. The next one, $\lambda_4=L^{2\alpha-d}$, is the eigenvalue of the quartic coupling, and it exceeds one exactly when $\alpha&gt;d/2$. So the statement that the quartic coupling is irrelevant below half the dimension, which the <a href="/articles/hierarchical-phi4-truncations/">truncations article</a> and the <a href="/articles/bleher-sinai-fixed-point/">fixed-point article</a> both rely on, is not an extra input: it is the second diagonal entry of the same matrix.</p>

<p>The formula also reproduces the familiar thresholds. A nearest-neighbour model has $\alpha=2$ in this language, and then $\lambda_4=L^{4-d}$: marginal at $d=4$, relevant below it, irrelevant above. That is the upper critical dimension, and the crossover at $\alpha=d/2$ is the same equation $\lambda_4=1$ read in the other variable. The classical long-range exponent values and the threshold are those of Fisher, Ma and Nickel [@fisher-ma-nickel-1972]; what this article adds is that in the hierarchical model they follow from the linearisation by a computation short enough to give in full.</p>

<p>Two limits on the statement are worth naming at the outset. It is a statement about the Gaussian fixed point, so it says when that fixed point is unstable, not what replaces it; the replacement is the subject of <a href="/articles/bleher-sinai-fixed-point/">the Bleher-Sinai article</a>. And it is a statement about finite-dimensional truncations of the space of perturbations, triangular in the monomial basis; the eigenvalues of the full map on a Banach space of interactions require the analytic estimates of the rigorous analyses.</p>

## Definitions and setting {#section-setting}

<p>Work in the potential form of <a href="/articles/hierarchical-phi4-truncations/#section-potentials">the truncations article</a>. A block-spin law with a smooth even density is written $e^{-V(s)}ds$, one decimation step and rescaling send</p>
<div class="math-display">$$V\longmapsto\Phi_\theta V,\qquad (\Phi_\theta V)(s)=-\log\int_{\mathbb R^{m-1}}\exp\Bigl(-V(s_1)-\cdots-V(s_m)+b\sum_{a&lt;a'}s_as_{a'}\Bigr)ds_1\cdots ds_{m-1}\Big|_{\textstyle s_m=L^\theta s-\sum_{a&lt;m}s_a},$$</div>
<p>with the additive constant dropped, and the rescaled variable $L^\theta s$ in place of the block spin. The Gaussian fixed point is $V^*(s)=\tfrac12s^2$ with the coupling $b$ chosen so that the variance is one:</p>
<div class="math-display">$$b^*=\frac{1-mL^{-2\theta_0}}{m-1},\qquad \theta_0=\frac{d+\alpha}{2}.$$</div>
<a id="tag-G5KM" data-assertion="definition" data-title="Monomial directions and the linearised map at the Gaussian fixed point"></a>
<p>For $K\geq1$ let $\mathcal P_K$ be the space of even polynomials of degree at most $2K$, with the basis $e_k(s)=s^{2k}$, $1\leq k\leq K$. The <em>linearised map</em> at $V^*$ is the derivative of $\Phi_{\theta_0}$ at $V^*$ in the direction of $\mathcal P_K$, that is the matrix $\Lambda$ with</p>
<div class="math-display">$$\Lambda_{jk}=\frac{\partial}{\partial\epsilon}\Big|_{\epsilon=0}\bigl[\Phi_{\theta_0}(V^*+\epsilon e_k)\bigr]_j,$$</div>
<p>where the subscript $j$ denotes the coefficient of $e_j$. The <em>eigenvalue</em> of the direction $e_k$ is the diagonal entry $\Lambda_{kk}$.</p>
<p>The map is well defined on $\mathcal P_K$ because the integral is finite for a polynomial potential of even degree with a positive leading term, and the derivative exists because the dependence on $\epsilon$ is analytic in a neighbourhood of $0$.</p>

## Statement {#section-statement}

<a id="tag-G2TR" data-assertion="theorem" data-title="Diagonal eigenvalues of the linearised map at the Gaussian fixed point"></a>
<p>Let $1\leq k\leq K$ and $0&lt;\alpha&lt;d$. The matrix $\Lambda$ is upper triangular — the $k$-th column has no entries below the diagonal — and its diagonal entries are</p>
<div class="math-display">$$\Lambda_{kk}=L^{\,d(1-k)+k\alpha}.$$</div>
<p>Hence the eigenvalues of the linearisation on $\mathcal P_K$ are the numbers $\lambda_{2k}=L^{d(1-k)+k\alpha}$, $1\leq k\leq K$, independently of $K$. The direction of degree $2k$ is relevant for the Gaussian fixed point exactly when</p>
<div class="math-display">$$k&lt;\frac{d}{d-\alpha},$$</div>
<p>marginal when $k=d/(d-\alpha)$, and irrelevant otherwise. In particular $\lambda_2=L^\alpha$ is relevant for every $\alpha&gt;0$, and $\lambda_4=L^{2\alpha-d}$ is relevant exactly when $\alpha&gt;d/2$.</p>
:::details Proof
<p>Condition on the block spin: conditionally on $S=L^{\theta_0}s$ the children's deviations $\delta_a=s_a-S/m$ sum to zero, and their conditional law is Gaussian, centred, with a covariance that does not depend on $s$. This is the structure of <a href="/articles/hierarchical-phi4-truncations/#section-gaussian">the quartic computation</a>, and it holds for every $m$: the tilt is quadratic and the constraint is linear, so the conditional law of the children given their sum is a Gaussian measure on an affine hyperplane.</p>
<p>Writing $s_a=S/m+\delta_a$ and expanding,</p>
<div class="math-display">$$\sum_a s_a^{2k}=\sum_a\Bigl(\frac{S}{m}+\delta_a\Bigr)^{2k}=m\Bigl(\frac{S}{m}\Bigr)^{2k}+(\text{terms of degree at most }2k-1\text{ in }S),$$</div>
<p>because the coefficient of the top power of $S$ receives no contribution from $\delta$: the only term of degree $2k$ in $S$ is $\sum_a(S/m)^{2k}=S^{2k}/m^{2k-1}$. Taking the conditional expectation gives a polynomial in $S$ of degree at most $2k$ with leading coefficient $1/m^{2k-1}$ and no powers of $S$ above $2k$. Since the conditional expectation of a polynomial in the children of degree $2k$ is a polynomial in $S$ of degree at most $2k$, the map $e_k\mapsto\Phi_{\theta_0}(V^*+\epsilon e_k)-V^*$ has, to first order in $\epsilon$, no component in $e_j$ for $j&gt;k$: the matrix is upper triangular.</p>
<p>For the diagonal entry, the first variation of $-\log$ of the integral in the direction $e_k$ is the conditional expectation of $\sum_as_a^{2k}$ under the tilted Gaussian measure with $S$ fixed, whose leading $S$-coefficient is $m^{-(2k-1)}$; replacing $S$ by $L^{\theta_0}s$ multiplies the coefficient of $s^{2k}$ by $L^{2k\theta_0}$. Hence</p>
<div class="math-display">$$\Lambda_{kk}=L^{2k\theta_0}m^{-(2k-1)}=L^{k(d+\alpha)}L^{-d(2k-1)}=L^{\,d(1-k)+k\alpha}.$$</div>
<p>The criterion is $\Lambda_{kk}&gt;1$, that is $d(1-k)+k\alpha&gt;0$, which is $k(\alpha-d)&gt;-d$ and hence $k&lt;d/(d-\alpha)$ because $\alpha-d&lt;0$. For $k=1$ the entry is $L^\alpha&gt;1$; for $k=2$ it is $L^{2\alpha-d}$, which exceeds one exactly when $\alpha&gt;d/2$.</p>
:::
<p>The theorem is a statement about $\mathcal P_K$ for each $K$, and the entries do not depend on $K$; that is what makes it a computation of eigenvalues rather than of a truncation. It is not a spectral theorem for the full linearisation, which acts on an infinite-dimensional space of interactions and whose spectrum needs the analytic control of <a href="/articles/bleher-sinai-fixed-point/">the fixed-point analysis</a>.</p>

## The quartic coupling and the crossover {#section-quartic}

<p>The $k=2$ entry is the one that decides whether the Gaussian fixed point can be the critical theory of a model with a quartic term, and it is worth reading out in the two parametrisations.</p>
<p><em>Long range.</em> With the kernel exponent $\alpha$ as the variable, $\lambda_4=L^{2\alpha-d}$ is increasing in $\alpha$ and equals one at $\alpha=d/2$. Below that value the quartic coupling is irrelevant and the Gaussian fixed point is stable in its direction; above it the coupling is relevant and the fixed point is unstable, so the critical theory must be something else, which is the <a href="/articles/bleher-sinai-fixed-point/">non-Gaussian fixed point</a>.</p>
<p><em>Short range.</em> A model with summable, essentially finite-range interactions has $\alpha$ large; setting $\alpha=2$ as the representative value gives $\lambda_4=L^{4-d}$, marginal at $d=4$. The same formula produces the upper critical dimension without any further input, which is the sense in which power counting is a computation of the linearisation rather than a separate principle.</p>
<p>The two readings agree at their common point: for $\alpha=d/2$ one has $L^{2\alpha-d}=1$ whatever the dimension, so the quartic direction is marginal along the whole curve $\alpha=d/2$, which is the curve on which the classical and non-classical descriptions meet.</p>

## Consequences and applications {#section-consequences}

<p><em>The correction spectrum at the Gaussian fixed point.</em> The irrelevant entries of the same matrix are the corrections to scaling of <a href="/articles/corrections-to-scaling/">the corrections article</a>: for $k\geq2$ with $\lambda_{2k}&lt;1$, the correction exponent of the $k$-th direction is</p>
<div class="math-display">$$\omega_k=\frac{d(k-1)-k\alpha}{\log L},$$</div>
<p>a positive number, in the logarithmic units of that article. At the marginal value $\alpha=d/2$ the quartic entry is exactly one and the first correction becomes logarithmic, which is the mechanism behind the logarithmic corrections at the marginal exponent.</p>

<p><em>What "relevant" buys.</em> The theorem says that the Gaussian fixed point is unstable in the quartic direction above $d/2$; it does not produce the stable fixed point, and the passage from the instability to the exponents is the content of the fixed-point literature. Reading it the other way is the useful direction for a proof: if a model with a quartic term has a critical theory whose linearisation has a one-dimensional unstable manifold and the Gaussian fixed point is unstable in the quartic direction at the same parameter values, the critical theory cannot be Gaussian.</p>

<p><em>Vector models.</em> For $r$ components the Gaussian fixed point is a product of $r$ independent scalar ones, so the linearisation has the same entries in each component; an $O(r)$-symmetric quartic perturbation has the same $k=2$ eigenvalue, and the counting of relevant directions is unchanged. This is the computation behind the statement in <a href="/articles/hierarchical-vector-models/#section-exponents">the vector article</a> that the Gaussian exponents do not depend on $r$.</p>

## Examples and non-examples {#section-examples}

<p><em>One dimension, $\alpha=\tfrac12$.</em> Then $\lambda_4=2^{1-1}=1$: the quartic direction is marginal, and the expansion of the exponents in $\alpha-d/2$ starts at order one in the departure. The numerical diagonalisation of the finite-dimensional linearisation gives $0.999987$ for this entry, the discrepancy being the truncation of the fit.</p>

<p><em>One dimension, $\alpha=0.3$.</em> Then $\lambda_4=2^{-0.4}=0.758$: irrelevant, so the Gaussian fixed point is stable in the quartic direction and the classical exponents hold, consistently with the region $\alpha&lt;d/2$ of the <a href="/articles/critical-exponents-from-rg/#section-examples">exponent dictionary</a>.</p>

<p><em>Three dimensions, short range.</em> With $\alpha=2$, $\lambda_4=2^{4-3}=2&gt;1$: relevant, which is why three-dimensional phi-fourth theory is not mean-field.</p>

<p><em>Non-example: the nontrivial fixed point.</em> Nothing here computes the spectrum at the non-Gaussian fixed point, and its eigenvalues are not the numbers above; a common error is to read the relevance of the quartic coupling at the Gaussian fixed point as the exponent of a correction at the critical fixed point.</p>

<p><em>Non-example: a non-polynomial perturbation.</em> The triangle is a statement about the monomial basis; a perturbation with a non-analytic dependence on $s$ is outside $\mathcal P_K$ and the argument says nothing about it. The linearisation on a space of measures acts on a larger space, which is why the rigorous analyses work with analytic norms.</p>

## Variants and generalisations {#section-variants}

<p><em>Ultrametric block systems.</em> Only $m$ and $\theta_0$ enter, so the formula holds verbatim on any block system of <a href="/articles/ultrametric-block-systems/">the general article</a> with branching $m$, including the p-adic integers, where $m$ is the prime.</p>

<p><em>Other single-spin spaces.</em> The computation uses the Gaussian fixed point, so it applies to any model whose fixed point is Gaussian: a $q$-state Potts model, or percolation, has a different fixed-point structure and the eigenvalues must be computed there. The counting of relevant directions at a Gaussian fixed point, however, depends only on the dimension and the kernel exponent.</p>

<p><em>Anisotropic perturbations.</em> A perturbation that depends on a direction in spin space rather than on the radius is a separate direction; at the Gaussian fixed point such perturbations evolve with the eigenvalue of their degree, and the counting of relevant directions is unchanged.</p>

## History and attribution {#section-history}

<p>The classical long-range exponent values, and the threshold at which they cease to hold, are those of Fisher, Ma and Nickel [@fisher-ma-nickel-1972]. The expansion of the exponents in the departure from the marginal exponent, which is the quantitative form of the statement that the quartic direction is marginal there, is due to Gawedzki and Kupiainen [@gawedzki-kupiainen-1983]. The fixed-point analysis in which these eigenvalues are the linearisation at the Gaussian fixed point is that of Bleher and Sinai [@bleher-sinai-1975]. The presentation of power counting as the linearisation of a map at a Gaussian fixed point is the one used in the renormalisation-group treatment of lattice fields [@bauerschmidt-brydges-slade-2019].</p>

## References {#section-references}

<ul>
<li>R. Bauerschmidt, D. C. Brydges and G. Slade, <em>Introduction to a Renormalisation Group Method</em>, Lecture Notes in Mathematics 2242, Springer, 2019.</li>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>M. E. Fisher, S.-k. Ma and B. G. Nickel, Critical exponents for long-range interactions, <em>Phys. Rev. Lett.</em> 29 (1972), 917&ndash;920.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian fixed points of the block spin transformation. Hierarchical model approximation, <em>Comm. Math. Phys.</em> 89 (1983), 191&ndash;220.</li>
</ul>
