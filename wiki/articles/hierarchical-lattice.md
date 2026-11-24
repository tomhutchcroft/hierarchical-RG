---
{
  "id": "hierarchical-lattice",
  "title": "The hierarchical lattice",
  "subtitle": "An ultrametric group whose blocks fall into L^d congruent children.",
  "kind": "model",
  "category": "Hierarchical models",
  "summary": "The hierarchical lattice is the direct sum of countably many copies of (Z/LZ)^d, with an ultrametric whose balls have exactly L^(dn) points. Each ball splits into L^d congruent children, every pair of vertices in different children of a ball sits at the top distance of that ball, and power kernels are summable exactly when their exponent exceeds the dimension. These three facts are what make block decimation close on one-variable laws.",
  "context": [
    "Integers $L\\geq2$ and $d\\geq1$, and $m=L^d$.",
    "Vertices have finite support; the full product is a compact group, not this lattice.",
    "The kernel exponent is $\\alpha$, and the coupling at level $k$ is $J_k=JL^{-(d+\\alpha)k}$."
  ],
  "related": [
    "hierarchical-gibbs-measure",
    "renormalisation-group-map",
    "hierarchical-and-euclidean-rg"
  ],
  "sourceIds": ["dyson-1969", "bleher-sinai-1973", "bauerschmidt-brydges-slade-2019"],
  "aliases": [
    "hierarchical lattice",
    "ultrametric lattice",
    "Dyson lattice",
    "block decomposition",
    "shell count"
  ]
}
---

<p>The <em>hierarchical lattice</em> $\mathbb H^d_L$ is the abelian group of finite sequences with entries in $(\mathbb Z/L\mathbb Z)^d$, carrying the ultrametric in which two vertices are at distance $L^k$ when the last coordinate at which they differ is the $k$-th. Its balls are nested subgroups, of exactly $L^{dn}$ vertices at radius $L^n$, and each ball splits into $L^d$ congruent children. Every pair of vertices in different children of a ball lies at the top distance of that ball, so a coupling that charges each pair according to its distance charges all pairs between two children at one rate, which depends only on the two block sums. This is the structure that makes <a href="/articles/renormalisation-group-map/">block decimation</a> an exact operation on a single variable, and it is why the model appears throughout the rigorous theory of the renormalisation group [@bauerschmidt-brydges-slade-2019].</p>

<p>The lattice was introduced by Dyson (1969) as a one-dimensional model with long-range couplings in which a phase transition can be proved [@dyson-1969], and the group-theoretic description used here, with balls as cosets of nested subgroups, is the form in which the <a href="/articles/bleher-sinai-fixed-point/">renormalisation group</a> is usually set up [@bleher-sinai-1973]. A power kernel $\lVert x\rVert^{-d-\alpha}$ is summable exactly when $\alpha&gt;0$, so the model with such a kernel is a <a href="/articles/hierarchical-gibbs-measure/">long-range spin system</a> with a finite interaction range in the only sense that matters: the total intensity at each vertex is finite.</p>

<p>Two conventions are worth fixing at the outset. The dimension enters the lattice only through the block volume $m=L^d$ and the decay ratio $\lambda=L^{d+\alpha}=mL^{\alpha}$; any integer $m\geq2$ and any ratio $\lambda&gt;m$ arise from some pair $(d,\alpha)$ once a scale $L$ is chosen. And the lattice is a group, so distances are translation invariant and every vertex looks like the origin.</p>

## Definitions and setting {#section-definitions}

