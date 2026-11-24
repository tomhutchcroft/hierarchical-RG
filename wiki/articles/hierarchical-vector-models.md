---
{
  "id": "hierarchical-vector-models",
  "title": "Hierarchical models with continuous symmetry",
  "subtitle": "With a vector spin the block direction does not settle at criticality, and the marginal exponent is decided by a slowly varying factor.",
  "kind": "theorem",
  "category": "Hierarchical models",
  "summary": "For the r-component hierarchical model the decimation map acts on laws on R^r by the same tilt, and it commutes with rotations. Bleher and Major proved Dyson's conjecture for this model: at the marginal kernel exponent a transition exists exactly when the level couplings are not summable, the spontaneous magnetisation vanishes at the critical temperature, and the normalised average spin still converges to the uniform law on the sphere. The Gaussian fixed point is r-independent; the continuous symmetry enters through a marginal angular direction.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$; $r\\geq1$ components; couplings $J_n=l_nL^{-(d+\\alpha)n}$ with $l_n>0$.",
    "Spins $\\sigma_x\\in\\mathbb R^r$ with a rotation invariant prior; $\\langle\\cdot,\\cdot\\rangle$ the Euclidean inner product.",
    "The marginal case of the potential of Bleher and Major is $\\alpha=d$, where summability is decided by $\\sum_n l_n$."
  ],
  "related": [
    "hierarchical-gibbs-measure",
    "hierarchical-phi4-truncations",
    "bleher-sinai-fixed-point",
    "critical-exponents-from-rg",
    "hierarchical-percolation-rg"
  ],
  "sourceIds": [
    "dyson-1969",
    "bleher-major-1984",
    "bleher-major-1987",
    "bleher-major-2021",
    "bleher-sinai-1973",
    "bleher-major-1988",
    "bleher-1987-vilnius"
  ],
  "aliases": [
    "vector hierarchical model",
    "continuous symmetry",
    "O(r) model",
    "Thouless effect",
    "Dyson's conjecture",
    "Goldstone mode"
  ]
}
---

<p>The <em>$r$-component hierarchical model</em> is the model of <a href="/articles/hierarchical-gibbs-measure/">the decimation article</a> with a vector spin: $\sigma_x\in\mathbb R^r$ and energy $-\sum_{\{x,y\}}J(\lVert x-y\rVert)\langle\sigma_x,\sigma_y\rangle$, with $J(L^n)=l_nL^{-(d+\alpha)n}$. Rotation invariance replaces the spin-flip symmetry, the block spin becomes a vector, and the decimation identity survives with inner products in place of products; what does not survive is the scalar picture of criticality. At the critical temperature the direction of the block spin does not concentrate: Bleher and Major proved that the normalised average spin converges in law to the uniform distribution on the sphere, while the spontaneous magnetisation vanishes [@bleher-major-2021].</p>

<p>The same work settles Dyson's conjecture for this model at the marginal exponent. When $\alpha=d$ the interaction is summable or not according to the level sequence: $\sum_nJ_nL^{dn}=\sum_nl_n$. Bleher and Major prove that a phase transition exists exactly when $\sum_nl_n=\infty$, so the marginal case is decided by the slowly varying factor and not by any exponent, and they prove that the transition is continuous — there is no Thouless effect, in which the magnetisation would jump. What replaces the jump is the failure of concentration of the direction at criticality: the order parameter is zero, and yet the block spin is not small.</p>

<p>Two structural facts organise the comparison with the scalar case. The decimation map commutes with rotations, so the state of the recursion is a rotation-covariant law on $\mathbb R^r$; and the Gaussian fixed point is $r$-independent, since the tilt couples the components separately and the variance recursion is the scalar one. The exponents $\kappa=\alpha$ and $\eta=2-\alpha$ are therefore unchanged by $r$, and the $r$-dependence enters through a marginal angular direction, the hierarchical counterpart of a Goldstone mode, which is what the <a href="/articles/bleher-sinai-fixed-point/">nontrivial fixed point</a> acquires when the symmetry is continuous.</p>

## Definitions and setting {#section-model}

