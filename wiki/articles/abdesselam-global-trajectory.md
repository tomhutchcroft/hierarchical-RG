---
{
  "id": "abdesselam-global-trajectory",
  "title": "Abdesselam's trajectory between two fixed points",
  "subtitle": "A whole orbit of the renormalisation group, from the Gaussian fixed point to the nontrivial one.",
  "kind": "theorem",
  "category": "Renormalisation group",
  "summary": "A fixed point describes one scale-invariant theory; a trajectory between two fixed points describes the whole crossover from the ultraviolet to the infrared. Abdesselam constructed such a trajectory rigorously and nonperturbatively for a three-dimensional phi-fourth model with modified propagator, joining the Gaussian fixed point to an analogue of the Wilson-Fisher fixed point, by a fixed point argument in a Banach space of sequences which perturbs a nonlinear one-dimensional iteration.",
  "context": [
    "Wilson's exact renormalisation group as a discrete map on effective potentials, one step per scale.",
    "The model is three-dimensional with a modified free propagator, the modification making the fluctuation covariance small.",
    "The unperturbed problem is a one-dimensional iteration of the kind the hierarchical model supplies."
  ],
  "related": [
    "koch-wittwer-fixed-point",
    "hierarchical-and-euclidean-rg",
    "hierarchical-phi4-truncations",
    "bleher-sinai-fixed-point"
  ],
  "sourceIds": ["abdesselam-2007", "abdesselam-2009", "brydges-mitter-scoppola-2003", "bauerschmidt-brydges-slade-2019"],
  "aliases": [
    "complete renormalization group trajectory",
    "heteroclinic orbit",
    "crossover",
    "modified propagator",
    "global renormalisation group flow"
  ]
}
---

<p>The renormalisation group of a lattice field theory is a map on a space of interactions, one step per scale, and most rigorous results about it are local: a fixed point, its stable and unstable manifolds, and the behaviour of orbits near it. A <em>complete trajectory</em> is a global object instead, an orbit defined at every scale and asymptotic at one end to the ultraviolet Gaussian fixed point and at the other to the nontrivial infrared one. Abdesselam constructed such a trajectory rigorously and nonperturbatively for the three-dimensional $\varphi^4$ model with a modified free propagator [@abdesselam-2007], joining the Gaussian fixed point to an analogue of the Wilson-Fisher fixed point of the kind constructed by Brydges, Mitter and Scoppola [@brydges-mitter-scoppola-2003].</p>

<p>Two features of the construction matter for this wiki. It does not use the hierarchical approximation — the map is the Euclidean one — and yet the unperturbed problem it perturbs is a nonlinear one-dimensional iteration of exactly the kind the <a href="/articles/hierarchical-gibbs-measure/">hierarchical model</a> provides, with the perturbation supplied by the modified propagator [@abdesselam-2009]. The hierarchical recursion is therefore not an analogy for the Euclidean renormalisation group in this work but its first approximation, and the trajectory is recovered from the one-dimensional flow by a fixed-point argument in a space of sequences of effective potentials.</p>

<p>The modification of the propagator is what makes the argument close: it suppresses the fluctuations at each scale by a fixed amount, so that the Euclidean step is a bounded perturbation of the hierarchical one. Whether the trajectory can be transported to the unmodified propagator is a separate question, and the construction is a statement about the modified model.</p>

## Definitions and setting {#section-setting}

