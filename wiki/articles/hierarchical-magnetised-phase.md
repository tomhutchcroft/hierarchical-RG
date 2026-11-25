---
{
  "id": "hierarchical-magnetised-phase",
  "title": "The magnetised phase, and what monotonicity gives",
  "subtitle": "Two extremal states, the order parameter, and why the FKG inequality cannot locate the threshold.",
  "kind": "theorem",
  "category": "Hierarchical models",
  "summary": "For ferromagnetic couplings the FKG inequality makes the Gibbs measures of the hierarchical Ising model a stochastically ordered family with a largest and a smallest element: the monotone limits of the plus and minus boundary conditions. The order parameter M of the plus state is positive exactly when the Gibbs measure is not unique, and is the block average of that state. Correlations under the plus state dominate M squared, so a magnetised phase has infinite susceptibility, and M is at most tanh of beta over the Gaussian critical intensity, which is the only bound on its size that monotonicity gives. The arguments are insensitive to the intensity, so the location of the threshold is not a monotonicity statement: it is the branch of the recursion's trichotomy, which is where Bleher and Sinai's analysis enters.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$, kernel exponent $\\alpha>0$; couplings $J_k=JL^{-(d+\\alpha)k}$ with $J>0$, so the model is ferromagnetic.",
    "The prior is the Ising one, $\\varrho=\\tfrac12(\\delta_{-1}+\\delta_{+1})$, so spins take the values $\\pm1$ and $+\\geq-$. The plus boundary condition is the configuration that is $+1$ everywhere outside the block, and minus is its negation.",
    "Finite-volume measures, the specification and the Gibbs property are those of the article on the infinite-volume limit; $M(\\beta)=\\mathbb E_{\\mu_+}[\\sigma_0]$ and $C=\\sum_{x\\neq0}J(\\lVert x\\rVert)$."
  ],
  "related": [
    "hierarchical-infinite-volume-limit",
    "hierarchical-gibbs-measure",
    "bleher-sinai-fixed-point",
    "hierarchical-percolation-rg",
    "hierarchical-symmetries"
  ],
  "sourceIds": [
    "fkg-1971",
    "griffiths-1967",
    "bleher-sinai-1973",
    "bleher-sinai-1975",
    "georgii-2011"
  ],
  "aliases": [
    "magnetised phase",
    "spontaneous magnetisation",
    "FKG inequality",
    "stochastic domination",
    "order parameter",
    "phase transition"
  ]
}
---

<p><a href="/articles/hierarchical-infinite-volume-limit/">The previous article</a> showed that the free-boundary measures have limit points and that these are Gibbs measures, but it said nothing about how many Gibbs measures there are. For a ferromagnetic model the answer has a shape, and the shape costs nothing: the Gibbs measures are stochastically ordered, there is a smallest and a largest, and the model is in one phase exactly when the two coincide. All of that follows from the FKG inequality, which for Ising spins says that increasing functions of the configuration are positively correlated [@fkg-1971], and from the monotone coupling that it implies.</p>

<p>What it does not follow from is where the transition is. Every inequality below is preserved if the couplings are replaced by any other ferromagnetic system with the same total mass, so no argument of this kind can distinguish the intensities at which the model is ordered — and this is not a gap in the exposition but a feature of monotonicity, which is why the wiki records the split. The threshold is located by the recursion, and the statement that above it the model is magnetised is that of Bleher and Sinai [@bleher-sinai-1973] [@bleher-sinai-1975], recorded here as the one external theorem the section on the threshold relies on.</p>

<p>The order parameter is the number this article is about. It is defined from the plus state, it is positive exactly when there are two phases, it bounds the correlation from below, and monotonicity gives one weak upper bound on it and no lower one.</p>

## Setting {#section-setting}

