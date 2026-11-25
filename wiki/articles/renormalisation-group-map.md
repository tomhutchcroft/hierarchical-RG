---
{
  "id": "renormalisation-group-map",
  "title": "The renormalisation group map",
  "subtitle": "Decimation as an operator on one-variable laws, and the scaling that makes it autonomous.",
  "kind": "definition",
  "category": "Renormalisation group",
  "summary": "Block decimation sends the law of a child's block spin to the law of the parent's: a nonlinear operator on probability measures on the line, a Gibbs tilt of a product measure followed by summation. Rescaling the spin by L to the power minus (d+alpha)/2 makes the operators at different scales into powers of a single map, whose fixed points and linearisations carry the critical behaviour.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$; kernel exponent $\\alpha\\gt 0$; $J\\gt 0$.",
    "Laws are Borel probability measures on $\\mathbb R$ with finite second moment unless stated otherwise.",
    "The scale of the block spin is $\\theta_0=(d+\\alpha)/2$; the coupling argument of the autonomous map is $b=\\beta J_1$."
  ],
  "related": [
    "hierarchical-gibbs-measure",
    "gaussian-renormalisation-group",
    "critical-exponents-from-rg",
    "bleher-sinai-fixed-point",
    "corrections-to-scaling",
    "hierarchical-lattice",
    "hierarchical-percolation-rg",
    "ultrametric-block-systems"
  ],
  "sourceIds": [
    "bleher-sinai-1973",
    "bleher-sinai-1975",
    "bauerschmidt-brydges-slade-2019"
  ],
  "aliases": [
    "renormalisation group map",
    "block spin transformation",
    "decimation operator",
    "fixed point equation",
    "linearisation"
  ]
}
---

<p>Block decimation turns the <a href="/articles/hierarchical-gibbs-measure/">exact recursion</a> of a hierarchical spin system into an operator $\mathcal T_b$ on probability measures on the line: take $m$ independent copies of a law, tilt them by $\exp(b\sum_{a&lt;a'}s_as_{a'})$, and record the law of their sum. The model applies $\mathcal T_{\beta J_n}$ with $J_n$ decaying geometrically, so the sequence of operators is not autonomous; rescaling the spin by $L^{-\theta}$ with $\theta=\tfrac12(d+\alpha)$ multiplies the coupling by $L^{2\theta}$ at each step and makes the composition a power of one map $\mathcal R_\theta$.</p>

<p>That map is the object whose fixed points, and whose linearisation at them, carry the critical behaviour: a fixed point is a self-similar block-spin law, and the eigenvalues of the derivative there are the exponents, in the way made precise in <a href="/articles/critical-exponents-from-rg/">the article on exponents</a>. Two of its properties are used constantly and are proved here: it commutes with dilations, in the sense that $\mathcal T_b$ applied to a dilated law is the dilation of $\mathcal T_{b\lambda^2}$ applied to the law, and it is continuous on laws supported in a fixed compact set.</p>

<p>The construction is that of Bleher and Sinai (1973), who studied the transformation directly for Dyson's model [@bleher-sinai-1973], and it is the map developed from scratch in the renormalisation-group treatment of lattice field theory [@bauerschmidt-brydges-slade-2019]. Nothing in this article depends on the model being Gaussian or Ising; the two cases are worked out in <a href="/articles/gaussian-renormalisation-group/">the Gaussian article</a> and, in its own form, in <a href="/articles/hierarchical-percolation-rg/">the percolation article</a>.</p>

## Definitions and setting {#section-definition}

<p>Write $A$ for the index set of children, of cardinality $m=L^d$, and let $\mu$ be a Borel probability measure on $\mathbb R$. For $b\geq0$ put</p>
<div class="math-display">$$Z_b(\mu)=\int_{\mathbb R^m}\exp\Bigl(b\sum_{a<a'}s_as_{a'}\Bigr)\prod_{a\in A}\mu(ds_a),$$</div>
<p>with the convention that the integral is $+\infty$ when it diverges. The <em>decimation operator</em> is defined when $0&lt;Z_b(\mu)&lt;\infty$ by</p>
<a id="tag-R1FB" data-assertion="definition" data-title="The decimation operator"></a>
<div class="math-display">$$\mathcal T_b\mu(A')=\frac{1}{Z_b(\mu)}\int_{\mathbb R^m}\mathbf 1_{A'}\Bigl(\sum_{a\in A}s_a\Bigr)\exp\Bigl(b\sum_{a<a'}s_as_{a'}\Bigr)\prod_{a\in A}\mu(ds_a)$$</div>
<p>for Borel $A'\subseteq\mathbb R$, and the <em>scaled decimation operator</em> at exponent $\theta&gt;0$ is</p>
<div class="math-display">$$\mathcal R_{\theta,b}\mu=\bigl(s\mapsto L^{-\theta}s\bigr)_*\bigl(\mathcal T_b\mu\bigr),$$</div>
<p>the image of $\mathcal T_b\mu$ under multiplication by $L^{-\theta}$. The <em>quadratic form</em> of the tilt is $\sum_{a&lt;a'}s_as_{a'}=\tfrac12\bigl(\bigl(\sum_as_a\bigr)^2-\sum_as_a^2\bigr)$, so the tilt rewards configurations whose sum is large in absolute value.</p>
<p>If $\mu$ is supported in $[-K,K]$ then $0&lt;Z_b(\mu)&lt;\infty$ for every $b\geq0$, because the exponent is bounded on $[-K,K]^m$; and $\mathcal T_b\mu$ is then supported in $[-mK,mK]$. For a law with tails heavier than Gaussian the normaliser can diverge, and then the operator is undefined at that $b$; the Gaussian case in <a href="/articles/gaussian-renormalisation-group/">the next article</a> locates the threshold exactly.</p>

