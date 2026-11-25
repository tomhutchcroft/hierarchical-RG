---
{
  "id": "critical-exponents-from-rg",
  "title": "Critical exponents from the renormalisation group",
  "subtitle": "Two numbers from the fixed point, and the algebra that turns them into the exponents.",
  "kind": "theorem",
  "category": "Renormalisation group",
  "summary": "The exponents of a hierarchical model are read off from its fixed point: one from the multiplier of the linearised map, giving the correlation-length exponent, and one from the growth of the block spin, giving the susceptibility exponent and hence the two-point exponent. The scaling relations are then algebra, and hyperscaling is the one hypothesis that is not automatic. A third route, through the concavity of the magnetisation in the boundary field, needs no fixed point: it sandwiches the finite-size magnetisation between the block-spin variances of the plus and the free states, and shows that at criticality a vanishing boundary field still pins the block spin.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$; kernel exponent $0\\lt \\alpha\\lt d$; $J\\gt 0$.",
    "The infinite-volume two-point function $\\tau_\\beta$ is assumed to decay exponentially for $\\beta\\lt \\beta_c$ and to satisfy the block bounds stated in the text.",
    "$\\kappa$ is the growth exponent of the critical block susceptibility and $\\nu$ the multiplier exponent; $\\theta=\\tfrac12(d+\\kappa)$."
  ],
  "related": [
    "renormalisation-group-map",
    "gaussian-renormalisation-group",
    "bleher-sinai-fixed-point",
    "hierarchical-percolation-rg"
  ],
  "sourceIds": [
    "bleher-sinai-1975",
    "fisher-ma-nickel-1972",
    "aizenman-fernandez-1988",
    "hutchcroft-hierarchical-2021",
    "ghs-1970"
  ],
  "aliases": [
    "critical exponents",
    "scaling relations",
    "hyperscaling",
    "anomalous dimension",
    "susceptibility exponent"
  ]
}
---

<p>A model with a renormalisation-group fixed point has two numbers that matter: the multiplier $\lambda_1$ of the linearised map at the fixed point, which says how fast a perturbation of the critical intensity is amplified per scale, and the growth exponent $\theta$ of the block spin at criticality, which says how large a block's magnetisation is at scale $L^n$. The first gives the correlation-length exponent through $\nu=\log L/\log\lambda_1$; the second gives the susceptibility exponent $\kappa=2\theta-d$, which is the same as the statement $\eta=2-\kappa$. Every other exponent follows from these two by algebra, provided the standard scaling hypotheses hold; hyperscaling is the one that can fail, and it fails in the classical regime of percolation.</p>

<p>The hierarchical model contributes something that the Euclidean theory does not have: the growth exponent is not free. Because the recursion is autonomous only at $\theta=\tfrac12(d+\alpha)$, as <a href="/articles/renormalisation-group-map/#section-autonomous">the map article</a> shows, any fixed point of the rescaled recursion with a finite nonzero variance has $\theta=\tfrac12(d+\alpha)$, so $\kappa=\alpha$ and $\eta=2-\alpha$ for every fixed point of this model. The nontrivial exponent is $\nu$; in the <a href="/articles/gaussian-renormalisation-group/">Gaussian case</a> it takes the classical value $1/\alpha$, and at the <a href="/articles/bleher-sinai-fixed-point/">Bleher–Sinai fixed point</a> it does not.</p>

<p>For percolation on the hierarchical lattice both statements are theorems: the two-point exponent is $2-\alpha$ for every $0&lt;\alpha&lt;d$ [@hutchcroft-hierarchical-2021], and the volume exponent satisfies $\delta\geq\frac{d+\alpha}{d-\alpha}$ above the triangle threshold, with equality conjectured. The classical long-range values are tabulated by Fisher, Ma and Nickel [@fisher-ma-nickel-1972]; the rigorous versions in the mean-field region are due to Aizenman and Fernandez [@aizenman-fernandez-1988].</p>

