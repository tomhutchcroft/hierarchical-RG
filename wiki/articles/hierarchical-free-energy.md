---
{
  "id": "hierarchical-free-energy",
  "title": "The free energy and its singularity",
  "subtitle": "The recursion summed scale by scale, the Gaussian case in closed form, and where the curvature diverges.",
  "kind": "theorem",
  "category": "Renormalisation group",
  "summary": "The free energy of a hierarchical model is a sum over scales, one elementary term per decimation step, and for a Gaussian prior each term is a Gaussian integral in closed form. That gives the free energy of the Gaussian model as an explicit series, convergent exactly up to the critical intensity, and a curvature that diverges there. The same computation gives the classical specific-heat exponent by a scaling argument, and the argument shows why the Ising case, where no term is elementary, cannot be treated this way.",
  "context": [
    "The model of the decimation article: block volume $m=L^d$, couplings $J_k=JL^{-(d+\\alpha)k}$, free energy per site $F_n=m^{-n}\\log Z_n$.",
    "The Gaussian prior $\\varrho=N(0,1)$ and the block-spin variance $v_n$ of the Gaussian article; $C=\\sum_{x\\neq0}J(\\lVert x\\rVert)$ and $\\beta_c=1/C$."
  ],
  "related": [
    "hierarchical-gibbs-measure",
    "gaussian-renormalisation-group",
    "critical-exponents-from-rg",
    "corrections-to-scaling"
  ],
  "sourceIds": ["bleher-sinai-1973"],
  "aliases": [
    "free energy",
    "specific heat",
    "heat capacity",
    "logarithmic correction",
    "singularity"
  ]
}
---

<p><a href="/articles/hierarchical-gibbs-measure/#section-free-energy">The decimation article</a> proves that the free energy per site converges, $F=\lim_nF_n$, and that it is convex in the intensity. It does not say what $F$ is, or what happens to it at the critical intensity, and those are the two questions this article answers for the one case in which they can be answered by computation.</p>

<p>The mechanism is the per-scale decomposition. Each decimation step contributes one term to $F$, the logarithm of an expectation taken over $m$ independent copies of the block spin one scale down; for a Gaussian prior that expectation is an integral of a quadratic form, and for a Gaussian vector the sum of the components and the sum of their squares are independent. So the term is a product of two one-dimensional Gaussian integrals, and the whole free energy is an explicit series. Nothing in the Ising case is elementary, and the last section says what survives there.</p>

## The per-scale terms {#section-terms}

<a id="tag-6D6N" data-assertion="proposition" data-title="The Gaussian free energy is an explicit series, one term per scale"></a>
<p>Let $\varrho=N(0,1)$, $b_k=\beta J_k$, and $v_n$ the variance of the block spin of $\Lambda_n$, which is $v_n=m^n/(1-\beta C_n)$ with $C_n=\sum_{x\in\Lambda_n\setminus0}J(\lVert x\rVert)$. Then</p>
<div class="math-display">$$F=\sum_{k\geq1}\frac{1}{m^k}\Bigl[-\tfrac12\log\bigl(1-b_k(m-1)v_{k-1}\bigr)-\tfrac{m-1}{2}\log\bigl(1+b_kv_{k-1}\bigr)\Bigr],$$</div>
<p>and the series converges uniformly on $0\leq\beta\leq\beta_c^{\mathrm G}=1/C$. Consequently $F$ is continuous on that interval and real analytic in its interior — while its second derivative diverges as $\beta\uparrow\beta_c$, which is where the transition is.</p>
:::details Proof
<p>By <a href="/articles/hierarchical-gibbs-measure/#section-free-energy">the free energy recursion</a>, the level-$k$ increment of $F$ is $m^{-k}$ times the logarithm of $\mathbb E[\exp(b_k\sum_{a&lt;a'}s_as_{a'})]$ over $m$ independent copies of $\mu_{k-1}$, which for the Gaussian prior is $N(0,v_{k-1})$. The exponent is the quadratic form of the matrix that is $\tfrac12$ off the diagonal and $0$ on it, whose eigenvalues are $\tfrac{m-1}{2}$ along the diagonal direction and $-\tfrac12$ on its orthogonal complement. In an orthonormal eigenbasis the coordinates are independent $N(0,v_{k-1})$, so the expectation factorises into $m$ one-dimensional Gaussian integrals, one with coefficient $b_k(m-1)$ and $m-1$ with coefficient $-b_k$:</p>
<div class="math-display">$$\bigl(1-b_k(m-1)v_{k-1}\bigr)^{-1/2}\bigl(1+b_kv_{k-1}\bigr)^{-(m-1)/2}.$$</div>
<p>The variance $v_{k-1}=m^{k-1}/(1-\beta C_{k-1})$ is the <a href="/articles/gaussian-renormalisation-group/#section-critical">closed form of the Gaussian article</a>. For convergence, put $\varepsilon=\beta_c-\beta\geq0$. For $k$ large enough that $\beta C_{k-1}$ is within $\varepsilon C$ of one, $v_{k-1}\asymp m^{k-1}/(\varepsilon C)$ and hence</p>
<div class="math-display">$$b_k(m-1)v_{k-1}\asymp\frac{(m-1)\beta}{L^d\,C\,\varepsilon}\,L^{-\alpha k},$$</div>
<p>which is $O(L^{-\alpha k}/\varepsilon)$ and so bounded by a constant depending on $\varepsilon$ but not on $k$; the second factor's argument lies between one and two. Hence each term is at most $m^{-k}$ times a constant, uniformly in $k$ and in $\beta\in[0,\beta_c]$, which gives the uniform convergence, the continuity of $F$ and its analyticity in the interior. The constant degenerates as $\varepsilon\downarrow0$, and that degeneration is what the divergence of the second derivative measures.</p>
:::
<p>Two features of the display are worth naming. The first factor is the one the variance recursion knows about: its argument is $1-b_k(m-1)v_{k-1}$, whose vanishing is exactly the blow-up of <a href="/articles/gaussian-renormalisation-group/#section-closure">the variance recursion</a>, so the free energy integral and the recursion fail at the same place. The second factor is the price of summing over the block's internal freedom: it comes from the $m-1$ directions of the tilt that are not the diagonal one, which the variance does not see, and without it the free energy would be a sum of the terms the recursion controls.</p>

