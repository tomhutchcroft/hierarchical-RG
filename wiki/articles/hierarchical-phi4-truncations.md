---
{
  "id": "hierarchical-phi4-truncations",
  "title": "The phi-fourth hierarchical model and its truncations",
  "subtitle": "The recursion is an integral operator on potentials; the Gaussian truncation is exact and every other truncation leaks.",
  "kind": "model",
  "category": "Hierarchical models",
  "summary": "Written on potentials rather than on laws, the decimation step is an explicit integral operator: the effective potential of a block is minus the logarithm of a constrained convolution of the child potential. Quadratic potentials are mapped to quadratic potentials and the flow on them is the fractional linear recursion for the variance; quartic and higher truncations are not invariant, because the constrained average of a quartic generates powers of every even order. The two rigorous treatments of the resulting infinite-dimensional flow are Koch and Wittwer's fixed point and, in the Euclidean setting, the trajectory of Abdesselam.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$; coupling $b$ between distinct children; $\\theta_0=\\tfrac12(d+\\alpha)$.",
    "Potentials $V:\\mathbb R\\to\\mathbb R$ even, bounded below, with $\\int e^{-V(s)}ds<\\infty$ and Gaussian moments.",
    "The marginal exponent of the quartic coupling is $\\alpha=d/2$; for $\\alpha&lt;2$ this is the only threshold relevant to the long-range family."
  ],
  "related": [
    "hierarchical-vector-models",
    "gaussian-renormalisation-group",
    "koch-wittwer-fixed-point",
    "abdesselam-global-trajectory",
    "bleher-sinai-fixed-point"
  ],
  "sourceIds": ["bleher-sinai-1973", "bleher-major-1984", "koch-wittwer-1986", "abdesselam-2007", "fisher-ma-nickel-1972", "bauerschmidt-brydges-slade-2019"],
  "aliases": [
    "phi-fourth model",
    "quartic truncation",
    "effective potential",
    "upper critical dimension",
    "epsilon expansion",
    "low temperature phase"
  ]
}
---

<p>In the <a href="/articles/hierarchical-gibbs-measure/">hierarchical model</a> with a spin prior of the form $e^{-V(s)}ds$ the state of the recursion is a potential, not a number: after one decimation step the block spin has a density whose negative logarithm is the <em>effective potential</em>, computed from the child potential by a constrained convolution. The recursion is exact and it is an operation on an infinite-dimensional space; the question is which finite-dimensional families it leaves invariant, and the answer is that only the quadratic one does. Write $V(s)=\tfrac{\mu}{2}s^2+\lambda s^4$; the Gaussian part flows by a fractional linear recursion solved in <a href="/articles/gaussian-renormalisation-group/">the Gaussian article</a>, and the quartic part generates powers of every even order, so a two-coupling truncation is an approximation whose error is not controlled by the recursion itself [@bleher-sinai-1973].</p>

<p>The two rigorous treatments of the full flow are Koch and Wittwer's proof of a nontrivial fixed point for scalar hierarchical models [@koch-wittwer-1986], described in <a href="/articles/koch-wittwer-fixed-point/">this wiki's article on it</a>, and, in the Euclidean setting, Abdesselam's construction of a complete trajectory between the Gaussian and nontrivial fixed points [@abdesselam-2007], described in <a href="/articles/abdesselam-global-trajectory/">the article on that</a>. The hierarchical recursion is the one-dimensional iteration which Abdesselam's construction perturbs, so the potential formulation of this article is where the two meet.</p>

<p>The quartic coupling is relevant exactly when the kernel exponent is above half the dimension, which is the hierarchical form of the upper critical dimension: for $\alpha&lt;d/2$ the interaction is long enough that the Gaussian fixed point governs, and for $\alpha&gt;d/2$ the nontrivial fixed point does. The values $\alpha=d/2$ and, for short-range models, $d=4$, are the same statement in the parametrisation of Fisher, Ma and Nickel [@fisher-ma-nickel-1972].</p>

## Definitions and setting {#section-potentials}

