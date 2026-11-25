---
{
  "id": "hierarchical-two-marginalities",
  "title": "The two marginal exponents",
  "subtitle": "Alpha equal to d decides summability, alpha equal to d/2 decides relevance, and they are not the same threshold.",
  "kind": "theorem",
  "category": "Hierarchical models",
  "summary": "Two values of the kernel exponent are distinguished in the hierarchical model and they are easy to conflate. At alpha equal to d the interaction stops being summable and the level sequence alone decides whether the model is a Gibbs system with a transition. At alpha equal to d/2 the quartic coupling is marginal at the Gaussian fixed point, so the nontrivial fixed point is relevant above that value and the classical exponents hold below it. The first threshold is about the measure, the second about the map; one is a criterion at a point, the other a bifurcation.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $m=L^d$; level couplings $J_k=l_kL^{-(d+\\alpha)k}$ with $l_k\\geq0$, so $\\alpha$ is the exponent and $l$ the slowly varying factor.",
    "The model is the one of the decimation article; the recursion is the one of the map article; the exponents are those of the dictionary."
  ],
  "related": [
    "hierarchical-gibbs-measure",
    "gaussian-fixed-point-spectrum",
    "hierarchical-vector-models",
    "hierarchical-percolation-rg",
    "bleher-sinai-fixed-point",
    "hierarchical-cluster-volume",
    "hierarchical-fixed-points"
  ],
  "sourceIds": [
    "bleher-major-2021",
    "bleher-sinai-1975",
    "gawedzki-kupiainen-1983",
    "koval-meester-trapman-2012",
    "hutchcroft-hierarchical-2021"
  ],
  "aliases": [
    "marginal exponent",
    "summability threshold",
    "quartic threshold",
    "upper critical dimension",
    "level sequence"
  ]
}
---

<p>Two numbers are singled out in everything written above, and the notation makes them look more alike than they are. The kernel exponent $\alpha$ enters the coupling as $J_k=l_kL^{-(d+\alpha)k}$, and two special values recur: $\alpha=d$, where the interaction stops being <a href="/articles/hierarchical-lattice/#section-kernels">summable</a>, and $\alpha=d/2$, where the quartic coupling stops being <a href="/articles/gaussian-fixed-point-spectrum/#section-quartic">irrelevant</a> at the Gaussian fixed point. One is a threshold of the measure, the other of the map, and the regimes they cut out are different: in three dimensions, $\alpha=3$ and $\alpha=3/2$ are both called marginal in the literature and they have nothing to do with each other.</p>

<p>This article separates them. It is a synthesis rather than a new argument: every ingredient is proved or attributed elsewhere in the wiki, and what is added is the statement of which criterion applies where, because the two have been used in different articles and never side by side.</p>

## The level sequence {#section-level-sequence}

<p>Write the coupling at level $k$ as $J_k=l_kL^{-(d+\alpha)k}$ with $l_k\geq0$, so that $\alpha$ is the exponent and $l$ carries whatever slow variation the kernel has. The total intensity at a vertex is then a sum over shells, and the shells grow at rate $m^k$.</p>
<a id="tag-2I6O" data-assertion="definition" data-title="The level sequence, and the two marginal values of the exponent"></a>
<p>The <em>level sequence</em> is $l=(l_k)_{k\geq1}$, and the model at exponent $\alpha$ has couplings $J_k=l_kL^{-(d+\alpha)k}$. The two marginal values are</p>
<div class="math-display">$$\alpha=d\ \text{(summability)},\qquad \alpha=d/2\ \text{(relevance of the quartic)}.$$</div>
<p>A kernel with $\alpha=d$ and $l_k\equiv1$ is <em>just not summable</em>: its shells contribute a constant, so the total intensity diverges logarithmically in the level. A kernel with $\alpha=d/2$ is summable for every $d>0$, and the marginality there is a statement about the linearisation of the recursion, not about the measure.</p>