<p>Let $J>0$, so that $J_k>0$ for every $k$, and let the prior be the Ising one, so that $\sigma_x\in\{\pm1\}$ and the pointwise order of configurations is the order of the spins. For a finite $\Lambda$ and a configuration $\omega$ let $\mathbb P_\Lambda^{\omega}$ be the finite-volume Gibbs measure with boundary condition $\omega$, as in <a href="/articles/hierarchical-infinite-volume-limit/#section-specification">the specification of the previous article</a>; write $\mathbb P_\Lambda^{+}$ and $\mathbb P_\Lambda^{-}$ for the constant boundary conditions $\omega\equiv+1$ and $\omega\equiv-1$, and $\mu_+,\mu_-$ for the limits of $\mathbb P_{\Lambda_n}^{+}$ and $\mathbb P_{\Lambda_n}^{-}$ along the exhausting sequence of blocks, whose existence is proved below.</p>
<a id="tag-144T" data-assertion="definition" data-title="Ferromagnetic measure, the two extremal boundary conditions, and the order parameter"></a>
<p>A configuration $\omega'$ <em>dominates</em> $\omega$ if $\omega'_x\geq\omega_x$ for every $x$, and a function $f$ is <em>increasing</em> if it is increasing in each spin. For probability measures on $\Omega$, $\nu\preceq\nu'$ means $\int f\,d\nu\leq\int f\,d\nu'$ for every bounded continuous increasing $f$: <em>stochastic domination</em>. Define</p>
<div class="math-display">$$M(\beta)=\mathbb E_{\mu_+}[\sigma_0],\qquad C=\sum_{x\neq0}J(\lVert x\rVert)=\frac{J(1-L^{-d})}{L^{\alpha}-1},$$</div>
<p>so that $C$ is the total coupling mass at a vertex, finite for every $\alpha>0$, and the <em>order parameter</em> is $M(\beta)$, the magnetisation of the plus state at the origin.</p>
<p>The two facts used throughout are the FKG inequality for the ferromagnetic Ising measures, $\mathbb E[fg]\geq\mathbb E[f]\mathbb E[g]$ for bounded increasing $f$ and $g$ [@fkg-1971] [@griffiths-1967], and its consequence that the measures are monotone in their boundary condition. The second is proved here, because the proof is a coupling and the coupling is what the later arguments run on.</p>

## Monotonicity in the boundary condition {#section-coupling}

