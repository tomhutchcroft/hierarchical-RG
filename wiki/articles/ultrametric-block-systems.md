---
{
  "id": "ultrametric-block-systems",
  "title": "Ultrametric block systems and the p-adic models",
  "subtitle": "What the recursion actually needs, and how little of it is specific to the hierarchical lattice.",
  "kind": "model",
  "category": "Hierarchical models",
  "summary": "The decimation recursion uses only a nested system of blocks with a constant number of children per block. Any ultrametric group with such a system carries the same model, the same map and the same exponents: the p-adic integers with their balls, the hierarchical lattice with its subgroups, and their variants. The child decomposition and the decimation identity are proved here in that generality, and the one place where the compact and discrete cases differ is isolated.",
  "context": [
    "An abelian group $G$ with a decreasing sequence of subgroups $G_0\\supset G_1\\supset\\cdots$ of finite index, constant branching $m=[G_n:G_{n+1}]\\geq2$.",
    "Blocks are cosets of the $G_n$; the level of a pair is the least $n$ with $x-y\\in G_n$; the coupling at level $k$ is $J_k=JL^{-(d+\\alpha)k}$.",
    "The group may be discrete (the hierarchical lattice) or compact (the p-adic integers), with counting or Haar measure respectively."
  ],
  "related": [
    "hierarchical-lattice",
    "hierarchical-gibbs-measure",
    "renormalisation-group-map",
    "hierarchical-and-euclidean-rg"
  ],
  "sourceIds": ["abdesselam-2018", "bleher-sinai-1973", "koval-meester-trapman-2012", "bauerschmidt-brydges-slade-2019"],
  "aliases": [
    "p-adic model",
    "ultrametric group",
    "block system",
    "p-adic integers",
    "hierarchical lattice generalisation"
  ]
}
---

<p>Every proof in this wiki about decimation uses exactly two facts: that the blocks of a fixed level are the cosets of a subgroup, and that each block has the same number $m$ of children. Nothing else about the <a href="/articles/hierarchical-lattice/">hierarchical lattice</a> is used: not the direct-sum construction, not countability, not the arithmetic of $(\mathbb Z/L\mathbb Z)^d$. This article states the construction for an arbitrary abelian group with a nested block system and proves the two structural results in that generality; the <a href="/articles/hierarchical-gibbs-measure/">decimation identity</a>, the <a href="/articles/renormalisation-group-map/">map</a> and the <a href="/articles/critical-exponents-from-rg/">exponent dictionary</a> then apply verbatim.</p>

<p>The standard compact example is the ring of <em>p-adic integers</em> $\mathbb Z_p$ with the balls of the p-adic metric, which are the cosets of $p^n\mathbb Z_p$: each ball has exactly $p$ children, at every scale, forever. The models on $\mathbb Z_p$ are used in the renormalisation-group approach to conformal field theory, where the exactness of the block structure is worth the loss of translation invariance in the Euclidean sense [@abdesselam-2018].</p>

<p>The one point at which the two settings differ is the meaning of the volume of a block: a coset of $\Lambda_n$ in the hierarchical lattice is a finite set and its volume is its cardinality, while a ball in $\mathbb Z_p$ is uncountable and its volume is its Haar measure. The recursion sees only the ratio of the volumes of a block and its child, which is $m$ in both cases, so the two models have the same renormalisation group.</p>

## Definitions and setting {#section-setting}

<a id="tag-U4PM" data-assertion="definition" data-title="Ultrametric block system and its levels"></a>
<p>Let $G$ be an abelian group and $G=G_0\supset G_1\supset G_2\supset\cdots$ a decreasing sequence of subgroups, each of finite index in $G$, with</p>
<div class="math-display">$$[G_n:G_{n+1}]=m\qquad\text{for every }n\geq0 .$$</div>
<p>The <em>level</em> of a pair $x\neq y$ is the least $n\geq1$ with $x-y\in G_n$, and $\operatorname{lev}(x)=0$ only for $x=0$. The <em>block</em> at $x$ of level $n$ is the coset $x+G_n$; the <em>children</em> of a block $x+G_n$ are its cosets of $G_{n+1}$. Vertices at level $n$ are those in $G_n\setminus G_{n-1}$, and the <em>shell</em> at level $n$ is $G_n\setminus G_{n-1}$.</p>
<p>Two examples carry the subject. For the <em>hierarchical lattice</em> $\mathbb H^d_L$ one takes $G_n=\Lambda_n$, the sequences supported on the first $n$ coordinates, and $m=L^d$; the blocks are finite and the volumes are cardinalities $m^n$. For the <em>p-adic integers</em> one takes $G=\mathbb Z_p$ and $G_n=p^n\mathbb Z_p$; then $[G_n:G_{n+1}]=p$, the blocks are the p-adic balls of radius $p^{-n}$, and the normalised Haar measure gives them volume $p^{-n}$. In both cases $G_n/G_{n+1}$ has $m$ elements and a block of level $n$ has $m^n$ children of level $0$.</p>
<p>A model on such a system is a spin system with coupling $J(x-y)=J_k$ for $\operatorname{lev}(x-y)=k$, exactly as in <a href="/articles/hierarchical-gibbs-measure/#section-model">the decimation article</a>; the prior is a fixed probability measure on the single-spin space, and the Gibbs measure on a block is normalised with counting measure or Haar measure according to which case one is in. When $G$ is uncountable, $\mathbb P_\beta$ is a measure on $S^{G}$ for a countable set $S$ of blocks; the statements below are about a block, which is a finite-index subgroup, and are unaffected.</p>