## The threshold of the measure {#section-summability}

<a id="tag-JBBF" data-assertion="proposition" data-title="At alpha = d summability is decided by the level sequence alone"></a>
<p>Let $\alpha=d$. Then</p>
<div class="math-display">$$\sum_{x\neq0}J(\lVert x\rVert)=(1-L^{-d})\sum_{k\geq1}l_k,$$</div>
<p>so the interaction is summable if and only if $\sum_kl_k<\infty$, and it is summable for every $\alpha>d$ and for no $\alpha<d$ with $l_k\not\to0$ fast enough. In particular the marginal case is not decided by the exponent.</p>
:::details Proof
<p>The shell at level $k$ has $(1-L^{-d})L^{dk}$ vertices by <a href="/articles/hierarchical-lattice/#section-blocks">the shell count</a>, and each contributes $J_k=l_kL^{-(d+\alpha)k}$. At $\alpha=d$ the two powers of $L$ cancel and the shell contributes $(1-L^{-d})l_k$, so the sum is the stated multiple of $\sum_kl_k$. For $\alpha>d$ the shell contributes $(1-L^{-d})l_kL^{-(\alpha-d)k}$, and convergence follows from $l_k$ bounded; for $\alpha<d$ the shell contributes a positive multiple of $l_kL^{(d-\alpha)k}$, which diverges unless $l$ decays at least that fast.</p>
:::
<p>Whether the marginal case is a Gibbs system at all is therefore a question about $l$, and the literature treats it as such. For the spin model, Bleher and Major prove that at $\alpha=d$ a phase transition exists exactly when $\sum_kl_k=\infty$: the divergent marginal interaction orders at low temperature, the convergent one does not, and in the divergent case the transition is continuous with a vanishing magnetisation and a block spin whose direction does not concentrate [@bleher-major-2021], which is the criterion <a href="/articles/hierarchical-vector-models/#section-thouless">the vector article</a> states. For percolation the corresponding statement is sharper still: $\beta_c<\infty$ exactly when $\alpha<d$ [@koval-meester-trapman-2012], so at $\alpha=d$ there is no transition at any intensity, for every level sequence with $l_k\not\to0$. The two models disagree at the marginal exponent — the spin model can order and the percolation model cannot — and that is itself the point: summability decides whether the model is well posed, and what happens at the threshold is a model-specific question that has to be answered, not deduced.</p>

## The threshold of the map {#section-relevance}

<a id="tag-RS6Z" data-assertion="proposition" data-title="The quartic eigenvalue is one exactly at alpha = d/2"></a>
<p>At the Gaussian fixed point the linearised potential map is triangular in the even monomials with eigenvalues $\Lambda_{kk}=L^{d(1-k)+k\alpha}$. The quadratic direction has eigenvalue $L^{\alpha}>1$ for every $\alpha>0$, and the quartic direction has eigenvalue</p>
<div class="math-display">$$\Lambda_{22}=L^{2\alpha-d},$$</div>
<p>which is one exactly at $\alpha=d/2$, larger above it and smaller below. Hence the quartic coupling is relevant for $\alpha>d/2$, marginal at it, and irrelevant below.</p>
:::details Proof
<p>The eigenvalue formula is <a href="/articles/gaussian-fixed-point-spectrum/#section-statement">the spectrum theorem</a>; setting $k=2$ gives $\Lambda_{22}=L^{d(1-2)+2\alpha}=L^{2\alpha-d}$, and $k=1$ gives $L^{\alpha}$. The sign of $2\alpha-d$ decides the comparison with one, and $L>1$ is increasing.</p>
:::
<p>This threshold is of a different kind. It is not a statement about whether the model is defined — the model is a Gibbs system for every $\alpha>0$ — but about which fixed point governs the critical behaviour: below $d/2$ the quartic is irrelevant, the critical orbit converges to the Gaussian fixed point after rescaling, and the exponents are the classical ones; above it the quartic is relevant, a nontrivial fixed point separates from the Gaussian one, and the correlation-length exponent is no longer $1/\alpha$ [@bleher-sinai-1975] [@gawedzki-kupiainen-1983]. At the threshold itself the two fixed points merge, the second eigenvalue tends to one, the leading correction becomes logarithmic, and the analysis needs its own treatment.</p>
<p>The dependence on the dimension is worth stating separately, because it is the reason the phrase "upper critical dimension" is used for two different things. Setting $\alpha=2$, which is the power law of a short-range interaction in the sense that $\lVert x\rVert^{-d-2}$ is the borderline of summability of the second moment, gives $\alpha=d/2$ exactly when $d=4$. So the four-dimensional theory is the marginal one for the quartic, which is why the four-dimensional $\lvert\varphi\rvert^4$ model is the case <a href="/articles/hierarchical-phi4-truncations/#section-potentials">the potential formulation</a> and the method of Bauerschmidt, Brydges and Slade are built for. The two thresholds coincide there, and nowhere else.</p>

