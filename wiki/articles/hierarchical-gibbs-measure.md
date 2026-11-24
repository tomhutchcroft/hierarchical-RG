---
{
  "id": "hierarchical-gibbs-measure",
  "title": "Hierarchical spin systems and decimation",
  "subtitle": "The block spin of a hierarchical model is distributed as a functional of independent copies of the block spin one scale down.",
  "kind": "theorem",
  "category": "Hierarchical models",
  "summary": "A spin system on the hierarchical lattice with couplings constant on levels has a Hamiltonian that splits into the Hamiltonians of its children plus one interaction between their sums. Consequently the partition function and the law of a block spin are recovered from the law one scale down by an explicit operation, the free energy has an exact recursion, and the whole renormalisation group is a recursion on one-variable laws.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$ and $m=L^d$; kernel exponent $\\alpha\\gt 0$.",
    "Couplings $J_k=JL^{-(d+\\alpha)k}\\gt 0$ between distinct children of a level-$k$ block; a single-spin prior $\\varrho$.",
    "Free boundary conditions on $\\Lambda_n$ throughout."
  ],
  "related": [
    "hierarchical-lattice",
    "renormalisation-group-map",
    "gaussian-renormalisation-group",
    "hierarchical-percolation-rg"
  ],
  "sourceIds": [
    "dyson-1969",
    "bleher-sinai-1973",
    "griffiths-1967",
    "bauerschmidt-brydges-slade-2019"
  ],
  "aliases": [
    "hierarchical Ising model",
    "Dyson hierarchical model",
    "decimation identity",
    "block spin",
    "free energy recursion"
  ]
}
---

<p>A <em>hierarchical spin system</em> is a spin model on $\mathbb H^d_L$ whose coupling between two vertices is a function of their <a href="/articles/hierarchical-lattice/">level</a> alone, so that the coupling at level $k$ has one value $J_k=JL^{-(d+\alpha)k}$. Its energy on a block splits exactly into the energies of the children of that block plus a single interaction between the child sums: pairs inside a child are at levels below the top, pairs in different children are all at the top level, and no pair inside the block is at a level above it. The partition function therefore factorises, and the law of a block spin is the image of the law one scale down under an explicit operation — <a href="/articles/renormalisation-group-map/">block decimation</a> — which acts on the single variable $\sum_{x\in\text{child}}\sigma_x$.</p>

<p>This article states that identity, its iterates, and the free energy recursion that follows; the operation itself is studied in <a href="/articles/renormalisation-group-map/">the next article</a> and solved exactly in the <a href="/articles/gaussian-renormalisation-group/">Gaussian case</a>. The identity is what is special about the lattice: on $\mathbb Z^d$ a decimation step produces an interaction that depends on the shape of the boundary between blocks, whereas here it produces one number per block.</p>

<p>The structure is Dyson's (1969), who introduced the hierarchical approximation to prove a phase transition for power-law couplings [@dyson-1969], and it is the setting of the renormalisation analysis of Bleher and Sinai [@bleher-sinai-1973]. Only free boundary conditions are used, so every object below is finite-dimensional and every identity is exact at finite volume.</p>

## Definitions and setting {#section-model}

<p>Fix integers $L\geq2$, $d\geq1$ and a real $\alpha&gt;0$, write $m=L^d$, and let $J&gt;0$. Let $\varrho$ be a probability measure on $\mathbb R$ with $\int\sigma^2\varrho(d\sigma)&lt;\infty$; the two cases used below are the Ising prior $\varrho=\tfrac12(\delta_{-1}+\delta_1)$ and the Gaussian prior $\varrho=N(0,1)$. Spins are real numbers $\sigma_x$.</p>
<a id="tag-C3RV" data-assertion="definition" data-title="Hierarchical interaction and its level decomposition"></a>
<p>For finite $S\subset\mathbb H^d_L$ and $\beta\geq0$, the <em>hierarchical Hamiltonian</em> is</p>
<div class="math-display">$$H_S(\sigma)=-\sum_{\{x,y\}\subset S}J(\lVert x-y\rVert)\sigma_x\sigma_y,\qquad J(L^k)=J_k=JL^{-(d+\alpha)k},$$</div>
<p>the <em>partition function</em> and <em>Gibbs measure</em> are</p>
<div class="math-display">$$Z_S(\beta)=\int_{\mathbb R^S}\exp\bigl(-\beta H_S(\sigma)\bigr)\prod_{x\in S}\varrho(d\sigma_x),\qquad \mathbb P_S(d\sigma)=\frac{e^{-\beta H_S(\sigma)}}{Z_S(\beta)}\prod_{x\in S}\varrho(d\sigma_x),$$</div>
<p>and the <em>block spin</em> of $S$ is $S_S=\sum_{x\in S}\sigma_x$. For $n\geq0$ put $Z_n=Z_{\Lambda_n}$, $\mathbb P_n=\mathbb P_{\Lambda_n}$ and $\mu_n$ for the law of $S_{\Lambda_n}$ under $\mathbb P_n$, so that $\mu_0=\varrho$. The <em>two-point function</em> is $\tau_\beta(x,y)=\mathbb E_{\mathbb P_{\Lambda_n}}[\sigma_x\sigma_y]$ for any $n$ with $x,y\in\Lambda_n$, a definition independent of $n$ because the Hamiltonian is a sum over pairs.</p>
<p>Pairs at level $k$ are those in different children of a common level-$k$ block, by the <a href="/articles/hierarchical-lattice/#section-children">child decomposition</a>, so the Hamiltonian may be regrouped by level. That regrouping is the first statement.</p>

