---
{
  "id": "corrections-to-scaling",
  "title": "Corrections to scaling",
  "subtitle": "The second eigenvalue, and why a power law is only ever the first term.",
  "kind": "theorem",
  "category": "Renormalisation group",
  "summary": "Near a fixed point the orbit approaches along the stable directions, so every power law carries corrections from the second eigenvalue. In the hierarchical model the corrections are geometric in the scale and therefore pure powers of the correlation length, one for each subleading eigenvalue, with exponent omega equal to minus the logarithm of the subleading eigenvalue over the logarithm of the scale; a complex pair makes them oscillate in the logarithm of the length, and an eigenvalue tending to one makes them logarithmic.",
  "context": [
    "A fixed point $\\nu^*$ of the rescaled map with simple leading eigenvalue $\\lambda_1&gt;1$ and remaining spectrum inside a disk of radius $\\rho&lt;1$.",
    "The orbit is assumed to admit the spectral expansion stated in the theorem, with coefficients that do not depend on the scale.",
    "Exponents are those of the dictionary: $\\kappa=2\\theta-d$, $\\nu=\\log L/\\log\\lambda_1$."
  ],
  "related": [
    "critical-exponents-from-rg",
    "renormalisation-group-map",
    "bleher-sinai-fixed-point",
    "gaussian-renormalisation-group",
    "gaussian-fixed-point-spectrum"
  ],
  "sourceIds": ["bleher-sinai-1975", "gawedzki-kupiainen-1983", "gawedzki-kupiainen-1984", "aizenman-fernandez-1988"],
  "aliases": [
    "corrections to scaling",
    "second eigenvalue",
    "correction exponent",
    "confluent singularity",
    "oscillatory corrections"
  ]
}
---

<p>A critical exponent describes the leading term of an asymptotic expansion, and the expansion has further terms. In the hierarchical model those terms are especially simple: a perturbation of the fixed point in a direction whose eigenvalue is $\lambda$ is multiplied by $\lambda$ per scale, and since the scale of the critical theory is the correlation length, the perturbation appears as a power of $\xi$, with exponent $-\log\lvert\lambda\rvert/\log L$. The leading irrelevant direction therefore gives a relative correction of order $\xi^{-\omega}$ with $\omega=-\log\lvert\lambda_2\rvert/\log L$, and each further eigenvalue gives one more power.</p>

<p>Three features are worth stating before the derivation. The corrections are <em>geometric in the scale</em>, so in the hierarchical model they are pure powers rather than powers times logarithms; the same is true in the Euclidean theory only after resummation. A complex conjugate pair of eigenvalues replaces the power by a power times a cosine of the logarithm of the length, which is the oscillatory correction that the numerical literature reports for the hierarchical model [@gawedzki-kupiainen-1983]. And when the second eigenvalue tends to one, as it does at the marginal exponent, the correction exponent tends to zero and the corrections become logarithmic, which is why the marginal case needs its own analysis.</p>

<p>Nothing here is specific to the model: the argument is the spectral expansion of the orbit, and the model determines the eigenvalues. What the hierarchical model contributes is that the expansion is in the scale with no mixing between scales, so the correction structure can be written down exactly given the spectrum.</p>

## Definitions and setting {#section-setting}

<p>This article uses the notation of <a href="/articles/renormalisation-group-map/#section-fixed-points">the map article</a>: $\mathcal R=\mathcal R_{\theta_0,b}$ is the rescaled decimation map, $\nu^*$ a fixed point with $0&lt;\int s^2d\nu^*&lt;\infty$, and $D\mathcal R$ its linearisation on signed measures of zero mass. Let $\lambda_1$ be the leading eigenvalue, simple and larger than one, and let the remaining spectrum lie in $\lvert\lambda\rvert\leq\rho$ with $\rho&lt;1$. Write $\rho_1$ for the eigenmeasure of $\lambda_1$ and $\rho_j$ for the others, normalised so that the expansion below has scale-free coefficients.</p>
<a id="tag-C6VW" data-assertion="definition" data-title="Correction exponent of a subleading eigenvalue"></a>
<p>For an eigenvalue $\lambda$ of $D\mathcal R$ with $\lvert\lambda\rvert&lt;1$, the <em>correction exponent</em> is</p>
<div class="math-display">$$\omega(\lambda)=-\frac{\log\lvert\lambda\rvert}{\log L},$$</div>
<p>a positive number; for a complex eigenvalue $\lambda=\lvert\lambda\rvert e^{i\varphi}$ the pair contributes the same power together with the phase $\varphi/\log L$ per unit of $\log\xi$. The <em>correction exponent of the model</em> is $\omega=\omega(\lambda_2)$ for the subleading eigenvalue.</p>
<p>The exponent measures the length scale at which a perturbation decays by a factor $e$: after $n$ scales a perturbation of size $\epsilon$ in the direction $\rho_2$ has size $\epsilon L^{-\omega n}=\epsilon\xi^{-\omega}$ when $L^n$ is the correlation length.</p>

## Statement {#section-statement}