## The regimes side by side {#section-table}

<p>The table collects what the two thresholds do, with the status of each statement.</p>
<table><thead><tr><th>Regime</th><th>Summability</th><th>Quartic at the Gaussian fixed point</th><th>What the exponents are</th></tr></thead>
<tbody>
<tr><td>$\alpha<d/2$</td><td>summable</td><td>irrelevant</td><td>classical, $\nu=1/\alpha$, proved</td></tr>
<tr><td>$\alpha=d/2$</td><td>summable</td><td>marginal</td><td>classical with logarithmic corrections</td></tr>
<tr><td>$d/2<\alpha<d$</td><td>summable</td><td>relevant</td><td>$\kappa=\alpha$ proved; $\nu\neq1/\alpha$, not known in closed form</td></tr>
<tr><td>$\alpha=d$</td><td>decided by $\sum_kl_k$</td><td>relevant</td><td>criterion of Bleher and Major; exponents not classical</td></tr>
<tr><td>$\alpha>d$</td><td>summable</td><td>relevant</td><td>outside the long-range range; the two-point bounds do not apply</td></tr>
</tbody></table>
<p>Reading down the first column, the model is a Gibbs system throughout except possibly at $\alpha=d$, where the level sequence decides; reading down the third, the fixed point changes character at $d/2$ whatever the level sequence. The two rows that are easiest to confuse are the two middle ones, and the table is here to keep them apart: at $\alpha=d/2$ the model is as summable as it ever is, and at $\alpha=d$ the quartic is as relevant as it ever is.</p>

## Examples and non-examples {#section-examples}

<p><em>One dimension.</em> Here the thresholds are $\alpha=1$ and $\alpha=1/2$, and Dyson's model lives in between: a transition with $\beta_c<\infty$ for every $\alpha<1$, no transition at $\alpha\geq1$ for the percolation model, and the classical exponents for $\alpha<1/2$. So in one dimension the interval $(1/2,1)$ is the one in which the exponents are not classical but the transition exists — which is why Dyson's paper and the whole subsequent literature are about that interval.</p>

<p><em>Four dimensions.</em> The thresholds are $\alpha=4$ and $\alpha=2$, and the second of them is the upper critical dimension of the phi-fourth theory. A reader who takes "α = d is the upper critical dimension" from the spin-glass or percolation literature and applies it to the phi-fourth model will get the wrong threshold by a factor of two, which is the confusion the table is meant to prevent.</p>

<p><em>A level sequence that decays at $\alpha=d$.</em> Take $l_k=L^{-\beta k}$ with $\beta>0$ and $\alpha=d$. The interaction is then summable, with the effective exponent $d+\beta$, and Bleher and Major's criterion puts the vector model below its transition: the sequence, not the exponent, decides. For the scalar model at $\alpha=d$ this wiki records no criterion, and that asymmetry is part of the point of the section — the marginal case is a question about a model and a sequence, not a formula.</p>