## Definitions and setting {#section-exponents}

<a id="tag-E1QZ" data-assertion="definition" data-title="The exponents of a hierarchical model"></a>
<p>Let $0&lt;\alpha&lt;d$. Write $\tau_n(x,y)$ for the two-point function of the model on the block $\Lambda_n$ with free boundary conditions — the connection probability for percolation, the spin correlation for an Ising model — and $\tau_\beta(x,y)$ for that of the model on $\mathbb H^d_L$, when it exists. Let $\beta_c$ be the critical intensity, and for $n\geq0$ let</p>
<div class="math-display">$$\chi_n(\beta)=\sum_{y\in\Lambda_n}\tau_n(0,y)$$</div>
<p>be the <em>block susceptibility</em>; for percolation $\chi_n(\beta)=\mathbb E_\beta\lvert K^{\Lambda_n}_0\rvert$ is the expected size of the restricted cluster of the origin. The exponents are defined by the following asymptotic statements, each a hypothesis on the model whenever it is used below.</p>
<div class="math-display">$$\chi_n(\beta_c)\asymp L^{\kappa n};\qquad \tau_{\beta_c}(0,y)\asymp\lVert y\rVert^{-(d-2+\eta)};\qquad \eta=2-\kappa;$$</div>
<div class="math-display">$$\tau_\beta(0,y)\asymp e^{-n/\xi(\beta)}\quad(\lVert y\rVert=L^n,\ \beta&lt;\beta_c);\qquad \xi(\beta)\asymp\lvert\beta_c-\beta\rvert^{-\nu};\qquad \chi(\beta)\asymp\lvert\beta_c-\beta\rvert^{-\gamma};$$</div>
<div class="math-display">$$M(\beta)\asymp(\beta-\beta_c)^{\beta_{\mathrm{o}}}\ (\beta\downarrow\beta_c);\qquad M(\beta_c,h)\asymp h^{1/\delta};\qquad F_{\mathrm{sing}}\asymp\lvert\beta_c-\beta\rvert^{2-\alpha_{\mathrm{hy}}}.$$</div>
<p>Here $M$ is the spontaneous magnetisation, the limit of the mean block spin per site
<div class="sim" data-sim="exponents" data-title="The dictionary as a calculator: choose the dimension, the scale and the kernel exponent and read the classical exponents of the Gaussian fixed point. The three scaling relations hold identically; the readout shows the residuals."></div>, and $F_{\mathrm{sing}}$ the singular part of the free energy per site. The two definitions of $\eta$ agree by the calculation below: if the critical two-point function is radial and of order $\lVert y\rVert^{-(d-2+\eta)}$, the shell at level $k$ contributes $L^{dk}\cdot L^{-(d-2+\eta)k}=L^{(2-\eta)k}$ to the block susceptibility, so $\chi_n\asymp L^{(2-\eta)n}$. The content of the definition is that $\kappa$ and $\eta$ are one number read at two scales.</p>

## Block identities {#section-identities}