<a id="tag-96HI" data-assertion="proposition" data-title="Domination in the boundary condition and in the field"></a>
<p>Let $\Lambda$ be finite and let $\omega\preceq\omega'$. Then $\mathbb P_\Lambda^{\omega}\preceq\mathbb P_\Lambda^{\omega'}$. The same holds with an external field: if $h\leq h'$ then the measure with field $h$ is dominated by the measure with field $h'$.</p>
:::details Proof by coupling the heat baths
<p>The heat-bath chain on $\Lambda$ updates one site at a time. Given the configuration $\sigma$ and a uniform $U$, it sets $\sigma_x=+1$ if $U\leq p_x(\sigma)$ and $-1$ otherwise, where</p>
<div class="math-display">$$p_x(\sigma)=\frac{1+\tanh\Bigl(\beta\sum_{y\in\Lambda\setminus x}J(x-y)\sigma_y+\beta\sum_{y\notin\Lambda}J(x-y)\omega_y+\beta h_x\Bigr)}{2}$$</div>
<p>is the conditional probability that $\sigma_x=+1$ given the other spins. Each $p_x$ is increasing in $\sigma$ and in $\omega$ and in $h$, because $J>0$ and $\tanh$ is increasing. The chain is irreducible and aperiodic on the finite state space, so it has a unique invariant law, which is the Gibbs measure $\mathbb P_\Lambda^{\omega}$, and it converges to that law from every starting point.</p>
<p>Run two chains with the same uniform variables and the same choice of updated site, one for $\omega$ and one for $\omega'$, from starting configurations $\sigma\preceq\sigma'$. The domination is preserved at every update, by the monotonicity of $p_x$: if the two configurations agree at the updated site then so do the new values, and otherwise the one with the larger background has a larger flip probability, so a uniform that flips the lower chain also flips the higher one. Hence the entire path satisfies $\sigma(t)\preceq\sigma'(t)$ for all $t$. Passing to the limit in $t$ gives a coupling of the two invariant laws supported on $\{\sigma\preceq\sigma'\}$, which is domination: for increasing $f$, $\int f\,d\mathbb P_\Lambda^{\omega}=\mathbb E[f(\sigma)]\leq\mathbb E[f(\sigma')]=\int f\,d\mathbb P_\Lambda^{\omega'}$.</p>
<p>The field case is identical, the field entering $p_x$ the same way as the boundary spin.</p>
:::
<p>Two consequences are used below. Taking $\omega\preceq\omega'$ to be the extreme configurations gives $\mathbb P_\Lambda^{-}\preceq\mathbb P_\Lambda^{+}$: the plus and minus boundary conditions are the largest and smallest available. Taking instead the boundary conditions produced by the spins outside a smaller block gives the monotonicity in the volume, which is where the limits come from.</p>

## The two extremal states {#section-extremal}

<a id="tag-N9S3" data-assertion="proposition" data-title="The plus and minus limits exist and sandwich every Gibbs measure"></a>
<p>The sequence $\mathbb P_{\Lambda_n}^{+}$ is decreasing in $n$ in the stochastic order and $\mathbb P_{\Lambda_n}^{-}$ is increasing, so both converge weakly; write $\mu_+$ and $\mu_-$ for the limits. They satisfy $\mu_-\preceq\mu_+$, and every Gibbs measure $\nu$ satisfies $\mu_-\preceq\nu\preceq\mu_+$. Consequently $\mu_+=\mu_-$ if and only if the model has exactly one Gibbs measure, and then it is that measure.</p>
:::details Proof
<p><em>The sequences are monotone.</em> Let $f$ be bounded, continuous and increasing, and local on $\Lambda_n$. Under $\mathbb P_{\Lambda_{n+1}}^{+}$, the conditional law of the spins in $\Lambda_n$ given the rest is $\mathbb P_{\Lambda_n}^{\omega}$, where $\omega$ is the configuration $\sigma$ itself, which is $+1$ outside $\Lambda_{n+1}$ and takes the values $\pm1$ in $\Lambda_{n+1}\setminus\Lambda_n$. Every configuration satisfies $\omega\preceq+$, so by <a href="/tag/96HI/">the domination proposition</a> $\mathbb E_{\mathbb P_{\Lambda_n}^{\omega}}[f]\leq\mathbb E_{\mathbb P_{\Lambda_n}^{+}}[f]$, and the tower property gives</p>
<div class="math-display">$$\mathbb E_{\mathbb P_{\Lambda_{n+1}}^{+}}[f]=\mathbb E\Bigl[\mathbb E_{\mathbb P_{\Lambda_n}^{\omega}}[f]\Bigr]\leq\mathbb E_{\mathbb P_{\Lambda_n}^{+}}[f].$$</div>
<p>So $\mathbb P_{\Lambda_{n+1}}^{+}\preceq\mathbb P_{\Lambda_n}^{+}$: the plus measure decreases as the block grows, which is what one expects, since a smaller block has the positive boundary closer. The same computation with $\omega\succeq-$ gives that $\mathbb P_{\Lambda_n}^{-}$ increases. A monotone sequence of probability measures on a compact space converges, so both limits exist. Since $\mathbb P_{\Lambda_n}^{-}\preceq\mathbb P_{\Lambda_n}^{+}$ for every $n$, the limits satisfy $\mu_-\preceq\mu_+$.</p>
<p><em>The sandwich.</em> Let $\nu$ be a Gibbs measure, let $f$ be bounded, continuous and increasing on $\Lambda_n$, and let $\Lambda_m\supset\Lambda_n$. By the Gibbs property, $\nu$ is the average of the conditional laws $\mathbb P_{\Lambda_m}^{\omega}$ against the law of $\omega$ under $\nu$; every $\omega$ satisfies $\omega\preceq+$, so $\mathbb E_\nu[f]\leq\mathbb E_{\mathbb P_{\Lambda_m}^{+}}[f]$, and letting $m\to\infty$ gives $\mathbb E_\nu[f]\leq\mathbb E_{\mu_+}[f]$. The other side is the same with $-$.</p>
<p><em>Consequences.</em> If $\mu_+=\mu_-$ then every Gibbs measure equals the common value, so it is unique. If the Gibbs measure is unique then $\mu_+$ and $\mu_-$ are both Gibbs measures and hence equal. Both states are Gibbs measures by <a href="/articles/hierarchical-infinite-volume-limit/#section-existence">the existence theorem</a>, applied to the fixed boundary conditions.</p>
:::
<p>The proposition also settles the question left open by the previous article, in the ferromagnetic case: the set of Gibbs measures is nonempty, and it is an interval in the stochastic order with endpoints that are explicit. That is the whole architecture of the phase diagram, and it was obtained without computing anything.</p>

## The order parameter {#section-order-parameter}

<a id="tag-7AD0" data-assertion="theorem" data-title="The order parameter is positive exactly when the Gibbs measure is not unique"></a>
<p>For every $\beta\geq0$, $M(\beta)\geq0$, and $M(\beta)>0$ if and only if $\mu_+\neq\mu_-$, that is, if and only if the hierarchical Ising model has more than one Gibbs measure.</p>
:::details Proof
<p>The global flip $\sigma\mapsto-\sigma$ maps $\mathbb P_\Lambda^{+}$ to $\mathbb P_\Lambda^{-}$ and preserves the Hamiltonian, so it maps $\mu_+$ to $\mu_-$. Hence $\mathbb E_{\mu_-}[\sigma_0]=-M(\beta)$; since $\mu_-\preceq\mu_+$ this gives $M\geq-M$, that is $M\geq0$, and $M>0$ gives $\mu_-\neq\mu_+$ at once.</p>
<p>For the converse, suppose $M=0$. Both $\mu_+$ and $\mu_-$ are translation invariant: $\mathbb P_{\Lambda_n}^{+}$ is invariant under translation by any $v\in\Lambda_n$, because the Hamiltonian, the prior and the constant boundary condition all are, and a limit of invariant measures is invariant. So $\mathbb E_{\mu_+}[\sigma_x]=M=0$ for every $x$, and the same on the minus side.</p>
<p>Couple the two states monotonically. For each $n$, the proof of <a href="/tag/96HI/">the domination proposition</a> gives a coupling of $\mathbb P_{\Lambda_n}^{-}$ and $\mathbb P_{\Lambda_n}^{+}$ supported on $\{\sigma\preceq\sigma'\}$. The set of probability measures on the compact space $\Omega\times\Omega$ is compact, so a subsequence of these couplings converges to a coupling $m$ of $\mu_-$ and $\mu_+$ supported on $\{\sigma\preceq\sigma'\}$. Under $m$, the differences $\sigma'_x-\sigma_x$ are nonnegative with $\mathbb E_m[\sigma'_x-\sigma_x]=0-0=0$, so $\sigma'_x=\sigma_x$ $m$-a.s.; intersecting over the countably many vertices gives $\sigma=\sigma'$ $m$-a.s., and therefore $\mu_-=\mu_+$.</p>
:::
<p>The theorem is the reason the order parameter deserves the name: non-uniqueness, which is a statement about a set of measures, is detected by one number. It says nothing yet about whether that number is positive, and the next two results are everything monotonicity has to say on that question.</p>
<a id="tag-GHFF" data-assertion="proposition" data-title="Positive correlations and the bound on the order parameter"></a>
<p>Assume $M(\beta)>0$. Then the correlations of the plus state dominate $M^2$: $\mathbb E_{\mu_+}[\sigma_x\sigma_y]\geq M^2$ for all $x,y$, so the susceptibility $\chi_+(\beta)=\sum_{y}\mathbb E_{\mu_+}[\sigma_0\sigma_y]$ is infinite. For every $\beta<\infty$,</p>
<div class="math-display">$$M(\beta)\leq\tanh\Bigl(\beta C\Bigr)=\tanh\bigl(\beta/\beta_c^{\mathrm{G}}\bigr),$$</div>
<p>where $\beta_c^{\mathrm G}=1/C$ is the critical intensity of the <a href="/articles/gaussian-renormalisation-group/#section-critical">Gaussian model</a>.</p>
:::details Proof
<p><em>Correlations.</em> By <a href="/articles/hierarchical-symmetries/">the symmetry article</a> the plus state is invariant under translations and the two-point function is radial, and by the Griffiths inequality, the second of the pair in [@griffiths-1967], $\mathbb E_{\mu_+}[\sigma_x\sigma_y]\geq\mathbb E_{\mu_+}[\sigma_x]\,\mathbb E_{\mu_+}[\sigma_y]=M^2$ for every pair. Summing over the shell at level $k$, which has $(1-L^{-d})L^{dk}$ vertices, gives a contribution at least $M^2(1-L^{-d})L^{dk}$, and the sum over $k$ diverges.</p>
<p><em>The bound.</em> By the Gibbs property at the single site $0$, $\sigma_0$ is a function of the other spins whose conditional expectation is $\tanh\bigl(\beta H\bigr)$ with $H=\sum_{y\neq0}J(\lVert y\rVert)\sigma_y$, so $M=\mathbb E_{\mu_+}[\tanh(\beta H)]$. Since $\tanh$ is odd and increasing, $\tanh(\beta H)\leq\tanh(\beta\lvert H\rvert)$; since $\lvert H\rvert\leq C$ and $\tanh$ is concave on $[0,\infty)$ with $\tanh0=0$, Jensen's inequality gives $\mathbb E[\tanh(\beta\lvert H\rvert)]\leq\tanh\bigl(\beta\mathbb E\lvert H\rvert\bigr)\leq\tanh(\beta C)$. The last value is $\tanh(\beta/\beta_c^{\mathrm G})$ because $C$ is the reciprocal of the Gaussian critical intensity.</p>
:::
<p>The same computation at finite volume with the plus boundary condition gives $\mathbb E_{\mathbb P_\Lambda^{+}}[\sigma_x]\leq\tanh\bigl(\beta(C_\Lambda+b_x)\bigr)$, where $C_\Lambda=\sum_{y\in\Lambda\setminus x}J(x-y)$ is the mass inside the block and $b_x=\sum_{y\notin\Lambda}J(x-y)$ the mass at the boundary; both forms follow from $\lvert H\rvert\leq$ the total mass seen by $x$.</p>

