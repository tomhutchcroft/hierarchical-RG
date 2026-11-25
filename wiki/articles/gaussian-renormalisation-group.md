---
{
  "id": "gaussian-renormalisation-group",
  "title": "The Gaussian renormalisation group",
  "subtitle": "On Gaussian laws the decimation closes on the variance, and the critical fixed point has multiplier L to the alpha.",
  "kind": "theorem",
  "category": "Renormalisation group",
  "summary": "For a Gaussian prior, the law of a block spin stays Gaussian and its variance obeys a fractional linear recursion that is solved in closed form. The critical intensity is the reciprocal of the total kernel mass, the susceptibility is exactly beta_c over beta_c minus beta, and the recursion, written in the dimensionless coupling, has a nonzero fixed point with multiplier L to the alpha; hence the correlation-length exponent is one over alpha and the two-point exponent is two minus alpha.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$; kernel exponent $\\alpha\\gt 0$; $J\\gt 0$ and $J_k=JL^{-(d+\\alpha)k}$.",
    "Gaussian prior $N(0,1)$; free boundary conditions on $\\Lambda_n$; $\\beta\\geq0$ the intensity.",
    "The critical intensity is $\\beta_c$; $\\chi(\\beta)$ is the susceptibility of the model on $\\mathbb H^d_L$."
  ],
  "related": [
    "hierarchical-gibbs-measure",
    "renormalisation-group-map",
    "critical-exponents-from-rg",
    "bleher-sinai-fixed-point",
    "corrections-to-scaling",
    "gaussian-fixed-point-spectrum",
    "hierarchical-phi4-truncations",
    "hierarchical-symmetries",
    "koch-wittwer-fixed-point",
    "hierarchical-free-energy"
  ],
  "sourceIds": [
    "bleher-sinai-1973",
    "fisher-ma-nickel-1972",
    "bauerschmidt-brydges-slade-2019"
  ],
  "aliases": [
    "Gaussian fixed point",
    "free field",
    "variance recursion",
    "critical coupling",
    "multiplier"
  ]
}
---

<p>With a Gaussian single-spin prior the <a href="/articles/renormalisation-group-map/">decimation operator</a> preserves Gaussianity: the tilt is quadratic and the sum is linear, so the block spin of a Gaussian model is Gaussian and the whole orbit is described by one number, its variance. The recursion for that variance is fractional linear, so it is solved in closed form: the block-spin variance at scale $n$ is $L^{dn}$ divided by $1-\beta\sum_{x\ne0}J(\lVert x\rVert)$ truncated to the first $n$ shells. Three consequences follow without further work. The critical intensity is the reciprocal of the total kernel mass, so the interaction is summable exactly in the regime in which the intensity is finite; the susceptibility is exactly $(\beta_c-\beta)^{-1}\beta_c$; and the recursion written in the dimensionless variable $u_n=\beta J_nv_n$ has a nonzero fixed point whose multiplier is $L^\alpha$.</p>

<p>The multiplier is the point of the exercise. In the dictionary of <a href="/articles/critical-exponents-from-rg/">the exponent article</a>, a multiplier $\lambda_1=L^\alpha$ at the critical fixed point gives $\nu=\log L/\log\lambda_1=1/\alpha$, which is the classical long-range value; together with the block-spin growth exponent $\theta=\tfrac12(d+\alpha)$, which the normalisation of the recursion at <a href="/articles/renormalisation-group-map/#section-autonomous">the autonomous scale</a> forces, it gives $\kappa=\alpha$ and hence $\eta=2-\alpha$. These are the values tabulated for long-range interactions by Fisher, Ma and Nickel [@fisher-ma-nickel-1972], and they are exact for this model.</p>

<p>The Gaussian model is the one case of the hierarchical recursion that is solved in closed form, and it is the reference point for the others: the non-Gaussian fixed point of <a href="/articles/bleher-sinai-fixed-point/">Bleher and Sinai</a> merges with it at $\alpha=d/2$ and governs the critical behaviour above that value, and the percolation exponents of <a href="/articles/hierarchical-percolation-rg/">the percolation article</a> coincide with the Gaussian ones in the sense that its two-point exponent is also $2-\alpha$.</p>

## Definitions and setting {#section-model}