<p>Two identities convert block quantities into correlations. The first is exact at finite volume and needs no assumption beyond the model.</p>
<a id="tag-C4ND" data-assertion="proposition" data-title="Block-spin variance is the volume times the block susceptibility"></a>
<p>For the spin model of <a href="/articles/hierarchical-gibbs-measure/">the decimation article</a> with $S_n=\sum_{x\in\Lambda_n}\sigma_x$ and free boundary conditions on $\Lambda_n$,</p>
<div class="math-display">$$\mathbb E_\beta[S_n^2]=L^{dn}\chi_n(\beta)$$</div>
<p>for every $\beta$ and every $n$.</p>
:::details Proof of the block identity
<p>Expanding the square and taking expectations gives $\mathbb E[S_n^2]=\sum_{x,y\in\Lambda_n}\tau_n(x,y)$. Translation by any $x\in\Lambda_n$ preserves $\Lambda_n$ because $\Lambda_n$ is a subgroup, and preserves the finite-volume Gibbs measure because the Hamiltonian depends only on differences and the prior is a product; hence $\tau_n(x,y)=\tau_n(0,y-x)$. Since $\Lambda_n$ is a subgroup, $y-x\in\Lambda_n$ for $x,y\in\Lambda_n$, and summing over $x$ first gives</p>
<div class="math-display">$$\mathbb E[S_n^2]=\sum_{y\in\Lambda_n}\sum_{x\in\Lambda_n}\tau_n(0,y-x)=\lvert\Lambda_n\rvert\sum_{z\in\Lambda_n}\tau_n(0,z)=L^{dn}\chi_n(\beta),$$</div>
<p>the inner sum being independent of $y$ by the substitution $z=y-x$.</p>
:::
<p>The identity is the bridge between the two descriptions. The left side is what the <a href="/articles/renormalisation-group-map/">decimation map</a> controls directly, since the block-spin law is the state of the recursion; the right side is a correlation sum. The equality says the two growth rates are the same number: a block spin of typical size $L^{(d+\kappa)n/2}$ is exactly a block susceptibility growing like $L^{\kappa n}$.</p>
<p>The second identity passes from the block sum to individual vertices, and it needs radial symmetry of the critical two-point function.</p>
<a id="tag-Y9KQ" data-assertion="proposition" data-title="Shell averages from the block susceptibility"></a>
<p>Suppose that $\tau_{\beta_c}$ is radial, $\tau_{\beta_c}(0,y)=f(\lVert y\rVert)$, and let $g_k$ be the mean of $f$ over the shell at level $k$. If $\chi_n(\beta_c)\asymp L^{\kappa n}$ then $g_k\leq CL^{-(d-\kappa)k}$ for every $k$, with $C$ depending only on $L,d$ and the constants in the hypothesis; and if $g_k\leq CL^{-(d-\kappa)k}$ for every $k$ then $\chi_n(\beta_c)\leq A'L^{\kappa n}$. Conversely, if $g_k\asymp L^{-(d-\kappa)k}$, then $\chi_n(\beta_c)\asymp L^{\kappa n}$; and if in addition $k\mapsto L^{(d-\kappa)k}g_k$ is monotone, then $\chi_n(\beta_c)\asymp L^{\kappa n}$ implies the two-sided bound $g_k\asymp L^{-(d-\kappa)k}$.</p>
:::details Proof of the shell estimates
<p>The shell at level $k$ has $S_k=(1-L^{-d})L^{dk}$ vertices, and $\chi_n=\sum_{k\leq n}S_kg_k$. Since all terms are nonnegative, $S_kg_k\leq\chi_k\leq AL^{\kappa k}$ for $k\leq n$, which is $g_k\leq\frac{A}{1-L^{-d}}L^{-(d-\kappa)k}$; this gives the first two statements, the second by summing the geometric series $\sum_{k\leq n}S_kCL^{-(d-\kappa)k}=C(1-L^{-d})\sum_{k\leq n}L^{\kappa k}$.</p>
<p>If $g_k\geq cL^{-(d-\kappa)k}$ for all $k$ then the sum is at least a constant times $L^{\kappa n}$, since the last term alone is $S_ng_n\geq c(1-L^{-d})L^{\kappa n}$; this gives the converse. Under the monotonicity hypothesis write $h_k=L^{(d-\kappa)k}g_k$ and note that $\chi_n=\sum_{k\leq n}(1-L^{-d})L^{\kappa k}h_k$; if $h_k\leq h_n$ for $k\leq n$ then $\chi_n\leq(1-L^{-d})h_n\sum_{k\leq n}L^{\kappa k}\leq C'h_nL^{\kappa n}$, so $aL^{\kappa n}\leq\chi_n$ and $\chi_n\leq C'h_nL^{\kappa n}$ give $h_n\geq a/C'$, which is the lower bound; the upper bound is the first statement.</p>
:::
<p>The second proposition is the version needed for percolation, where the two-point function is known to be radial and the exponent is proved from the block sums. The averaging is essential: the block susceptibility controls the shell means, and the pointwise statement is a separate result, requiring <a href="/articles/hierarchical-symmetries/">the level-isometry symmetry of the lattice</a> in addition.</p>