<p>Fix $r\geq1$, integers $L\geq2$, $d\geq1$, $m=L^d$, a real $\alpha>0$ and a sequence $l_n>0$ with $l_n$ bounded above and below on each level. The <em>coupling at level $n$</em> is $J_n=l_nL^{-(d+\alpha)n}$, and the Hamiltonian on a finite $S\subset\mathbb H^d_L$ is</p>
<div class="math-display">$$H_S(\sigma)=-\sum_{\{x,y\}\subset S}J(\lVert x-y\rVert)\langle\sigma_x,\sigma_y\rangle,\qquad J(L^n)=J_n .$$</div>
<p>The model is a problem about the limit distribution of a strongly dependent sequence, which is the framing of Bleher and Major's survey [@bleher-major-1987]. The prior is a rotation invariant probability measure $\varrho$ on $\mathbb R^r$ with finite second moment; the two cases below are the classical spin $\varrho$ uniform on $\mathbb S^{r-1}$, and the Gaussian $\varrho=N(0,I_r)$. For $r=1$ this is the scalar model, and the inner product is the product.</p>
<a id="tag-V3MC" data-assertion="definition" data-title="Vector block spin and the rotation covariant decimation map"></a>
<p>The block spin of $S$ is $S_S=\sum_{x\in S}\sigma_x\in\mathbb R^r$ and $\mu_n$ is its law under the Gibbs measure of $\Lambda_n$ with free boundary. The decimation map at coupling $b$ acts on probability measures on $\mathbb R^r$ by</p>
<div class="math-display">$$\mathcal T_b\nu(A')=\frac{1}{Z_b(\nu)}\int_{(\mathbb R^r)^m}\mathbf 1_{A'}\Bigl(\sum_{a}s_a\Bigr)\exp\Bigl(b\sum_{a&lt;a'}\langle s_a,s_{a'}\rangle\Bigr)\prod_a\nu(ds_a),$$</div>
<p>with $Z_b(\nu)$ the corresponding normaliser, and $\mathcal R_{\theta,b}$ is its composition with $s\mapsto L^{-\theta}s$ as in <a href="/articles/renormalisation-group-map/#section-definition">the map article</a>. The <em>critical exponent</em> of the interaction is the value $\alpha=d$ at which $\sum_nL^{dn}J_n=\sum_nl_n$ may converge or diverge.</p>

## Decimation and rotation covariance {#section-decimation}