<p>Fix integers $L\geq2$ and $d\geq1$ and write $m=L^d$ and $A=(\mathbb Z/L\mathbb Z)^d$, so that $\lvert A\rvert=m$. The vertex set is the direct sum</p>
<div class="math-display">$$\mathbb H^d_L=\bigoplus_{i\geq1}A=\bigl\{x=(x_1,x_2,\ldots):x_i\in A,\ x_i=0\text{ for all but finitely many }i\bigr\},$$</div>
<p>an abelian group under coordinatewise addition. Write $0$ for its identity.</p>
<a id="tag-L4Q7" data-assertion="definition" data-title="Level, distance and hierarchical balls"></a>
<p>For $x\neq0$ put $\operatorname{lev}(x)=\max\{i\geq1:x_i\neq0\}$ and $\operatorname{lev}(0)=0$, and define the <em>hierarchical distance</em></p>
<div class="math-display">$$\lVert x\rVert=L^{\operatorname{lev}(x)}\quad(x\neq0),\qquad \lVert0\rVert=0,$$</div>
<p>and $\lVert x-y\rVert$ for a pair of vertices. For $n\geq0$ the <em>level-$n$ block</em> at the origin is $\Lambda_n=\{x:\operatorname{lev}(x)\leq n\}$, the set of sequences vanishing above coordinate $n$, and the level-$n$ block at $x$ is the coset $x+\Lambda_n$. A vertex of level $n$ is one at distance $L^n$ from the origin; the <em>shell</em> at level $n$ is $\Lambda_n\setminus\Lambda_{n-1}$.</p>
<p>Here $\Lambda_0=\{0\}$, and the first nontrivial displacement available on $\mathbb H^d_L$ has length $L$. The notation $\langle x\rangle=\max\{1,\lVert x\rVert\}$ regularises the distance at the origin and is used whenever a formula has to be read at $x=0$.</p>

## Blocks, shells and the triangle inequality {#section-blocks}

<a id="tag-M8ZR" data-assertion="proposition" data-title="Ultrametricity, nested blocks and exact shell counts"></a>
<p>The level is subadditive under addition, $\operatorname{lev}(u+v)\leq\max\{\operatorname{lev}(u),\operatorname{lev}(v)\}$, and invariant under negation. Consequently $\lVert x-z\rVert\leq\max\{\lVert x-y\rVert,\lVert y-z\rVert\}$ for all $x,y,z$, the distance is symmetric and translation invariant, and $\lVert x\rVert=0$ only at $x=0$. Each $\Lambda_n$ is a subgroup, the blocks of a fixed level are its cosets, and two blocks are disjoint or one contains the other. Finally</p>
<div class="math-display">$$\lvert\Lambda_n\rvert=L^{dn}=m^n,\qquad \bigl\lvert\{x:\operatorname{lev}(x)=n\}\bigr\rvert=L^{dn}-L^{d(n-1)}\quad(n\geq1).$$</div>
:::details Proof of ultrametricity and the counts
<p>Let $u,v\in\mathbb H^d_L$ and $k=\max\{\operatorname{lev}(u),\operatorname{lev}(v)\}$. Both vanish above coordinate $k$, hence so does $u+v$, and $\operatorname{lev}(u+v)\leq k$; the coordinates of $-u$ are the negatives of those of $u$, so $\operatorname{lev}(-u)=\operatorname{lev}(u)$. Taking $u=x-y$ and $v=y-z$ gives the strong triangle inequality. Symmetry is $\operatorname{lev}(y-x)=\operatorname{lev}(x-y)$, translation invariance is $\operatorname{lev}((x+w)-(y+w))=\operatorname{lev}(x-y)$, and positive definiteness is the definition together with $\operatorname{lev}(x)\geq1$ for $x\neq0$.</p>
<p>The condition $\operatorname{lev}(z)\leq n$ is exactly $z_i=0$ for $i&gt;n$, and the set of such $z$ is closed under addition and negation, so $\Lambda_n$ is a subgroup; it is contained in $\Lambda_{n+1}$. A translate of a subgroup is a coset, and two cosets of the same subgroup coincide or are disjoint; nested subgroups give the same statement for blocks of different levels.</p>
<p>Restriction to the first $n$ coordinates maps $\Lambda_n$ bijectively onto $A^n$, with inverse given by appending zeros, so $\lvert\Lambda_n\rvert=\lvert A\rvert^n=m^n=L^{dn}$. The shell at level $n$ is $\Lambda_n\setminus\Lambda_{n-1}$ and the two blocks are nested, so its cardinality is the difference.</p>
:::
<p>Every vertex of $\Lambda_n$ is within distance $L^n$ of every other: a pair of points of $\Lambda_n$ differs only in coordinates at most $n$, so its level is at most $n$. This is the sense in which a block has no boundary: the diameter of $\Lambda_n$ is exactly the radius at which it first appears.</p>