<p>The renormalisation group is the following operation, in the form used in the renormalisation-group treatment of lattice fields [@bauerschmidt-brydges-slade-2019]. One fixes a <em>fluctuation covariance</em> $C$, a positive definite kernel on the lattice, and a decomposition of it into pieces $C=\sum_jC_j$ indexed by scale. Given an effective potential $V_j$ at scale $j$, one defines</p>
<div class="math-display">$$e^{-V_{j+1}(\varphi)}=\int e^{-V_j(\varphi+\zeta)}\,\mu_{C_j}(d\zeta),$$</div>
<p>the convolution of the Boltzmann weight with the Gaussian measure of covariance $C_j$, followed by the rescalings of field and position that put the result in a fixed normal form. The map $V_j\mapsto V_{j+1}$ is the renormalisation step, and a fixed point of the step is a scale-invariant theory.</p>
<a id="tag-D8WK" data-assertion="definition" data-title="Trajectory between two fixed points"></a>
<p>A <em>trajectory between two fixed points</em> is a sequence $(V_j)_{j\in\mathbb Z}$ of effective potentials, each in the domain of the map, such that $V_{j+1}$ is the image of $V_j$ for every $j$, and such that $V_j$ converges to the Gaussian fixed point as $j\to-\infty$ and to the nontrivial fixed point as $j\to+\infty$. The first limit is the ultraviolet, the second the infrared; the intermediate potentials describe the crossover, which is the region in which neither fixed point's linearisation controls the flow.</p>
<p>For the hierarchical model the corresponding object is a sequence of laws $\nu_j=\mathcal R_{\theta_0,b}^{\,j}\nu_0$ under the single map of <a href="/articles/renormalisation-group-map/#section-autonomous">the autonomous form</a>, and a trajectory between fixed points is an orbit whose two ends are the Gaussian and nontrivial fixed points of that map. In that case the trajectory is a property of a one-dimensional iteration and can be analysed by the methods of <a href="/articles/bleher-sinai-fixed-point/">the fixed-point article</a>.</p>

## Statement {#section-statement}

<a id="tag-D4XR" data-assertion="theorem" data-title="Existence of a complete trajectory in three dimensions"></a>
<p>Let the field be three-dimensional with a modified free propagator, and let the interaction be a $\varphi^4$ perturbation with a small coupling. Then there is a sequence of effective potentials $(V_j)_{j\in\mathbb Z}$ satisfying the renormalisation recursion exactly, asymptotic to the ultraviolet Gaussian fixed point as $j\to-\infty$ and to the nontrivial infrared fixed point as $j\to+\infty$. The construction is nonperturbative in the sense that no order-by-order expansion is resummed: it produces the trajectory as the solution of a fixed-point equation in a Banach space of sequences.</p>
<p>The statement is Theorem 1 of Abdesselam [@abdesselam-2007], with the summary of the method and of the role of the modified propagator in the six-page account of the same construction [@abdesselam-2009]. The infrared endpoint is an analogue of the Wilson-Fisher fixed point: it is the nontrivial fixed point of the model with the modified propagator rather than a statement about the unmodified three-dimensional $\varphi^4$ theory, whose renormalisation-group trajectory is constructed by different means in the work of Brydges, Mitter and Scoppola [@brydges-mitter-scoppola-2003].</p>

## Idea of the proof {#section-idea}

<p>The three steps below are the ones the account of the construction names; the estimates are in the paper.</p>
<p><em>The one-dimensional problem.</em> With a propagator that is constant on blocks and a field that is constant on blocks, the renormalisation step becomes an operation on the law of one number, that is, a nonlinear one-dimensional iteration. For such an iteration the two fixed points and the orbit joining them can be constructed explicitly or by the methods of the scalar hierarchical analysis, and the resulting sequence is the unperturbed trajectory.</p>
<p><em>The Euclidean problem as a perturbation.</em> For the modified propagator the difference between the Euclidean step and the block step is small, uniformly in the scale, because the modification suppresses the fluctuations that the block approximation discards. The trajectory is then sought as a perturbation of the unperturbed sequence, with the perturbation carried by the couplings of the model.</p>
<p><em>The fixed-point argument.</em> The space of sequences is given a norm that measures, at each scale, the size of the deviation of the effective potential from the unperturbed one, with a weight that grows in the direction of the unstable manifold and decays in the stable directions. On that space the renormalisation recursion becomes a fixed-point equation whose linearisation is invertible, the inverse being controlled by the spectral gap of the one-dimensional problem at each of its two ends; the contraction principle then gives the trajectory. The weights are the reason the argument works at a fixed point of the flow and not only near one: the unstable direction at the ultraviolet end is the stable direction at the infrared end, and the weights are chosen to be summable along the whole orbit.</p>

## Consequences and applications {#section-consequences}

<p><em>The crossover region.</em> The trajectory controls the intermediate scales, where the linearisation at either fixed point gives no information. Correlation functions of the model at momenta in the crossover region are governed by the corresponding intermediate effective potential, so a statement about the whole orbit is a statement about the region in which the exponents alone do not determine the behaviour.</p>

<p><em>The hierarchical model as the organising centre.</em> The construction makes precise the sense in which the hierarchical recursion is the first approximation to the Euclidean renormalisation group: the Euclidean trajectory is obtained from the one-dimensional one by a perturbation whose size is controlled by the propagator, and the one-dimensional trajectory is the input. This is the quantitative form of the comparison drawn in <a href="/articles/hierarchical-and-euclidean-rg/">the article on the two settings</a>.</p>

