---
{
  "id": "hierarchical-percolation-rg",
  "title": "Renormalisation for hierarchical percolation",
  "subtitle": "Cluster amplification is the relevant direction, and the triangle threshold is three alpha against d.",
  "kind": "theorem",
  "category": "Hierarchical models",
  "summary": "For long-range percolation on the hierarchical lattice the renormalisation group acts on clusters rather than on a one-variable law, and its relevant direction is the amplification of large clusters across a block. The critical two-point function decays like the distance to the power minus d minus alpha for every exponent in the long-range range, and the triangle diagram converges exactly when three alpha is below d, which is where the model stops being mean-field.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$; kernel exponent $0\\lt \\alpha\\lt d$; $J\\gt 0$; $J_k=JL^{-(d+\\alpha)k}$.",
    "Bonds are open independently with probability $1-e^{-\\beta J(x-y)}$ at intensity $\\beta\\geq0$; free boundary conditions on $\\Lambda_n$.",
    "$\\beta_c$ is the critical intensity, $K_x$ a cluster, $\\tau_\\beta(x,y)$ a connection probability."
  ],
  "related": [
    "hierarchical-gibbs-measure",
    "renormalisation-group-map",
    "critical-exponents-from-rg",
    "hierarchical-lattice"
  ],
  "sourceIds": [
    "koval-meester-trapman-2012",
    "hutchcroft-hierarchical-2021",
    "dyson-1969"
  ],
  "aliases": [
    "hierarchical percolation",
    "long-range percolation",
    "cluster amplification",
    "triangle condition",
    "critical two-point function"
  ]
}
---

<p>Long-range percolation on the hierarchical lattice has bond intensities $J\lVert x-y\rVert^{-d-\alpha}$, so the intensity of the edge between two vertices depends only on their level, and the model inherits the <a href="/articles/hierarchical-lattice/#section-children">child decomposition</a> of the lattice. Its renormalisation group does not act on the law of one number: the state of a block is the partition of its vertices into clusters, and the operation of decimation is the passage from the cluster partition of the children to that of the block. What survives from the spin case is the amplification: two large clusters in sibling blocks are joined with probability comparable to $\beta J_n$ times their product of sizes, so a block whose clusters are atypically large produces a parent whose clusters are larger still.</p>

<p>That mechanism gives the exact exponents. At criticality the expected size of the restricted cluster of the origin in $\Lambda_n$ grows like $L^{\alpha n}$ — the growth exponent $\kappa=\alpha$ of <a href="/articles/critical-exponents-from-rg/">the exponent dictionary</a> — and the critical connection probability between vertices at distance $L^n$ is of order $L^{-(d-\alpha)n}$, so $\eta=2-\alpha$ for every $0&lt;\alpha&lt;d$. This is unambiguous in the mean-field region, where the second moment of the cluster size diverges, and it holds beyond it as well; the theorem is Hutchcroft's, and it is the only case in which the two-point exponent is known across the whole long-range range [@hutchcroft-hierarchical-2021].</p>

<p>The phase transition itself is classical: $\beta_c$ is finite exactly when $\alpha&lt;d$, and there is no infinite cluster at $\beta_c$ [@koval-meester-trapman-2012]. The renormalisation group enters at the level of exponents, and the question it answers is why the model is mean-field below $\alpha=d/3$ and not above: the triangle diagram is a convergent sum below that value and a divergent one above it, and the diagram is computable here because the lattice is ultrametric.</p>

## Definitions and setting {#section-model}