## The child decomposition {#section-children}

<p>The single structural fact behind the exactness of decimation is that a block is the disjoint union of congruent children, and that the interaction between two children is a function of their total spins alone. For $a\in A$ and $n\geq1$ let $e_n(a)$ be the vertex whose $n$-th coordinate is $a$ and whose other coordinates vanish.</p>
<a id="tag-J2WK" data-assertion="theorem" data-title="Children of a block and the top level between them"></a>
<p>For $n\geq1$,</p>
<div class="math-display">$$\Lambda_n=\bigsqcup_{a\in A}\bigl(e_n(a)+\Lambda_{n-1}\bigr),$$</div>
<p>the pieces are the blocks of radius $L^{n-1}$ contained in $\Lambda_n$, each is a translate of $\Lambda_{n-1}$, and $e_n(a)$ has level $n$. If $x$ and $y$ lie in different pieces then $\lVert x-y\rVert=L^n$, whatever the distance between the two pieces as sets.</p>
:::details Proof of the child decomposition
<p>Let $z\in\Lambda_n$ and $a=z_n$. Then $z-e_n(a)$ has vanishing $n$-th coordinate and vanishes above $n$ because $z$ does, so $z-e_n(a)\in\Lambda_{n-1}$ and $z\in e_n(a)+\Lambda_{n-1}$. If $z\in e_n(a)+\Lambda_{n-1}$ then $z_n=a$, so the pieces for distinct $a$ are disjoint, which gives the union. Since $e_n(a)\in\Lambda_n$ and $\Lambda_n$ is a subgroup, $e_n(a)+\Lambda_{n-1}$ is a coset of $\Lambda_{n-1}$ inside $\Lambda_n$; the blocks of radius $L^{n-1}$ are exactly the cosets of $\Lambda_{n-1}$, and by the previous section each is contained in or disjoint from $\Lambda_n$. Finally $\operatorname{lev}(e_n(a))=n$ because the $n$-th coordinate is the last nonzero one.</p>
<p>For the last claim let $x=e_n(a)+u$ and $y=e_n(b)+v$ with $u,v\in\Lambda_{n-1}$ and $a\neq b$. Then $x-y=e_n(a-b)+(u-v)$, and $u-v\in\Lambda_{n-1}$ vanishes at coordinate $n$, so the $n$-th coordinate of $x-y$ is $a-b\neq0$ and no coordinate above $n$ is nonzero. Hence $\operatorname{lev}(x-y)=n$.</p>
:::
<p>The count is consistent: $\lvert A\rvert\cdot\lvert\Lambda_{n-1}\rvert=m\cdot m^{n-1}=m^n=\lvert\Lambda_n\rvert$. The theorem is what a decimation step needs, since a pair chosen from two different children of $\Lambda_n$ has the same level $n$ whatever the vertices, so a kernel that is constant on levels assigns the same intensity to all $m(m-1)/2$ pairs of distinct children, and the energy of the block depends on the children only through their sums.</p>

## Power kernels {#section-kernels}