## The child decomposition in general {#section-children}

<p>The first structural fact was proved for the lattice in <a href="/articles/hierarchical-lattice/#section-children">the lattice article</a>. Its proof uses only the group axioms.</p>
<a id="tag-U7KQ" data-assertion="proposition" data-title="Cosets, children and the top level, in any block system"></a>
<p>Let $n\geq1$. The children of $G_n$ are the $m$ cosets of $G_{n+1}$ in $G_n$, they partition $G_n$, each is a translate of $G_{n+1}$, and if $x,y$ lie in different children of a block $B$ then $\operatorname{lev}(x-y)=\operatorname{lev}(B)$. The same holds with $G_n$ replaced by any coset of it.</p>
:::details Proof
<p>Since $G_{n+1}\subseteq G_n$ are subgroups, the cosets of $G_{n+1}$ inside $G_n$ are disjoint and their union is $G_n$; there are $[G_n:G_{n+1}]=m$ of them. A coset $g+G_{n+1}$ with $g\in G_n$ is a translate of $G_{n+1}$. If $x\in g+G_{n+1}$ and $y\in g'+G_{n+1}$ with $g\neq g'$ modulo $G_{n+1}$, then $x-y\in G_n$ because both terms lie in $G_n$, while $x-y\notin G_{n+1}$ because its class in $G_n/G_{n+1}$ is $g-g'\neq0$. Hence the least $k$ with $x-y\in G_k$ is exactly $n$. For a coset $z+G_n$ the same argument applies after translating both points by $-z$, and levels are translation invariant because $G_k$ is a subgroup.</p>
:::
<p>The proposition is what "the block has no boundary" means algebraically: any two vertices in different children of a block are at the top level of that block, whatever their distance, so a coupling that depends only on the level charges all of them the same rate. In $\mathbb Z_p$ this says that the two balls of radius $p^{-(n+1)}$ inside a ball of radius $p^{-n}$ are joined by edges of one intensity, even though the p-adic distance between a point near the middle of one and a point near the middle of the other is much smaller than $p^{-n}$ — the ultrametric makes every such pair equal.</p>

## The decimation identity in general {#section-decimation}

