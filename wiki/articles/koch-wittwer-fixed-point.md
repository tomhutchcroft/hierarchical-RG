---
{
  "id": "koch-wittwer-fixed-point",
  "title": "Koch and Wittwer's non-Gaussian fixed point",
  "subtitle": "A fixed point proved at a specific parameter, with no small parameter and no truncation.",
  "kind": "theorem",
  "category": "Renormalisation group",
  "summary": "Koch and Wittwer proved the existence of a non-quadratic fixed point of the scalar hierarchical renormalisation map at explicit parameter values, by an a posteriori argument: an approximate fixed point is computed and estimates on the linearisation upgrade it to an exact one. The companion papers supply the functional-analytic framework and treat the Dyson-Baker variant of the block structure.",
  "context": [
    "The scalar hierarchical model with $m\\geq2$ children and a fixed coupling, in the potential formulation of the article on truncations.",
    "Interactions are even real-analytic potentials with Gaussian bounds; the map is the effective-potential map up to the additive free energy constant.",
    "The parameter values are those of the papers; no small parameter and no epsilon expansion is used."
  ],
  "related": [
    "hierarchical-phi4-truncations",
    "bleher-sinai-fixed-point",
    "gaussian-renormalisation-group",
    "abdesselam-global-trajectory"
  ],
  "sourceIds": ["koch-wittwer-1986", "koch-wittwer-1991", "koch-wittwer-1994", "bleher-sinai-1975", "gawedzki-kupiainen-1983"],
  "aliases": [
    "non-Gaussian fixed point",
    "computer-assisted proof",
    "Dyson-Baker model",
    "Koch-Wittwer",
    "a posteriori estimate"
  ]
}
---

<p>A fixed point of the hierarchical renormalisation map that is not quadratic is the critical theory of the scalar model above the marginal exponent, and the two general routes to it leave a gap. The theorem of <a href="/articles/bleher-sinai-fixed-point/">Bleher and Sinai</a> proves existence in a class of measures, but its statement is qualitative and its hypotheses are those of a parameter range; the <a href="/articles/bleher-sinai-fixed-point/#section-spectrum">epsilon expansion</a> of Gawedzki and Kupiainen describes a neighbourhood of the marginal exponent, not a point away from it. Koch and Wittwer closed the gap for the scalar hierarchical model by proving that a non-quadratic fixed point exists at explicit parameter values, with an argument that uses the computer to verify estimates but no small parameter at all [@koch-wittwer-1986].</p>

<p>The strategy is the one now standard for computer-assisted existence proofs in analysis. An approximate fixed point is computed numerically, to high order, as a finite vector of Taylor coefficients; the map is then shown to be a contraction on a small ball around that approximation, in a Banach space of even analytic potentials, with the contraction constant and the radius certified by explicit numerical estimates; and a fixed point follows from the contraction principle. The companion paper sets out the space of interactions, the map and the estimates on which the certification rests [@koch-wittwer-1991], and the third paper carries the same programme out for the Dyson-Baker block structure [@koch-wittwer-1994].</p>

<p>What the result adds to the general theory is a fixed point at a named parameter rather than in a range, and with it the possibility of computing the exponents of that fixed point to whatever accuracy the numerical part is carried. What it does not do is explain why the fixed point exists: the mechanism, in which a quadratic fixed point loses stability at the marginal exponent and a pair of non-quadratic ones appear, is the content of the epsilon expansion, and Koch and Wittwer's theorem is the existence statement that the expansion predicts.</p>

## Definitions and setting {#section-setting}