## The level decomposition {#section-split}

<a id="tag-H7PN" data-assertion="proposition" data-title="Splitting a block Hamiltonian into children and one top interaction"></a>
<p>For $n\geq1$ let $\Lambda^{(a)}=e_n(a)+\Lambda_{n-1}$, $a\in A$, be the children of $\Lambda_n$ and let $Q_k(\sigma)$ be the sum of $\sigma_x\sigma_y$ over the pairs at level $k$. Then</p>
<div class="math-display">$$-\beta H_{\Lambda_n}(\sigma)=\sum_{a\in A}\bigl(-\beta H_{\Lambda^{(a)}}(\sigma)\bigr)+\beta J_n\sum_{a<a'}S_aS_{a'},\qquad S_a=\sum_{x\in\Lambda^{(a)}}\sigma_x,$$</div>
<p>and $-\beta H_{\Lambda_n}=\beta\sum_{k=1}^nJ_kQ_k$.</p>
:::details Proof of the level decomposition
<p>Every pair $\{x,y\}\subset\Lambda_n$ lies in a unique pair of children, since the children partition $\Lambda_n$. If $x,y$ lie in the same child, the child is a coset $e_n(a)+\Lambda_{n-1}$ and levels are translation invariant, so the pair's level is at most $n-1$; the term it contributes is one of the pairs summed by $H_{\Lambda^{(a)}}$, and conversely every pair of a child is a pair of $\Lambda_n$ with the same level. If $x,y$ lie in different children, the pair has level exactly $n$ by the <a href="/articles/hierarchical-lattice/#section-children">child decomposition</a>, so it contributes $J_n\sigma_x\sigma_y$, and summing over the pairs of the two children gives $J_nS_aS_{a'}$. No pair of $\Lambda_n$ lies at a level above $n$, because every vertex of $\Lambda_n$ vanishes above coordinate $n$ and a difference of two of them therefore does. Collecting the terms of level $k$ gives the second display.</p>
:::
<p>The regrouping shows where the exactness comes from: the interaction between two children is a function of their two sums, and the interaction between a child and all the others is a function of its sum as well, so a child's influence on the rest of the block is carried by one number.</p>

## The decimation identity {#section-decimation}

