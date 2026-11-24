---
{
  "id": "bleher-sinai-fixed-point",
  "title": "The Bleher–Sinai fixed point",
  "subtitle": "Above the threshold a non-Gaussian law is self-similar, and its multiplier is not one over alpha.",
  "kind": "theorem",
  "category": "Renormalisation group",
  "summary": "For kernel exponent above half the dimension the critical orbit of the hierarchical recursion converges to a self-similar law that is not Gaussian: the fixed point of Bleher and Sinai and of Gawedzki and Kupiainen. Its linearisation has a simple leading eigenvalue, which gives a correlation-length exponent different from the classical one over alpha, and a spectrum whose next eigenvalue controls corrections to scaling, sometimes oscillating.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$, kernel exponent $0\\lt \\alpha\\lt d$.",
    "The prior is $\\pm1$ spins or a symmetric law with exponential tails; $b=\\beta J_1$ and $\\theta_0=\\tfrac12(d+\\alpha)$.",
    "The threshold of this article is $\\alpha=d/2$, the value at which the classical long-range exponents meet the Ising ones."
  ],
  "related": [
    "renormalisation-group-map",
    "gaussian-renormalisation-group",
    "critical-exponents-from-rg",
    "hierarchical-and-euclidean-rg"
  ],
  "sourceIds": [
    "bleher-sinai-1973",
    "bleher-sinai-1975",
    "gawedzki-kupiainen-1983",
    "gawedzki-kupiainen-1984",
    "sinai-1982"
  ],
  "aliases": [
    "non-Gaussian fixed point",
    "nontrivial fixed point",
    "Bleher–Sinai",
    "epsilon expansion",
    "crossover"
  ]
}
---

<p>For $\alpha$ above half the dimension the critical orbit of the hierarchical recursion does not settle at a Gaussian law. It converges instead to a self-similar law $\nu^*$ which is symmetric, has exponential tails and finite variance, and is not Gaussian; the multiplier of the linearised map there is a number $\lambda_1&gt;1$ other than $L^{\alpha}$, and the correlation-length exponent $\nu=\log L/\log\lambda_1$ therefore differs from the classical value $1/\alpha$. The existence of such a law, the convergence of the orbit to it, and the reading of the indices from the linearisation are the results of Bleher and Sinai (1973, 1975) for Dyson's model [@bleher-sinai-1973] [@bleher-sinai-1975]; the local analysis of the map around the fixed point, including the $\varepsilon$-expansion and the normal form of the unstable manifold, is due to Gawedzki and Kupiainen [@gawedzki-kupiainen-1983].</p>

<p>The threshold $\alpha=d/2$ is where the classical long-range exponents stop being the Ising ones. At $\alpha=d/2$ the classical values are $\nu=2/d$, $\eta=2-d/2$, $\delta=3$ and $\beta_{\mathrm{o}}=\tfrac12$, which are the mean-field values with $\nu$ adjusted by hyperscaling; below it the classical values hold, and above it the nontrivial fixed point takes over. In the language of <a href="/articles/critical-exponents-from-rg/">the exponent dictionary</a> the growth exponent is still $\kappa=\alpha$, because the autonomy of the recursion fixes it, and what changes is $\nu$ alone.</p>

<p>Two features make this the hard case and the reason the hierarchical model is worth studying. The fixed point is not explicit: it is the solution of a nonlinear integral equation, and its existence is proved by a combination of an invariant cone, a truncation and a contraction. And the map is not contracting everywhere: the leading eigenvalue exceeds one, so the interesting statement is about the unstable manifold of dimension two, which is what makes the critical exponents well defined at all. The rest of this article states the theorem, gives the mechanism of its proof, and describes the spectrum.</p>

## Definitions and setting {#section-setting}