<p>The two statements are of very different strength, and the difference is the point of the article. The first is a genuine consequence: a magnetised phase has infinite susceptibility, so the divergence of $\chi$ is not an extra assumption but a corollary of order, and this is the inequality behind the exponent relation $\gamma\geq0$ in <a href="/articles/critical-exponents-from-rg/">the dictionary</a>. The second is nearly empty: it says that $M$ is below one at every finite intensity, which was clear from $\lvert\sigma_0\rvert=1$, and that it tends to one as $\beta\to\infty$. It does not say that $M$ is zero anywhere, and no argument of this kind will.</p>

## Where the threshold comes from {#section-threshold}

<p>It is worth being explicit about why monotonicity cannot locate the transition, because the reason is structural rather than technical. Every assertion in the previous sections is preserved under replacing the kernel by another ferromagnetic one with the same total mass $C$: the domination, the sandwich, the equivalence of the theorem, and both bounds depend on the couplings only through their signs and their sum. In particular the one inequality that mentions the intensity, $M\leq\tanh(\beta C)$, holds at every $\beta$ and is therefore compatible both with $M>0$ at every intensity and with $M=0$ at every intensity. An argument whose conclusions are invariant under a change of kernel that preserves $C$ cannot produce a threshold, and the invariance here is exact, not a matter of the estimates being crude: no sharper use of the same inequalities will do better.</p>