## Dilation covariance and continuity {#section-properties}

<p>Two properties make the operator usable: it scales in a fixed way when the input is dilated, and it is continuous in the input law.</p>
<a id="tag-P4YS" data-assertion="proposition" data-title="Dilation covariance of the decimation operator"></a>
<p>For $\lambda&gt;0$, with $\lambda_*\mu$ the law of $\lambda s$ under $\mu$,</p>
<div class="math-display">$$\mathcal T_b(\lambda_*\mu)=\lambda_*\bigl(\mathcal T_{b\lambda^2}\mu\bigr),\qquad \mathcal R_{\theta,b}(\lambda_*\mu)=\lambda_*\bigl(\mathcal R_{\theta,b\lambda^2}\mu\bigr).$$</div>
:::details Proof of dilation covariance
<p>Sampling $s_a$ from $\lambda_*\mu$ is the same as writing $s_a=\lambda t_a$ with $t_a$ sampled independently from $\mu$. The exponent becomes $b\lambda^2\sum_{a&lt;a'}t_at_{a'}$, the normaliser becomes $Z_{b\lambda^2}(\mu)$, and the sum becomes $\lambda\sum_at_a$. Hence the law of $\sum_as_a$ is the image under multiplication by $\lambda$ of the law of $\sum_at_a$ computed with coupling $b\lambda^2$, which is the first identity. Multiplying by $L^{-\theta}$ afterwards gives the second, since dilations commute.</p>
:::
<p>The identity is the reason no separate analysis is needed at each scale: a factor $\lambda$ in the spin is a factor $\lambda^2$ in the coupling, so the pair $(\text{scale},\text{coupling})$ flows on a cone.</p>
<a id="tag-E7NM" data-assertion="proposition" data-title="Continuity of decimation on compactly supported laws"></a>
<p>Fix $K&lt;\infty$ and $B&lt;\infty$. The map $(\mu,b)\mapsto\mathcal T_b\mu$ is continuous on the set of laws supported in $[-K,K]$ and couplings $b\in[0,B]$, for the topology of weak convergence, and $\mathcal T_b$ maps that set into the laws supported in $[-mK,mK]$.</p>
:::details Proof of continuity
<p>On $[-K,K]^m$ the tilt $\exp(b\sum_{a&lt;a'}s_as_{a'})$ is continuous in $(s,b)$ and bounded above by $e^{Bm(m-1)K^2/2}$ and below by $e^{-Bm(m-1)K^2/2}$, and the sum $\sum_as_a$ is continuous and bounded by $mK$. If $\mu_j\Rightarrow\mu$ weakly with all $\mu_j$ supported in $[-K,K]$ and $b_j\to b$, then $\mu_j^{\otimes m}\Rightarrow\mu^{\otimes m}$ because the product of a weakly convergent sequence of laws on a compact set converges weakly to the product, and the integrands above are continuous and bounded, so $Z_{b_j}(\mu_j)\to Z_b(\mu)$. The normalisers are bounded below by $e^{-Bm(m-1)K^2/2}$, which is positive, so the normalised measures converge weakly by the same bounded convergence applied to $\mathbf 1_{A'}(\sum_as_a)$ tested against bounded continuous functions of $\sum_as_a$. The support statement is immediate from $\lvert s_a\rvert\leq K$.</p>
:::
<p>The hypothesis of compact support is met by the Ising prior at finite volume, where the block spin of $\Lambda_n$ lies in $[-m^n,m^n]$, and it is met after rescaling only in the sense that the support bound $L^{(d-\theta)n}$ grows with $n$ when $\theta&lt;d$. The rescaled orbit is therefore not confined to a fixed compact set, and the continuity above does not by itself give compactness: what compactness requires is a uniform bound on the second moment of the rescaled laws, and supplying that bound is where the analysis of a particular model enters. Below the critical intensity the block spin has typical size $L^{dn/2}$, above it $L^{dn}$, and at the critical intensity $L^{\theta_0n}$ with $\theta_0=\tfrac12(d+\alpha)$; the rescaled orbit therefore shrinks, grows, or stays of order one in the three cases.</p>

## The autonomous form {#section-autonomous}

<p>The model applies a different operator at each scale. Rescaling the spin makes the sequence a power of one map, and this is the precise sense in which the renormalisation group is a dynamical system here.</p>
<a id="tag-T3GD" data-assertion="theorem" data-title="Self-similar form of the block-spin recursion"></a>
<p>Let $\beta\geq0$, $\theta_0=\tfrac12(d+\alpha)$ and $\nu_n$ be the law of $L^{-\theta_0n}S_{\Lambda_n}$ under $\mathbb P_n$ of the <a href="/articles/hierarchical-gibbs-measure/">hierarchical model</a>. Then, with $b=\beta J_1=\beta JL^{-(d+\alpha)}$,</p>
<div class="math-display">$$\nu_n=\mathcal R_{\theta_0,b}^{\,n}\nu_0\qquad(n\geq0).$$</div>
:::details Proof of the autonomous form
<p>The decimation identity gives $\mu_n=\mathcal T_{\beta J_n}\mu_{n-1}$ with $J_n=J_1L^{-(d+\alpha)(n-1)}$. Let $s_a$ have law $\mu_{n-1}$ and write $s_a=L^{\theta_0(n-1)}t_a$, so that $t_a$ has law $\nu_{n-1}$. Then $\beta J_n\sum_{a&lt;a'}s_as_{a'}=\beta J_nL^{2\theta_0(n-1)}\sum_{a&lt;a'}t_at_{a'}$, and $2\theta_0=d+\alpha$ gives $\beta J_nL^{2\theta_0(n-1)}=\beta J_1$. Hence $\mathcal T_{\beta J_n}\mu_{n-1}$ is the image under multiplication by $L^{\theta_0(n-1)}$ of $\mathcal T_{\beta J_1}\nu_{n-1}$, and $S_{\Lambda_n}=\sum_as_a=L^{\theta_0(n-1)}\sum_at_a$. Multiplying by $L^{-\theta_0n}$ gives $\nu_n=\mathcal R_{\theta_0,\beta J_1}\nu_{n-1}$. Induction from $\nu_0$ gives the statement.</p>
:::
<p>The exponent $\theta_0$ is not a physical prediction but the unique choice for which the coupling does not depend on $n$: with any other $\theta$ the argument of $\mathcal T$ would be $\beta J_1L^{2(\theta-\theta_0)(n-1)}$, growing or decaying geometrically, and the composition would not be a power of one map. Two consequences follow, and both are used later. The trajectory is the orbit of the initial law $\nu_0$ under a single map, so its asymptotics are those of a dynamical system; and if the orbit converges to a limit $\nu^*$ with $0&lt;\int s^2d\nu^*&lt;\infty$, then $\mathbb E[S_{\Lambda_n}^2]=L^{2\theta_0n}\int s^2d\nu^*\,(1+o(1))$, which fixes the growth of the block spin and hence one exponent, as <a href="/articles/critical-exponents-from-rg/">the exponent article</a> shows.</p>

## Fixed points and the linearisation {#section-fixed-points}

<a id="tag-V2HD" data-assertion="definition" data-title="Fixed point, relevant direction and eigenvalue"></a>
<p>A law $\nu^*$ is a <em>fixed point</em> of $\mathcal R_{\theta,b}$ if $\mathcal R_{\theta,b}\nu^*=\nu^*$ and $0&lt;\int s^2d\nu^*&lt;\infty$. At a fixed point, a bounded linear operator $D\mathcal R$ on the space of signed measures of zero total mass is the <em>linearisation</em> if</p>
<div class="math-display">$$\frac{\mathcal R_{\theta,b}\bigl((1-\epsilon)\nu^*+\epsilon\rho\bigr)-\nu^*}{\epsilon}\longrightarrow D\mathcal R\,\rho\quad(\epsilon\downarrow0)$$</div>
<p>for every signed measure $\rho$ of zero mass with $\int\lvert s\rvert^2d\lvert\rho\rvert(s)&lt;\infty$. A <em>direction</em> is an eigenmeasure $D\mathcal R\rho=\lambda\rho$; it is <em>relevant</em> if $\lvert\lambda\rvert&gt;1$, <em>marginal</em> if $\lvert\lambda\rvert=1$ and <em>irrelevant</em> if $\lvert\lambda\rvert&lt;1$.</p>
<p>The classification is the standard one for a map on a space of laws and it is used here in the following way. The orbit approaches the fixed point along its stable directions and leaves it along its unstable ones; the critical model is the one whose orbit stays, and the two relevant directions of the hierarchical model are the thermal one, which measures the distance from the critical intensity, and an irrelevant or marginal partner that controls corrections. The exponents are functions of the relevant eigenvalues; the dictionary is the content of <a href="/articles/critical-exponents-from-rg/">the exponent article</a>, and the linearisation is computed in closed form only in the <a href="/articles/gaussian-renormalisation-group/">Gaussian case</a>.</p>
<div class="fig" data-fig="flow" data-title="The two-coupling picture of the flow: a Gaussian fixed point, a nontrivial one, and the critical trajectory joining them. The exponents are read off the linearisation at whichever fixed point governs the model."></div>

## Examples and non-examples {#section-examples}

<p><em>The Gaussian orbit.</em> For $\nu_0=N(0,1)$ and the Gaussian prior, both the tilt and the summation preserve Gaussianity, so the orbit stays in the one-parameter family of centred Gaussians and the map reduces to a recursion on the variance: $\mathcal T_bN(0,v)=N(0,mv/(1-bv(m-1)))$ whenever the denominator is positive. This is worked out in <a href="/articles/gaussian-renormalisation-group/">the Gaussian article</a>, where the fixed point and the eigenvalue $L^\alpha$ are computed.</p>

<p><em>A degenerate fixed point.</em> The point mass $\delta_0$ is a fixed point of $\mathcal R_{\theta,b}$ for every $\theta$ and $b$: the tilt of a product of point masses is a point mass at $0$, and the sum is $0$. It carries zero variance and is excluded by the definition above. In the model it is the limit of the orbit below the critical intensity, where the rescaled block spin vanishes.</p>

<p><em>Non-example: a law with divergent normaliser.</em> If $\mu$ has a density decaying like $e^{-c\lvert s\rvert^p}$ with $0&lt;p&lt;2$, so that its tails are heavier than Gaussian, then $Z_b(\mu)=\infty$ for every $b&gt;0$ and $\mathcal T_b\mu$ is undefined. The Gaussian threshold at $b=1/((m-1)v)$ is the borderline case, and it is the reason the fixed-point analysis of the Gaussian model stops at the critical coupling.</p>

<p><em>Non-example: decimation of a Euclidean model.</em> On $\mathbb Z^d$ the analogous operation produces a law of the block magnetisation that is not a function of the block law alone, because the boundary between two blocks carries an interaction that depends on the arrangement of spins inside them. This is the subject of <a href="/articles/hierarchical-and-euclidean-rg/">the comparison article</a>.</p>

## Variants and generalisations {#section-variants}

<p><em>External field.</em> Adding a field gives a family $\mathcal T_{b,h}$ acting on laws of the block spin with the argument $h$ carried along, and the magnetic eigenvalue is the derivative of the flow at the fixed point in $h$. The single-field versions are what appears in the model with $-\beta h\sum_x\sigma_x$ in the Hamiltonian.</p>

<p><em>Anisotropic scaling.</em> Replacing $\theta_0$ by another exponent corresponds to weighting the sum differently at each scale and gives a map whose coupling is scale dependent. A fixed point of such a map is a self-similar law with anomalous scaling; the model's own recursion sits at $\theta_0$ and it is the physical exponents that decide whether the orbit of $\nu_0$ converges to a fixed point of $\mathcal R_{\theta_0,b}$ at all.</p>

<p><em>Other numbers of children.</em> Nothing in the definitions uses $m=L^d$ beyond the cardinality of $A$: the same operator makes sense with any integer $m\geq2$, and the lattice realisation with $m$ children and ratio $\lambda$ is the one described in <a href="/articles/hierarchical-lattice/#section-variants">the lattice article</a>.</p>

## History and attribution {#section-history}

<p>The transformation $\mathcal T_b$ is the renormalisation transformation of Bleher and Sinai (1973), who introduced it as a nonlinear integral operator on probability measures, proved that its fixed points govern the critical behaviour of Dyson's model, and computed the indices from its linearisation [@bleher-sinai-1973] [@bleher-sinai-1975]. The autonomous form of the recursion, and the reading of the model's block-spin sequence as an orbit of one map, are the derivations of that work; the systematic treatment in the language of measures with exponential tails, including the existence of the nontrivial fixed point, is in <a href="/articles/bleher-sinai-fixed-point/">the next article but one</a>, following Gawedzki and Kupiainen [@gawedzki-kupiainen-1983].</p>

## References {#section-references}

<ul>
<li>R. Bauerschmidt, D. C. Brydges and G. Slade, <em>Introduction to a Renormalisation Group Method</em>, Lecture Notes in Mathematics 2242, Springer, 2019.</li>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian fixed points of the block spin transformation. Hierarchical model approximation, <em>Comm. Math. Phys.</em> 89 (1983), 191&ndash;220.</li>
</ul>