## The growth exponent is fixed {#section-growth}

<a id="tag-A8VL" data-assertion="theorem" data-title="Any convergent rescaled orbit has the prescribed block-spin growth"></a>
<p>Let $\nu_n$ be the law of $L^{-\theta_0n}S_n$ with $\theta_0=\tfrac12(d+\alpha)$ and suppose that $\nu_n$ converges weakly to a law $\nu^*$ with $0&lt;\int s^2d\nu^*&lt;\infty$, the second moments being uniformly integrable. Then</p>
<div class="math-display">$$\mathbb E_\beta[S_n^2]=L^{(d+\alpha)n}\int s^2d\nu^*\,(1+o(1)),\qquad \chi_n(\beta)\asymp L^{\alpha n},$$</div>
<p>so $\kappa=\alpha$ and $\eta=2-\alpha$. The growth exponent is $\theta_0$ for every fixed point of the rescaled recursion, independently of the intensity and of the fixed point.</p>
:::details Proof of the growth theorem
<p>By definition $\mathbb E[S_n^2]=L^{2\theta_0n}\int s^2d\nu_n$ and $2\theta_0=d+\alpha$. Weak convergence together with uniform integrability of the second moments gives $\int s^2d\nu_n\to\int s^2d\nu^*$, which is the first display after substituting $2\theta_0=d+\alpha$. The second follows from the block identity $\chi_n=L^{-dn}\mathbb E[S_n^2]=L^{\alpha n}\int s^2d\nu^*(1+o(1))$, and $\kappa=\alpha$ is the definition of $\kappa$.</p>
:::
<p>The mechanism is worth separating from the bookkeeping. The autonomy of the recursion at $\theta_0$ is a statement about the couplings, and it says that the only self-similar law consistent with them has block spins growing at rate $L^{\theta_0n}$. What the theorem adds is convergence of the orbit, which is the content of the fixed-point theory in the <a href="/articles/gaussian-renormalisation-group/">Gaussian</a> and <a href="/articles/bleher-sinai-fixed-point/">non-Gaussian</a> cases. The exponent that is not fixed this way is $\nu$, which measures the rate at which the orbit leaves the fixed point and is computed from the linearisation.</p>

## The variance route to the growth exponent {#section-variance-route}

<p>The growth theorem above reads the exponent off a fixed point, so it presupposes that the orbit converges. There is a second route, which assumes nothing about the orbit and instead compares the block spin of the plus state with that of the free state; it gives an inequality rather than an identity, and the inequality is valid at every intensity, including at the critical one.</p>