<p>The threshold is located by the recursion. In the language of <a href="/articles/bleher-sinai-fixed-point/#section-statement">the fixed-point article</a>, the orbit of the Ising initial law under the rescaled decimation map converges to the point mass at $0$ below a critical coupling, to a nontrivial fixed point at it, and to a law of unbounded variance above it; that trichotomy is the theorem of Bleher and Sinai [@bleher-sinai-1973] [@bleher-sinai-1975]. The third branch is the magnetised phase: above the critical coupling the block spin per site has a nonzero limit $\pm M$, the two signs being the two states of this article. The identification with the order parameter defined here is through the block averages of the boundary-conditioned measures, which decrease to $M(\beta)$ by the proof of <a href="/tag/N9S3/">the extremal-state proposition</a>, so a nonzero limit of the block spin is exactly a nonzero order parameter.</p>

<p>So the division of labour is this. Monotonicity gives the shape of the phase diagram — two extremal states, an order parameter, uniqueness exactly when the order parameter vanishes — and answers the previous article's open question about how many Gibbs measures there are, in the sense that it reduces the question to the sign of one number. The recursion decides the sign. That the sign requires the recursion, and is not available from the inequalities of this article, is what the paragraph above argues, and it is the reason the wiki treats the two arguments as separate.</p>