<p>The object is the effective-potential map of <a href="/articles/hierarchical-phi4-truncations/#section-potentials">the truncations article</a>: for an even potential $V$ and a coupling $b\geq0$,</p>
<div class="math-display">$$e^{-(\mathcal V_bV)(s)}=\int_{\mathbb R^{m-1}}\exp\Bigl(b\sum_{a&lt;a'}s_as_{a'}\Bigr)\prod_{a=1}^{m}e^{-V(s_a)}\,ds_1\cdots ds_{m-1},\qquad s_m=s-\sum_{a&lt;m}s_a,$$</div>
<p>with the normalising constant dropped. A <em>fixed point</em> is an even potential $V^*$ with $\mathcal V_bV^*=V^*$ up to an additive constant. The quadratic potential $\tfrac{\mu}{2}s^2$ is a fixed point for exactly one curvature, computed in <a href="/articles/gaussian-renormalisation-group/#section-multiplier">the Gaussian article</a>, and it is that fixed point which loses stability at the marginal exponent.</p>
<a id="tag-C7QF" data-assertion="definition" data-title="The scalar fixed-point problem"></a>
<p>The problem is to find $V^*$, not quadratic, with $\mathcal V_bV^*=V^*$. Equivalently, writing $V(s)=\sum_{j\geq1}v_j s^{2j}$ in a neighbourhood of the origin, the problem is the infinite system of equations obtained by matching the Taylor coefficients of $\mathcal V_bV$ with those of $V$; the constant term is fixed by the normalisation and plays no role.</p>
<p>The space in which the problem is posed consists of even functions, analytic in a disc of a fixed radius, whose Taylor coefficients decay at a prescribed rate and which satisfy a bound of the form $\lvert V(s)\rvert\leq C(1+\lvert s\rvert^p)$ with $p$ fixed. The map $\mathcal V_b$ is well defined on that space for the parameter values of the theorem, and its derivative at a point of the space is an explicit integral operator with a Gaussian kernel, obtained by differentiating the constraint and the tilt.</p>

## Statement {#section-statement}

<a id="tag-C2ZB" data-assertion="theorem" data-title="Existence of a non-quadratic fixed point at explicit parameter values"></a>
<p>There are explicit values of the number of children $m$ and of the coupling $b$, given in the papers, and an even real-analytic potential $V^*$, not quadratic, with the following properties: $\mathcal V_bV^*=V^*$ up to an additive constant; $V^*$ satisfies the growth condition of the space; the derivative of $\mathcal V_b$ at $V^*$ is a bounded operator with a simple eigenvalue $\lambda_1&gt;1$ and the rest of its spectrum inside a disc of radius less than one; and in the Dyson-Baker variant of the block structure the same conclusion holds with the corresponding map [@koch-wittwer-1986] [@koch-wittwer-1994].</p>
<p>The eigenvalue statement is what makes the fixed point a critical theory rather than a solution of an equation: it says that the unstable direction is one-dimensional, so a one-parameter family of models is critical at the fixed point and the correlation-length exponent is $\log L/\log\lambda_1$ by the dictionary of <a href="/articles/critical-exponents-from-rg/#section-dictionary">the exponent article</a>. The eigenvalue is computed from the certified approximation, and its accuracy is that of the estimates.</p>
<p>The theorem is stated here in the form in which it is used in this wiki, namely existence at a parameter value and one-dimensional instability. The papers state their results with the explicit constants and the norms in which they are measured; those constants are the substance of the proof and are not reproduced here.</p>

## Idea of the proof {#section-idea}

<p>The argument is a posteriori: it starts from a candidate and certifies it.</p>
<p><em>The approximate fixed point.</em> The Taylor coefficients of $\mathcal V_bV$ are polynomials, or convergent series, in the coefficients of $V$ and in the moments of the tilted Gaussian measure at $b=0$; truncating the system at order $N$ and solving the truncated system numerically gives a vector $(v_1,\ldots,v_N)$ which is an approximate solution. The truncation is only a device for producing the candidate, not a step in the proof.</p>
<p><em>The linearisation.</em> The derivative of $\mathcal V_b$ at the candidate has an explicit form: differentiating the defining integral gives the expectation, under the tilted Gaussian measure with the candidate as potential, of a polynomial in the child spins, and therefore an integral operator whose kernel is a Gaussian density times a polynomial. Its spectrum on the space of even analytic potentials is analysed directly, and the estimates give bounds on the inverse on the complement of the leading eigenspace.</p>
<p><em>The contraction.</em> With the inverse in hand, Newton's equation for the fixed-point problem becomes a fixed-point equation for the correction, whose right-hand side is of second order in the correction. If the residual of the candidate is smaller than a computable bound and the second derivative of the map is bounded on the ball of radius $\rho$, then the correction map contracts that ball into itself, and the contraction principle gives a true fixed point inside it. Both bounds are numerical, and both are verified.</p>
<p><em>The verification.</em> The estimates are finite-dimensional inequalities in the Taylor coefficients. They are checked numerically, with the rounding controlled, and the result is conditional on that check. This is the sense in which the proof is computer-assisted: no step is heuristic, but the constants are produced by computation rather than by hand.</p>
<p>Nothing in the argument needs a small parameter, and nothing is truncated in the proof. That is what distinguishes the result from the epsilon expansion: the expansion proves existence in a neighbourhood of the marginal exponent for a range of parameters, while the certified computation proves existence at one point of the parameter space with explicit bounds.</p>

