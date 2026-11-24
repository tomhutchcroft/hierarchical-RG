---
{
  "id": "hierarchical-symmetries",
  "title": "The isometries of the hierarchical lattice",
  "subtitle": "Why any two pairs at the same level are the same pair, and why block sums of a block are exchangeable.",
  "kind": "theorem",
  "category": "Hierarchical models",
  "summary": "Translations and coordinate-wise bijections are isometries of the hierarchical lattice, and together they act transitively on ordered pairs at each level. Three statements that other articles use as \"by symmetry\" follow: a radial kernel gives a radial two-point function, the block sums of a block are exchangeable, and conditional expectations given the block sums are constant on the vertices of a child. A bijection that preserves the level of every vertex need not be an isometry, so the criterion has content.",
  "context": [
    "Integers $L\\geq2$, $d\\geq1$, $A=(\\mathbb Z/L\\mathbb Z)^d$, $\\mathbb H^d_L=\\bigoplus_{i\\geq1}A$; $\\operatorname{lev}$ and $\\lVert\\cdot\\rVert$ as in the lattice article.",
    "An isometry is a bijection of $\\mathbb H^d_L$ preserving $\\lVert x-y\\rVert$ for all pairs; it need not be a group homomorphism.",
    "The model is the hierarchical spin system with couplings depending on the level only, free boundary conditions on a block."
  ],
  "related": [
    "hierarchical-lattice",
    "hierarchical-gibbs-measure",
    "gaussian-renormalisation-group",
    "hierarchical-percolation-rg",
    "hierarchical-vector-models"
  ],
  "sourceIds": ["hutchcroft-hierarchical-2021", "bleher-sinai-1973", "abdesselam-2018"],
  "aliases": [
    "isometry group",
    "level isometry",
    "symmetry",
    "exchangeability",
    "transitivity"
  ]
}
---

<p>Five articles in this wiki reason "by symmetry", and this article supplies the symmetry. The statements are that the two-point function of a <a href="/articles/hierarchical-lattice/">radial kernel</a> depends only on the distance; that the block sums of the children of a block are exchangeable; and that a conditional expectation given those block sums is constant over the vertices of a child. Each is true, and each follows from the same two facts: translations are isometries, and so are bijections that act on each coordinate separately. Together they move any ordered pair of vertices at a given level onto any other such pair.</p>

<p>The last of the three is the one that does real work. In the <a href="/articles/gaussian-renormalisation-group/#section-two-point">Gaussian two-point computation</a> the conditional expectation of a single spin given the block sums is replaced by the block sum divided by the size of the block; in <a href="/articles/hierarchical-percolation-rg/#section-two-point">the percolation article</a> the level isometries convert an averaged bound into a pointwise one; and in <a href="/articles/hierarchical-vector-models/#section-decimation">the vector model</a> it is exchangeability of the child sums that reduces the recursion to the law of one block sum, with all components moving together. Without a transitivity statement each of those steps is an assertion about a picture.</p>

<p>One caution organises the proofs. Preserving the <em>level of every vertex</em> is strictly weaker than being an isometry: on a block of eight vertices a transposition of two vertices of level three preserves all vertex levels and changes the level of a pair. The example is given below, and it is the reason the theorem is about pairs.</p>

## Definitions and setting {#section-setting}

<a id="tag-H8SN" data-assertion="definition" data-title="Isometries of the hierarchical lattice"></a>
<p>A bijection $\phi:\mathbb H^d_L\to\mathbb H^d_L$ is an <em>isometry</em> if $\lVert\phi(x)-\phi(y)\rVert=\lVert x-y\rVert$ for all $x,y$, equivalently if $\operatorname{lev}(\phi(x)-\phi(y))=\operatorname{lev}(x-y)$. Write $\operatorname{Isom}$ for the set of isometries; it is a group under composition, and it contains the translations $\tau_v(x)=x+v$ for $v\in\mathbb H^d_L$.</p>
<p>For $a\in A$ let $\psi_a$ be the map that acts on each coordinate separately by a bijection of $A$: if $\sigma=(\sigma_1,\sigma_2,\ldots)$ is a sequence of bijections of $A$, then $\psi_\sigma(x)^{(i)}=\sigma_i(x^{(i)})$ for every $i$. These are the <em>coordinate-wise bijections</em>.</p>

## Two families of isometries {#section-isometries}