## Examples and non-examples {#section-examples}

<p><em>No interaction.</em> For $J=0$ the Gibbs measure is the product of the prior and is unique, so $M(\beta)=0$ for every $\beta$; the plus and minus boundary conditions have no effect beyond the boundary itself, and the two limits coincide with the product measure.</p>

<p><em>An external field.</em> A field $h\sum_x\sigma_x$ adds the constant $h$ to every field in the specification, and <a href="/tag/96HI/">the domination proposition</a> applies in $h$ as it does in the boundary condition: the finite-volume measures are nondecreasing in $h$, hence so is $M(\beta,h)$, and the limit $h\downarrow0$ exists and is the order parameter of this article. The field also breaks the flip symmetry, so the minus state is no longer the mirror image of the plus one, and the two magnetisations, one positive and one negative at $h=0$, move towards each other as $h$ increases. That monotonicity is what makes the phase diagram of a model with a field a pair of curves rather than a pair of symmetric ones; where they meet is not a question monotonicity answers.</p>

<p><em>Non-example: the antiferromagnet.</em> For $J&lt;0$ the FKG inequality in the form used here fails, since the lattice condition has the wrong sign, and with it every step of this article: the heat bath is no longer monotone, the plus and minus boundary conditions no longer bound the Gibbs measures, and the order parameter defined above has no reason to detect anything. Recovering a monotone structure for an antiferromagnet needs a gauge transformation, that is a choice of signs $\chi$ with $\chi(x)\chi(y)=-1$ across each coupled pair, which presupposes a bipartition of the coupled pairs; on the hierarchical lattice every pair is coupled, at some level, and no such $\chi$ exists. The wiki treats ferromagnetic models throughout, and this is the hypothesis the article rests on.</p>

<p><em>Percolation.</em> The same architecture holds for <a href="/articles/hierarchical-percolation-rg/">bond percolation</a> on the lattice: the Harris–FKG inequality gives that the connection probabilities increase in the intensity, the percolation probability $\theta(\beta)=\mathbb P_\beta(\lvert K_0\rvert=\infty)$ plays the role of the order parameter and is positive exactly in the percolating phase. The threshold there is $\beta_c$ of the percolation article, and its finiteness is decided by $\alpha&lt;d$ through a comparison with the recursion, again not by monotonicity.</p>