<p>Let $V$ be even, bounded below, with $\int e^{-V(s)}ds<\infty$ and $\int e^{cs^2-V(s)}ds<\infty$ for some $c>0$. The hierarchical model with prior $e^{-V(s)}ds$ has the decimation recursion of <a href="/articles/hierarchical-gibbs-measure/#section-decimation">the decimation article</a>, and its block-spin law has a density because the tilt and the convolution of a density are densities.</p>
<a id="tag-P2KV" data-assertion="definition" data-title="Effective potential of a decimation step"></a>
<p>For $b\geq0$ the <em>effective potential</em> $\mathcal V_bV$ is defined by</p>
<div class="math-display">$$e^{-(\mathcal V_bV)(s)}=\frac{1}{Z_b(V)}\int_{\mathbb R^{m-1}}\exp\Bigl(b\sum_{a&lt;a'}s_as_{a'}\Bigr)\prod_{a=1}^{m-1}e^{-V(s_a)}\,ds_1\cdots ds_{m-1},$$</div>
<p>with $s_m=s-\sum_{a&lt;m}s_a$, and the <em>scaled potential</em> at exponent $\theta$ is $(\mathcal R_\theta V)(s)=(\mathcal V_bV)(L^{\theta}s)$ up to an additive constant. The potential formulation and the law formulation of <a href="/articles/renormalisation-group-map/">the map article</a> carry the same information: $e^{-(\mathcal V_bV)}$ is the density of $\mathcal T_b(e^{-V}ds)$.</p>
<p>The constant in front is fixed by normalisation and plays no role in the flow of the shape of the potential; additive constants are the free energy increments of <a href="/articles/hierarchical-gibbs-measure/#section-free-energy">the free energy recursion</a> and are dropped from the potential from here on.</p>

## The Gaussian truncation {#section-gaussian}