<p>Let $\mathcal E$ be the set of Borel probability measures on $\mathbb R$ that are symmetric, $\mu(A)=\mu(-A)$, have $\int s^2d\mu(s)\in(0,\infty)$, and satisfy $\int e^{cs^2}d\mu(s)&lt;\infty$ for some $c&gt;0$ depending on $\mu$. The <a href="/articles/renormalisation-group-map/#section-definition">decimation operator</a> $\mathcal T_b$ and its rescaled form $\mathcal R_{\theta,b}$ act on $\mathcal E$ when they are defined, and the model's orbit is $\nu_n=\mathcal R_{\theta_0,b_1}^{\,n}\nu_0$ with $\theta_0=\tfrac12(d+\alpha)$ and $b_1=\beta J_1$ by <a href="/articles/renormalisation-group-map/#section-autonomous">the autonomous form</a>.</p>
<a id="tag-B2SR" data-assertion="definition" data-title="Critical coupling of the rescaled recursion"></a>
<p>The <em>critical coupling</em> $b_c=b_c(m,\lambda)$ is the value of $b$ at which the orbit of the Ising initial law $\nu_0=\tfrac12(\delta_{-1}+\delta_1)$ under $\mathcal R_{\theta_0,b}$ neither converges to the point mass at $0$ nor leaves every compact set of laws with bounded variance; it is the value $b_c=\beta_cJ_1$ at which $\beta_c$ is the critical intensity of the model.</p>
<p>The Gaussian laws form an invariant family, and the fixed points of the rescaled map inside that family are computed by one line of algebra. The computation is the reference point for everything else, so it is stated first.</p>
<a id="tag-S8FR" data-assertion="proposition" data-title="Gaussian fixed points of the rescaled map"></a>
<p>Let $b&gt;0$ and $\theta=\tfrac12(d+\alpha)$. The map $\mathcal R_{\theta,b}$ sends $N(0,v)$ to $N(0,w)$ with</p>
<div class="math-display">$$w=\frac{mv}{\lambda\bigl(1-bv(m-1)\bigr)},\qquad \lambda=L^{d+\alpha},$$</div>
<p>and has the unique Gaussian fixed point $N(0,v_b)$ with $v_b=\dfrac{\lambda-m}{\lambda b(m-1)}$. At $b=b_1^{(0)}=\dfrac{\lambda-m}{\lambda(m-1)}$ this fixed point is $N(0,1)$ and the multiplier of $\mathcal R_{\theta,b}$ in the variance direction is $\lambda/m=L^{\alpha}$.</p>
:::details Proof of the fixed-point equation and the multiplier
<p>The first display is the <a href="/articles/gaussian-renormalisation-group/#section-closure">variance recursion</a> composed with the rescaling $v\mapsto L^{-2\theta}v$. A fixed point satisfies $v=\frac{mv}{\lambda(1-bv(m-1))}$ with $v&gt;0$, which is $\lambda(1-bv(m-1))=m$, that is $v=v_b$; the normalisability condition $bv(m-1)&lt;1$ holds because $bv_b(m-1)=1-m/\lambda&lt;1$.</p>
<p>At $b=b_1^{(0)}$ the variance is $v=\frac{\lambda-m}{\lambda(m-1)}\cdot\frac{\lambda(m-1)}{\lambda-m}=1$. The derivative of $w$ in $v$ at the fixed point is $\frac{m}{\lambda}\cdot\frac{1}{(1-bv(m-1))^2}=\frac{m}{\lambda}\cdot\frac{\lambda^2}{m^2}=\frac{\lambda}{m}$, using $1-bv_b(m-1)=m/\lambda$.</p>
:::
<p>For the Ising prior the fixed point is not Gaussian. This is the content of the theorem below; the proposition above shows only that the Gaussian candidate at the Ising critical coupling would have to be $N(0,v_{b_c})$, a single number, and the theorem says that the critical law is a different one.</p>

## Statement {#section-statement}