<a id="tag-C3XD" data-assertion="theorem" data-title="Power laws with corrections from the subleading spectrum"></a>
<p>Assume that for $\beta$ near $\beta_c$ the rescaled orbit admits the expansion</p>
<div class="math-display">$$\nu_n=\nu^*+a\,\lvert\beta-\beta_c\rvert\,\lambda_1^{\,n}\rho_1+\sum_{j\geq2}b_j\lambda_j^{\,n}\rho_j+O\bigl(\rho^{2n}\bigr),$$</div>
<p>with $\lvert\lambda_j\rvert\leq\rho&lt;1$ and coefficients $a,b_j$ independent of $n$ and $\beta$. Then, with $\kappa$ the growth exponent of the dictionary and $\gamma=\kappa\nu$,</p>
<div class="math-display">$$\chi_n(\beta)=L^{\kappa n}\Bigl(m_2(\nu^*)+a\,\lvert\beta-\beta_c\rvert\,\lambda_1^{\,n}m_2(\rho_1)+\sum_{j\geq2}b_j\lambda_j^{\,n}m_2(\rho_j)+O(\rho^{2n})\Bigr),$$</div>
<p>and taking $n$ of order the crossover scale, $L^{n}\asymp\lvert\beta-\beta_c\rvert^{-\nu}$, gives</p>
<div class="math-display">$$\chi(\beta)=A\lvert\beta-\beta_c\rvert^{-\gamma}\Bigl(1+\sum_{j\geq2}C_j\lvert\beta-\beta_c\rvert^{\,\nu\omega(\lambda_j)}+O\bigl(\lvert\beta-\beta_c\rvert^{2\nu\omega_2}\bigr)\Bigr),$$</div>
<p>with $A=m_2(\nu^*)$ and constants $C_j$ that depend on the direction but not on $\beta$. The two-point function carries the same relative corrections at every pair of vertices, and the singular free energy carries them with its own amplitude.</p>
:::details Proof
<p>The block susceptibility is $\chi_n=L^{-dn}\mathbb E[S_n^2]$ by <a href="/articles/critical-exponents-from-rg/#section-identities">the block identity</a>, and $\mathbb E[S_n^2]=L^{2\theta_0 n}m_2(\nu_n)$ with $2\theta_0-d=\kappa$. Substituting the expansion gives the second display, since $m_2$ is linear and the expansion is finite up to the stated error.</p>
<p>For the third display, let $\xi=\lvert\beta-\beta_c\rvert^{-\nu}$ and choose $n$ with $L^n=\xi$, so that $\lambda_1^{\,n}=\xi^{\log\lambda_1/\log L}=\xi^{1/\nu}$ and $\lvert\beta-\beta_c\rvert\lambda_1^{\,n}=\lvert\beta-\beta_c\rvert^{1-\nu\cdot(1/\nu)}=1$: the relevant term is of the same size as the fixed-point term, which is what makes $n$ the crossover scale. At that scale the $j$-th correction has relative size $\lvert\lambda_j\rvert^{n}=\xi^{-\omega(\lambda_j)}=\lvert\beta-\beta_c\rvert^{\nu\omega(\lambda_j)}$, and the error is of the order of the square of the largest correction. Dividing by the leading behaviour $\xi^{\kappa}=\lvert\beta-\beta_c\rvert^{-\kappa\nu}=\lvert\beta-\beta_c\rvert^{-\gamma}$ gives the display.</p>
<p>The statement for the two-point function is the same computation applied to $\tau$, whose block values are the off-diagonal entries of the covariance of the child spins; each is linear in the expansion, so the relative correction is the same at every pair. For the free energy the increment at scale $n$ is a smooth function of the orbit, so its expansion is the linear one composed with the derivative of the increment, which changes only the constants.</p>
:::
<p>The hypothesis is the whole content of the statement, and it is what the fixed-point theory supplies: an expansion of the orbit in the eigenmeasures of the linearisation, with coefficients that vary smoothly with the temperature. The theorem then says that everything the model can do to a power law, in this class, is a sum of terms $\lvert\beta-\beta_c\rvert^{\nu\omega_j}$.</p>

## Consequences and applications {#section-consequences}

<p><em>Effective exponents.</em> Differentiating the logarithm of the susceptibility gives</p>
<div class="math-display">$$\gamma_{\mathrm{eff}}(\beta)=-\frac{d\log\chi}{d\log\lvert\beta-\beta_c\rvert}=\gamma-\sum_{j\geq2}C_j\,\nu\omega(\lambda_j)\,\lvert\beta-\beta_c\rvert^{\nu\omega(\lambda_j)}+\cdots,$$</div>
<p>so a numerical estimate of $\gamma$ drifts towards its limit at a rate set by the smallest $\omega$. This is the reason exponents extracted from finite ranges of temperature are biased in a direction fixed by the sign of the corrections.</p>

<p><em>The oscillatory case.</em> If $\lambda_2,\bar\lambda_2$ are a complex pair with argument $\pm\varphi$, the correction term of the theorem reads $C\lvert\beta-\beta_c\rvert^{\nu\omega}\cos\bigl(\nu\varphi\log\lvert\beta-\beta_c\rvert+\vartheta\bigr)$: a power times a cosine of the logarithm, which looks like a drifting oscillation when plotted against $\log\xi$. The analysis of the linearisation at the nontrivial fixed point, where such pairs occur, is that of Gawedzki and Kupiainen [@gawedzki-kupiainen-1983].</p>