<p>Let $0&lt;\alpha&lt;d$, $\beta\geq0$, and for distinct $x,y\in\mathbb H^d_L$ declare the pair an open edge independently with probability $p_\beta(x,y)=1-e^{-\beta J\lVert x-y\rVert^{-d-\alpha}}$. The cluster $K_x$ is the set of vertices joined to $x$ by open paths, $K^{\Lambda_n}_x$ is the same object computed with edges inside $\Lambda_n$, and</p>
<div class="math-display">$$\tau_\beta(x,y)=\mathbb P_\beta(x\leftrightarrow y),\qquad \tau^{\Lambda_n}_\beta(x,y)=\mathbb P_\beta\bigl(x\xleftrightarrow{\Lambda_n}y\bigr),\qquad \chi_n(\beta)=\mathbb E_\beta\lvert K^{\Lambda_n}_0\rvert .$$</div>
<p>The critical intensity is $\beta_c=\inf\{\beta:\mathbb P_\beta(\lvert K_0\rvert=\infty)&gt;0\}$, and $\chi_n$ is the block susceptibility of <a href="/articles/critical-exponents-from-rg/#section-exponents">the exponent article</a>. Two auxiliary quantities are used below: the level-$n$ quantile</p>
<div class="math-display">$$R_n(\beta)=\min\bigl\{r\geq1:\mathbb P_\beta\bigl(\max_{x\in\Lambda_n}\lvert K^{\Lambda_n}_x\rvert\geq r\bigr)\leq e^{-1}\bigr\},$$</div>
<p>the typical size of the largest cluster of a block, and the amplification factor $\beta J_n=\beta JL^{-(d+\alpha)n}$, which is the intensity of every edge joining two distinct children of $\Lambda_n$.</p>

## Two exact recursion inequalities {#section-recursion}