<a id="tag-N5XD" data-assertion="theorem" data-title="Exact recursion for the partition function and the block-spin law"></a>
<p>For $n\geq1$,</p>
<div class="math-display">$$Z_n(\beta)=Z_{n-1}(\beta)^m\int_{\mathbb R^m}\exp\Bigl(\beta J_n\sum_{a<a'}s_as_{a'}\Bigr)\prod_{a\in A}\mu_{n-1}(ds_a),$$</div>
<p>and the law of $(S_a)_{a\in A}$ under $\mathbb P_n$ is the normalised version of that measure. Hence, writing</p>
<div class="math-display">$$\mathcal T_b\mu(A')=\frac{\displaystyle\int_{\mathbb R^m}\mathbf 1_{A'}\Bigl(\sum_{a}s_a\Bigr)\exp\Bigl(b\sum_{a<a'}s_as_{a'}\Bigr)\prod_{a}\mu(ds_a)}{\displaystyle\int_{\mathbb R^m}\exp\Bigl(b\sum_{a<a'}s_as_{a'}\Bigr)\prod_{a}\mu(ds_a)}$$</div>
<p>for $b\geq0$, the block-spin laws satisfy $\mu_n=\mathcal T_{\beta J_n}\mu_{n-1}$.</p>
:::details Proof of the decimation identity
<p>Write $\sigma=(\sigma^{(a)})_{a\in A}$ with $\sigma^{(a)}$ the restriction to the child $\Lambda^{(a)}$, and $S_a=\sum_{x\in\Lambda^{(a)}}\sigma^{(a)}_x$. The prior is a product over vertices, hence over children, and the level decomposition gives</p>
<div class="math-display">$$\exp(-\beta H_{\Lambda_n}(\sigma))=\prod_{a\in A}\exp\bigl(-\beta H_{\Lambda^{(a)}}(\sigma^{(a)})\bigr)\exp\Bigl(\beta J_n\sum_{a<a'}S_aS_{a'}\Bigr).$$</div>
<p>Because a child is a translate of $\Lambda_{n-1}$ and the Hamiltonian only depends on differences, the integral of the $a$-th factor against the prior over that child is $Z_{n-1}$ on the set where $S_a=s_a$, as the definition of the Hamiltonian gives the same function of the translated configuration. Integrating out all children with $S_a$ held fixed therefore produces $\prod_aZ_{n-1}\mu_{n-1}(ds_a)$, and integrating the remaining factor over $(s_a)$ gives the displayed identity for $Z_n$. Dividing by $Z_n$ gives the law of $(S_a)$, and the law of $\sum_as_a$ is its image.</p>
:::
<p>In this form the identity is the renormalisation transformation of Bleher and Sinai, who made the law of the block spin the object of study [@bleher-sinai-1973].
<div class="fig" data-fig="decimation" data-title="One decimation step. The children are independent with law μ; the tilt depends only on their sums; the result is the law of the block spin, which is the new state of the recursion."></div> The display is the whole renormalisation group, at finite volume: the state of the model after $n$ scales is the law of one number, and one more scale acts on that law by a fixed rule depending on the coupling $b=\beta J_n$. Three features are immediate. First, $\mathcal T_b$ is a nonlinear but explicit operation, given by a Gibbs tilt of a product measure by the variance-type quantity $\sum_{a&lt;a'}s_as_{a'}=\tfrac12\bigl((\sum_as_a)^2-\sum_as_a^2\bigr)$; second, the coupling argument decreases geometrically, $J_n=L^{-(d+\alpha)n}J$; third, the identity holds for any prior $\varrho$, so it applies to Ising, Gaussian and $\varphi^4$ spins at once, differing only in the initial law $\mu_0$.</p>

## Iteration and the free energy {#section-free-energy}