## The singularity {#section-singularity}

<p>The series is explicit, so its singularity can be located exactly in the variable that matters, the distance to the critical intensity.</p>
<div class="fig" data-fig="free-energy" data-title="The Gaussian free energy per site and its curvature, against the intensity as a fraction of the critical one, for d = 1 and alpha = 1/2. Both are normalised by their largest plotted value, so the two curves are comparable in height rather than in units; the vertical line is the critical intensity, where the curvature diverges and the free energy itself stays finite and continuous."></div>
<p>The figure is the statement in one picture. $F$ increases and remains finite up to the critical intensity, which is what the uniform convergence gives; the curvature increases without bound, so $F$ is continuously differentiable but not twice so, and the transition is second order. Neither feature is special to the Gaussian case: what is special is that here the two can be computed.</p>
<p>The exponent can be read off the same series by a scaling argument, and it is worth recording because it is the dictionary's hyperscaling relation derived rather than assumed. Write $\varepsilon=\beta_c-\beta$. Differentiating the $k$-th term twice in $\beta$ brings down a factor $\varepsilon^{-2}$ from its dependence through $1-\beta C_{k-1}$, for the scales at which that denominator is of order $\varepsilon$; those are the scales with $L^{-\alpha k}\asymp\varepsilon$, and each carries the weight $m^{-k}\asymp\varepsilon^{d/\alpha}$. All other scales contribute less, so</p>
<div class="math-display">$$F''(\beta)\ \asymp\ \varepsilon^{d/\alpha}\cdot\varepsilon^{-2}=\varepsilon^{-(2-d/\alpha)},$$</div>
<p>so the heat capacity $C_V=\beta^2F''$ diverges like $\varepsilon^{-(2-d/\alpha)}$ — that is, the specific-heat exponent is $\alpha_{\mathrm{hy}}=2-d/\alpha$, which is what <a href="/articles/critical-exponents-from-rg/#section-dictionary">the dictionary</a> obtains from hyperscaling once $\nu=1/\alpha$. At $d/\alpha=2$, which for $d=1$ is $\alpha=1/2$, the exponent vanishes and the divergence is logarithmic; the finite sum plotted above cannot distinguish a logarithm from a small power, and the argument is what distinguishes them. This derivation is a scaling argument, not a proof: it identifies the terms that dominate and their weight, and a proof would need the sum bounded above and below uniformly in $\varepsilon$, which is not done here.</p>

## What survives for Ising spins {#section-ising}

<p>Nothing in the derivation is available for the Ising prior. The per-scale expectation is an average over $m$ integer-valued spins, it is not a Gaussian integral, and its logarithm is not elementary; the recursion for the law of the block spin is the only access, and it is infinite-dimensional. What survives is everything that did not use the closed form: the free energy exists and is convex and continuous, the per-scale decomposition holds with the expectation written as it stands, and the location of the singularity is the intensity at which the orbit leaves the domain of attraction of the trivial fixed point — which is <a href="/articles/bleher-sinai-fixed-point/">the trichotomy</a>, not a computation.</p>
<p>So the honest summary of the specific heat for the Ising model in this wiki is: the dictionary's relation $\alpha_{\mathrm{hy}}=2-d\nu$ holds if hyperscaling does, the value of $\nu$ is known only through the linearisation at the nontrivial fixed point, and the free energy's own curvature is not computed anywhere. The Gaussian case is the one in which the three statements are a computation, and that is why it is recorded separately rather than as a remark in the exponent article.</p>

## Variants and generalisations {#section-variants}

<p><em>Other priors with a closed form.</em> The derivation used only that the prior is Gaussian, so that $S$ and $Q$ are independent. For a prior that is a mixture of Gaussians the same computation gives a sum over the mixture, and the per-scale term becomes a finite sum of logarithms; for a prior with a quartic term the integral is not elementary and the series in $\beta$ is only asymptotic, which is where <a href="/articles/koch-wittwer-fixed-point/">the large-field problem</a> begins.</p>

<p><em>An external field.</em> A field adds a linear term to the tilt, the Gaussian integral still closes, and the per-scale term gains a factor depending on the field and on the block spin's mean; the free energy then has a singularity along the whole critical curve rather than at a point. The wiki does not develop this, and the reason is that the field's recursion in <a href="/articles/renormalisation-group-map/">the map article</a> is a separate argument.</p>

<p><em>The single-file edition.</em> The numbers in the figure come from <code>free_energy</code> in <code>tools/simulate.py</code>, which is the series above truncated after eighty scales; the truncation error at the intensities plotted is below the resolution of the drawing, and the closed form of the first two terms is checked against direct two-dimensional quadrature in <code>tools/numeric_checks.py</code>.</p>