<a id="tag-B7WD" data-assertion="theorem" data-title="Existence, uniqueness and attractivity of the nontrivial fixed point"></a>
<p>Let $0&lt;\alpha&lt;d$. There is a coupling $b_c\in(0,\infty)$ and a law $\nu^*\in\mathcal E$ such that:</p>
<p>(i) $\mathcal R_{\theta_0,b_c}\nu^*=\nu^*$, and $\nu^*$ is not Gaussian when $\alpha&gt;d/2$;</p>
<p>(ii) the orbit of the Ising initial law converges weakly to $\nu^*$ when $b=b_c$, to $\delta_0$ when $b&lt;b_c$, and to a law of unbounded variance when $b&gt;b_c$;</p>
<p>(iii) the linearisation $D\mathcal R$ at $\nu^*$ is a compact operator on the space of symmetric signed measures of zero mass with finite exponential moments, its spectrum consists of a simple eigenvalue $\lambda_1&gt;1$ together with the rest inside a disk of radius $\rho&lt;1$, and complex pairs occur among the remaining eigenvalues;</p>
<p>(iv) consequently the correlation-length exponent is $\nu=\log L/\log\lambda_1$, and it differs from $1/\alpha$ when $\alpha&gt;d/2$.</p>
<p>The statements are those of Bleher and Sinai [@bleher-sinai-1973] [@bleher-sinai-1975]; the local analysis of (iii), the $\varepsilon$-expansion of $\lambda_1$ in powers of $\alpha-d/2$, and the normal form of the unstable manifold are in Gawedzki and Kupiainen [@gawedzki-kupiainen-1983].</p>
<p>Below the threshold the Gaussian fixed point is the critical one, and the exponents are the classical values.</p>
<a id="tag-D3LT" data-assertion="theorem" data-title="Classical region and the crossover at alpha equal to half the dimension"></a>
<p>For $0&lt;\alpha&lt;d/2$ the critical orbit of the Ising initial law converges, after rescaling, to a Gaussian law, and the exponents take the classical values of <a href="/articles/gaussian-renormalisation-group/#section-exponents">the Gaussian fixed point</a>. At $\alpha=d/2$ the nontrivial fixed point merges with the Gaussian one, $\lambda_1\to L^{d/2}$, and the classical values hold with logarithmic corrections.</p>
<p>The arithmetic that connects the two statements is the proposition above: at $\alpha=d/2$ the classical correlation-length exponent is $1/\alpha=2/d$, so $\lambda_1=L^{d/2}$, and the two fixed points coincide at that value of the multiplier. The identification of the critical fixed point for $\alpha&lt;d/2$ with the Gaussian one, and of the exponents with the classical values, is the content of the classical region in Bleher and Sinai [@bleher-sinai-1975]; the Euclidean counterpart at the same threshold is due to Aizenman and Fernandez [@aizenman-fernandez-1988].</p>
<p>The two theorems together describe a bifurcation: at $\alpha=d/2$ a nontrivial fixed point separates from the Gaussian one as $\alpha$ increases, taking over the critical behaviour. The exponents move continuously from the classical values at the threshold, which is why the classical formulas remain a good approximation just above $d/2$ and why the $\varepsilon$-expansion is organised in powers of $\alpha-d/2$ rather than in powers of a coupling.</p>

## Examples and non-examples {#section-examples}

<p><em>The Gaussian case as the threshold member.</em> For every $b$ the rescaled map has exactly one Gaussian fixed point, of variance $v_b$; at the Gaussian model's critical coupling $b_1^{(0)}$ it is $N(0,1)$ with multiplier $L^{\alpha}$. The classical exponents are therefore a one-parameter family in $\alpha$, and the threshold $\alpha=d/2$ is where $\nu=1/\alpha$ meets the mean-field value $2/d$.</p>

<p><em>One dimension, $\alpha\in(\tfrac12,1)$.</em> Here $d=1$ and the threshold is $\alpha=\tfrac12$: below it the classical values $\nu=1/\alpha$, $\delta=\frac{1+\alpha}{1-\alpha}$ hold; above it the nontrivial fixed point governs, and $\delta=\frac{1+\alpha}{1-\alpha}$ is still the conjectured value while $\nu$ is not $1/\alpha$. This is Dyson's original model, and the phase transition exists for every $\alpha&lt;1$ with $\beta_c&lt;\infty$ exactly in that range.</p>