<a id="tag-Z8BM" data-assertion="corollary" data-title="Iterated decimation and the free energy recursion"></a>
<p>For $1\leq k\leq n$, $\mu_n=\mathcal T_{\beta J_n}\cdots\mathcal T_{\beta J_{k+1}}\mu_k$. With $F_n=m^{-n}\log Z_n$,</p>
<div class="math-display">$$F_n=F_0+\sum_{k=1}^n\frac{1}{m^k}\log\mathbb E_{\mu_{k-1}^{\otimes m}}\Bigl[\exp\Bigl(\beta J_k\sum_{a<a'}s_as_{a'}\Bigr)\Bigr],\qquad F_0=\log\int\varrho(d\sigma).$$</div>
<p>If the prior satisfies $\lvert\sigma\rvert\leq1$ and $J_k&gt;0$ for every $k$, then $F_n$ is nondecreasing in $n$ and</p>
<div class="math-display">$$F_0\leq F_n\leq F_0+\tfrac{\beta}{2}\sum_{x\neq0}J\lVert x\rVert^{-d-\alpha}$$</div>
<p>for every $n$, so $F=\lim_nF_n$ exists and is finite; $F$ is convex in $\beta$.</p>
:::details Proof of the free energy recursion
<p>The iterate is the decimation identity applied $n-k$ times. Taking logarithms in the identity for $Z_n$ and dividing by $m^n=m\cdot m^{n-1}$ gives $F_n=F_{n-1}+m^{-n}\Lambda_n$ with $\Lambda_n$ the logarithm in the display, and iterating this relation gives the stated formula.</p>
<p>For the monotonicity, apply the second Griffiths inequality [@griffiths-1967] to the ferromagnetic measure $\mathbb P_{k-1}^{\otimes m}$, whose couplings between distinct children are all zero: it gives $\mathbb E[s_as_{a'}]\geq0$ for $a\neq a'$. Hence $\mathbb E[\sum_{a&lt;a'}s_as_{a'}]\geq0$, and Jensen's inequality $\log\mathbb E[e^X]\geq\mathbb E[X]$ gives $\Lambda_k\geq0$, so $F_n-F_{n-1}\geq0$.</p>
<p>For the upper bound, $\lvert\sigma_x\sigma_y\rvert\leq1$ gives $\exp(-\beta H_{\Lambda_n})\leq\exp(\beta\sum_{\{x,y\}\subset\Lambda_n}J(\lVert x-y\rVert))$, so $Z_n\leq(\int\varrho)^{m^n}\exp(\beta\sum_{\{x,y\}}J(\lVert x-y\rVert))$ and $F_n\leq F_0+\beta m^{-n}\sum_{\{x,y\}\subset\Lambda_n}J(\lVert x-y\rVert)$. Each vertex of $\Lambda_n$ has at most $\sum_{x\neq0}J(\lVert x\rVert)$ total intensity to its partners, so the double sum is at most $m^n\sum_{x\neq0}J(\lVert x\rVert)/2$, which is finite by the <a href="/articles/hierarchical-lattice/#section-kernels">summability criterion</a>. Convexity follows because $\beta\mapsto\log Z_n(\beta)$ has second derivative the variance of $H_{\Lambda_n}$.</p>
:::
<p>For the Ising prior, $F_0=\log2$, and the bounds read $\log2\leq F_n\leq\log2+\frac{\beta}{2}\sum_{x\neq0}J(\lVert x\rVert)$. The recursion is the useful statement: the increment at scale $k$ is a function of the level-$(k-1)$ block-spin law alone, so the free energy is a sum of per-scale contributions, each computed from the renormalised state at that scale. This is the form in which the free energy is used in <a href="/articles/critical-exponents-from-rg/">the article on exponents</a>.</p>

## Correlations of block sums {#section-correlations}

<p>The derivative of the free energy in a level coupling identifies a block correlation, and this is the observable the renormalisation group controls.</p>
<a id="tag-D6QL" data-assertion="proposition" data-title="Level couplings and the block-sum correlations"></a>
<p>For $k\geq1$ let $T_k=\mathbb E_{\mathbb P_k}[S_1S_2]$, where $S_1$ and $S_2$ are the sums over two distinct children of $\Lambda_k$; by the symmetry of the model on $\Lambda_k$ this does not depend on which two children are chosen. Then</p>
<div class="math-display">$$\frac{\partial}{\partial J_k}\log Z_k(\beta)=\beta\,\frac{m(m-1)}{2}\,T_k,\qquad \frac{\partial}{\partial J_k}\log Z_n(\beta)=\beta\,\mathbb E_{\mathbb P_n}[Q_k]\quad(n\geq k).$$</div>
:::details Proof of the derivative identity
<p>Differentiating $Z_n=\int\exp(\beta\sum_{j\leq n}J_jQ_j)\prod_{x\in\Lambda_n}\varrho(d\sigma_x)$ in $J_k$ brings down the factor $\beta Q_k$, so the derivative is $\beta\mathbb E_{\mathbb P_n}[Q_k]$, which is the second identity.</p>
<p>For $n=k$ the only level-$k$ block in $\Lambda_k$ is $\Lambda_k$ itself, so $Q_k$ is the sum of $S_aS_{a'}$ over the unordered pairs of distinct children, $m(m-1)/2$ terms. An isometry of $\mathbb H^d_L$ that fixes $0$ and preserves $\Lambda_k$ permutes its children, and it preserves the Hamiltonian because the Hamiltonian depends on distances, hence preserves $\mathbb P_k$; so every term has the same expectation $T_k$, and the first identity follows.</p>
:::
<p>Two cautions attach to this identity. The derivative is taken in a coupling that is present in the model, so it computes the block-sum correlation at the same intensity and not at a shifted one; and the second identity is a statement about $\mathbb P_n$, in which the spins of a level-$k$ block also interact with the rest of $\Lambda_n$, so it does not reduce to $T_k$ times the number of blocks. What the identity controls is the correlation of <a href="/articles/hierarchical-lattice/#section-children">child sums</a>, not of individual spins. For the Gaussian prior the two are related by a linear factor, which is how the <a href="/articles/gaussian-renormalisation-group/">exact solution</a> obtains its two-point function; for other priors individual-spin correlations require separate arguments.</p>

## Examples and non-examples {#section-examples}

<p><em>Ising spins.</em> With $\varrho=\tfrac12(\delta_{-1}+\delta_1)$, each $s_a$ is an integer between $-m^{n-1}$ and $m^{n-1}$, and $\mu_0$ is uniform on $\{\pm1\}$. The decimation identity reproduces the standard block-spin recursion of the Dyson model: the level-$n$ measure is $m$ independent copies of the level-$(n-1)$ measure, reweighted by a ferromagnetic coupling between their sums.</p>

<p><em>Gaussian spins.</em> With $\varrho=N(0,1)$ the same identity holds, and both the tilt and the pushforward preserve Gaussianity, so the recursion closes on the variance. This is the <a href="/articles/gaussian-renormalisation-group/">Gaussian renormalisation group</a>, and it is the only case in which the recursion is solved in closed form.</p>

<p><em>A kernel that is not constant on levels.</em> If $J$ depends on the pair rather than on the level, the first display fails: the interaction between two children is then a sum of terms with different intensities, and the block's energy depends on the internal arrangement of spins, not only on the sums. The <a href="/articles/hierarchical-and-euclidean-rg/">Euclidean obstruction</a> is of this kind but worse, since there the geometry of the blocks also changes with scale.</p>

<p><em>Periodic boundary conditions.</em> With the torus $\mathbb Z^d$ replacing $\mathbb H^d_L$ there is no ultrametric and no analogue of the level decomposition. Within the hierarchical lattice one can impose a "periodic" condition by identifying $\Lambda_n$ with a quotient of $\mathbb H^d_L$, but the resulting model is a finite graph whose blocks at the top have no children above them, and the identity then describes one decimation step only.</p>

## Variants and generalisations {#section-variants}

<p><em>External field.</em> Adding $-h\sum_x\sigma_x$ to the Hamiltonian multiplies the exponent of the decimation identity by $e^{h\sum_as_a}$, so the recursion becomes one for the law of the block spin with a field argument: $\mu_n=\mathcal T_{\beta J_n,h}\mu_{n-1}$. The field is relevant at the level of single spins and must be rescaled together with the spin.</p>

<p><em>Other priors.</em> A $\varphi^4$ prior $e^{-V(\sigma)}d\sigma$ with $V$ a quartic polynomial gives the same identity with $\mu_0$ not Gaussian, and the recursion no longer closes: it generates an infinite-dimensional family of laws. Controlling that family is the content of <a href="/articles/bleher-sinai-fixed-point/">the Bleher–Sinai analysis</a>.</p>

<p><em>Infinite volume.</em> The measures $\mathbb P_n$ are not consistent under restriction, because a restricted Gibbs measure is not Gibbsian for the restricted Hamiltonian; the infinite-volume limit requires a boundary condition and a compactness argument. Every identity above is finite-volume and exact, which is what the renormalisation group needs; passing to the limit is a separate step, taken in the articles on the <a href="/articles/bleher-sinai-fixed-point/">fixed point</a> and on <a href="/articles/critical-exponents-from-rg/">exponents</a>.</p>

## History and attribution {#section-history}

<p>Dyson (1969) introduced the block structure and the coupling $J_k$ decaying as a power to exhibit a phase transition in one dimension [@dyson-1969]. Bleher and Sinai (1973) made the block-spin law the object of study and wrote the recursion of this article as a nonlinear transformation of probability measures [@bleher-sinai-1973]; the presentation in terms of a level decomposition of the Hamiltonian is the one used in the modern renormalisation-group treatment of lattice field theory [@bauerschmidt-brydges-slade-2019]. The positivity of the block-sum correlations used for the free energy bound is a case of Griffiths's correlation inequalities for ferromagnetic systems [@griffiths-1967].</p>

## References {#section-references}

<ul>
<li>R. Bauerschmidt, D. C. Brydges and G. Slade, <em>Introduction to a Renormalisation Group Method</em>, Lecture Notes in Mathematics 2242, Springer, 2019.</li>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>F. J. Dyson, Existence of a phase-transition in a one-dimensional Ising ferromagnet, <em>Comm. Math. Phys.</em> 12 (1969), 91&ndash;107.</li>
<li>R. B. Griffiths, Correlations in Ising ferromagnets, <em>J. Math. Phys.</em> 8 (1967), 478&ndash;489.</li>
</ul>
