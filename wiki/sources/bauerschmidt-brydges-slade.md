# Bauerschmidt, Brydges and Slade: the method, and the four-dimensional case

This is the reading map for the one book in the catalogue that is not a paper: the Lecture Notes
volume in which Roland Bauerschmidt, David Brydges and Gordon Slade develop their renormalisation
group method, in the setting of the four-dimensional `n`-component `|φ|⁴` model. The group is one
work, so the map is not a survey of a literature; it says what the book is for, which parts of this
wiki lean on it, and what it does not cover.

The method is the one that made the four-dimensional case rigorous, and its organisation is worth
knowing before opening the book. The renormalisation group is presented as a flow of *potentials*
rather than of measures: one writes the effective potential after a decimation step as a sum of
local polynomials, and the whole analysis is the control of the remainder under that flow. Two
devices carry the control: a family of seminorms in which the flow is a contraction on the
irrelevant directions, and a perturbation expansion whose terms are indexed by the scale at which
they first appear. The book develops these for the hierarchical model first, because there the
decimation step is an identity and the flow is a recursion on one variable; the Euclidean model is
the target and the reason the machinery has to be as heavy as it is.

## The work

| Work | What it establishes | Where this wiki uses it |
|---|---|---|
| *Introduction to a Renormalisation Group Method*, Lecture Notes in Mathematics 2242, Springer, 2019; [Zbl 1471.81001](https://zbmath.org/?q=an:1471.81001) | A self-contained development of the renormalisation group method that the authors developed for the four-dimensional n-component phi-fourth spin system and the four-dimensional weakly self-avoiding walk, presented in the context of the hierarchical model, where the decimation step is exact | [The lattice as a group](/articles/hierarchical-lattice/#section-definitions), [the potential formulation](/articles/hierarchical-phi4-truncations/#section-potentials), [power counting as linearisation](/articles/gaussian-fixed-point-spectrum/#section-quartic), [why the Euclidean case is harder](/articles/hierarchical-and-euclidean-rg/#section-failure) |

## What this wiki takes from it

Three things, and none of them is a theorem about the hierarchical model of this wiki.

*The potential formulation.* This wiki writes the recursion on the law of the block spin, which is
Bleher and Sinai's form. The book writes it on the negative logarithm of the density, which is the
form in which the flow of couplings appears as a differential equation and in which truncations can
be controlled. The two are the same recursion, and
[the phi-fourth article](/articles/hierarchical-phi4-truncations/#section-potentials) says where they
part company: the law carries the whole measure, the potential only its logarithm, and a truncation
of the potential is not a truncation of the law.

*Power counting as the linearisation of a map at a Gaussian fixed point.* The eigenvalues
`L^{d(1-k)+kα}` of [the spectrum article](/articles/gaussian-fixed-point-spectrum/#section-statement)
are usually introduced as dimensional analysis. The book introduces them as the derivative of a map,
which is what they are, and that is the presentation this wiki follows.

*The reason the Euclidean case needs more.* The hierarchical model is not a warm-up in the book; it
is the case in which the method closes, and the Euclidean case is where the seminorms, the
localisation theorem and the supersymmetric representation earn their place. For this wiki the
value is the contrast: it shows what an argument needs when the blocks have boundaries.

## What it does not give this wiki

The book is about the marginal dimension. Its subject is the four-dimensional `|φ|⁴` model, where
the quartic coupling is marginal and the flow has to be controlled at the marginal direction; the
long-range models of this wiki have an exponent `α` that plays the role of the distance from the
marginal dimension. The correspondence is made in
[the phi-fourth article](/articles/hierarchical-phi4-truncations/#section-gaussian) and it is not an
identity: changing `α` changes the kernel, whereas changing the dimension changes the lattice.

Nothing in the book decides the questions this wiki leaves open about the hierarchical model itself:
the upper bound on the free block-spin variance that would certify `κ = α`
([the variance route](/articles/critical-exponents-from-rg/#section-variance-route)), or the
existence of a magnetised phase without the recursion. Those are questions about a model the book
uses as a setting, not about the method it develops.