<p><em>A template for other models.</em> The argument uses only that the unperturbed problem is a one-dimensional iteration with two hyperbolic fixed points and that the perturbation is small; the same scheme applies to the vector models and to the $p$-adic and ultrametric settings in which the block structure is exact, which is the content of Abdesselam's programme for a three-dimensional conformal field theory [@abdesselam-2018].</p>

## Examples and non-examples {#section-examples}

<p><em>The hierarchical model itself.</em> For a prior with a small quartic coupling and a kernel exponent above the marginal one, the orbit of the recursion from the Gaussian neighbourhood towards the nontrivial fixed point is a trajectory between fixed points in the sense above; it is the unperturbed object of the Euclidean construction.</p>

<p><em>A critical orbit.</em> The orbit that starts exactly on the stable manifold of the nontrivial fixed point is critical: its correlation length is infinite at every scale, and it is a trajectory between fixed points only in the sense of convergence to one of them. The trajectory of the theorem has both ends and a finite crossover scale; the two objects answer different questions.</p>

<p><em>Non-example: a massive orbit.</em> An orbit that leaves the neighbourhood of the Gaussian fixed point along the relevant direction and does not return describes a model with a finite correlation length. It is a perfectly good orbit, but not a trajectory between two fixed points.</p>

<p><em>Non-example: without the modified propagator.</em> The construction rests on the smallness of the difference between the block step and the Euclidean step. For the unmodified propagator that difference is not small, and the trajectory of the unmodified theory requires the polymer and cluster expansions of the Brydges-Mitter-Scoppola programme rather than a perturbation of a one-dimensional iteration.</p>

## Variants and generalisations {#section-variants}

<p><em>Other crossovers.</em> A trajectory can join any two hyperbolic fixed points between which the flow is defined, and the same Banach-space scheme applies when the intermediate region is described by a known one-dimensional model. The crossover from mean field to critical behaviour is the case at hand; crossovers associated with a change of symmetry or with a change of the number of components would require a different unperturbed problem.</p>

<p><em>Ultrametric and $p$-adic versions.</em> In settings where the block structure is exact the unperturbed problem is the model itself, and the trajectory is the orbit of the one-dimensional map; the ultrametric version of the construction is part of Abdesselam's programme for conformal probability [@abdesselam-2018].</p>

<p><em>Logarithmic corrections.</em> At the marginal exponent the two fixed points merge and the trajectory is no longer hyperbolic at either end; the flow then has a logarithmic scale dependence, and the Banach-space argument has to be replaced by one adapted to the marginal case.</p>

## History and attribution {#section-history}

<p>The nontrivial infrared fixed point of the modified three-dimensional model is due to Brydges, Mitter and Scoppola [@brydges-mitter-scoppola-2003]. The complete trajectory between the two fixed points, and the observation that the Euclidean problem is a perturbation of a one-dimensional iteration, are Abdesselam's [@abdesselam-2007], with an account of the method in the proceedings of the 2009 congress [@abdesselam-2009]. The renormalisation group in the potential formulation used here is the subject of Bauerschmidt, Brydges and Slade [@bauerschmidt-brydges-slade-2019].</p>

## References {#section-references}

<ul>
<li>A. Abdesselam, A complete renormalization group trajectory between two fixed points, <em>Comm. Math. Phys.</em> 276 (2007), 727&ndash;772.</li>
<li>A. Abdesselam, Renormalization group trajectories between two fixed points, in <em>Proc. XVI Int. Congr. Math. Phys.</em>, Prague, 2010.</li>
<li>A. Abdesselam, Towards three-dimensional conformal probability, <em>p-Adic Numbers Ultrametric Anal. Appl.</em> 10 (2018), 233&ndash;247.</li>
<li>R. Bauerschmidt, D. C. Brydges and G. Slade, <em>Introduction to a Renormalisation Group Method</em>, Lecture Notes in Mathematics 2242, Springer, 2019.</li>
<li>D. C. Brydges, P. K. Mitter and B. Scoppola, Critical $(\Phi^4)_3$, <em>Comm. Math. Phys.</em> 240 (2003), 281&ndash;327.</li>
</ul>