<p>The one family the recursion preserves is the quadratic one, and on it the recursion is explicit.</p>
<a id="tag-K5WQ" data-assertion="proposition" data-title="Quadratic potentials are invariant and the quartic coupling is generated"></a>
<p>Let $V(s)=\tfrac{\mu}{2}s^2$ with $\mu>0$ and $b&lt;1/(v(m-1))$, where $v=1/\mu$. Then $\mathcal V_bV$ is quadratic, with curvature $\mu'$ given by</p>
<div class="math-display">$$\frac{1}{\mu'}=\frac{m}{\mu-b(m-1)},$$</div>
<p>that is $\mu'=(\mu-b(m-1))/m$: the curvature flows affinely, and the variance recursion $v'=mv/(1-bv(m-1))$ is the same statement for $v=1/\mu$. A quartic potential is not mapped to a quartic potential: at $\tfrac{\mu}{2}s^2+\lambda s^4$ with $\lambda\neq0$ the first-order term in $\lambda$ is again a quartic in $s$, but the second and higher orders are not polynomials of degree four, and a sixth power appears.</p>
:::details Proof
<p>For the first part, the tilted product of Gaussians is Gaussian and the law of the sum is Gaussian, as in <a href="/articles/gaussian-renormalisation-group/#section-closure">the closure theorem</a>; the displayed relation is that theorem with $\mu=1/v$ and $\mu'=1/v'$.</p>
<p>For the second part, expand the constrained integral in powers of $\lambda$. The zeroth order is the Gaussian computation of the first part. The first order is $-\lambda\sum_a\mathbb E_{\mathbb Q_0}[s_a^4\mid \sum_as_a=s]$, where $\mathbb Q_0$ is the tilted Gaussian law of the children at $\lambda=0$. Write $s_a=s/m+\delta_a$; conditionally on $\sum_as_a=s$ the vector $\delta$ is Gaussian, centred and independent of $s$, so $\sum_a(s/m+\delta_a)^4$ has conditional expectation $m(s/m)^4+6(s/m)^2\sum_a\mathbb E[\delta_a^2]+\sum_a\mathbb E[\delta_a^4]$, a polynomial of degree four in $s$: no new power appears at first order, and the quartic family is preserved to that order.</p>
<p>The second order is $\tfrac{\lambda^2}{2}$ times the second cumulant of $\sum_as_a^4$ under $\mathbb Q_0$ conditioned on $\sum_as_a=s$, and this is where the family fails to be preserved. The conditioned law of $\delta$ does not depend on $s$; hence the conditional cumulants of $\sum_as_a^4$ are polynomials in $s$ whose degree is twice the number of factors of $s/m$ picked up by $\delta$ in the expansion, and the quartic term of $\sum_a(s/m+\delta_a)^4$ is the one that carries the dependence. The fourth cumulant of a quartic polynomial in Gaussian variables is a nonzero polynomial of degree eight in its mean parameters, so its degree-eight and degree-six parts in $s$ are not both zero, and after subtracting the square of the first-order term a nonzero multiple of $s^6$ remains. Hence the quartic family is not invariant, and the first power that appears beyond the fourth is the sixth.</p>
:::
<p>The proposition is the precise form of two statements that are often made informally: the Gaussian truncation is exact, and every other truncation leaks. The leak is second order in the quartic coupling, so a two-coupling truncation is a controlled approximation only in a regime where the coupling is small, and the renormalisation-group flow of the hierarchical model has no such regime at the nontrivial fixed point.</p>

## Truncations and what replaces them {#section-truncations}

<p>A truncation is a projection of the flow onto finitely many couplings, and the proposition above shows that the projection does not commute with the flow beyond the quadratic term. Three routes replace it.</p>
<p><em>Infinite-dimensional analysis.</em> The flow is studied on a Banach space of potentials, with the fixed point found by an existence argument rather than by truncation. This is Koch and Wittwer's route for the scalar hierarchical model [@koch-wittwer-1986], and the setting is the one described in <a href="/articles/koch-wittwer-fixed-point/">the article on it</a>.</p>
<p><em>Expansion in a parameter.</em> Near $\alpha=d/2$ the nontrivial fixed point is close to the Gaussian one and the flow can be expanded in $\alpha-d/2$, which gives the $\varepsilon$-expansion of Gawedzki and Kupiainen [@gawedzki-kupiainen-1983] and, in the hierarchical model, of Bleher and Sinai. The expansion is a statement about a neighbourhood of the marginal exponent, not about a truncation of the potential.</p>
<p><em>Exact solutions of special models.</em> For a quadratic prior the flow is explicit, and for the vector model at low temperature it is explicit around a nonzero magnetisation; those are the two cases in which the recursion is solved rather than analysed.</p>
<p>The $\varphi^4$ flow in two couplings nevertheless predicts the qualitative picture correctly: a Gaussian fixed point at the origin of the quartic coupling, a nontrivial fixed point at a positive quartic coupling for $\alpha&gt;d/2$, and a critical surface separating the two phases. What it cannot do is give the position of the nontrivial fixed point or the value of $\nu$ there.</p>

## The low-temperature vector model {#section-low-temperature}

<p>For the $r$-component model with $r\geq2$ the ordered phase has a direction, and the renormalisation group has to be set up around a nonzero magnetisation. Bleher and Major carry this out for the vector-valued $\varphi^4$ hierarchical model [@bleher-major-1984].</p>
<p>In the ordered phase the block spin has a mean $M\neq0$ and fluctuations that are decomposed into a longitudinal part, along $M$, and $r-1$ transverse parts. The transverse directions are massless: the energy depends on the transverse components only through gradients, so no quadratic term is generated for them at any scale. The renormalisation of the model is the analysis of the coupled flow of the longitudinal potential and of the transverse stiffness, and in the hierarchical model it reduces to a recursion of the same type as the one for the symmetric phase, with the field expanded around $M$ rather than around $0$. The result is that the low-temperature phase of the vector model is renormalisable in the hierarchical setting, and that the transverse fluctuations do not generate a mass.</p>
<p>This is the origin of the marginal angular direction of <a href="/articles/hierarchical-vector-models/#section-thouless">the vector article</a>: at criticality the same transverse modes are the ones that make the direction of the block spin asymptotically uniform, and the two statements are the ordered-phase and critical forms of one mechanism.</p>

## Examples and non-examples {#section-examples}

<p><em>The scalar case at $\alpha&gt;d/2$.</em> Here the nontrivial fixed point governs, the quartic coupling is relevant, and the two-coupling truncation places the fixed point at a value of the coupling that the exact analysis corrects; the exponent $\nu$ differs from $1/\alpha$, as <a href="/articles/bleher-sinai-fixed-point/">the fixed-point article</a> records.</p>

<p><em>Short-range $\varphi^4$ in three dimensions.</em> The Euclidean model with a modified propagator, for which the renormalisation-group trajectory is constructed by Brydges, Mitter and Scoppola [@brydges-mitter-scoppola-2003], has the same structure of a Gaussian ultraviolet fixed point and a nontrivial infrared one; the hierarchical counterpart of the modified propagator is the geometric kernel of the <a href="/articles/hierarchical-lattice/#section-kernels">lattice article</a>, and the trajectory joining the two is Abdesselam's.</p>

<p><em>Non-example: a quartic truncation at the fixed point.</em> Setting the sixth and higher couplings to zero is not a consistent approximation at a fixed point with a nonzero quartic coupling, by the second part of the proposition; the truncated flow has a fixed point, but the potential there is not the effective potential of any model.</p>

<p><em>Non-example: the Gaussian model with a quartic term added by hand.</em> Adding $\lambda s^4$ to the prior without following its flow gives a model whose critical behaviour is Gaussian, because the added term is a bounded perturbation of a quadratic potential for the purposes of the recursion at small $\lambda$; it is not an approximation to the $\varphi^4$ fixed point.</p>

## Variants and generalisations {#section-variants}

<p><em>Finite-component vectors.</em> For $r$ components the potential is a function of $\lvert s\rvert$, and the flow preserves rotation invariance; the space of radial potentials is infinite-dimensional for every $r$, and the marginal angular directions are absent from it, which is why the radial truncation is more nearly consistent than a truncation in powers of $s$.</p>

<p><em>Hierarchical models on other geometries.</em> The Baker-based block structure gives the same kind of potential flow with different constants, and it is the model for which Koch and Wittwer prove a nontrivial fixed point in their third paper [@koch-wittwer-1994]; the $p$-adic and ultrametric groups give further variants with the same structure [@abdesselam-2018].</p>

<p><em>The free energy along the flow.</em> The additive constants dropped in the definition are the per-scale increments of the free energy, so the potential flow carries the free energy as a cocycle: the increment at scale $k$ is the logarithm of the normaliser of the step. This is how the singular part of the free energy is computed from the flow in <a href="/articles/critical-exponents-from-rg/#section-dictionary">the exponent dictionary</a>.</p>

## History and attribution {#section-history}

<p>The potential formulation is that of Bleher and Sinai, who wrote the recursion as a nonlinear transformation of measures and, equivalently, of the negative logarithm of their densities [@bleher-sinai-1973]. The low-temperature analysis of the vector model is Bleher and Major's [@bleher-major-1984]; the existence of the nontrivial fixed point without truncation and without a small parameter is Koch and Wittwer's [@koch-wittwer-1986]; the $\varepsilon$-expansion around the marginal exponent is Gawedzki and Kupiainen's [@gawedzki-kupiainen-1983]; and the classical long-range exponent values, with the upper critical exponent $\alpha=d/2$, are those of Fisher, Ma and Nickel [@fisher-ma-nickel-1972]. The systematic treatment of the renormalisation group as an operation on potentials is the one developed by Bauerschmidt, Brydges and Slade [@bauerschmidt-brydges-slade-2019].</p>

## References {#section-references}

<ul>
<li>A. Abdesselam, Towards three-dimensional conformal probability, <em>p-Adic Numbers Ultrametric Anal. Appl.</em> 10 (2018), 233&ndash;247.</li>
<li>R. Bauerschmidt, D. C. Brydges and G. Slade, <em>Introduction to a Renormalisation Group Method</em>, Lecture Notes in Mathematics 2242, Springer, 2019.</li>
<li>P. M. Bleher and P. Major, Renormalization of Dyson's hierarchical vector valued &phi;<sup>4</sup> model at low temperatures, <em>Comm. Math. Phys.</em> 95 (1984), 487&ndash;532.</li>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>D. C. Brydges, P. K. Mitter and B. Scoppola, Critical $(\Phi^4)_3$, <em>Comm. Math. Phys.</em> 240 (2003), 281&ndash;327.</li>
<li>M. E. Fisher, S.-k. Ma and B. G. Nickel, Critical exponents for long-range interactions, <em>Phys. Rev. Lett.</em> 29 (1972), 917&ndash;920.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian fixed points of the block spin transformation. Hierarchical model approximation, <em>Comm. Math. Phys.</em> 89 (1983), 191&ndash;220.</li>
<li>H. Koch and P. Wittwer, A non-Gaussian renormalization group fixed point for hierarchical scalar lattice field theories, <em>Comm. Math. Phys.</em> 106 (1986), 495&ndash;532.</li>
<li>H. Koch and P. Wittwer, A nontrivial renormalization group fixed point for the Dyson-Baker hierarchical model, <em>Comm. Math. Phys.</em> 164 (1994), 627&ndash;647.</li>
</ul>