<a id="tag-U2NB" data-assertion="theorem" data-title="The decimation identity holds for every block system"></a>
<p>Let $B$ be a block of level $n$ with children $B_1,\ldots,B_m$, let $\mu_{n-1}$ be the law of the total spin of a block of level $n-1$ in the model with couplings $J_1,\ldots,J_{n-1}$ on that block, and let $Z_{n-1}$ be its partition function. Then</p>
<div class="math-display">$$Z_B=Z_{n-1}^{\,m}\int\exp\Bigl(\beta J_n\sum_{a&lt;a'}s_as_{a'}\Bigr)\prod_a\mu_{n-1}(ds_a),$$</div>
<p>and the law of the $m$-tuple of child spins is the normalised version. Consequently the block-spin law satisfies $\mu_n=\mathcal T_{\beta J_n}\mu_{n-1}$, with $\mathcal T_b$ as in <a href="/articles/renormalisation-group-map/#section-definition">the map article</a>, and the rescaled orbit is the orbit of $\mathcal R_{\theta_0,\beta J_1}$ with $\theta_0=\tfrac12(d+\alpha)$.</p>
:::details Proof
<p>By the proposition, the pairs of vertices inside $B$ split into the pairs inside the children, at levels at most $n-1$, and the pairs joining two different children, all at level $n$. The energy is therefore the sum of the children's energies plus $\beta J_n\sum_{a&lt;a'}S_aS_{a'}$, where $S_a$ is the total spin of the $a$-th child. A child is a translate of a level-$(n-1)$ block, and the Hamiltonian depends only on differences, so integrating the child at fixed $S_a$ gives $Z_{n-1}\mu_{n-1}(dS_a)$ — the additive constant in the couplings makes no difference. Multiplying over the children and integrating over the normalised measures gives the display. The rescaling step is the computation of the autonomous form, which uses only $2\theta_0=d+\alpha$ and the ratio $J_n/J_{n-1}$.</p>
:::
<p>Two remarks isolate what the generality does and does not buy. The identity needs the amount of branching to be constant: with $[G_n:G_{n+1}]=m_n$ varying, the tilt has $m_n$ children and the coupling ratio is unchanged, so the map is the same but the composition is no longer a power of one operator, and the exponents of the dictionary no longer follow from a single fixed point. And it needs the coupling to depend only on the level, which in the group setting is the statement that the interaction is invariant under the isometries that preserve the block structure.</p>

## The volume, and where the two cases differ {#section-volume}

<p>For the exponents, the volume of a block enters through the growth exponent $\kappa=2\theta_0-d$ and through the summability criterion. In the discrete case the volume of a level-$n$ block is $m^n$; in the compact case it is $\mu(G_n)=m^{-n}$ for the normalised Haar measure if the measure is chosen so that $\mu(G_0)=1$. The two are reciprocal, and the recipe is the same in both: the number of children is the ratio of the volumes of a block and of its child, and the shell at level $n$ has volume the difference.</p>
<p>Because of this, a percolation model on $\mathbb Z_p$ with a summable kernel behaves as follows: the number of open edges at a vertex is a sum of independent Bernoulli variables with summable probabilities, so it is finite almost surely, and every cluster is countable. The percolation thresholds and the two-point exponent are the same statements as on the hierarchical lattice, since they are statements about the block system.</p>

## Examples and non-examples {#section-examples}

<p><em>The p-adic integers.</em> Here $m=p$ for every $p$, so the branching is the prime and cannot be varied while keeping the ring: changing $m$ means changing the prime. The dimension is $d=1$ in the normalisation of this wiki, and the kernel exponent $\alpha$ is a free parameter; the models are the ones in Abdesselam's programme for conformal probability [@abdesselam-2018].</p>

<p><em>The hierarchical lattice.</em> Here $m=L^d$ and both the scale and the branching are free, which is why the model is used to draw phase diagrams in $(d,\alpha)$ rather than at one prime.</p>

<p><em>Subgroups with varying index.</em> Taking $G_n=p^{n^2}\mathbb Z_p$ gives $[G_n:G_{n+1}]=p^{2n+1}$, so the branching grows; the decimation identity still holds at each scale but the map at scale $n$ depends on $n$, and the model behaves as though the kernel exponent changed with scale. This is a useful non-example: it separates the part of the theory that needs constant branching from the part that does not.</p>

<p><em>Non-example: the regular tree.</em> A rooted tree with constant branching is not a group, and its "blocks" have no canonical translates: the children of a vertex are distinguishable by their position, and there is no isometry moving one to another while fixing the structure. The decimation identity holds for the spin model on the tree in the form of a cavity recursion, but the state is a distribution of cavity fields rather than a block spin, and the exponents are not those of a fixed point of a single map.</p>

<p><em>Non-example: $\mathbb R$ or $\mathbb Z$ with the usual metric.</em> There is no nested system of finite-index subgroups with constant branching, and the analogue of a block has a boundary of codimension one; this is the obstruction of <a href="/articles/hierarchical-and-euclidean-rg/#section-exactness">the comparison article</a> in its group-theoretic form.</p>

## Variants and generalisations {#section-variants}

<p><em>p-adic fields and finite extensions.</em> Replacing $\mathbb Z_p$ by a finite extension of $\mathbb Q_p$ changes the residue field and hence the branching, and multiplies the volume by the ramification index; the recursion is unchanged with the new $m$.</p>

<p><em>Products and sums.</em> A product of block systems is a block system with the product branching, which is how the hierarchical lattice is built from copies of $\mathbb Z/L\mathbb Z$; a direct sum of copies is the discrete case of the same construction.</p>

<p><em>Vector and percolation models.</em> Nothing in the two proofs refers to the single-spin space, so the <a href="/articles/hierarchical-vector-models/">vector models</a> and <a href="/articles/hierarchical-percolation-rg/">percolation</a> transfer as well, with the branching $m$ replacing $L^d$ throughout.</p>

## History and attribution {#section-history}

<p>The hierarchical model of Bleher and Sinai was formulated on the lattice of the <a href="/articles/hierarchical-lattice/">first article</a>, but their transformation uses only the block structure, as the proof above makes explicit [@bleher-sinai-1973]. The p-adic and ultrametric versions, and their use as a route to a three-dimensional conformal field theory, are developed by Abdesselam [@abdesselam-2018]. The percolation model on the hierarchical lattice is that of Koval, Meester and Trapman [@koval-meester-trapman-2012]; the transfer to an arbitrary block system is the content of this article and is not claimed in those sources. The general framework in which the block structure is one of the data of a renormalisation-group problem is the one of Bauerschmidt, Brydges and Slade [@bauerschmidt-brydges-slade-2019].</p>

## References {#section-references}

<ul>
<li>A. Abdesselam, Towards three-dimensional conformal probability, <em>p-Adic Numbers Ultrametric Anal. Appl.</em> 10 (2018), 233&ndash;252.</li>
<li>R. Bauerschmidt, D. C. Brydges and G. Slade, <em>Introduction to a Renormalisation Group Method</em>, Lecture Notes in Mathematics 2242, Springer, 2019.</li>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>V. Koval, R. Meester and P. Trapman, Long-range percolation on the hierarchical lattice, <em>Electron. J. Probab.</em> 17 (2012), no. 57.</li>
</ul>
