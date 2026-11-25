# Gawedzki and Kupiainen: the local analysis of a non-Gaussian fixed point

This is the reading map for the five papers in which Krzysztof Gawedzki and Antti Kupiainen built
the local theory of the nontrivial fixed point of the hierarchical renormalisation map. The group is
more varied than Koch and Wittwer's, and its role in this wiki is specific: it is where the
*neighbourhood* of the fixed point is analysed — the expansion of the exponents in the distance from
the marginal kernel exponent, the unstable manifold, and the convergence of rescaled correlations —
as opposed to the questions of existence, which belong to Bleher and Sinai and to Koch and Wittwer.

Two parameters organise the group, and both are small in the papers that use them: the departure
`ε = d/2 - α` of the kernel exponent from the marginal value at which the quartic coupling becomes
relevant, and the inverse number of components `1/N` of the spin. Neither is a small parameter of the
model. The fixed point exists for every α in (0,d), but the *analysis* of it is local, and the
hierarchical approximation is what makes the local analysis into a theorem rather than a formal
series.

The group is also the reason the wiki distinguishes the marginal exponent α = d/2 from the others:
the expansion in ε is an expansion around that value, so the threshold announced in
[the exponent dictionary](/articles/critical-exponents-from-rg/#section-dictionary) and computed in
[the spectrum article](/articles/gaussian-fixed-point-spectrum/#section-quartic) is the point at
which these papers expand.

## The works

| Work | What it establishes | Where this wiki uses it |
|---|---|---|
| A rigorous block spin approach to massless lattice theories, *Comm. Math. Phys.* 77 (1980), 31-64; [doi:10.1007/BF01205038](https://doi.org/10.1007/BF01205038) | A convergent block-spin expansion for lattice field theories, with the hierarchical model as the worked example and as the approximation that justifies the Euclidean expansion | [Why the lattice is the comparison](/articles/hierarchical-and-euclidean-rg/#section-exactness), [the hierarchical approximation](/articles/hierarchical-and-euclidean-rg/#section-failure) |
| Triviality of phi-fourth in four dimensions and all that in a hierarchy model approximation, *J. Statist. Phys.* 29 (1982), 683-699 | The hierarchy-model approximation used to discuss the triviality of phi-fourth in four dimensions | [The large-field problem](/articles/koch-wittwer-fixed-point/#section-idea), where the analyticity technique this paper introduced is the one Koch and Wittwer improve on |
| Non-Gaussian fixed points of the block spin transformation. Hierarchical model approximation, *Comm. Math. Phys.* 89 (1983), 191-220; [Zbl 0542.60095](https://zbmath.org/?q=an:0542.60095) | Control of the corrections to the leading nontrivial order in `ε` and in `1/N`: a neighbourhood of the approximate fixed point is preserved by the transformation except for one relevant direction, and successive iterates inside it contract at the critical point | [The statement of the theorem](/articles/bleher-sinai-fixed-point/#section-statement), [the spectrum](/articles/bleher-sinai-fixed-point/#section-spectrum), [the quartic threshold](/articles/gaussian-fixed-point-spectrum/#section-quartic) |
| Non-Gaussian scaling limits. Hierarchical model approximation, *J. Statist. Phys.* 35 (1984), 267-284; [Zbl 0589.60094](https://zbmath.org/?q=an:0589.60094) | The scaling limit itself: the rescaled correlations converge to those of a nontrivial limit law rather than to a Gaussian one | [Non-Gaussian scaling limits](/articles/bleher-sinai-fixed-point/#section-statement), [what the flow produces](/articles/hierarchical-phi4-truncations/#section-potentials) |
| Borel summability of the perturbation series in a hierarchical lambda-nabla-phi-fourth model, with B. Tirozzi, *J. Statist. Phys.* 36 (1984), 145-162; [Zbl 0587.60099](https://zbmath.org/?q=an:0587.60099) | Borel summability of the perturbation series for the dielectric constant and the free energy density of the hierarchical gradient model, by nonperturbative renormalisation-group analysis | [Borel summation](/articles/koch-wittwer-fixed-point/#section-idea), where the technique is taken up for the non-gradient case |

## What is taken from each

### The 1983 paper

This is the paper the wiki cites for the linear theory of the nontrivial fixed point, and the citation
is narrow on purpose. Bleher and Sinai prove that a nontrivial fixed point exists, that the critical
orbit converges to it, and that the correlation-length exponent is read off the linearisation; what
they do not give is the *value* of the leading eigenvalue away from the marginal exponent. The 1983
paper is where that is computed, by expanding in the distance from the marginal exponent: the
fixed point is close to the Gaussian one, the correction to the multiplier is of first order in
`ε = d/2 - α`, and the resulting value of `ν` is not the classical `1/α`.

The mechanism, in the reviewer's summary, is worth recording because it is the model for every
local analysis in the field: find a small set of laws which the transformation maps into itself
except along one direction, and show that inside it two successive iterates move closer together at
the critical coupling. The one direction that is not contracted is the relevant one, and it is what
produces the second exponent. Everything the wiki says about the spectrum at the nontrivial fixed
point is an instance of this statement with the eigenvalues made explicit.

### The 1984 paper

Its subject is the consequence the exponent dictionary needs: not the fixed point but the *field* it
generates. If the critical orbit converges after rescaling, the correlations of the model converge to
those of a limit law, and the two-point exponent `η = 2 - α` is the rate at which the rescaled block
spin's mass is spread. The 1984 paper is where the convergence of the rescaled correlations is
proved in the hierarchical approximation, and the wiki cites it jointly with the 1983 paper for that
statement rather than separating the two.

### The 1980 paper and the 1982 paper

The 1980 paper is the general programme: a block-spin expansion for massless lattice theories that
converges, with the hierarchical model as the example in which the expansion can be completed. For
this wiki it is the honest statement of where the exactness ends — the Euclidean expansion has the
same shape, but the geometry of the blocks changes with scale and the expansion is no longer an
identity. The 1982 paper is the triviality discussion: the hierarchy model is used to argue that
phi-fourth in four dimensions is trivial, and it is also where the analyticity technique appears
that Koch and Wittwer later replace. Neither is cited for a theorem the wiki uses; they are cited for
the programme and for the method.

### The 1984 paper with Tirozzi

The gradient model differs from the models of the rest of this wiki in that the interaction acts on
differences of the field, so the large-field region behaves differently and the perturbation series
can be resummed in the Borel sense. The paper proves that the series for the dielectric constant and
the free energy density are Borel summable. It matters here because it is the technique Koch and
Wittwer import into the non-gradient case, which is what allows them to prove existence without a
small parameter.

## What the group does not do

Three boundaries are worth stating, because the wiki relies on them.

*Existence is not the subject.* The fixed point is assumed or constructed locally; the global
existence theorem for the hierarchical model is Bleher and Sinai's, and the parameter-free
construction for the three-dimensional scalar case is Koch and Wittwer's, as
[that reading map](/articles/koch-wittwer-fixed-point/#section-statement) records.

*The analysis is local.* The results are for `ε` small or `N` large. They are not statements about
the three-dimensional Ising model at the physical value of the parameters, and the wiki does not use
them as such; where an exponent is quoted away from the neighbourhood, it is quoted as a
conjecture.

*The setting is the hierarchical approximation.* The 1980 paper is explicit that the Euclidean
expansion is the target and the hierarchical model the place where it is completed. The
[Euclidean comparison](/articles/hierarchical-and-euclidean-rg/#section-failure) says what fails when
the hierarchy is dropped, and no paper in this group closes that.

## How to read the group

For a reader who wants the exponents, the order is 1983 then 1984: the first gives the multiplier and
hence `ν`, the second the scaling limit and hence `η`. For a reader who wants the method, read the
1983 paper after [the statement of the Bleher-Sinai theorem](/articles/bleher-sinai-fixed-point/#section-statement),
because the local analysis is the linearisation of a theorem that is already known to hold. The 1980
and 1982 papers are for the context in which the hierarchical model is a step towards the Euclidean
theory, and the Tirozzi paper belongs with [the Koch-Wittwer method](/articles/koch-wittwer-fixed-point/#section-idea)
rather than with the rest.