<p>The input is the concavity of the magnetisation in a positive field. Turn the boundary condition on gradually: for $t\in[0,1]$ let $\mathbb P^{(t)}_{\Lambda_n}$ be the measure whose boundary spins are all $t$, so that $t=0$ is free and $t=1$ is the plus condition, and recall from <a href="/articles/hierarchical-magnetised-phase/#section-block-average">the block-average section</a> that the boundary energy is $-tB_nS_{\Lambda_n}$ with $B_n=CL^{-\alpha n}$.</p>
<a id="tag-XZYU" data-assertion="proposition" data-title="The block-spin variance is maximal at zero boundary field, and the sandwich it gives"></a>
<p>For every $\beta$ and $n$, the map $t\mapsto\mathbb E_{\mathbb P^{(t)}_{\Lambda_n}}[S_{\Lambda_n}]$ is concave and increasing on $[0,1]$, so $t\mapsto\operatorname{Var}_{\mathbb P^{(t)}}(S_{\Lambda_n})$ is nonincreasing there; hence</p>
<div class="math-display">$$\frac{\beta C\operatorname{Var}_{\mathbb P^{+}}(S_{\Lambda_n})}{L^{2\theta_0n}}\ \leq\ M_n(\beta)\ \leq\ \frac{\beta C\operatorname{Var}_{\mathbb P^{\mathrm{free}}}(S_{\Lambda_n})}{L^{2\theta_0n}},$$</div>
<p>where $M_n(\beta)=\mathbb E_{\mathbb P_{\Lambda_n}^{+}}[\sigma_x]$ is the finite-size magnetisation and $2\theta_0=d+\alpha$.</p>
:::details Proof
<p>The two derivatives of the identity are $\frac{d}{dt}\mathbb E_{\mathbb P^{(t)}}[S_{\Lambda_n}]=\beta B_n\operatorname{Var}_{\mathbb P^{(t)}}(S_{\Lambda_n})$ and</p>
<div class="math-display">$$\frac{d^2}{dt^2}\mathbb E_{\mathbb P^{(t)}}[S_{\Lambda_n}]=(\beta B_n)^2\sum_{x,y,z\in\Lambda_n}\mathbb E_{\mathbb P^{(t)}}\bigl[\sigma_x;\sigma_y;\sigma_z\bigr],$$</div>
<p>the sum of third cumulants, which is nonpositive by the GHS inequality for ferromagnetic Ising spins in a nonnegative field [@ghs-1970]. So the mean is concave, its derivative is nonincreasing, and by the previous display so is the variance. The variance is even in $t$, because $\mathbb P^{(-t)}$ is the image of $\mathbb P^{(t)}$ under the global flip, so the integral of the variance over $[-1,1]$ lies between twice its value at $t=1$ and twice its value at $t=0$. Multiplying the identity $m^nM_n(\beta)=\tfrac12\beta B_n\int_{-1}^{1}\operatorname{Var}_{\mathbb P^{(t)}}(S_{\Lambda_n})\,dt$ by these bounds and using $B_n=CL^{-\alpha n}$ together with $L^{2\theta_0n}=m^nL^{\alpha n}$ gives the sandwich.</p>
:::
<p>Three consequences follow, and none of them needs the orbit to converge.</p>
<a id="tag-QCCM" data-assertion="theorem" data-title="The plus block spin is pinned at least at the mean-field rate, the free one fluctuates at least that much"></a>
<p>(i) The block average of the plus state concentrates: with $Y_n=S_{\Lambda_n}/m^n$,</p>
<div class="math-display">$$\operatorname{Var}_{\mathbb P^{+}}(Y_n)\leq\frac{L^{-(d-\alpha)n}}{\beta C},$$</div>
<p>so its fluctuations vanish at least like $L^{-(d-\alpha)n/2}$, and the plus block spin never grows faster than the mean-field rate, $2\theta_+\leq d+\alpha$.</p>
<p>(ii) The free block average does not concentrate faster than the mean-field rate: $\operatorname{Var}_{\mathbb P^{\mathrm{free}}}(Y_n)\geq M_n(\beta)L^{-(d-\alpha)n}/(\beta C)$.</p>
<p>(iii) Suppose that at the critical intensity the rescaled orbit converges with a second moment $v^*=\int s^2d\nu^*\in(0,\infty)$, as in <a href="/tag/A8VL/">the growth theorem</a>, and that the transition is continuous, so that $M_n(\beta_c)\to0$. Then the free variance is $L^{2\theta_0n}v^*(1+o(1))$ and the sandwich gives</p>
<div class="math-display">$$M_n\leq\beta Cv^*(1+o(1)),\qquad\frac{\operatorname{Var}_{\mathbb P^{+}}(Y_n)}{\operatorname{Var}_{\mathbb P^{\mathrm{free}}}(Y_n)}\leq\frac{M_n}{v^*}\longrightarrow0:$$</div>
<p>at criticality a boundary field of size $B_n\to0$ still pins the block spin, and the ratio of the two fluctuations measures the finite-size magnetisation.</p>
:::details Proof
<p>(i) Divide the lower half of the sandwich by $m^{2n}$ and use $M_n\leq1$, which holds because $\lvert\sigma_x\rvert\leq1$.</p>
<p>(ii) Divide the upper half by $m^{2n}$.</p>
<p>(iii) Under the hypothesis of the growth theorem the free variance is $L^{2\theta_0n}v^*(1+o(1))$, and the upper half of the sandwich is $M_n\leq\beta C\operatorname{Var}_{\mathbb P^{\mathrm{free}}}(S_{\Lambda_n})/L^{2\theta_0n}$. The ratio bound divides the two halves of the sandwich by each other, and $M_n\to0$ is the continuity hypothesis, which is where the vanishing of the ratio comes from.</p>
:::
<p>The third consequence is the one worth reading twice. The free block spin at criticality has a genuine scaling limit, so it fluctuates over a range of order $L^{\theta_0n}$; the plus block spin, whose boundary field is only $B_n=CL^{-\alpha n}$ — vanishing, and at a rate that makes the boundary energy of a block grow — fluctuates over a range that is a vanishing fraction of that. The mechanism is the one the identity in the previous article describes: the boundary injects magnetisation into the block, and the injected magnetisation is what the finite-size $M_n$ measures.</p>