<p><em>The marginal limit.</em> As $\lambda_2\uparrow1$ the correction exponent $\omega\downarrow0$ and the correction becomes $\lvert\beta-\beta_c\rvert^{o(1)}$, that is, a power of a logarithm. This is exactly what happens at the marginal kernel exponent, where the two fixed points merge, and it is the origin of the logarithmic corrections recorded there in <a href="/articles/bleher-sinai-fixed-point/#section-statement">the fixed-point article</a>.</p>

<p><em>Reading data.</em> Because the corrections are pure powers of $\xi$ with exponents determined by the spectrum, a fit that includes one correction term and excludes the next is well posed only if $\omega_2$ is not close to an integer multiple of $\omega$; otherwise the two terms are hard to separate, which is the practical form of the "confluent corrections" problem.</p>

## Examples and non-examples {#section-examples}

<p><em>The Gaussian fixed point.</em> There the only relevant direction is the variance, whose eigenvalue is $L^{\alpha}$, and the subleading directions are the non-Gaussian perturbations; the quartic one is the first, and its eigenvalue is the quantity computed in the epsilon expansion around the marginal exponent [@gawedzki-kupiainen-1983]. At the Gaussian fixed point itself the corrections vanish identically for a Gaussian initial law, which is why the Gaussian model has exact power laws.</p>

<p><em>Corrections in the Euclidean theory.</em> On $\mathbb Z^d$ the same spectral picture holds near the fixed point, but the decimation does not close, so the corrections are not pure powers of $\xi$: they are powers times logarithms arising from the infinitely many irrelevant directions generated at each step. The hierarchical model is the case in which that sum collapses to one geometric series per eigenvalue.</p>

<p><em>Non-example: a first-order transition.</em> At a first-order transition there is no fixed point governing the transition, the correlation length stays finite, and no expansion of the above form exists; the power-law apparatus does not apply, and the observed behaviour is a discontinuity.</p>

<p><em>Non-example: the marginal exponent.</em> At $\alpha=d/2$ the assumption $\lambda_2$ bounded away from one fails, and the theorem as stated gives no rate; the logarithmic corrections have to be derived separately, and they are not of the form $\lvert\beta-\beta_c\rvert^{c}$ for a constant $c&gt;0$.</p>

## Variants and generalisations {#section-variants}

<p><em>Corrections to the correlation length.</em> The same argument applies to any quantity that is a smooth function of the orbit, with the constants changed: the correlation length itself satisfies $\xi=\xi_0\lvert\beta-\beta_c\rvert^{-\nu}(1+O(\lvert\beta-\beta_c\rvert^{\nu\omega}))$, which is the form in which the two-point function's correction is usually written.</p>

<p><em>Several irrelevant directions.</em> With a pair of eigenvalues of comparable modulus the correction is a sum, and the exponents $\nu\omega_j$ need not be commensurable; a two-term fit is then the smallest well-posed model.</p>

<p><em>Scaling fields.</em> The coefficient of the relevant eigenmeasure is the scaling field $t(\beta)$ of the renormalisation group, and the corrections are the higher scaling fields; the statement of the theorem is that in the hierarchical model the scaling fields are analytic in $\beta$ and their images under the flow are powers of $\xi$. This is the form in which the corrections enter the Euclidean analysis as well [@aizenman-fernandez-1988].</p>

## History and attribution {#section-history}

<p>The computation of the indices from the linearisation, and the presence of further eigenvalues controlling the corrections, is in Bleher and Sinai's second paper on the hierarchical model [@bleher-sinai-1975]. The complex pairs at the nontrivial fixed point, and the oscillatory corrections they produce, are analysed by Gawedzki and Kupiainen, who also identify the marginal limit at which the corrections become logarithmic [@gawedzki-kupiainen-1983]; the scaling limit and the flow of the relevant direction around the fixed point are the subject of their second paper [@gawedzki-kupiainen-1984]. The classical long-range values, for which the corrections vanish in the Gaussian case, are those of the Gaussian fixed point.</p>

## References {#section-references}

<ul>
<li>M. Aizenman and R. Fernandez, Critical exponents for long-range interactions, <em>Lett. Math. Phys.</em> 16 (1988), 39&ndash;49.</li>
<li>P. M. Bleher and Ya. G. Sinai, Critical indices for Dyson's asymptotically-hierarchical models, <em>Comm. Math. Phys.</em> 45 (1975), 247&ndash;278.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian fixed points of the block spin transformation. Hierarchical model approximation, <em>Comm. Math. Phys.</em> 89 (1983), 191&ndash;220.</li>
<li>K. Gawedzki and A. Kupiainen, Non-Gaussian scaling limits. Hierarchical model approximation, <em>J. Statist. Phys.</em> 35 (1984), 267&ndash;284.</li>
</ul>