<p>A kernel is a nonnegative symmetric function $J:\mathbb H^d_L\to[0,\infty)$ with $J(0)$ irrelevant for the graph. The power kernel at exponent $\alpha$ is $J(x)=\lVert x\rVert^{-d-\alpha}$ off the origin, and its level-$k$ value is $J_k=L^{-(d+\alpha)k}$, so it charges each pair of the level-$k$ shell by one constant.</p>
<a id="tag-Q6HD" data-assertion="proposition" data-title="Summability of power kernels and the exact row sum"></a>
<p>For real $\alpha$ and $J\geq0$,</p>
<div class="math-display">$$\sum_{x\neq0}\lVert x\rVert^{-d-\alpha}<\infty\quad\Longleftrightarrow\quad\alpha>0,$$</div>
<p>and for $\alpha&gt;0$ the row sum of the kernel $J\lVert x\rVert^{-d-\alpha}$ is</p>
<div class="math-display">$$\sum_{x\neq0}J\lVert x\rVert^{-d-\alpha}=(1-L^{-d})\,J\,\frac{L^{-\alpha}}{1-L^{-\alpha}}.$$</div>
:::details Proof of the summability criterion
<p>The shell at level $k$ has $(1-L^{-d})L^{dk}=L^{dk}-L^{d(k-1)}$ vertices, all at distance $L^k$, so the sum is $(1-L^{-d})\sum_{k\geq1}L^{dk}L^{-(d+\alpha)k}=(1-L^{-d})\sum_{k\geq1}L^{-\alpha k}$. All terms are nonnegative, so the sum may be regrouped. The geometric series $\sum_{k\geq1}L^{-\alpha k}$ converges exactly when $L^{-\alpha}&lt;1$, that is when $\alpha&gt;0$, and then equals $L^{-\alpha}/(1-L^{-\alpha})$.</p>
:::
<p>Since $\alpha&gt;0$, the kernel is integrable and the intensity of the interaction at a vertex is finite; this is the sense in which the model is nearest-neighbour-like despite its long range. At $\alpha=0$ each shell contributes the same mass $1-L^{-d}$ and the sum diverges; for $\alpha&lt;0$ the mass of the shells grows.</p>

## Examples and non-examples {#section-examples}

<p><em>The level-2 block.</em> Take $d=1$, $L=2$, so that $m=2$ and $\Lambda_2$ has four vertices. With $e_2(1)$ the sequence $(0,1,0,\ldots)$ and $e_1(1)=(1,0,\ldots)$, the children of $\Lambda_2$ are $\{0,e_1(1)\}$ and $\{e_2(1),e_1(1)+e_2(1)\}$, each a translate of $\Lambda_1$; the four pairs between the children have distance $4$, and the two pairs inside them have distance $2$. A coupling that charges pairs by distance therefore charges the within-child pairs at $J_1$ and the between-child pairs at $J_2$, so the block splits into two interacting copies of itself.</p>

<p><em>The geometric kernel.</em> The kernel $J(x)=Cr^{\operatorname{lev}(x)}$ on $\mathbb H^d_L$, with $C\geq0$ and $0\leq r&lt;L^{-d}$, is summable, with row sum $C(1-L^{-d})r/(1-L^dr)$. This family is closed under rescalings of the level, and it contains the power kernel at $r=L^{-(d+\alpha)}$; a Gaussian model with such a kernel is exactly solvable, which is the subject of the <a href="/articles/gaussian-renormalisation-group/">Gaussian article</a>.</p>

<p><em>A pair-dependent kernel.</em> If $J(x,y)$ depends on the pair and not on the level, as for instance a kernel that charges only pairs inside a fixed family of blocks, then the children of a block are still congruent but the energy of the block is no longer a function of the child sums. The decimation identity of <a href="/articles/hierarchical-gibbs-measure/">the next article</a> is specific to kernels that are constant on levels.</p>

<p><em>The borderline exponent.</em> At $\alpha=0$ the power kernel is not summable and the corresponding percolation model is $\beta_c=0$ for every $\beta&gt;0$: every vertex has infinitely many neighbours of infinite total intensity. The condition $\alpha&gt;0$ is therefore not a technical convenience in the hypotheses below.</p>

<p><em>The full product.</em> The compact group $\prod_{i\geq1}A$, with the same definition of level for pairs differing in finitely many coordinates, is not $\mathbb H^d_L$: it is uncountable, and the distance between two of its points can be zero even when the points differ, at coordinates tending to infinity. All statements here concern the direct sum.</p>

## Variants and generalisations {#section-variants}