## Consequences and applications {#section-consequences}

<p><em>The exponents of the scalar model.</em> Given the certified fixed point, the exponents follow from the linearisation: $\nu$ from the leading eigenvalue, the rest from the dictionary, with the growth exponent $\kappa=\alpha$ fixed by the autonomy of the recursion as in <a href="/articles/critical-exponents-from-rg/#section-growth">the growth theorem</a>. The accuracy of the exponents is limited by the accuracy of the certification.</p>

<p><em>A benchmark for expansions.</em> The certified values are a check on the epsilon expansion and on numerical truncations: a truncation that predicts the fixed point at a different place, or a different $\nu$, is wrong by more than the certified error.</p>

<p><em>The Dyson-Baker variant.</em> The block structure of the Dyson-Baker model comes from a piecewise linear expanding map of the interval rather than from the ultrametric blocks of <a href="/articles/hierarchical-lattice/">the lattice article</a>, and the renormalisation map is of the same type with different constants. The third paper proves the corresponding fixed point there [@koch-wittwer-1994], which shows that the existence is a property of the class of maps rather than of one arithmetic choice of the lattice.</p>

## Examples and non-examples {#section-examples}

<p><em>The quadratic fixed point.</em> For $m$ children and coupling $b$ there is exactly one quadratic fixed point, of curvature $(\mu-b(m-1))/m$ in the flow of the truncations article; it is the Gaussian theory, and it is stable below the marginal exponent and unstable above it.</p>

<p><em>Non-example: a truncated system.</em> Solving the system truncated at order $N$ gives an approximate fixed point but not a fixed point; the error is of the order of the first omitted coefficient, which is not small for the truncations of <a href="/articles/hierarchical-phi4-truncations/#section-truncations">the truncations article</a> unless $N$ is large.</p>

<p><em>Non-example: the epsilon expansion at a distance.</em> The expansion is organised in powers of $\alpha-d/2$ and its radius of convergence is not known; it certifies nothing at a fixed positive distance from the marginal exponent.</p>

## Variants and generalisations {#section-variants}

<p><em>Other block structures.</em> Any block structure whose decimation is an integral operator of the same type admits the same treatment, and the Dyson-Baker case is one instance. The hierarchical lattice is the case in which the operator is simplest.</p>

<p><em>Component count.</em> The scalar case is the one treated; for $r$ components the potential is radial and the space is a space of functions of one variable, so the analysis is formally the same, but the marginal angular directions of <a href="/articles/hierarchical-vector-models/">the vector article</a> have to be separated out.</p>

<p><em>The Euclidean counterpart.</em> A certified fixed point at a parameter value is the model for the requirement that a Euclidean construction produce a fixed point with explicit bounds; Abdesselam's trajectory between fixed points is the corresponding global object, and is described in <a href="/articles/abdesselam-global-trajectory/">the next article</a>.</p>

## History and attribution {#section-history}

<p>Koch and Wittwer proved the existence of the nontrivial fixed point for hierarchical scalar lattice field theories in 1986 [@koch-wittwer-1986], with the functional-analytic framework in the paper of 1991 [@koch-wittwer-1991] and the Dyson-Baker case in 1994 [@koch-wittwer-1994]. The general existence theorem for the class of measures is Bleher and Sinai's [@bleher-sinai-1975], and the local picture around the marginal exponent, with the epsilon expansion and the unstable manifold, is Gawedzki and Kupiainen's [@gawedzki-kupiainen-1983]. The article records the statements and the shape of the argument; the estimates themselves are in the papers.</p>

## References {#section-references}

<ul>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian fixed points of the block spin transformation. Hierarchical model approximation, <em>Comm. Math. Phys.</em> 89 (1983), 191&ndash;220.</li>
<li>H. Koch and P. Wittwer, A non-Gaussian renormalization group fixed point for hierarchical scalar lattice field theories, <em>Comm. Math. Phys.</em> 106 (1986), 495&ndash;532.</li>
<li>H. Koch and P. Wittwer, On the renormalization group transformation for scalar hierarchical models, <em>Comm. Math. Phys.</em> 138 (1991), 537&ndash;568.</li>
<li>H. Koch and P. Wittwer, A nontrivial renormalization group fixed point for the Dyson-Baker hierarchical model, <em>Comm. Math. Phys.</em> 164 (1994), 627&ndash;647.</li>
</ul>