<p>What this route does <em>not</em> give is the value of $\kappa$. The lower half of the sandwich bounds the free variance below, in terms of $M_n$, and $M_n\to0$ at criticality, so it cannot certify a growth of order $L^{2\theta_0n}$; the upper half bounds the plus variance, not the free one. That is not an accident of the estimates: the two variances differ by the factor between them, which is exactly what distinguishes a pinned block spin from a fluctuating one. Certifying $\kappa=\alpha$ therefore still needs either the convergence of the rescaled orbit, which is <a href="/tag/A8VL/">the growth theorem</a>, or an upper bound on the free block-spin variance which this argument does not supply.</p>

## The dictionary {#section-dictionary}

<a id="tag-G6YW" data-assertion="theorem" data-title="Exponents in terms of the two renormalisation-group numbers"></a>
<p>Suppose that $\chi_n(\beta_c)\asymp L^{\kappa n}$ and that, uniformly in $n$ and $\beta$,</p>
<div class="math-display">$$\chi_n(\beta)\asymp\min\bigl\{L^{\kappa n},\ \xi(\beta)^{\kappa}\bigr\},\qquad \xi(\beta)\asymp\lvert\beta_c-\beta\rvert^{-\nu}.$$</div>
<p>Then $\chi(\beta)\asymp\lvert\beta_c-\beta\rvert^{-\kappa\nu}$, that is $\gamma=\kappa\nu$. If in addition $F_{\mathrm{sing}}\asymp\xi^{-d}$ then $2-\alpha_{\mathrm{hy}}=d\nu$, and if in addition $M\asymp\xi^{-(d-\kappa)/2}$ then $\beta_{\mathrm{o}}=\tfrac{\nu}{2}(d-\kappa)$; under these two, together with the two relations just displayed,</p>
<div class="math-display">$$\delta=\frac{d+\kappa}{d-\kappa},\qquad \alpha_{\mathrm{hy}}=2-d\nu,\qquad \gamma=\nu(2-\eta),\qquad \gamma=\beta_{\mathrm{o}}(\delta-1).$$</div>
:::details Proof of the dictionary
<p>For $\gamma$: the supremum over $n$ of $\min\{L^{\kappa n},\xi^\kappa\}$ is $\xi^\kappa$ up to constants, and $\xi\asymp\lvert\beta_c-\beta\rvert^{-\nu}$ gives $\chi\asymp\lvert\beta_c-\beta\rvert^{-\kappa\nu}$.</p>
<p>For $\alpha_{\mathrm{hy}}$: $F_{\mathrm{sing}}\asymp\xi^{-d}\asymp\lvert\beta_c-\beta\rvert^{d\nu}$, and comparing with $F_{\mathrm{sing}}\asymp\lvert\beta_c-\beta\rvert^{2-\alpha_{\mathrm{hy}}}$ gives the identity.</p>
<p>For $\beta_{\mathrm{o}}$: $M\asymp\xi^{-(d-\kappa)/2}\asymp\lvert\beta_c-\beta\rvert^{\nu(d-\kappa)/2}$, and comparing with the definition gives $\beta_{\mathrm{o}}=\tfrac{\nu}{2}(d-\kappa)$, which is the same as $\beta_{\mathrm{o}}=\tfrac{\nu}{2}(d-2+\eta)$ because $\kappa=2-\eta$.</p>
<p>For $\delta$: Widom's relation $\gamma=\beta_{\mathrm{o}}(\delta-1)$ is the definition of $\delta$ once the other two exponents are known, and substituting $\gamma=\kappa\nu$ and $\beta_{\mathrm{o}}=\tfrac{\nu}{2}(d-\kappa)$ gives $\kappa\nu=\tfrac{\nu}{2}(d-\kappa)(\delta-1)$, hence $\delta-1=\frac{2\kappa}{d-\kappa}$ and $\delta=\frac{d+\kappa}{d-\kappa}$. The last two displays restate the first two relations with $\kappa=2-\eta$.</p>
:::
<p>Which of these is a theorem of the model and which is an extra hypothesis is the point of the small print. The first display of the dictionary is a theorem of percolation in the hierarchical model below the triangle threshold, where the block susceptibility is known to grow like $L^{\kappa n}$ and the truncated form is a consequence of the finite correlation length; hyperscaling, the identity $F_{\mathrm{sing}}\asymp\xi^{-d}$, is the hypothesis that fails in the classical regime. The relations $\gamma=\kappa\nu$ and the identification $\kappa=2-\eta$ are renormalisation-group statements and hold whenever the fixed point exists with a finite variance; $\delta=\frac{d+\kappa}{d-\kappa}$ follows only when hyperscaling does.</p>