<p>Take the prior $\varrho=N(0,1)$ in the <a href="/articles/hierarchical-gibbs-measure/#section-model">hierarchical model</a>, with $J_k=JL^{-(d+\alpha)k}$ and $\beta\geq0$, and let $\mu_n$ be the law of the block spin $S_{\Lambda_n}$. The measure $\mathbb P_n$ is then a centred Gaussian measure on $\mathbb R^{\Lambda_n}$ and $\mu_n=N(0,v_n)$ with $v_n=\mathbb E_{\mathbb P_n}[S_{\Lambda_n}^2]$. Write $A$ for the operator on $\ell^2(\mathbb H^d_L)$ of convolution by the kernel $x\mapsto J(\lVert x\rVert)$, and $A_n$ for its compression to $\Lambda_n$, that is the symmetric matrix $A_n(x,y)=J(\lVert x-y\rVert)$ for distinct $x,y\in\Lambda_n$ and zero on the diagonal.</p>
<p>Two quantities organise the computation. The <em>coupling at level $n$</em> is $b_n=\beta J_n=\beta JL^{-(d+\alpha)n}$, and the <em>dimensionless coupling</em> is $u_n=b_nv_n$. The ratio of successive couplings is $\lambda=L^{d+\alpha}$.</p>

## Closure and the variance recursion {#section-closure}