<a id="tag-H3WQ" data-assertion="theorem" data-title="Translations and coordinate-wise bijections are isometries, and act transitively on levels"></a>
<p>Translations are isometries, and so is every coordinate-wise bijection. Consequently, for each $n\geq0$ and every pair of ordered pairs $(x,y)$, $(x',y')$ with $\operatorname{lev}(y-x)=\operatorname{lev}(y'-x')=n$, there is an isometry $\phi$ with $\phi(x)=x'$ and $\phi(y)=y'$.</p>
:::details Proof
<p>A translation satisfies $\operatorname{lev}((x+v)-(y+v))=\operatorname{lev}(x-y)$ because levels of differences are translation invariant, which was proved in <a href="/articles/hierarchical-lattice/#section-blocks">the lattice article</a>.</p>
<p>For a coordinate-wise bijection, the coordinates at which $\psi_\sigma(x)$ and $\psi_\sigma(y)$ differ are exactly the coordinates at which $x$ and $y$ differ: if $x^{(i)}\neq y^{(i)}$ then $\sigma_i(x^{(i)})\neq\sigma_i(y^{(i)})$ because $\sigma_i$ is injective, and if $x^{(i)}=y^{(i)}$ then the images are equal. The set of indices at which two vertices differ is therefore preserved, so its maximum is preserved, which is the level.</p>
<p>For transitivity, let $x,y$ have $y-x=z$ of level $n$, and let $x',y'$ have $y'-x'=z'$ of level $n$. Translate by $-x$: the pair becomes $(0,z)$. By the previous paragraph, choose bijections $\sigma_i$ of $A$ with $\sigma_i(z^{(i)})=z'^{(i)}$ for $i\leq n$ and arbitrary for $i&gt;n$ (possible because $A$ is a set and $\sigma_i$ is only required to take one prescribed value); the corresponding coordinate-wise bijection fixes $0$ and sends $z$ to $z'$. Composing with the translation by $x'$ gives an isometry taking $(x,y)$ to $(x',y')$.</p>
:::
<p>The proof uses no structure of $A$ beyond its cardinality, so the statement holds for the coefficient group $\mathbb Z^d$ as well, where the lattice is the direct sum of copies of $\mathbb Z^d$: the levels are unaffected.</p>

## Consequences that were being assumed {#section-consequences}

<a id="tag-H6LV" data-assertion="corollary" data-title="Radial two-point functions, exchangeable block sums, and conditional expectations on a child"></a>
<p>Let the kernel depend only on the level, and let the model be the hierarchical spin system on a block with free boundary.</p>
<p>(i) <em>Radiality.</em> For the model on $\mathbb H^d_L$, the two-point function satisfies $\tau(x,y)=\tau(0,y-x)$ and depends only on $\operatorname{lev}(y-x)$.</p>
<p>(ii) <em>Exchangeability of child sums.</em> In the model on $\Lambda_N$, the $m$-tuple of block sums $(S_a)$ of the children of $\Lambda_N$ is exchangeable, and so is the corresponding tuple for the children of any block.</p>
<p>(iii) <em>Constancy on a child.</em> For $x,y$ in the same child of a block of level $n$, and for any function $F$ of the child sums, $\mathbb E[\sigma_xF]=\mathbb E[\sigma_yF]$ and $\mathbb E[\sigma_x\mid(S_a)]$ takes the same value at $x$ and $y$.</p>
:::details Proof
<p>An isometry preserving the level of every difference preserves the Hamiltonian, because the Hamiltonian is a sum of couplings that depend only on the level; and it preserves the prior, which is a product. Hence it preserves the Gibbs measure, and expectations of functions of the configuration composed with it are unchanged. This is the mechanism of all three statements.</p>
<p>(i) Given $x,y$ with $z=y-x$ of level $n$, the theorem gives an isometry fixing $0$ and sending $z$ to any prescribed vertex of level $n$; the pair $(x,y)$ is sent to $(0,w)$ with $w$ of level $n$, and $\tau$ is preserved. So $\tau(x,y)$ depends only on $n$ and equals $\tau(0,w)$ for every $w$ at that level.</p>
<p>(ii) Translation by any $v\in\Lambda_N$ preserves $\Lambda_N$, preserves the Hamiltonian (levels are translation invariant) and permutes the children, since the children are the cosets of $\Lambda_{N-1}$ and $v+\cdot$ is a bijection of the set of cosets. For any two children $B,B'$ choose $v\in B-B'$; then the translation by $v$ maps $B'$ to $B$ and permutes the others, and it preserves the law. Iterating gives exchangeability of the tuple.</p>
<p>(iii) Translation by any $v\in\Lambda_{n-1}$ maps each child of a level-$n$ block to itself — the children are cosets of $\Lambda_{n-1}$ — so it fixes every child sum, and it is an isometry, so it preserves the law. Any two vertices of a child differ by an element of $\Lambda_{n-1}$, so the transitivity of these translations inside the child gives the first identity; the second follows by taking $F$ to run over the generating functions of the conditional law, or directly from the definition of conditional expectation.</p>
:::
<p>Statement (iii) is exactly what licenses the step "$\mathbb E[\sigma_x\mid(S_a)]=S_a/\lvert\Lambda_{n-1}\rvert$" in the Gaussian two-point computation, and its analogues elsewhere. Note that it is a statement about conditional expectations given the sums, not about the conditional law being uniform: the conditional law of the spins in a child given their sum is not uniform, but its first moment is.</p>

## Examples and non-examples {#section-examples}