<p><em>Non-example: a law with heavy tails.</em> If the prior has a density decaying like $\lvert s\rvert^{-p}$ with $p$ large, the tilt is not normalisable for any $b&gt;0$ and the orbit is undefined. The class $\mathcal E$ is chosen to exclude this: the exponential moment is what makes the tilt integrable and what makes the linearisation compact.</p>

<p><em>Non-example: the orbit above criticality.</em> For $b&gt;b_c$ the rescaled variance grows without bound; the block spin per site has a nonzero limit and the law concentrates on the two points $\pm M$ with $M$ the spontaneous magnetisation. That limit is a fixed point of the map only in the degenerate sense of a law with infinite variance after rescaling, and it is not in $\mathcal E$.</p>

## Idea of the proof {#section-idea}

<p>The argument has four parts, and only the first is elementary.</p>

<p><em>An invariant class.</em> The tilt $\exp(b\sum_{a&lt;a'}s_as_{a'})$ grows at most like $\exp(\tfrac b2(\sum_as_a)^2)\leq\exp(\tfrac{bm}{2}\sum_as_a^2)$, and the sum $\sum_as_a$ of $m$ variables with exponential moments has exponential moments with a constant depending on $m$ and $b$. Hence $\mathcal R_{\theta,b}$ maps $\mathcal E$ into a subset of itself on which the exponential constant is bounded in terms of $b$ and the input constant. This gives compactness: a sequence of laws in $\mathcal E$ with a uniform exponential constant is tight with uniformly integrable moments, so every orbit has convergent subsequences.</p>

<p><em>A truncation.</em> The tilt is replaced by $\exp(b\sum_{a&lt;a'}s_as_{a'})$ cut off at $\lvert s\rvert\leq K$, which is bounded and continuous; the truncated map is continuous on the laws supported in $[-K,K]$, and an invariant compact convex set plus Schauder's theorem gives a fixed point for each $K$. The a priori bounds of the first part are uniform in $K$, and a limit of fixed points as $K\to\infty$ along a subsequence is a fixed point of the original map.</p>

<p><em>Identification of the critical coupling.</em> The orbit from the Ising initial law is compared with the orbits of the Gaussian family: below a certain $b$ the variance decreases geometrically to zero, above it the variance grows geometrically, and $b_c$ is the value between. Since the variance recursion of the Gaussian family is explicit, the two regimes can be separated by explicit inequalities, and the fixed point at $b_c$ is the limit of the critical orbit.</p>