<p>The percolation analogue of the decimation identity is a pair of inequalities, both exact consequences of the child decomposition and the independence of the bonds between children.</p>
<a id="tag-P5CJ" data-assertion="proposition" data-title="One-edge joining of sibling clusters"></a>
<p>Let $n\geq0$, let $B,B'$ be distinct children of $\Lambda_{n+1}$, let $x\in B$ and $y\in B'$, and let $I=\lvert K^{B}_x\rvert$ and $I'=\lvert K^{B'}_y\rvert$ computed with the bonds inside $B$ and $B'$ respectively. Then the pair $(I,I')$ is independent and</p>
<div class="math-display">$$\tau^{\Lambda_{n+1}}_\beta(x,y)\ \geq\ \mathbb E_\beta\bigl[1-e^{-\beta J_{n+1}II'}\bigr].$$</div>
:::details Proof of the one-edge bound
<p>Children are disjoint and every edge joining them is at level $n+1$, so the bonds of $B$ and of $B'$ are disjoint sets and $(I,I')$ is a pair of independent random variables, each with the law of the restricted cluster size in the model on $\Lambda_n$ with free boundary. Given $I=i$ and $I'=i'$, the $ii'$ pairs $\{u,v\}$ with $u$ in the cluster of $x$ and $v$ in the cluster of $y$ are distinct and their edges are independent of the internal bonds, each open with probability $1-e^{-\beta J_{n+1}}$. Any one open edge among them joins $x$ to $y$, so the conditional probability of connection is $1-(e^{-\beta J_{n+1}})^{ii'}=1-e^{-\beta J_{n+1}ii'}$. Averaging gives the inequality, which is an inequality rather than an identity because a connection may also use a chain of children.</p>
:::
<p>The inequality is the mechanism of amplification in one line: the probability of joining two clusters grows like $\beta J_{n+1}II'$ when the product is small, so an intensity decaying at rate $L^{-(d+\alpha)}$ is compensated by clusters growing at rate $L^{\alpha n}$, and a cluster size growing faster than $L^{\alpha n}$ produces parents that grow faster still. Used at the level of expectations with a truncation of the product, it gives the iteration</p>
<div class="math-display">$$\chi_{n+1}\ \geq\ c\,L^{-(d+\alpha)(n+1)}\chi_n^2,\qquad \chi_n\leq L^{dn},$$</div>
<p>with $c$ depending on $\beta$ and on the truncation, as long as the cluster sizes are bounded by a constant multiple of $L^{(d+\alpha)(n+1)/2}$ with high probability. The iteration has the fixed point $\chi_n\asymp L^{\alpha n}$: a growth exponent below $\alpha$ is pushed up, and a growth exponent above $\alpha$ is incompatible with the quantile bound, which is why the critical orbit sits at $\alpha$.</p>

## The critical two-point function {#section-two-point}

<a id="tag-W4HK" data-assertion="theorem" data-title="Critical two-point function on the hierarchical lattice"></a>
<p>Let $0&lt;\alpha&lt;d$, let $J$ be symmetric, and suppose that there are $c,C&gt;0$ with $c\lVert x\rVert^{-d-\alpha}\leq J(x)\leq C\lVert x\rVert^{-d-\alpha}$ for $x\neq0$. Then $\beta_c\in(0,\infty)$, and there are $a,A&gt;0$, depending only on $d,L,\alpha,c,C$, such that for every $n\geq1$,</p>
<div class="math-display">$$a\,L^{-(d-\alpha)n}\ \leq\ \frac{1}{L^{dn}}\sum_{x\in\Lambda_n\setminus\Lambda_{n-1}}\tau^{\Lambda_n}_{\beta_c}(0,x)\ \leq\ \frac{1}{L^{dn}}\sum_{x\in\Lambda_n}\tau_{\beta_c}(0,x)\ \leq\ A\,L^{-(d-\alpha)n}.$$</div>
<p>If in addition $J$ is radial, then for every $x,y\in\mathbb H^d_L$,</p>
<div class="math-display">$$a\,\langle x-y\rangle^{-(d-\alpha)}\ \leq\ \tau^{\Lambda(x,y)}_{\beta_c}(x,y)\ \leq\ \tau_{\beta_c}(x,y)\ \leq\ A\,\langle x-y\rangle^{-(d-\alpha)},$$</div>
<p>where $\Lambda(x,y)$ is the smallest block containing both. Both constants are those of the averaged statement; the passage from averages to points uses the level isometries of the lattice.</p>
<p>The averaged statement is Theorem 1.1 and the pointwise one Corollary 1.2 of Hutchcroft [@hutchcroft-hierarchical-2021], where the lower bound is proved for connections inside the smallest common block and the upper bound for unrestricted connections. The proof runs through <a href="/articles/hierarchical-lattice/#section-children">block quantiles</a>: the amplification of the previous section shows that $R_n(\beta)^2$ is at most a constant times $L^{(d+\alpha)n}$ at $\beta_c$, sharpness supplies a lower bound on the flux of intensity leaving a block, and the two together pin $\chi_n$ between constants times $L^{\alpha n}$; the conversion to connection probabilities is a BK decomposition according to the smallest block containing the path.</p>

## The triangle threshold {#section-triangle}

<p>The triangle diagram is the sum $\sum_{x,y}\tau(0,x)\tau(x,y)\tau(y,0)$, and on an ultrametric space it can be computed scale by scale.</p>
<a id="tag-T6NB" data-assertion="theorem" data-title="The triangle diagram converges exactly when three alpha is below d"></a>
<p>Let $0&lt;\alpha&lt;d$, let $\tau(0)=1$ and $\tau(z)=L^{-(d-\alpha)\operatorname{lev}(z)}$ for $z\neq0$, and put</p>
<div class="math-display">$$T_N=\sum_{x,y\in\Lambda_N}\tau(0,x)\,\tau(x-y)\,\tau(y).$$</div>
<p>Then $T_N\asymp\sum_{n=0}^{N}L^{(3\alpha-d)n}$. In particular the infinite sum converges if $3\alpha&lt;d$, diverges like $N$ if $3\alpha=d$, and grows like $L^{(3\alpha-d)N}$ if $3\alpha&gt;d$. Consequently, under the two-point bounds of the previous section, the triangle diagram at $\beta_c$ is finite exactly when $3\alpha&lt;d$.</p>
:::details Proof of the triangle threshold
<p>Write $a=\operatorname{lev}(x)$, $b=\operatorname{lev}(x-y)$ and $c=\operatorname{lev}(y)$. The ultrametric inequality gives $\operatorname{lev}(x)=\operatorname{lev}((x-y)+y)\leq\max\{b,c\}$ and its two analogues, so the largest two of $a,b,c$ are equal. Group the pairs by the common value $m$ of the two largest and by which of the three is the smallest.</p>
<p><em>Case $a=c=m$, $b=j\leq m$.</em> Both $x$ and $y$ have level $m$ and their difference has level $j$. The number of such pairs is at most the product of the shell sizes at levels $m$ and $j$, and at least a constant times it: the map $(x,z)\mapsto(x,x+z)$ is injective, $x$ ranges over a shell of size $(1-L^{-d})L^{dm}$, $z$ over a shell of size $(1-L^{-d})L^{dj}$, and $x+z$ has level $m$ whenever $j&lt;m$. Each term is $L^{-(d-\alpha)(2m+j)}$, so the contribution of the level $m$ is $L^{dm+dj-(d-\alpha)(2m+j)}=L^{m(2\alpha-d)+\alpha j}$; summing over $j\leq m$ gives a constant times $L^{m(3\alpha-d)}$, because the geometric sum is dominated by its last term as $\alpha&gt;0$.</p>
<p><em>Case $a=b=m&gt;c$, and its mirror image.</em> Here $x$ has level $m$, $y$ has level $c$, and the difference has level $m$. For each $y$ of level $c$ there are at most $(1-L^{-d})L^{dm}$ choices of $x$ of level $m$, and all of them give difference of level $m$ because $y$ vanishes above coordinate $c&lt;m$. The contribution is $L^{dm+dc-(d-\alpha)(2m+c)}=L^{m(2\alpha-d)}L^{\alpha c}$, and summing over $c&lt;m$ gives a constant times $L^{m(2\alpha-d)+\alpha m}=L^{m(3\alpha-d)}$. The mirror case $b=c=m&gt;a$ is the same with the roles of $x$ and $y$ exchanged.</p>
<p>All three cases contribute the same order at scale $m$, so $T_N\asymp\sum_{m\leq N}L^{(3\alpha-d)m}$, which is bounded, linear, or geometric according to the sign of $3\alpha-d$. The last claim is the comparison of $\tau_{\beta_c}$ with $\tau$ in the two-sided form of the previous section.</p>
:::
<p>The exponent in the display is the one that decides mean-field behaviour: $3\alpha-d&gt;0$ is exactly the regime in which the triangle diagram diverges and the volume exponent, if it exists, exceeds its mean-field value. For $3\alpha&lt;d$ the diagram is finite, the triangle condition holds and the exponents of <a href="/articles/critical-exponents-from-rg/">the dictionary</a> take their mean-field values, $\delta=2$ and $\beta_{\mathrm{o}}=1$; at $3\alpha=d$ the divergence is logarithmic.</p>

## Consequences and applications {#section-consequences}

<p><em>The growth exponent.</em> The theorem gives $\chi_n(\beta_c)\asymp L^{\alpha n}$ directly, which is $\kappa=\alpha$ and $\eta=2-\alpha$ in the notation of <a href="/articles/critical-exponents-from-rg/#section-exponents">the exponent article</a>. This agrees with the general statement that the growth exponent is fixed by the autonomy of the recursion at $\theta_0=\tfrac12(d+\alpha)$: the quantile bound $R_n(\beta_c)^2\lesssim L^{(d+\alpha)n}$ is the upper half of the variance growth, and the boundary flux supplies the lower half.</p>

<p><em>The volume exponent.</em> For $3\alpha&gt;d$ the model is not mean-field, and the cluster-volume tail is constrained. If $\mathbb P_{\beta_c}(\lvert K_0\rvert\geq n)=n^{-1/\delta+o(1)}$, then $\delta\geq\frac{d+\alpha}{d-\alpha}$, which is strictly greater than $2$; the value $\delta=\frac{d+\alpha}{d-\alpha}$ is conjectured, and it is the value that the scaling relations give when the two-point exponent is $2-\alpha$. This is Corollary 1.5 of Hutchcroft [@hutchcroft-hierarchical-2021].</p>

<p><em>The exponent $\nu$.</em> Nothing in the two-point theorem identifies the correlation-length exponent, and it is the one quantity the percolation analysis does not determine in the non-mean-field regime. In the mean-field regime $\nu=1/\alpha$ follows from the classical values and $\gamma=1$; for $\alpha&gt;d/3$ the value of $\nu$ is not known, and it is where the comparison with the spin model's nontrivial fixed point would enter.</p>

## Examples and non-examples {#section-examples}

<p><em>The power kernel with $\alpha\downarrow0$.</em> Then $d-\alpha\uparrow d$ and the critical two-point exponent tends to $d$: the connection probability decays like the inverse volume of the ball, the marginal case in which the susceptibility diverges logarithmically. At $\alpha=0$ the intensity is not summable, $\beta_c=0$, and the exponent statements above have no content.</p>

<p><em>A kernel vanishing on a level.</em> The two-point theorem needs a two-sided comparison with the power kernel on every level. If $J$ vanishes, or is much smaller, on a sparse set of levels, the amplification fails at those scales and the critical behaviour changes: the model behaves as though the exponent were larger on those levels, and the block-quantile argument gives bounds at the worst scale rather than at each scale.</p>

<p><em>Non-example: the nearest-neighbour lattice.</em> On $\mathbb Z^d$ the block geometry is not ultrametric, the triangle diagram is not a geometric sum in the scale, and the mean-field threshold is a dimension rather than a relation between $\alpha$ and $d$. The transfer of the computation to that setting is the subject of <a href="/articles/hierarchical-and-euclidean-rg/">the comparison article</a>.</p>

<p><em>Non-example: percolation with $q$ states.</em> The Fortuin-Kasteleyn random-cluster model on the hierarchical lattice has the same block decomposition but a cluster weight $q^{\#\text{clusters}}$ that is not a product over children, so the decimation state is a partition function with boundary conditions and not a one-variable law. The amplification inequalities survive; the exact two-point exponent is not available by this route.</p>

## Variants and generalisations {#section-variants}

<p><em>Inhomogeneous intensities.</em> Replacing $J_k$ by a level-dependent sequence $J_k$ with $J_k\asymp L^{-(d+\alpha)k}$ changes no bound in the argument, and the exponents are unchanged; this is the form in which the model appears in comparisons with Euclidean percolation, where the hierarchical kernel is a comparison object rather than a model of interest.</p>

<p><em>Full connectivity.</em> The event that a block is fully connected, with no isolated bond structure, has its own recursion and is the percolation analogue of a one-variable law: the probability that $\Lambda_n$ is connected satisfies a recursion driven by the probability that the children and the cross edges form a connected structure. For large $m$ this is a mean-field-looking recursion, and it is not the recursion that governs $\tau_{\beta_c}$.</p>

<p><em>Other lattices.</em> The child decomposition is available on any ultrametric group, including the $p$-adic integers and the solenoids; the counting arguments use only that a ball of radius $L^n$ has $L^{dn}$ points and $m$ children, so they apply verbatim wherever that holds.</p>

## History and attribution {#section-history}

<p>Long-range percolation on the hierarchical lattice was studied by Koval, Meester and Trapman, who proved that $\beta_c&lt;\infty$ exactly when $\alpha&lt;d$ and that there is no infinite cluster at criticality [@koval-meester-trapman-2012]. The two-point theorem, the pointwise form for radial kernels, the triangle threshold and the volume-exponent bound are Hutchcroft's [@hutchcroft-hierarchical-2021]. The block-quantile amplification that drives the argument is the percolation form of the amplification in <a href="/articles/hierarchical-gibbs-measure/">decimation</a>, and the hierarchical lattice itself goes back to Dyson's approximation [@dyson-1969].</p>

## References {#section-references}

<ul>
<li>F. J. Dyson, Existence of a phase-transition in a one-dimensional Ising ferromagnet, <em>Comm. Math. Phys.</em> 12 (1969), 91&ndash;107.</li>
<li>T. Hutchcroft, The critical two-point function for long-range percolation on the hierarchical lattice, <a href="https://arxiv.org/abs/2103.17013">arXiv:2103.17013</a> (2021).</li>
<li>V. Koval, R. Meester and P. Trapman, Long-range percolation on the hierarchical lattice, <em>Electron. J. Probab.</em> 17 (2012), no. 57.</li>
</ul>