<p><em>Translations alone are not enough.</em> A translation preserves the displacement $y-x$, so it moves a pair only within its own class and cannot relate two different pairs at the same level. The coordinate-wise bijections supply the rest, and they are generally not translations: in $\Lambda_2$ with $L=3$, $d=1$, the map sending $(x_1,x_2)$ to $(2x_1,x_2)$ is a coordinate-wise bijection fixing $0$, and it is not a translation, since it exchanges $(1,0)$ and $(2,0)$ while a translation fixing $0$ is the identity.</p>

<p><em>A level-preserving bijection that is not an isometry.</em> Take $d=1$, $L=2$ and the block $\Lambda_3$ of eight vertices, written as triples. Transpose $(0,1,1)$ and $(1,0,1)$ and fix everything else. Both moved vertices have level three, and every other vertex is fixed, so the level of every vertex is preserved. But the pair $\{(0,0,1),(0,1,1)\}$ has level two, being a pair differing in coordinate two, while its image $\{(0,0,1),(1,0,1)\}$ has level one. The map therefore changes a level of a pair and is not an isometry.</p>

<p><em>The same symmetry on another block system.</em> The theorem is stated for the lattice; on a general ultrametric block system of <a href="/articles/ultrametric-block-systems/">the general article</a> the translation part survives verbatim, since levels are translation invariant there too, and transitivity on pairs at a level holds whenever the coefficient group is large enough to carry the coordinate-wise bijections.</p>

<p><em>The p-adic case.</em> On $\mathbb Z_p$ the maps $x\mapsto a+bx$ with $a\in\mathbb Z_p$ and $\lvert b\rvert_p=1$ are isometries, since $\lvert b(x-y)\rvert_p=\lvert x-y\rvert_p$, and they are already transitive on pairs at a level: if $\lvert x-y\rvert_p=\lvert x'-y'\rvert_p$ then $b=(x'-y')/(x-y)$ has $\lvert b\rvert_p=1$ and $a=x'-bx$ lies in $\mathbb Z_p$. So the conclusion of the theorem holds there with a smaller group.</p>

<p><em>The two families are a subgroup, not the whole group.</em> The isometry group is larger. Permuting the $L^d$ children of a single block and leaving every other vertex alone is an isometry, since it moves each child of that block onto a child of the same block and preserves the internal structure of each; and such a map need not be a composition of a translation with coordinate-wise bijections. What cannot be done is to permute the coordinates: the level records which coordinate is the outermost, so in $\Lambda_2$ with $L=2$, $d=2$ the vertices $0$ and $((0,0),(1,0))$ are at level two, while their images under the interchange of the two coordinates are at level one. The two families are used below because they are the ones that act transitively on pairs, not because they exhaust $\operatorname{Isom}$.</p>

## Variants and generalisations {#section-variants}

<p><em>Isometries of a general block system.</em> For a block system $(G,G_n)$ the same two families exist whenever $G_n/G_{n+1}$ carries enough bijections; the translation part always does, and the conclusion (i) of the corollary then holds for radial kernels with no further hypothesis.</p>

<p><em>Vector spins and percolation.</em> The isometries act on configurations by permuting vertices, so they preserve vector-valued models and percolation configurations as well. This is why the two-point function of a radial kernel is radial in those models, and why the sibling clusters in <a href="/articles/hierarchical-percolation-rg/#section-recursion">the percolation recursion</a> are equidistributed.</p>

<p><em>Symmetry breaking.</em> Below the critical temperature the Gibbs measure need not be invariant under the full isometry group; the symmetric state is the average over the broken ones. The statements above are about the symmetric Gibbs measure, which is the one the free-boundary finite-volume models converge to along symmetric subsequences.</p>

## History and attribution {#section-history}

<p>The level isometries are used by Hutchcroft to convert an averaged two-point bound into a pointwise one, on the grounds that any two pairs at a distance are exchanged by an isometry preserving the law [@hutchcroft-hierarchical-2021]; the proof given here is the elementary form of that observation. The symmetry of the block sums is used from the beginning of the subject, in the reduction of the recursion to a single variable [@bleher-sinai-1973], and again in the p-adic setting [@abdesselam-2018]. The counterexample in the examples section is included because the distinction between preserving vertex levels and preserving pair levels is easy to miss.</p>

## References {#section-references}

<ul>
<li>A. Abdesselam, Towards three-dimensional conformal probability, <em>p-Adic Numbers Ultrametric Anal. Appl.</em> 10 (2018), 233&ndash;252.</li>
<li>P. M. Bleher and Ya. G. Sinai, Investigation of the critical point in models of the type of Dyson's hierarchical models, <em>Comm. Math. Phys.</em> 33 (1973), 23&ndash;42.</li>
<li>T. Hutchcroft, The critical two-point function for long-range percolation on the hierarchical lattice, <em>Ann. Appl. Probab.</em> 34 (2024), 986&ndash;1002.</li>
</ul>