<a id="tag-N1GK" data-assertion="theorem" data-title="Gaussian closure and the variance recursion"></a>
<p>Let $b\geq0$ and let $\mu=N(0,v)$ with $v&gt;0$. If $bv(m-1)&lt;1$ then $Z_b(\mu)&lt;\infty$ and</p>
<div class="math-display">$$\mathcal T_b\mu=N(0,v'),\qquad v'=\frac{mv}{1-bv(m-1)};$$</div>
<p>if $bv(m-1)\geq1$ then $Z_b(\mu)=\infty$ and $\mathcal T_b\mu$ is undefined.</p>
:::details Proof of the closure and the variance recursion
<p>Write $s=(s_a)_{a\in A}$ and let $\Sigma^{-1}=(v^{-1}+b)I-b\mathbf 1\mathbf 1^T$, where $\mathbf 1$ is the vector with all entries $1$. Completing the square,</p>
<div class="math-display">$$-\frac{1}{2v}\sum_as_a^2+\frac b2\Bigl(\bigl(\sum_as_a\bigr)^2-\sum_as_a^2\Bigr)=-\tfrac12s^T\Sigma^{-1}s,$$</div>
<p>so the tilted measure is $N(0,\Sigma)$ when $\Sigma^{-1}$ is positive definite, and in that case the law of $\sum_as_a$ is $N(0,\mathbf 1^T\Sigma\mathbf 1)$. Positive definiteness of $\Sigma^{-1}$ means $v^{-1}+b&gt;0$ and the determinant is positive; the eigenvalues of $\Sigma^{-1}$ are $v^{-1}+b$ with multiplicity $m-1$ and $v^{-1}+b-bm$ with multiplicity one, so the condition is $v^{-1}&gt;b(m-1)$, which is $bv(m-1)&lt;1$.</p>
<p>For the variance, apply the Woodbury identity $(A-uu^T)^{-1}=A^{-1}+\frac{A^{-1}uu^TA^{-1}}{1-u^TA^{-1}u}$ with $A=(v^{-1}+b)I$ and $u=\sqrt b\,\mathbf 1$. Then $\mathbf 1^TA^{-1}\mathbf 1=\frac{mv}{1+bv}$, so</p>
<div class="math-display">$$\mathbf 1^T\Sigma\mathbf 1=\frac{mv}{1+bv}+\frac{b\,(mv/(1+bv))^2}{1-bmv/(1+bv)}=\frac{mv}{1+bv-bmv}=\frac{mv}{1-bv(m-1)}.$$</div>
<p>If $bv(m-1)\geq1$, the quadratic form $s^T\Sigma^{-1}s$ takes nonpositive values on the line $\mathbb R\mathbf 1$, so the tilted density is not integrable and the normaliser diverges.</p>
:::
<p>The recursion is fractional linear in $v$, increasing and convex on its domain, and it blows up at the boundary $v=1/(b(m-1))$. It is the exact statement that the block spin of a Gaussian model is Gaussian: the tilt by a function of the sum and the pushforward by the sum preserve the class of centred Gaussians.</p>

## The closed form and the critical intensity {#section-critical}

<a id="tag-F9KB" data-assertion="theorem" data-title="Block-spin variance in closed form and the critical intensity"></a>
<p>For every $n\geq0$,</p>
<div class="math-display">$$v_n=\frac{m^n}{1-\beta J\,(1-L^{-d})\displaystyle\sum_{k=1}^{n}L^{-\alpha k}} ,$$</div>
<p>the model on $\Lambda_n$ exists for every $n$ exactly when $\beta\leq\beta_c$, where</p>
<div class="math-display">$$\beta_c=\frac{1}{\sum_{x\neq0}J(\lVert x\rVert)}=\frac{1-L^{-\alpha}}{J(1-L^{-d})L^{-\alpha}},$$</div>
<p>and for $\beta&lt;\beta_c$ one has $\chi(\beta):=\lim_nv_nL^{-dn}=\dfrac{\beta_c}{\beta_c-\beta}$. At $\beta=\beta_c$ one has $v_n=L^{(d+\alpha)n}$ for every $n$, and for $\beta&gt;\beta_c$ there is a first $n$ with $bv_n(m-1)\geq1$.</p>
:::details Proof of the closed form and the critical intensity
<p>Put $\rho=1/m=L^{-d}$, so that $\frac{1}{v_n}=\frac{1}{mv_{n-1}}-\frac{m-1}{m}b_n$ by the recursion, and iterate from $v_0=1$:</p>
<div class="math-display">$$\frac{1}{v_n}=\frac{1}{m^n}\Bigl(1-(m-1)\sum_{k=1}^nm^{k-1}b_k\Bigr).$$</div>
<p>Since $b_k=\beta Jm^{-(1+\alpha/d)k}$ and $m^{k-1}b_k=\beta Jm^{-1}m^{-\alpha k/d}=\beta JL^{-d}L^{-\alpha k}$, this is $\frac{1}{v_n}=L^{-dn}\bigl(1-\beta J(1-L^{-d})\sum_{k\leq n}L^{-\alpha k}\bigr)$, which is the first display after inversion. The bracket is decreasing in $n$ and its limit is $1-\beta J(1-L^{-d})\frac{L^{-\alpha}}{1-L^{-\alpha}}=1-\beta/\beta_c$ with $\beta_c$ as displayed; the row sum was computed in the <a href="/articles/hierarchical-lattice/#section-kernels">lattice article</a>. Hence the bracket stays positive for all $n$ exactly when $\beta&lt;\beta_c$, and then $v_nL^{-dn}\to\frac{1}{1-\beta/\beta_c}=\frac{\beta_c}{\beta_c-\beta}$. At $\beta=\beta_c$ the bracket is $1-(1-L^{-\alpha n})=L^{-\alpha n}$, giving $v_n=L^{dn}L^{\alpha n}$. For $\beta&gt;\beta_c$ the bracket is eventually negative, so the recursion leaves its domain at some finite $n$.</p>
:::
<p>The threshold has a second description, which does not use the recursion and which identifies it as the norm of the interaction rather than as an artefact of the block structure.</p>
<a id="tag-B5WC" data-assertion="proposition" data-title="The critical intensity is the reciprocal of the operator norm"></a>
<p>Let $A$ be convolution by $J(\lVert\cdot\rVert)$ on $\ell^2(\mathbb H^d_L)$ and $A_n$ its compression to $\Lambda_n$. Then $\lVert A\rVert=\sum_{x\neq0}J(\lVert x\rVert)$, and $\lambda_{\max}(A_n)\to\lVert A\rVert$ as $n\to\infty$.</p>
:::details Proof that the norm is the row sum
<p>For $\phi\in\ell^2$ with finite support, $\langle\phi,A\phi\rangle=\sum_{x,y}\phi_xJ(x-y)\phi_y\leq\lVert\phi\rVert_2^2\sup_x\sum_yJ(x-y)=\lVert\phi\rVert_2^2\sum_{z\neq0}J(z)$ by the Cauchy-Schwarz inequality applied to the pairs $(x,y)$ with weight $J$. For the reverse inequality take $\phi=\mathbf 1_{\Lambda_n}/\sqrt{\lvert\Lambda_n\rvert}$, which has norm one: then $\langle\phi,A\phi\rangle=\sum_zJ(z)\lvert\Lambda_n\cap(\Lambda_n-z)\rvert/\lvert\Lambda_n\rvert$. For fixed $z$ the ratio tends to $1$ as $n\to\infty$, and it is at most $1$, so dominated convergence gives convergence to $\sum_zJ(z)$. Hence $\lVert A_n\rVert\to\lVert A\rVert$, and $\lVert A\rVert$ is at least the limit of quotients and at most $\sum_zJ(z)$.</p>
:::
<p>For the finite-volume model, the Gaussian measure with density $\exp(-\frac\beta2\sigma^TA_n\sigma)$ exists exactly when $I-\beta A_n$ is positive definite, that is $\beta&lt;1/\lambda_{\max}(A_n)$, and the critical intensity of the infinite lattice is the limit. This agrees with the recursion, and it shows that the two-sided role of $\alpha&gt;0$ is unavoidable: at $\alpha\leq0$ the row sum diverges and there is no finite intensity at which the field exists.</p>

## The autonomous flow and the multiplier {#section-multiplier}

<p>Written in the dimensionless coupling, the recursion has a nonzero fixed point, and its multiplier is the exponent.</p>
<div class="sim" data-sim="rg-orbit" data-title="The Gaussian orbit: choose the intensity and watch the block-spin variance against the scale. Above βc it grows, below it dies, and on the dashed critical orbit it grows like L^{(d+α)n}."></div>
<a id="tag-K7DR" data-assertion="theorem" data-title="Fixed point of the dimensionless coupling and the multiplier L to the alpha"></a>
<p>Let $u_n=b_nv_n$ with $b_n=\beta J_n$. Then $u_n=g(u_{n-1})$, where</p>
<div class="math-display">$$g(u)=\frac{mu}{\lambda-(m-1)u},\qquad \lambda=L^{d+\alpha},$$</div>
<p>on the domain $u&lt;\lambda/(m-1)$. The map $g$ has the fixed point $u^*=\dfrac{m(L^{\alpha}-1)}{m-1}$, and $g'(u^*)=\lambda/m=L^{\alpha}$. The critical orbit is $u_n\equiv u^*$; for $\beta&lt;\beta_c$ one has $u_n\to0$ with ratio $L^{-\alpha}$, and for $\beta&gt;\beta_c$ the orbit leaves the domain.</p>
:::details Proof of the fixed point and the multiplier
<p>Multiply the variance recursion by $b_n$: $u_n=\frac{mb_nv_{n-1}}{1-b_nv_{n-1}(m-1)}$. Since $b_nv_{n-1}=\lambda^{-1}b_{n-1}v_{n-1}=\lambda^{-1}u_{n-1}$, this is $u_n=\frac{m\lambda^{-1}u_{n-1}}{1-(m-1)\lambda^{-1}u_{n-1}}=g(u_{n-1})$.</p>
<p>The fixed point equation $u=g(u)$ with $u\neq0$ is $1-(m-1)\lambda^{-1}u=m\lambda^{-1}$, giving $u^*=\lambda\frac{1-m/\lambda}{m-1}=\frac{\lambda-m}{m-1}=\frac{m(L^\alpha-1)}{m-1}$. Differentiating, $g'(u)=\frac{m\lambda}{(\lambda-(m-1)u)^2}$, and at $u^*$ the denominator is $\lambda-(m-1)u^*=\lambda-m(L^\alpha-1)=L^d(L^\alpha-L^\alpha+1)=L^d=m$, so $g'(u^*)=\frac{m\lambda}{m^2}=\lambda/m=L^\alpha$.</p>
<p>For the critical orbit, the closed form at $\beta=\beta_c$ gives $v_n=L^{(d+\alpha)n}$ and $b_n=\beta_cJL^{-(d+\alpha)n}$, so $u_n=\beta_cJ$ for every $n$, and $\beta_cJ=\frac{L^\alpha-1}{1-L^{-d}}=\frac{m(L^\alpha-1)}{m-1}=u^*$. For $\beta&lt;\beta_c$ the orbit converges to the fixed point $0$ of $g$, where $g'(0)=m/\lambda=L^{-\alpha}$. For $\beta&gt;\beta_c$ the variance recursion leaves its domain, so the orbit of $g$ leaves the interval $[0,\lambda/(m-1))$.</p>
:::
<p>The multiplier $L^\alpha$ is the whole content of the model's critical behaviour. A perturbation of the critical orbit is multiplied by $L^\alpha$ per scale, so the distance from criticality acts like a length growing as $L^\alpha$ per scale; inverting, a system at distance $\delta$ from criticality has correlation length of order $\delta^{-1/\alpha}$, which is the statement $\nu=1/\alpha$. The vanishing of $u_n$ below criticality at rate $L^{-\alpha}$ says the same thing for the approach to the disordered fixed point.</p>

## The exponents {#section-exponents}

<a id="tag-H3MX" data-assertion="corollary" data-title="Exponents of the Gaussian fixed point"></a>
<p>The Gaussian fixed point has</p>
<div class="math-display">$$\nu=\frac{1}{\alpha},\qquad \eta=2-\alpha,\qquad \gamma=1,\qquad \beta_{\mathrm{o}}=\frac{d-\alpha}{2\alpha},\qquad \delta=\frac{d+\alpha}{d-\alpha},\qquad \alpha_{\mathrm{hy}}=2-\frac{d}{\alpha}.$$</div>
:::details Proof of the exponent values
<p>The multiplier at the fixed point is $\lambda_1=L^\alpha$, so $\nu=\log L/\log\lambda_1=1/\alpha$ by the definition of $\nu$ in <a href="/articles/critical-exponents-from-rg/#section-dictionary">the dictionary</a>. The normalisation of the recursion is at $\theta_0=\tfrac12(d+\alpha)$, and the critical orbit has $v_n=L^{2\theta_0n}$ by the previous section, so the susceptibility of a block grows like $L^{\alpha n}$ and $\kappa=\alpha$, that is $\eta=2-\alpha$. The remaining values follow from the dictionary with $\kappa=\alpha$ and $\nu=1/\alpha$: $\gamma=\kappa\nu=1$, $\beta_{\mathrm{o}}=\tfrac{\nu}{2}(d-\kappa)=\frac{d-\alpha}{2\alpha}$, $\delta=\frac{d+\kappa}{d-\kappa}=\frac{d+\alpha}{d-\alpha}$ and $\alpha_{\mathrm{hy}}=2-d\nu=2-d/\alpha$, and the susceptibility exponent is checked directly by the closed form $\chi=\beta_c(\beta_c-\beta)^{-1}$.</p>
:::
<p>The values are those of the classical long-range theory, with $\nu=1/\alpha$ independent of the dimension and $\eta$ tending to $1$ as $\alpha\uparrow d$. They satisfy the scaling relations $\gamma=\nu(2-\eta)$, $\gamma=\beta_{\mathrm{o}}(\delta-1)$ and $2-\alpha_{\mathrm{hy}}=d\nu$ identically in $\alpha$ and $d$; the second is $\frac{d-\alpha}{2\alpha}\cdot\frac{2\alpha}{d-\alpha}=1$, and the third is $2-(2-d/\alpha)=d/\alpha$. At $\alpha=d/2$ they reduce to $\nu=2/d$, $\eta=2-d/2$, $\delta=3$, $\beta_{\mathrm{o}}=1/2$ and $\alpha_{\mathrm{hy}}=0$: the Ising values of $\delta$, $\gamma$ and $\beta_{\mathrm{o}}$, with $\nu=2/d$ in place of the short-range mean-field value $\tfrac12$, the difference being the hyperscaling relation $2-\alpha_{\mathrm{hy}}=d\nu$, which holds here with $\alpha_{\mathrm{hy}}=0$ and fails for the short-range mean-field exponents above $d=4$.</p>

## The two-point function in a block {#section-two-point}

<a id="tag-M6TP" data-assertion="proposition" data-title="Gaussian two-point function at the top level of a block"></a>
<p>Let $n\geq1$ and let $x,y\in\Lambda_n$ lie in different children of $\Lambda_n$, so that $\lVert x-y\rVert=L^n$. Then in the free-boundary model on $\Lambda_n$,</p>
<div class="math-display">$$\tau_\beta(x,y)=\frac{1}{L^{2d(n-1)}}\cdot\frac{b_nv_{n-1}^2}{(1+b_nv_{n-1})\bigl(1-b_nv_{n-1}(m-1)\bigr)}.$$</div>
<p>Consequently, at $\beta=\beta_c$,</p>
<div class="math-display">$$\tau_{\beta_c}(x,y)=\frac{L^{\alpha}-1}{L^{d}-L^{-\alpha}}\,L^{-(d-\alpha)(n-1)},$$</div>
<p>and for fixed $\beta&lt;\beta_c$, as $n\to\infty$, $\tau_\beta(x,y)\sim\beta J\chi(\beta)^2L^{-(d+\alpha)n}$.</p>
:::details Proof of the two-point formula
<p>By the decimation identity the law of $(S_a)$, the child sums of $\Lambda_n$, is the tilt of $\mu_{n-1}^{\otimes m}$ by $\exp(b_n\sum_{a&lt;a'}s_as_{a'})$, so the covariance of two distinct child sums is an off-diagonal entry of the matrix $\Sigma$ of the closure theorem, with $v=v_{n-1}$ and $b=b_n$:</p>
<div class="math-display">$$\Sigma_{aa'}=\frac{b_nv_{n-1}^2}{(1+b_nv_{n-1})\bigl(1-b_nv_{n-1}(m-1)\bigr)},\qquad \Sigma_{aa}=\frac{v_{n-1}}{1+b_nv_{n-1}}+\Sigma_{aa'}.$$</div>
<p>Conditionally on the child sums $(S_a)$, the configuration in the child $a$ is the level-$(n-1)$ Gibbs measure on that child with its total spin prescribed, and by <a href="/articles/hierarchical-symmetries/#section-consequences">the translation symmetry of a child</a>, $\mathbb E[\sigma_x\mid(S_a)]=S_a/\lvert\Lambda_{n-1}\rvert=S_a/L^{d(n-1)}$ for $x$ in the child $a$. The Hamiltonian factorises over children once the sums are fixed, so the fields in two different children are conditionally independent given $(S_a)$, and $\tau_\beta(x,y)=\mathbb E[S_aS_{a'}]/L^{2d(n-1)}=\Sigma_{aa'}/L^{2d(n-1)}$.</p>
<p>At $\beta=\beta_c$ one has $b_nv_{n-1}=q:=\frac{1-L^{-\alpha}}{m-1}$ and $v_{n-1}=L^{(d+\alpha)(n-1)}$, so $\Sigma_{aa'}=\frac{qL^{\alpha}}{1+q}v_{n-1}$ and $\tau_{\beta_c}=\frac{qL^\alpha}{1+q}L^{-(d-\alpha)(n-1)}$, with $\frac{qL^\alpha}{1+q}=\frac{L^\alpha-1}{L^d-L^{-\alpha}}$. For $\beta&lt;\beta_c$, $v_{n-1}=\chi L^{d(n-1)}(1+o(1))$ and $b_nv_{n-1}\to0$, so $\Sigma_{aa'}\sim b_nv_{n-1}^2\sim\beta J\chi^2L^{-(d+\alpha)n}L^{2d(n-1)}$.</p>
:::
<p>The proposition is a statement about the top level of a block at free boundary, and the restriction matters: a pair at level $j$ inside the larger block $\Lambda_n$ with $n&gt;j$ has a larger covariance, because paths inside $\Lambda_n$ that leave the level-$j$ block also join the pair. What is uniform is the asymptotic form, which is read off from the sequence of top levels.</p>
<p>The two regimes are worth distinguishing. Below criticality the correlation of two adjacent children is of the order of the coupling that joins them, $L^{-(d+\alpha)n}$, which is the kernel itself; the sum over scales then converges and the susceptibility is finite, in agreement with the closed form. At criticality the correlation is larger by a factor $L^{2\alpha n}$ and decays only as $L^{-(d-\alpha)n}$, so the shell sums diverge and the susceptibility with them. The difference between the two exponents is exactly the multiplier: the pair correlation gains $L^{\alpha}$ per scale at criticality, and the modulus $\lVert x-y\rVert^{-(d-\alpha)}$ is the same statement in the variable $\lVert x-y\rVert=L^n$.</p>

## Examples and non-examples {#section-examples}

<p><em>One dimension, two children, $\alpha=\tfrac12$.</em> Here $L=2$, $d=1$, $m=2$, $J_k=2^{-3k/2}$ and $\beta_c=2(\sqrt2-1)\approx0.828$. The block-spin variance at criticality is $2^{3n/2}$, and the covariance of two vertices at distance $2^j$ is $0.3204\ldots\times2^{-j/2}$, which is $\lVert x-y\rVert^{-(1-\frac12)}$ up to the constant. The multiplier is $\sqrt2$.</p>

<p><em>The free field on $\mathbb Z^d$.</em> Replacing $\mathbb H^d_L$ by $\mathbb Z^d$ with the same power kernel leaves the Gaussian computation meaningful only in the limit of a continuum scaling limit; the block recursion no longer closes, because the block magnetisation is a vector and the interaction between neighbouring blocks depends on their relative position. This is the contrast drawn in <a href="/articles/hierarchical-and-euclidean-rg/">the comparison article</a>.</p>

<p><em>Non-example: a $\varphi^4$ prior.</em> With $\varrho\propto e^{-\lambda\sigma^4-\frac{\mu}{2}\sigma^2}d\sigma$ the tilted image of a quartic law is not quartic: the summation and the tilt generate all even powers. The recursion leaves the one-parameter family, and the fixed point of the full map is the subject of <a href="/articles/bleher-sinai-fixed-point/">the Bleher–Sinai article</a>.</p>

<p><em>Non-example: the critical field at $\beta=\beta_c$.</em> The formula for $\tau_{\beta_c}$ is a statement about correlations inside a block at free boundary. The infinite-volume Gaussian field does not exist at $\beta_c$, because $I-\beta_cA$ is not invertible on $\ell^2$; the critical object is a scaling limit, and the formula above is the finite-volume shadow of it.</p>

## Variants and generalisations {#section-variants}

<p><em>External field.</em> Adding $-\beta h\sum_x\sigma_x$ makes the block-spin law Gaussian with a mean, and the recursion becomes affine: the mean is multiplied by $1/(1+b_nv_{n-1}(m-1))$ per scale. The magnetic eigenvalue of that recursion is the number that appears in $\delta$ for models where the scaling relations hold; in the Gaussian case it reproduces $\delta=\frac{d+\alpha}{d-\alpha}$.</p>

<p><em>Any $m$ and $\lambda$.</em> The computation uses only $m$ and $\lambda=L^{d+\alpha}$, so it applies to the operator $\mathcal T_b$ with any integer $m\geq2$ and any coupling ratio $\lambda&gt;m$; with $\alpha=\log(\lambda/m)/\log L$; the multiplier is $\lambda/m=L^{\alpha}$ and the exponents are $\nu=1/\alpha$ and $\kappa=\alpha$, as in <a href="/articles/hierarchical-lattice/#section-variants">the lattice article</a>.</p>

<p><em>Complex eigenvalues.</em> The linearisation of the full (non-Gaussian) map at its nontrivial fixed point can have a complex pair of eigenvalues, which produces oscillatory corrections to scaling. In the Gaussian case the linearisation is triangular on the moments and the eigenvalues are real; the phenomenon belongs to <a href="/articles/bleher-sinai-fixed-point/">the nontrivial fixed point</a>.</p>

## History and attribution {#section-history}

<p>The variance recursion and the identification of the critical point as the value at which the block-spin variance starts to grow like $L^{(d+\alpha)n}$ are in Bleher and Sinai's treatment of Dyson's model [@bleher-sinai-1973], where the Gaussian case is the model problem solved before the general one. The exponent values $\eta=2-\alpha$ and $\nu=1/\alpha$ are the classical long-range values of Fisher, Ma and Nickel [@fisher-ma-nickel-1972], and the role of the Gaussian fixed point as the reference for the renormalisation-group analysis of lattice fields is set out by Bauerschmidt, Brydges and Slade [@bauerschmidt-brydges-slade-2019].</p>

## References {#section-references}

<ul>
<li>R. Bauerschmidt, D. C. Brydges and G. Slade, <em>Introduction to a Renormalisation Group Method</em>, Lecture Notes in Mathematics 2242, Springer, 2019.</li>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>M. E. Fisher, S.-k. Ma and B. G. Nickel, Critical exponents for long-range interactions, <em>Phys. Rev. Lett.</em> 29 (1972), 917&ndash;920.</li>
</ul>