## Examples and non-examples {#section-examples}

<p><em>The Gaussian fixed point.</em> With $\kappa=\alpha$ and $\nu=1/\alpha$ the dictionary gives $\gamma=1$, $\beta_{\mathrm{o}}=\frac{d-\alpha}{2\alpha}$, $\delta=\frac{d+\alpha}{d-\alpha}$ and $\alpha_{\mathrm{hy}}=2-d/\alpha$. These are the classical long-range values and they satisfy all three scaling relations identically; see <a href="/articles/gaussian-renormalisation-group/#section-exponents">the Gaussian article</a>, where they are computed from the recursion rather than from the dictionary.</p>

<p><em>Hierarchical percolation.</em> Here $\kappa=\alpha$ is a theorem for every $0&lt;\alpha&lt;d$ [@hutchcroft-hierarchical-2021], so $\eta=2-\alpha$ and $\gamma=\nu\alpha$. For $\alpha&lt;d/3$ the model is mean-field in the sense that the triangle condition holds and $\delta=2$, $\beta_{\mathrm{o}}=1$, while $\nu=1/\alpha$; hyperscaling fails there, and indeed $\frac{d+\alpha}{d-\alpha}&lt;2$ for $\alpha&lt;d/3$. For $\alpha&gt;d/3$ the volume exponent satisfies $\delta\geq\frac{d+\alpha}{d-\alpha}&gt;2$, with equality conjectured, and the value of $\nu$ is not known. Details are in <a href="/articles/hierarchical-percolation-rg/">the percolation article</a>.</p>