<p><em>Non-example: applying the percolation criterion to the spin model.</em> At $\alpha=d$ the percolation model has $\beta_c=\infty$ for every nondecaying $l$, and the spin model can have a transition. A criterion is a statement about a model, not about an exponent, and this pair is the counterexample to treating them as interchangeable.</p>

## Variants and generalisations {#section-variants}

<p><em>The vector case.</em> Nothing in either threshold involves the number of components: the summability computation is about the kernel, and the quartic eigenvalue is computed in <a href="/articles/gaussian-fixed-point-spectrum/">the spectrum article</a> within the scalar sector, which the vector article shows is enough because the Gaussian fixed point is $r$-independent. The marginal criteria at $\alpha=d$ do differ with $r$: for $r=1$ the direction is a sign and the phenomenon of non-concentrating direction has no scalar analogue, which is what <a href="/articles/hierarchical-vector-models/">that article</a> is about.</p>

<p><em>The percolation triangle threshold.</em> A third special value, $\alpha=d/3$, appears in percolation and is of neither kind: it is where the triangle diagram at criticality changes from convergent to divergent, which is a statement about a diagram rather than about the measure or the linearisation. <a href="/articles/hierarchical-percolation-rg/#section-triangle">The percolation article</a> derives it, and it is the threshold that decides whether the model is mean-field, not whether it is defined or which fixed point governs the scalar spin model.</p>

<p><em>Slowly varying factors elsewhere.</em> The same device — an exponent fixed and a sequence left free — is used for the correlation-length exponent at $\alpha=d/2$, where the corrections become logarithmic because the second eigenvalue tends to one. That is the third place in the wiki where a threshold is resolved by a sequence rather than by a number, and <a href="/articles/corrections-to-scaling/#section-examples">the corrections article</a> treats it.</p>

## History and attribution {#section-history}

<p>The summability criterion is the elementary computation of <a href="/articles/hierarchical-lattice/#section-kernels">the lattice article</a>, and the marginal case $\alpha=d$ is where Bleher and Major's analysis of Dyson's conjecture lives: the criterion in terms of the level sequence, the continuity of the transition and the non-concentration of the direction are theirs [@bleher-major-2021]. The percolation counterpart at $\alpha=d$ is part of the classical theory of long-range percolation on the hierarchical lattice [@koval-meester-trapman-2012], and the two-point bounds at criticality beyond the marginal exponent are Hutchcroft's [@hutchcroft-hierarchical-2021].</p>

<p>The quartic threshold $\alpha=d/2$ is the value at which the quartic eigenvalue of <a href="/articles/gaussian-fixed-point-spectrum/">the spectrum article</a> crosses one; that it is where the exponents change from classical to non-classical is the content of the fixed-point analysis of Bleher and Sinai [@bleher-sinai-1975], and the local description near the threshold, with the expansion in $\alpha-d/2$, is that of Gawedzki and Kupiainen [@gawedzki-kupiainen-1983]. That the two thresholds coincide at $\alpha=2$, $d=4$ is arithmetic, and it is the reason the four-dimensional theory is the marginal one for the quartic.</p>

## References {#section-references}

<ul>
<li>P. M. Bleher and P. Major, A Thouless-like effect in the Dyson hierarchical model with continuous symmetry, <em>Pure Appl. Funct. Anal.</em> 6 (2021), 101&ndash;175.</li>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian fixed points of the block spin transformation. Hierarchical model approximation, <em>Comm. Math. Phys.</em> 89 (1983), 191&ndash;220.</li>
<li>T. Hutchcroft, The critical two-point function for long-range percolation on the hierarchical lattice, <em>Ann. Appl. Probab.</em> 34 (2024), no. 1B, 986&ndash;1002.</li>
<li>V. Koval, R. Meester and A. Trapman, Long-range percolation on the hierarchical lattice, <em>Electron. J. Probab.</em> 17 (2012), no. 57.</li>
</ul>