<p>The two structural statements are proved exactly as in the scalar case, with an inner product in place of a product.</p>
<a id="tag-R7DN" data-assertion="theorem" data-title="Decimation identity for vector spins"></a>
<p>For $n\geq1$ the children $\Lambda^{(a)}=e_n(a)+\Lambda_{n-1}$ of $\Lambda_n$ satisfy</p>
<div class="math-display">$$\exp\bigl(-\beta H_{\Lambda_n}(\sigma)\bigr)=\prod_{a}\exp\bigl(-\beta H_{\Lambda^{(a)}}(\sigma^{(a)})\bigr)\exp\Bigl(\beta l_nL^{-(d+\alpha)n}\sum_{a&lt;a'}\langle S_a,S_{a'}\rangle\Bigr),$$</div>
<p>so $Z_n=Z_{n-1}^mZ_{\beta J_n}(\mu_{n-1})$ and $\mu_n=\mathcal T_{\beta J_n}\mu_{n-1}$; with $\theta_0=\tfrac12(d+\alpha)$ and $b=\beta J_1$ the rescaled laws satisfy $\nu_n=\mathcal R_{\theta_0,b}^{\,n}\nu_0$.</p>
:::details Proof of the vector decimation identity
<p>By the child decomposition every pair of $\Lambda_n$ lies either inside a child, at a level at most $n-1$, or in two distinct children, in which case it is at level exactly $n$. The energy therefore splits as in the scalar case, and the cross term is $\sum_{a&lt;a'}J_n\langle S_a,S_{a'}\rangle$ because the sum of $\langle\sigma_x,\sigma_y\rangle$ over the pairs of two children factors as the inner product of the two child sums. A child is a translate of $\Lambda_{n-1}$ and the Hamiltonian depends on differences, so the integral over a child at fixed $S_a$ is $Z_{n-1}\mu_{n-1}(dS_a)$. Dividing by $Z_n$ gives the recursion, and the scaling computation is the scalar one, the factor $L^{2\theta_0}$ multiplying every inner product uniformly.</p>
:::
<a id="tag-W8PK" data-assertion="proposition" data-title="Rotation covariance and the r-independence of the Gaussian fixed point"></a>
<p>For every orthogonal $Q\in O(r)$, $\mathcal T_b(Q_*\nu)=Q_*\mathcal T_b\nu$. For the Gaussian prior $\varrho=N(0,I_r)$ the law of the block spin is $N(0,v_nI_r)$ with $v_n$ given by the scalar recursion</p>
<div class="math-display">$$v_n=\frac{mv_{n-1}}{1-\beta J_nv_{n-1}(m-1)},\qquad v_0=1,$$</div>
<p>so the critical coupling, the fixed point of the rescaled recursion and its multiplier $L^{\alpha}$ are those of <a href="/articles/gaussian-renormalisation-group/">the Gaussian article</a>, independently of $r$.</p>
:::details Proof
<p>Rotations preserve the inner product, so the tilted product measure and the sum $\sum_as_a$ are transported by $Q$; this gives the covariance. For the Gaussian prior the computation is componentwise: the exponent is $b\sum_{a&lt;a'}\sum_{j=1}^r s_{a,j}s_{a',j}$, a sum of $r$ copies of the scalar exponent, so the tilted law is a product over $j$ of scalar tilted laws, and the law of the sum is $N(0,v'I_r)$ with $v'$ the scalar value. The scalar recursion and its closed form then apply to each component, and neither the critical coupling $\beta_c=1/\sum_{x\neq0}J(\lVert x\rVert)$ nor the multiplier depends on $r$.</p>
:::
<p>The proposition is the reason the mean-field exponents of the vector model are the scalar ones. It also isolates what continuous symmetry can change: nothing in the Gaussian orbit, and therefore nothing in the two renormalisation-group numbers $\kappa$ and $\nu$ at the level of the Gaussian fixed point. The change appears at the non-Gaussian fixed point, whose linearisation acquires a marginal direction in the angular variable.</p>

## The direction of a rotation invariant block spin {#section-direction}

<p>The vector case has an observable the scalar case does not: the direction $S/\lvert S\rvert$. For a rotation invariant law it carries no information about the size.</p>
<a id="tag-N4TZ" data-assertion="proposition" data-title="Uniform direction and independence for rotation invariant laws"></a>
<p>Let $\nu$ be a rotation invariant probability measure on $\mathbb R^r$ with $\nu(\{0\})=0$, $r\geq2$. Then under $\nu$ the random variable $S/\lvert S\rvert$ is uniform on $\mathbb S^{r-1}$ and independent of $\lvert S\rvert$. In particular the conclusion holds for every law of the Gaussian orbit and for every rotation invariant fixed point of $\mathcal R_{\theta,b}$.</p>
:::details Proof
<p>Let $f$ be bounded measurable on $\mathbb S^{r-1}$ and $g$ bounded measurable on $[0,\infty)$. Since $\lvert QS\rvert=\lvert S\rvert$ for orthogonal $Q$ and $\nu$ is invariant,</p>
<div class="math-display">$$\int f(S/\lvert S\rvert)g(\lvert S\rvert)\,d\nu(S)=\int f(QS/\lvert QS\rvert)g(\lvert S\rvert)\,d\nu(S)$$</div>
<p>for every $Q$. Averaging over $Q$ against the Haar measure of $O(r)$ and using Fubini, the right-hand side is $\int \bar f\,g(\lvert S\rvert)d\nu(S)$ with $\bar f$ the average of $f$ over the sphere, which is $\int f\,d\sigma$ for the uniform $\sigma$. Taking $g=\mathbf 1_{B}$ for a Borel $B\subseteq[0,\infty)$ gives $\int f(S/\lvert S\rvert)\mathbf 1_B(\lvert S\rvert)d\nu=\bigl(\int f\,d\sigma\bigr)\nu(\lvert S\rvert\in B)$, which is the product statement; the case $f\equiv1$ gives uniformity.</p>
:::
<p>The proposition explains why "the direction is uniform" is not by itself a critical phenomenon: it holds at every temperature in the Gaussian model. What Bleher and Major prove is that it holds at the critical temperature of the interacting model as well, where the direction could have concentrated, and that this coexists with a vanishing spontaneous magnetisation.</p>

## Dyson's conjecture and the Thouless-like effect {#section-thouless}

<p>At the marginal exponent the interaction is summable exactly when the level couplings are, and the question is whether summability is the same as the absence of a transition. Dyson conjectured that it is, and Bleher and Major proved the conjecture for the vector model.</p>
<a id="tag-B9HL" data-assertion="theorem" data-title="Dyson's conjecture for the vector model and the critical direction"></a>
<p>Let $r\geq2$, let the interaction be $U(x,y)=-l_nL^{-2n}\langle\sigma_x,\sigma_y\rangle$ at level $n$, and let the prior be uniform on $\mathbb S^{r-1}$. Then a phase transition exists if and only if $\sum_nl_n=\infty$. At the critical temperature the spontaneous magnetisation vanishes, and the law of the normalised average spin of $\Lambda_N$ converges to the uniform distribution on $\mathbb S^{r-1}$ as $N\to\infty$.</p>
<p>The statement is Theorem 1 of Bleher and Major [@bleher-major-2021], where the model is written with the potential $-l(d)d^{-2}$ in the hierarchical distance $d$; the exponent $-2$ is the marginal one, $\alpha=d$ in the notation of this wiki, and the condition $\sum_nl_n=\infty$ is the failure of summability of the interaction. The same paper gives the corresponding statements for the scalar case as the boundary of its analysis.</p>
<p>Three consequences are worth separating. First, at the marginal exponent the criterion is a condition on the level sequence and not on a power: replacing $l_n$ by a sequence with the same growth but a convergent sum removes the transition. Second, the transition is continuous: the spontaneous magnetisation tends to zero at $T_c$, so the Thouless effect — a jump of the order parameter at the transition — does not occur. Third, the direction of the block spin is asymptotically uniform at $T_c$, so the order parameter vanishes while the block spin is of the size it has at criticality: the transition is carried by the fluctuations of the size, not by a selected direction.</p>
<p>Below the critical temperature the limits change character. For the vector model the block sums have non-central limit theorems at every temperature below $T_c$, and the non-Gaussian large-scale limit of the ordered phase is described by Bleher and Major in the two-part paper of 1988 [@bleher-major-1988], with the phenomenon recorded in their survey as one of the features that distinguishes the vector model from the scalar one [@bleher-major-1987]. The mechanism is the transverse enhancement of <a href="/articles/hierarchical-phi4-truncations/#section-low-temperature">the low-temperature section of the truncations article</a>: the orthogonal fluctuations grow faster than the square root of the volume, and their limit need not be Gaussian.</p>
<p>The three statements of the theorem together are the vector counterpart of the scalar picture of <a href="/articles/critical-exponents-from-rg/">the exponent article</a>. In the scalar case the block spin at criticality is a number whose law has a nontrivial limit after rescaling; in the vector case the direction is asymptotically free and the limit law of the rescaled block spin is rotation invariant, so the angular variable contributes a marginal direction rather than a third independent exponent.</p>

## Consequences for the exponents {#section-exponents}

<p>The growth exponent is fixed by autonomy in the vector case as in the scalar one, since the argument of <a href="/articles/critical-exponents-from-rg/#section-growth">the growth theorem</a> uses only the law of the block spin and its second moment.</p>
<p>Consequently $\kappa=\alpha$ and $\eta=2-\alpha$ for the vector model at any rotation invariant fixed point with finite nonzero variance, and the exponents that involve the order parameter are those of the scalar model with the same $\nu$. The $r$-dependence sits in $\nu$, which is read off the linearisation at the non-Gaussian fixed point, and in the critical fluctuations of the direction, which are not captured by any exponent. This is the sense in which the vector model has the same two renormalisation-group numbers as the scalar one: the angular marginality changes the fixed point and the fluctuations, not the count of relevant directions.</p>
<p>At the marginal exponent $\alpha=d$ the interaction is not summable and the model is at its own boundary; the level sequence $l_n$ then replaces the exponent as the parameter that decides criticality, which is why the exponents of the vector model at $\alpha=d$ are not obtained from the formulas above by substitution.</p>

## Examples and non-examples {#section-examples}

<p><em>The scalar case $r=1$.</em> The direction is a sign, the uniform law on $\mathbb S^0$ is the fair coin, and the phenomenon of the previous section reduces to the symmetry $\sigma\mapsto-\sigma$: the block spin's sign is asymptotically fair at $T_c$ whenever the law is symmetric. This is why the vector phenomenon has no scalar analogue of interest.</p>

<p><em>Dyson's original model.</em> With $r=1$, $\alpha=d=1$ and $l_n\equiv1$ the criterion $\sum_nl_n=\infty$ holds and the transition exists, which is Dyson's theorem [@dyson-1969]; the vector statement extends it to every $r$ and to every level sequence.</p>

<p><em>The Gaussian prior.</em> For $\varrho=N(0,I_r)$ the direction is uniform at every temperature by the proposition above, and the critical behaviour is entirely in the size: the model has no phase transition in the sense of symmetry breaking at any $\beta$, and its exponents are the Gaussian ones.</p>

<p><em>Non-example: a discrete symmetry.</em> For the $q$-state Potts model, or for $r=1$, there is no continuous group and no marginal angular direction. The critical behaviour is then of the scalar type, and the marginal-exponent criterion of the theorem is replaced by the corresponding statement for percolation, where $\beta_c&lt;\infty$ exactly when $\alpha&lt;d$ [@koval-meester-trapman-2012].</p>

<p><em>Non-example: the ordered phase.</em> Below $T_c$ the direction concentrates: the block spin is asymptotically parallel to a fixed vector, and the transverse fluctuations are massless. The renormalisation of that phase is a different problem, treated for the vector $\varphi^4$ model by Bleher and Major [@bleher-major-1984] and described in <a href="/articles/hierarchical-phi4-truncations/#section-low-temperature">the article on truncations</a>.</p>

## Variants and generalisations {#section-variants}

<p><em>Other marginal structures.</em> The same question — whether summability decides criticality — can be asked at the marginal exponent of any model in the class, and the answer depends on the symmetry: for the percolation class the marginal exponent is $\alpha=d$ as well, and the criterion at $\alpha=d$ involves the level sequence in the same way.</p>

<p><em>Ultrametric and $p$-adic models.</em> The construction uses only the ultrametric block structure, so it applies to the $p$-adic integers and to other ultrametric groups; the renormalisation group on those spaces, and its use as a model for a three-dimensional conformal field theory, is the subject of Abdesselam's programme [@abdesselam-2018].</p>

<p><em>The number of components as a parameter.</em> The linearisation at the non-Gaussian fixed point depends on $r$ through the dimension of the space of angular perturbations. The scalar case has none, the $O(r)$ case has $r-1$ marginal directions at leading order, and the exponents are expected to depend on $r$ only through the eigenvalue associated with the radial direction.</p>

## History and attribution {#section-history}

<p>Dyson introduced the hierarchical model to prove a transition for power-law couplings [@dyson-1969], and conjectured that for continuous symmetry the criterion for a transition is the failure of summability of the interaction; the conjecture and its proof are the subject of Bleher and Major's paper, which circulated from 2002 and appeared in 2021 [@bleher-major-2021]. The low-temperature phase of the vector $\varphi^4$ model was treated by the same authors in 1984 [@bleher-major-1984], and the survey of 1987 presents the hierarchical model as a problem about limit distributions of strongly dependent random variables, with the vector phenomena and a list of conjectures [@bleher-major-1987], and the limit theorems for multicomponent models were announced in the Vilnius proceedings of the same period [@bleher-1987-vilnius]. The transformation itself, in the scalar case, is that of Bleher and Sinai [@bleher-sinai-1973]; the historical account of the Moscow seminar in which this circle of ideas developed is Bleher's [@bleher-2012].</p>

## References {#section-references}

<ul>
<li>P. M. Bleher, Hierarchical models and renormalisation group, <em>Eur. Phys. J. H</em> 37 (2012), 605&ndash;618.</li>
<li>P. M. Bleher and P. Major, Renormalization of Dyson's hierarchical vector valued &phi;<sup>4</sup> model at low temperatures, <em>Comm. Math. Phys.</em> 95 (1984), 487&ndash;532.</li>
<li>P. M. Bleher, Limit theorems for multicomponent hierarchical models, in <em>Probability Theory and Mathematical Statistics</em>, Proc. 4th Vilnius Conf., Vol. 1, 211&ndash;229, 1987.</li>
<li>P. M. Bleher and P. Major, Critical phenomena and universal exponents in statistical physics. On Dyson's hierarchical model, <em>Ann. Probab.</em> 15 (1987), 431&ndash;477.</li>
<li>P. M. Bleher and P. Major, The large-scale limit of Dyson's hierarchical vector valued model at low temperatures. The non-Gaussian case, <em>Ann. Inst. H. Poincar&eacute; Phys. Th&eacute;or.</em> 49 (1988), 7&ndash;85 and 87&ndash;143.</li>
<li>P. M. Bleher and P. Major, A Thouless-like effect in the Dyson hierarchical model with continuous symmetry, <em>Pure Appl. Funct. Anal.</em> 6 (2021), 101&ndash;175.</li>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>F. J. Dyson, Existence of a phase-transition in a one-dimensional Ising ferromagnet, <em>Comm. Math. Phys.</em> 12 (1969), 91&ndash;107.</li>
<li>V. Koval, R. Meester and P. Trapman, Long-range percolation on the hierarchical lattice, <em>Electron. J. Probab.</em> 17 (2012), no. 57.</li>
<li>A. Abdesselam, Towards three-dimensional conformal probability, <em>p-Adic Numbers Ultrametric Anal. Appl.</em> 10 (2018), 233&ndash;247.</li>
</ul>