<p><em>The Ising model.</em> For $\alpha&lt;d/2$ the exponents are the classical ones, $\nu=1/\alpha$ and $\kappa=\alpha$, by Aizenman and Fernandez [@aizenman-fernandez-1988] and, in the Euclidean case, by the lace expansion [@heydenreich-hofstad-sakai-2008]. For $\alpha&gt;d/2$ the critical behaviour is governed by the <a href="/articles/bleher-sinai-fixed-point/">non-Gaussian fixed point</a>, $\nu$ differs from $1/\alpha$, and the growth exponent stays at $\kappa=\alpha$ by the theorem above. At $\alpha=d/2$ the classical values hold with logarithmic corrections.</p>

<p><em>Non-example: a model without a finite-variance fixed point.</em> If the rescaled orbit diverges, as it does for $\beta&gt;\beta_c$ in the Gaussian model, no exponent is defined at that intensity: the block spin per site tends to a nonzero limit and the susceptibility is infinite. The definitions above are statements about the critical orbit and its neighbourhood only.</p>

## Variants and generalisations {#section-variants}

<p><em>Finite-size scaling.</em> The block susceptibility at criticality is the finite-size susceptibility of the block, so $\chi_n(\beta_c)\asymp L^{\kappa n}$ is a finite-size scaling statement with $\kappa=\gamma/\nu$: the susceptibility of a block of side $L^n$ at criticality grows like its side to the power $\gamma/\nu$. This is the form in which the exponents are measured numerically, and it requires no infinite-volume limit.</p>

<p><em>Corrections to scaling.</em> The approach to a fixed point along an irrelevant direction with eigenvalue $\lambda_2$, $\lvert\lambda_2\rvert&lt;1$, modifies each power law by a factor $1+O(L^{-n(1-\log\lvert\lambda_2\rvert/\log L)})$. A complex pair of eigenvalues produces an oscillating factor, which is what distinguishes the hierarchical model's subleading behaviour from a pure power law and is analysed at <a href="/articles/bleher-sinai-fixed-point/#section-spectrum">the nontrivial fixed point</a>.</p>

<p><em>Two independent exponents.</em> The dictionary uses exactly two inputs, $\kappa$ and $\nu$; a model with a fixed point but no hyperscaling has two independent exponents and the other three relations fail, as in percolation for $\alpha&lt;d/3$. Five exponents cannot be independent in a model with a one-parameter family of fixed points, which is the content of the scaling hypothesis in its general form.</p>

## History and attribution {#section-history}

<p>The reading of the indices off the linearised renormalisation map is the content of Bleher and Sinai's second paper on the hierarchical model [@bleher-sinai-1975], where the indices are computed as functions of the spectrum at the fixed point. The classical long-range values are those of Fisher, Ma and Nickel [@fisher-ma-nickel-1972], and the rigorous mean-field region for long-range Ising models is due to Aizenman and Fernandez [@aizenman-fernandez-1988]. The two-point exponent for hierarchical percolation and the volume-exponent obstruction are Hutchcroft's [@hutchcroft-hierarchical-2021].</p>

## References {#section-references}

<ul>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>R. B. Griffiths, C. A. Hurst and S. Sherman, Concavity of magnetization of an Ising ferromagnet in a positive external field, <em>J. Math. Phys.</em> 11 (1970), 790&ndash;795.</li>
<li>M. Aizenman and R. Fernandez, Critical exponents for long-range interactions, <em>Lett. Math. Phys.</em> 16 (1988), 39&ndash;49.</li>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>M. E. Fisher, S.-k. Ma and B. G. Nickel, Critical exponents for long-range interactions, <em>Phys. Rev. Lett.</em> 29 (1972), 917&ndash;920.</li>
<li>M. Heydenreich, R. van der Hofstad and A. Sakai, Mean-field behavior for long- and finite range Ising model, percolation and self-avoiding walk, <em>J. Statist. Phys.</em> 132 (2008), 1001&ndash;1049.</li>
<li>T. Hutchcroft, The critical two-point function for long-range percolation on the hierarchical lattice, <em>Ann. Appl. Probab.</em> 34 (2024), 986&ndash;1002 (arXiv:2103.17013).</li>
</ul>