## Variants and generalisations {#section-variants}

<p><em>Other boundary conditions.</em> Every configuration $\omega$ satisfies $-\preceq\omega\preceq+$, so the sandwich holds with $\mathbb P_\Lambda^{\omega}$ in place of $\mathbb P_\Lambda^{\pm}$: the plus and minus states bound every finite-volume measure, not only the Gibbs measures. Free boundary conditions are not of that form, since there is no outside configuration to compare with, but the same domination holds: the plus measure is the free measure reweighted by $\exp\bigl(\beta\sum_{x\in\Lambda}b_x\sigma_x\bigr)$ with $b_x=\sum_{y\notin\Lambda}J(x-y)\geq0$, a bounded increasing function of the configuration, so the FKG inequality gives $\mathbb P_\Lambda^{\mathrm{free}}\preceq\mathbb P_\Lambda^{+}$ and the free limit of the previous article lies between $\mu_-$ and $\mu_+$ as well.</p>

<p><em>Monotonicity in the intensity.</em> That $M(\beta)$ is nondecreasing in $\beta$ is the first Griffiths inequality, the companion of the second used above, and is the same statement as the monotonicity of the correlations in the couplings [@griffiths-1967]. It gives a critical intensity $\beta_c=\inf\{\beta:M(\beta)>0\}$ as a well-defined number, and it is what makes the phase diagram a diagram rather than a set of values; it still does not evaluate the infimum.</p>

<p><em>The general block system.</em> Nothing in the argument uses the lattice beyond the fact that the blocks exhaust the vertex set and that the model is ferromagnetic with a finite total mass at a vertex. For any attractive spin system on a countable set the same two propositions hold, with the same proofs: the boundary-conditioned measures increase in the boundary configuration, the plus and minus limits exist, and every Gibbs measure lies between them. That the Gibbs measures of an attractive system form an interval in the stochastic order is the general form of <a href="/tag/N9S3/">the sandwich</a>.</p>

## History and attribution {#section-history}

<p>The inequality that increasing functions are positively correlated under a ferromagnetic measure is due to Fortuin, Kasteleyn and Ginibre [@fkg-1971]; for Ising spins the correlation inequalities, including the pair used here, are Griffiths's [@griffiths-1967]. The extremal states of an attractive system, obtained as the monotone limits of the plus and minus boundary conditions, and the statement that every Gibbs measure lies between them, are part of the general theory in Georgii's book [@georgii-2011], where the argument is given for a general specification; the monotone coupling used above is the standard proof in the finite volume.</p>

<p>The phase transition of the hierarchical Ising model, with a nonzero spontaneous magnetisation above the critical coupling, is the third branch of the trichotomy of Bleher and Sinai [@bleher-sinai-1973] [@bleher-sinai-1975]; <a href="/articles/bleher-sinai-fixed-point/">the fixed-point article</a> states their theorem and describes the mechanism of its proof. The separation recorded in the previous section — that the architecture is a matter of monotonicity and the threshold a matter of the recursion — is not a claim about the literature, in which the two are usually proved together for a particular model, but about which argument carries which statement.</p>

## References {#section-references}

<ul>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>C. M. Fortuin, P. W. Kasteleyn and J. Ginibre, Correlation inequalities on some partially ordered sets, <em>Comm. Math. Phys.</em> 22 (1971), 89&ndash;103.</li>
<li>H.-O. Georgii, <em>Gibbs Measures and Phase Transitions</em>, 2nd extended edition, De Gruyter Studies in Mathematics 9, de Gruyter, 2011.</li>
<li>R. B. Griffiths, Correlations in Ising ferromagnets, <em>J. Math. Phys.</em> 8 (1967), 478&ndash;489.</li>
</ul>