<p><em>Dimension as bookkeeping.</em> Only $m=L^d$ and the ratios $J_k/J_{k+1}=L^{d+\alpha}$ enter the definitions, so a model is parametrised by the integer $m\geq2$, the ratio $\lambda&gt;m$ and the amplitude $J$, and the pair $(d,\alpha)$ records a choice of scale: $d=\log m/\log L$ and $\alpha=\log(\lambda/m)/\log L$. Fixing integer $d$ costs nothing.</p>
<a id="tag-W9TF" data-assertion="proposition" data-title="The hierarchical lattices of different dimensions are the same group"></a>
<p>Let $d\geq1$ and $L\geq2$, and let $\psi:(\mathbb Z/L\mathbb Z)^d\to\mathbb Z/L^d\mathbb Z$ be a bijection taking $0$ to $0$. Applying $\psi$ in every coordinate gives a group isomorphism $\Psi:\mathbb H^d_L\to\mathbb H^1_{L^d}$ with</p>
<div class="math-display">$$\lVert\Psi(x)-\Psi(y)\rVert_{\mathbb H^1_{L^d}}=\lVert x-y\rVert_{\mathbb H^d_L}^{\,d}.$$</div>
:::details Proof of the distance identity
<p>The map $\psi(a)=\sum_{j=1}^da_jL^{j-1}$ is a bijection of the underlying sets fixing $0$, and applying it coordinatewise is a bijection of the direct sums. A vertex of $\mathbb H^d_L$ has level $k$ exactly when its last nonzero entry is the $k$-th, which the coordinatewise application preserves because level is read off the index and not the entry; a vertex of $\mathbb H^1_{L^d}$ at level $k$ has distance $(L^d)^k=L^{dk}$ from the origin and distance $L^k$ in the other lattice. Group structure is not needed for the distance identity, and it holds for $\Psi$ applied to a difference since the map is applied entrywise.</p>
:::
<p>Under this identification the power kernel $\lVert x\rVert^{-d-\alpha}$ on $\mathbb H^d_L$ becomes $\lVert y\rVert^{-1-\alpha/d}$ on $\mathbb H^1_{L^d}$, so a statement about power kernels at every exponent on the one-dimensional lattice covers every dimension. The dimensional parameter is thus the ratio $\alpha/d$, which is why exponents in this model are functions of $\alpha/d$ and of the ratio of the kernel to the scale, and not of $d$ alone.</p>

<p><em>Other coefficient groups.</em> Nothing in the definitions uses finiteness of $A$ except the counts. With $A=\mathbb Z^d$ the level-one block is infinite, the shells are infinite, the summability criterion changes, and the model is a long-range system on a tree-like group; the child decomposition survives, the counting arguments do not.</p>

## History and attribution {#section-history}

<p>Dyson (1969) introduced the one-dimensional model with couplings decaying as a power and proved that a phase transition occurs for decay exponents between one and two [@dyson-1969]; the hierarchical approximation used there is the lattice above with $d=1$ and a coupling that is constant on the shells of the ultrametric. The group-theoretic description, in which blocks are cosets of nested subgroups with $L^d$ children each, is the form in which Bleher and Sinai set up the renormalisation transformation [@bleher-sinai-1973], and it is the presentation used in the modern development of the renormalisation group for lattice field theory [@bauerschmidt-brydges-slade-2019].</p>

<p>The counts of this article are elementary and appear in each of those sources; the statement that all pairs between two children of a block lie at the top level of that block is the property that distinguishes this lattice from a Euclidean block partition, where the interaction between two neighbouring blocks depends on the shape of their common boundary. The comparison is the subject of <a href="/articles/hierarchical-and-euclidean-rg/">Hierarchical and Euclidean renormalisation</a>.</p>

## References {#section-references}

<ul>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>R. Bauerschmidt, D. C. Brydges and G. Slade, <em>Introduction to a Renormalisation Group Method</em>, Lecture Notes in Mathematics 2242, Springer, 2019.</li>
<li>F. J. Dyson, Existence of a phase-transition in a one-dimensional Ising ferromagnet, <em>Comm. Math. Phys.</em> 12 (1969), 91&ndash;107.</li>
</ul>