<p><em>The linearisation.</em> The derivative of $\mathcal R_{\theta_0,b_c}$ at $\nu^*$ is the sum of two terms: the linearisation of the tilt, which is a bounded integral operator with kernel $\sum_{a&lt;a'}(s_as_{a'}-\mathbb E[s_as_{a'}])$, and the linearisation of the summation and rescaling, which is the dilation composed with the $m$-fold convolution. The second is the operator whose spectrum at the Gaussian fixed point is computed by the variance multiplier; the first is a compact perturbation, so the spectrum is discrete with the leading eigenvalue simple by a Perron-Frobenius argument on the cone of positive perturbations. Composing, one obtains $\lambda_1$ as the leading eigenvalue and $L^{\alpha}$ as the value it takes at the Gaussian fixed point.</p>

<p>What this sketch does not do is exhibit the fixed point or prove the convergence, and those are the substance of the two papers cited. The point of writing it out is to locate where each hypothesis is used: exponential moments give compactness, truncation gives existence, comparison with the Gaussian family gives the critical coupling, and compactness of the perturbation gives simplicity of the leading eigenvalue.</p>

## The spectrum {#section-spectrum}

<p>The eigenvalues of the linearisation are the exponents and their corrections, so their structure is worth stating separately.</p>
<p>The leading eigenvalue $\lambda_1&gt;1$ is the thermal direction: a perturbation of the critical coupling changes the orbit by a factor $\lambda_1$ per scale, and inverting gives $\xi\asymp\lvert\beta_c-\beta\rvert^{-\nu}$ with $\nu=\log L/\log\lambda_1$. The second eigenvalue $\mu_1$ is the leading correction: it multiplies the $n$-th scale by $\mu_1^n$, so each power law acquires a factor $1+O(\lvert\mu_1\rvert^n)$ in the scale variable, that is a correction of order $\xi^{-\lvert\log\lvert\mu_1\rvert\rvert/\log L}$. A pair of complex conjugate eigenvalues $\mu_1,\bar\mu_1$ replaces that factor by $1+O(\lvert\mu_1\rvert^n\cos(n\arg\mu_1))$, which is an oscillation in $\log\lvert x\rvert$ and is visible in the hierarchical model's numerical exponents as a modulation of the corrections; the $\varepsilon$-expansion and the normal-form analysis of this phenomenon are in Gawedzki and Kupiainen [@gawedzki-kupiainen-1983].</p>
<p>The magnetic direction is the second relevant one, and it is not an eigenmeasure of the zero-field map: it appears when the recursion is carried with a field, as a derivative in the field at zero. Its eigenvalue is the number that enters $\delta$; in the classical regime it gives the value $\frac{d+\alpha}{d-\alpha}$ through the dictionary of <a href="/articles/critical-exponents-from-rg/#section-dictionary">the exponent article</a>.</p>

## Variants and generalisations {#section-variants}

<p><em>The scaling limit.</em> The decay of the orbit to $\nu^*$ at the rate $\lambda_1^{-n}$ is what makes the scaling limit exist: after centring and rescaling by $\xi^{\theta_0}$, the block-spin process converges to a nontrivial limit whose law is determined by $\nu^*$ and the unstable manifold. This is the content of Gawedzki and Kupiainen's second paper [@gawedzki-kupiainen-1984], and it is the analogue for the hierarchical model of the construction of a critical Euclidean field theory.</p>

<p><em>Other initial laws.</em> The domain of attraction of $\nu^*$ is a codimension-one set of initial laws: the critical manifold. Any symmetric prior with exponential moments whose orbit meets that manifold converges to $\nu^*$, so the exponents depend on $\alpha$ and $d$ and not on the prior. This is the hierarchical model's version of universality, and it is a theorem here rather than a hypothesis.</p>

<p><em>The $\varphi^4$ parametrisation.</em> Writing the prior as $e^{-\lambda s^4-\frac{\mu}{2}s^2}ds$ and following the orbit of $(\lambda,\mu)$ gives the flow on the two-dimensional truncation of the space of interactions, which has the same bifurcation structure at $\alpha=d/2$; the truncation is not closed, and the exact statement requires the full infinite-dimensional map.</p>

## History and attribution {#section-history}

<p>Bleher and Sinai introduced the renormalisation transformation of the hierarchical model and proved the existence of the nontrivial fixed point, the trichotomy of the orbit and the formula for the indices in terms of the linearisation [@bleher-sinai-1973] [@bleher-sinai-1975]; Sinai's monograph is the systematic account of the framework of limit Gibbs distributions in which the model sits [@sinai-1982]. Gawedzki and Kupiainen gave the local analysis: the $\varepsilon$-expansion around $\alpha=d/2$, the unstable manifold and its normal form, and the convergence of the rescaled correlations to a nontrivial scaling limit [@gawedzki-kupiainen-1983] [@gawedzki-kupiainen-1984]. The identification of the classical region with the mean-field exponents, in the Euclidean setting and at the same threshold, is due to Aizenman and Fernandez [@aizenman-fernandez-1988].</p>

## References {#section-references}

<ul>
<li>M. Aizenman and R. Fernandez, Critical exponents for long-range interactions, <em>Lett. Math. Phys.</em> 16 (1988), 39&ndash;49.</li>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian fixed points of the block spin transformation. Hierarchical model approximation, <em>Comm. Math. Phys.</em> 89 (1983), 191&ndash;220.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian scaling limits. Hierarchical model approximation, <em>J. Statist. Phys.</em> 35 (1984), 267&ndash;284.</li>
<li>Ya. G. Sinai, <em>Theory of Phase Transitions: Rigorous Results</em>, Pergamon Press, 1982.</li>
</ul>
