#!/usr/bin/env python3
"""Numerical checks on the statements the wiki makes about the hierarchical model.

Each check compares a formula asserted in an article with a direct computation on a
finite block. They are recommendations about the mathematics, not a substitute for
the proofs: pass/fail here says a displayed identity is right, not that a theorem is.

Usage: python3 tools/numeric_checks.py
Requires numpy.
"""
from __future__ import annotations

import itertools
import math
import re

from pathlib import Path

import numpy as np

sys_path = Path(__file__).resolve().parent
import sys as _sys
_sys.path.insert(0, str(sys_path))
import simulate  # noqa: E402

RESULTS = []


def note(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")


def vertices(d, L, n):
    return [t for t in itertools.product(range(L), repeat=d * n)]


def lev(x, y, d):
    """Level of a pair: the distance is L to the level, per the lattice article."""
    out = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            out = i // d + 1
    return out


def interaction(d, L, n, alpha, beta, J=1.0):
    V = vertices(d, L, n)
    N = len(V)
    A = np.zeros((N, N))
    for a in range(N):
        for b in range(a + 1, N):
            k = lev(V[a], V[b], d)
            A[a, b] = A[b, a] = beta * J * L ** (-(d + alpha) * k)
    return A, V


def row_sum(d, L, alpha, J=1.0):
    return J * (1 - L ** (-d)) * L ** (-alpha) / (1 - L ** (-alpha))


def check_variance():
    """Gaussian: the variance recursion and its closed form (Gaussian RG, sections closure/critical)."""
    for d, L, alpha, beta in [(1, 2, 0.5, 0.5), (2, 2, 1.0, 0.2), (1, 3, 0.7, 0.3)]:
        J, m = 1.0, L ** d
        for n in range(1, 4):
            A, _ = interaction(d, L, n, alpha, beta)
            N = len(A)
            one = np.ones(N)
            exact = one @ np.linalg.solve(np.eye(N) - A, one)
            v = 1.0
            for j in range(1, n + 1):
                bj = beta * J * L ** (-(d + alpha) * j)
                v = m * v / (1 - bj * v * (m - 1))
            closed = m ** n / (1 - beta * J * (1 - L ** (-d)) * sum(L ** (-alpha * j) for j in range(1, n + 1)))
            note(f"variance d={d} L={L} a={alpha} b={beta} n={n}",
                 abs(v - exact) < 1e-8 * max(1, exact) and abs(closed - exact) < 1e-8 * max(1, exact),
                 f"exact {exact:.8f}, recursion {v:.8f}, closed form {closed:.8f}")


def check_beta_c():
    """Gaussian: the top eigenvalue of the interaction tends to the row sum (Gaussian RG, critical)."""
    for d, L, alpha in [(1, 2, 0.5), (2, 2, 1.0)]:
        evs = []
        for n in [2, 3, 4, 5]:
            A, _ = interaction(d, L, n, alpha, 1.0)
            evs.append(np.linalg.eigvalsh(A)[-1])
        note(f"critical intensity d={d} L={L} a={alpha}",
             all(evs[i] < evs[i + 1] < row_sum(d, L, alpha) for i in range(len(evs) - 1)),
             f"top eigenvalues {[round(e, 6) for e in evs]} increasing to row sum {row_sum(d, L, alpha):.6f}")


def check_multiplier():
    """Gaussian: g'(u*) = L^alpha symbolically replaced by a high-precision finite difference."""
    for d, L, alpha in [(1, 2, 0.5), (2, 3, 0.7), (1, 5, 1.3)]:
        m, lam = L ** d, L ** (d + alpha)
        u = (lam - m) / (m - 1)
        g = lambda x: m * x / (lam - (m - 1) * x)
        h = 1e-6
        num = (g(u + h) - g(u - h)) / (2 * h)
        note(f"multiplier d={d} L={L} a={alpha}", abs(num - L ** alpha) < 1e-4 * L ** alpha,
             f"numeric g'(u*) = {num:.8f}, L^alpha = {L ** alpha:.8f}")


def check_block_identity():
    """Block identity E[S_n^2] = L^{dn} chi_n (exponents article, section identities)."""
    for d, L, alpha, beta in [(1, 2, 0.5, 0.5), (2, 2, 1.0, 0.2), (1, 2, 0.5, 1.2)]:
        for n in [1, 2, 3]:
            A, V = interaction(d, L, n, alpha, beta)
            N = len(A)
            tau = np.linalg.inv(np.eye(N) - A)
            i0 = V.index(tuple([0] * (d * n)))
            chi = sum(tau[i0, j] for j in range(N))
            es2 = tau.sum()
            note(f"block identity d={d} L={L} b={beta} n={n}", abs(es2 - L ** (d * n) * chi) < 1e-9 * max(1, es2),
                 f"E[S^2] = {es2:.8f}, L^(dn) chi_n = {L ** (d * n) * chi:.8f}")


def check_decimation_ising():
    """Ising: the decimation identity for the partition function (decimation article)."""
    L, d, alpha, J, beta = 2, 1, 0.5, 1.0, 0.7
    Jk = lambda k: J * L ** (-(d + alpha) * k)

    def partition(n):
        C = vertices(d, L, n)
        pairs = [(i, j) for i in range(len(C)) for j in range(i + 1, len(C))]
        weights = [Jk(lev(C[i], C[j], d)) for i, j in pairs]
        total = 0.0
        for s in itertools.product([-1, 1], repeat=len(C)):
            total += math.exp(beta * sum(w * s[i] * s[j] for (i, j), w in zip(pairs, weights)))
        return total, C, pairs, weights

    Z2, _, _, _ = partition(2)
    Z1, C1, pairs1, w1 = partition(1)
    law = {}
    for s in itertools.product([-1, 1], repeat=len(C1)):
        law[sum(s)] = law.get(sum(s), 0.0) + math.exp(beta * sum(w * s[i] * s[j] for (i, j), w in zip(pairs1, w1)))
    law = {k: v / Z1 for k, v in law.items()}
    rhs = Z1 ** 2 * sum(p * q * math.exp(beta * Jk(2) * a * b) for a, p in law.items() for b, q in law.items())
    note("Ising decimation identity", abs(Z2 - rhs) < 1e-10, f"Z_2 = {Z2:.10f}, Z_1^2 E[exp(b J_2 s s')] = {rhs:.10f}")


def check_triangle():
    """Triangle diagram: the increment at level N is of order L^((3 alpha - d) N) (percolation article)."""
    d, L = 1, 2
    for alpha in [0.2, 0.4, 0.6]:
        tot = []
        for N in range(2, 11):
            V = vertices(d, L, N)
            Nv = len(V)
            c = np.array([1.0] + [L ** (-(d - alpha) * k) for k in range(1, N + 1)])
            lv = np.zeros((Nv, Nv), dtype=np.int16)
            for i in range(Nv):
                for j in range(Nv):
                    lv[i, j] = lev(V[i], V[j], d)
            t = c[lv]
            tot.append(float(np.tensordot(t[0, :], t @ t[:, 0], axes=1)))
        inc = [tot[i + 1] - tot[i] for i in range(len(tot) - 1)]
        ratio = inc[-1] / inc[-2]
        predicted = L ** (3 * alpha - d)
        note(f"triangle increment a={alpha}", abs(ratio - predicted) < 0.05 * predicted,
             f"increment ratio {ratio:.4f}, predicted L^(3a-d) = {predicted:.4f}"
             f" ({'growing' if predicted > 1 else 'decaying'} case)")


def check_quartic_generation():
    """phi-fourth: a quartic potential generates a sixth power at third order in the coupling."""
    mu0, b, m = 1.0, 0.1, 2

    def neglog(s, lam, zmax=10.0, n=20001):
        z = np.linspace(-zmax, zmax, n)
        vz = 0.5 * mu0 * z * z + lam * z ** 4
        s2 = s - z
        integrand = np.exp(b * z * s2 - vz - (0.5 * mu0 * s2 * s2 + lam * s2 ** 4))
        return -np.log(np.trapezoid(integrand, z))

    def coefs(lam, half=0.6, pts=81, order=4):
        s = np.linspace(-half, half, pts)
        f = np.array([neglog(x, lam) for x in s])
        A = np.vstack([s ** (2 * k) for k in range(order + 1)]).T
        c, *_ = np.linalg.lstsq(A, f, rcond=None)
        return c  # c[1] is the s^2 coefficient, c[2] the s^4 one, c[3] the s^6 one

    # calibration: at quadratic order the density is Gaussian with the known variance
    v = 1 / mu0
    vp = m * v / (1 - b * v * (m - 1))
    c = coefs(0.0)
    note("quartic calibration at zero coupling", abs(c[1] - 1 / (2 * vp)) < 1e-8,
         f"s^2 coefficient {c[1]:.10f}, exact {1 / (2 * vp):.10f}")

    # The slope approaches 3 as the coupling goes to zero; larger couplings carry the
    # expected O(lambda) correction, which is why the smallest pair is the one tested.
    lams = np.array([0.00125, 0.0025, 0.005, 0.01])
    c6 = np.array([coefs(l)[3] for l in lams])
    slopes = np.diff(np.log(c6)) / np.diff(np.log(lams))
    note("quartic generates a sixth power at third order",
         bool(np.all(c6 > 0)) and abs(slopes[0] - 3) < 0.15,
         f"s^6 coefficients {[f'{x:.2e}' for x in c6]}, log-log slopes "
         f"{[round(float(x), 2) for x in slopes]} (leading slope predicts 3)")


def check_gaussian_spectrum():
    """The linearisation at the Gaussian fixed point: diagonal entries L^(d(1-k)+k alpha)."""
    L, d, K = 2.0, 1.0, 3

    def step_function(alpha):
        theta = (d + alpha) / 2
        m = L ** d
        b = (1 - m / L ** (2 * theta)) / (m - 1)
        x = np.linspace(-20.0, 20.0, 40001)
        S = np.linspace(-0.7, 0.7, 81)
        A = np.vstack([S ** (2 * k) for k in range(K + 1)]).T

        def step(coeffs):
            def V(z):
                return sum(c * z ** (2 * (k + 1)) for k, c in enumerate(coeffs))
            vals = np.empty_like(S)
            for i, sv in enumerate(S):
                s1 = x
                s2 = L ** theta * sv - s1
                vals[i] = -np.log(np.trapezoid(np.exp(-V(s1) - V(s2) + b * s1 * s2), x))
            out, *_ = np.linalg.lstsq(A, vals, rcond=None)
            return out
        return step

    for alpha in (0.3, 0.5, 0.8):
        step = step_function(alpha)
        vstar = np.array([0.5, 0.0, 0.0])
        base = step(vstar)
        h = 1e-6
        M = np.zeros((K, K))
        for j in range(K):
            pert = vstar.copy()
            pert[j] += h
            M[:, j] = (step(pert)[1:] - base[1:]) / h
        ev = np.sort(np.real(np.linalg.eigvals(M)))[::-1]
        predicted = np.array([L ** (d * (1 - k) + k * alpha) for k in (1, 2, 3)])
        rel = np.max(np.abs(ev - predicted) / predicted)
        note(f"Gaussian spectrum alpha={alpha}", rel < 1e-3,
             f"eigenvalues {[round(float(x), 6) for x in ev]} vs "
             f"L^(d(1-k)+k alpha) {[round(float(x), 6) for x in predicted]}, "
             f"largest relative error {rel:.1e}")


# ---------------------------------------------------------------- infinite-volume limit

def block_vertices(d, L, n, M):
    """Vertices of the ambient block Lambda_M, split into Lambda_n and its complement."""
    V = vertices(d, L, M)
    zero = tuple([0] * (d * M))
    inside = [x for x in V if lev(x, zero, d) <= n]
    outside = [x for x in V if lev(x, zero, d) > n]
    return inside, outside


def check_boundary_field():
    """The boundary field of a block: closed form, independence of the vertex, and its sum over the block."""
    for d, L, alpha in [(1, 2, 0.5), (1, 2, 1.5), (2, 2, 0.7)]:
        J = 1.0
        for n in range(0, 4):
            M = n + 5
            inside, outside = block_vertices(d, L, n, M)
            # every vertex of Lambda_n sees the same complement, and the closed form is right
            vals = {round(sum(J * L ** (-(d + alpha) * lev(x, y, d)) for y in outside), 12) for x in inside}
            # the vertices above level M are omitted from the sum, and contribute exactly this tail
            closed = row_sum(d, L, alpha, J) * L ** (-alpha * n)
            tail = J * (1 - L ** (-d)) * L ** (-alpha * (M + 1)) / (1 - L ** (-alpha))
            ok = len(vals) == 1 and abs(vals.copy().pop() - (closed - tail)) < 1e-9 * max(closed, 1e-12)
            note(f"boundary field d={d} L={L} alpha={alpha} n={n}", ok,
                 f"{len(vals)} distinct value(s) {sorted(vals)[:2]}, closed form minus the tail "
                 f"{closed - tail:.12f}")
        # the total coupling to the complement grows or decays according as alpha is below or above d
        tots = [L ** (d * n) * row_sum(d, L, alpha, J) * L ** (-alpha * n) for n in range(0, 6)]
        rates = [tot / L ** ((d - alpha) * n) for n, tot in enumerate(tots)]
        ok = max(abs(r - rates[0]) for r in rates) < 1e-12 * rates[0] and (tots[-1] > tots[0]) == (alpha < d)
        note(f"boundary volume d={d} alpha={alpha}", ok,
             f"|Lambda_n| B_n at n=0..5: {[round(t, 3) for t in tots]}; divided by L^((d-alpha)n) "
             f"{[round(t, 6) for t in rates]} and alpha {'<' if alpha < d else '>'} d")


def tv(p, q):
    return 0.5 * sum(abs(a - b) for a, b in zip(p, q))


def check_conditional_lipschitz():
    """The Gibbs conditional is Lipschitz in the boundary field, with the constants of the proposition."""
    rng = np.random.default_rng(20260216)
    worst = 0.0
    for _ in range(400):
        beta = float(rng.uniform(0.1, 2.0))
        h = float(rng.normal() * 2.0)
        hp = h + float(rng.normal())
        lhs = abs(math.tanh(beta * h) - math.tanh(beta * hp)) / 2
        bound = math.tanh(beta * abs(h - hp) / 2)
        worst = max(worst, lhs / bound if bound else 0.0)
    note("single-site conditional is Lipschitz", worst <= 1 + 1e-12,
         f"largest ratio of the true distance to tanh(beta|h-h'|/2) over 400 random pairs: {worst:.4f}")

    # two sites, all four configurations: total variation against the bound
    d, L, beta, n = 1, 2, 0.7, 2
    A, V = interaction(d, L, n, 0.5, beta)
    states = list(itertools.product([-1, 1], repeat=2))
    worst = 0.0
    for _ in range(50):
        h = rng.normal(size=2) * 1.5
        hp = h + rng.normal(size=2) * 0.8

        def law(field):
            w = []
            for s in states:
                e = -beta * sum(s[a] * s[b] for a in range(2) for b in range(a + 1, 2))
                e = beta * 0.5 * s[0] * s[1] + beta * sum(field[i] * s[i] for i in range(2))
                w.append(math.exp(e))
            Z = sum(w)
            return [x / Z for x in w]

        lhs = tv(law(h), law(hp))
        bound = math.tanh(beta * float(np.sum(np.abs(h - hp))) / 2)
        worst = max(worst, lhs / bound if bound > 1e-12 else 0.0)
    note("two-site conditional is Lipschitz", worst <= 1 + 1e-9,
         f"largest ratio of the total variation distance to tanh(beta|A||h-h'|/2): {worst:.4f}")


def check_free_measure_conditional():
    """The free-boundary conditional of a block uses only the spins of the block, and tau depends on the level alone."""
    d, L, alpha, beta, n = 1, 2, 0.5, 0.6, 3
    V = vertices(d, L, n)
    zero = tuple([0] * (d * n))
    weights = {}
    for s in itertools.product([-1, 1], repeat=len(V)):
        e = 0.0
        for a in range(len(V)):
            for b in range(a + 1, len(V)):
                e += L ** (-(d + alpha) * lev(V[a], V[b], d)) * s[a] * s[b]
        weights[s] = math.exp(beta * e)
    Z = sum(weights.values())
    # the two-point function, and whether it depends on the level alone
    tau = {}
    for a in range(len(V)):
        for b in range(a + 1, len(V)):
            tau[(a, b)] = sum(w * s[a] * s[b] for s, w in weights.items()) / Z
    by_level = {}
    for (a, b), t in tau.items():
        by_level.setdefault(lev(V[a], V[b], d), []).append(t)
    spread = max(max(v) - min(v) for v in by_level.values())
    note("free-boundary two-point function is radial", spread < 1e-9,
         f"levels {sorted(by_level)}, largest spread within a level {spread:.2e}, "
         f"values {[round(sum(v) / len(v), 6) for k, v in sorted(by_level.items())]}")

    # the conditional law of the first two sites given the rest, against the Gibbs conditional built from the field
    A = [0, 1]
    worst = 0.0
    for s in list(weights)[:40]:
        outside = s[2:]
        h = [sum(L ** (-(d + alpha) * lev(V[x], V[y], d)) * s[y] for y in range(2, len(V))) for x in A]
        cond = {}
        for sa in itertools.product([-1, 1], repeat=2):
            e = beta * (L ** (-(d + alpha) * lev(V[0], V[1], d))) * sa[0] * sa[1]
            e += beta * sum(h[i] * sa[i] for i in range(2))
            cond[sa] = math.exp(e)
        Zc = sum(cond.values())
        cond = {k: v / Zc for k, v in cond.items()}
        # by enumeration of the free-boundary measure restricted to the same outside configuration
        num = {}
        for sa in cond:
            full = tuple(sa) + outside
            num[sa] = weights[full]
        Zn = sum(num.values())
        num = {k: v / Zn for k, v in num.items()}
        worst = max(worst, max(abs(cond[k] - num[k]) for k in cond))
    note("free conditional equals the Gibbs conditional of the field", worst < 1e-12,
         f"largest discrepancy over 40 configurations: {worst:.2e}")


# ---------------------------------------------------------------- the ferromagnetic phase

def total_mass(d, L, alpha, J=1.0):
    """The total coupling mass at a vertex, C = sum over the shells."""
    return J * (1 - L ** (-d)) / (L ** alpha - 1)


def boundary_mass(d, L, n, alpha, J=1.0):
    """The mass from outside Lambda_n at each vertex of Lambda_n: the same number at every vertex, C L^{-alpha n}."""
    return [total_mass(d, L, alpha, J) * L ** (-alpha * n) for _ in vertices(d, L, n)]


def ising_block(d, L, n, alpha, beta, boundary=1, J=1.0):
    """Weights of the Ising measure on Lambda_n with a constant boundary condition, by enumeration."""
    V = vertices(d, L, n)
    b = boundary_mass(d, L, n, alpha, J)
    w = {}
    for s in itertools.product([-1, 1], repeat=len(V)):
        e = 0.0
        for a in range(len(V)):
            for c in range(a + 1, len(V)):
                e += J * L ** (-(d + alpha) * lev(V[a], V[c], d)) * s[a] * s[c]
            e += boundary * b[a] * s[a]
        w[s] = math.exp(beta * e)
    Z = sum(w.values())
    return {k: v / Z for k, v in w.items()}, V, b


def check_ferromagnetic_phase():
    """Domination in the boundary condition, monotonicity in the volume, the one-site identity and its bound."""
    d, L, alpha, beta, n = 1, 2, 0.5, 0.5, 2
    plus, V, _ = ising_block(d, L, n, alpha, beta, boundary=1)
    minus, _, _ = ising_block(d, L, n, alpha, beta, boundary=-1)
    # stochastic domination, tested on every upper set
    diffs = [sum(p for s, p in plus.items() if all(s[i] >= t[i] for i in range(len(V)))) -
             sum(p for s, p in minus.items() if all(s[i] >= t[i] for i in range(len(V))))
             for t in itertools.product([-1, 1], repeat=len(V))]
    note("plus dominates minus on every upper set", max(-d for d in diffs) <= 1e-12,
         f"the excess of P_plus over P_minus ranges from {min(diffs):+.6f} to {max(diffs):+.6f} "
         f"over {len(diffs)} upper sets")

    # monotonicity in the volume: the plus measure on the smaller block magnetises more
    d, L, alpha, beta = 1, 2, 0.5, 0.5
    small, Vs, _ = ising_block(d, L, 1, alpha, beta, boundary=1)
    big, Vb, _ = ising_block(d, L, 2, alpha, beta, boundary=1)
    ms = sum(p * s[0] for s, p in small.items())
    # site 0 of Lambda_2 is also index 0 of Lambda_1 under the coordinate convention
    mb = sum(p * s[0] for s, p in big.items())
    note("plus measure decreases with the volume", mb <= ms + 1e-12,
         f"E[sigma_0] under Lambda_1: {ms:.6f}, under Lambda_2: {mb:.6f}")

    # the one-site identity, and the bound of the proposition, in finite volume
    d, L, alpha, beta, n = 1, 2, 0.5, 0.7, 3
    tab, V, bmass = ising_block(d, L, n, alpha, beta, boundary=1)
    N = len(V)
    m = sum(p * s[0] for s, p in tab.items())
    rhs = sum(p * math.tanh(beta * (sum(L ** (-(d + alpha) * lev(V[0], V[c], d)) * s[c]
                                        for c in range(1, N)) + bmass[0]))
              for s, p in tab.items())
    inside = sum(L ** (-(d + alpha) * lev(V[0], V[c], d)) for c in range(1, N))
    bound = math.tanh(beta * (inside + bmass[0]))
    note("plus state is magnetised at finite volume", m > 1e-3,
         f"E[sigma_0] = {m:.6f} under the plus boundary condition")
    note("one-site Gibbs identity under plus", abs(m - rhs) < 1e-12,
         f"E[sigma_0] = {m:.12f} against E[tanh(beta H)] = {rhs:.12f}")
    note("order parameter below the tanh bound", m <= bound + 1e-12,
         f"E[sigma_0] = {m:.6f} <= tanh(total mass) = {bound:.6f}")

    # Griffiths: correlations dominate the product, and so M squared
    worst = min(sum(p * s[0] * s[1] for s, p in tab.items()) -
                sum(p * s[0] for s, p in tab.items()) * sum(p * s[1] for s, p in tab.items())
                for _ in [0])
    note("positive correlations", worst >= -1e-12,
         f"E[s0 s1] - E[s0]E[s1] = {worst:+.6f}")


def check_block_average():
    """Block average equals the single-site magnetisation; the bound in any boundary field; the variance identity."""
    d, L, alpha, beta = 1, 2, 0.5, 0.9
    rows = []
    for n in (1, 2, 3):
        tab, V, bmass = ising_block(d, L, n, alpha, beta, boundary=1)
        per_site = {x: sum(p * s[x] for s, p in tab.items()) for x in range(len(V))}
        block = sum(p * sum(s) for s, p in tab.items()) / L ** (d * n)
        rows.append((n, min(per_site.values()), max(per_site.values()), block))
    flat = max(r[2] - r[1] for r in rows)
    identity = max(abs(r[3] - r[2]) for r in rows)
    note("plus state: every vertex of the block is equivalent", flat < 1e-12,
         f"largest spread of E[sigma_x] within a block over n=1,2,3: {flat:.2e}")
    note("block average equals the single-site magnetisation", identity < 1e-12,
         f"largest discrepancy: {identity:.2e}; values {[round(r[3], 6) for r in rows]}")
    note("block average decreases with the volume", rows[0][3] > rows[1][3] > rows[2][3],
         f"M_n = {[round(r[3], 6) for r in rows]}")

    # the bound |E[S]| <= m^n max_x E_{P^+}[sigma_x], for every constant boundary field
    n = 2
    tab_plus, V, bmass = ising_block(d, L, n, alpha, beta, boundary=1)
    cap = max(sum(p * s[x] for s, p in tab_plus.items()) for x in range(len(V))) * L ** (d * n)
    worst = 0.0
    for t in (-1.0, -0.6, -0.2, 0.0, 0.35, 0.8, 1.0):
        tab, _, _ = ising_block(d, L, n, alpha, beta, boundary=t)
        worst = max(worst, abs(sum(p * sum(s) for s, p in tab.items())) / cap)
    note("block average is bounded by the order parameter", worst <= 1 + 1e-12,
         f"largest |E[S]| / (m^n max_x E_+[sigma_x]) over seven boundary fields: {worst:.4f}")

    # the variance identity, by Gauss-Legendre quadrature in the boundary field
    nodes, weights = np.polynomial.legendre.leggauss(40)  # on [-1, 1]
    B = bmass[0]
    acc = 0.0
    for t, w in zip(nodes, weights):
        tab, _, _ = ising_block(d, L, n, alpha, beta, boundary=float(t))
        S = {s: sum(s) for s in tab}
        m1 = sum(p * S[s] for s, p in tab.items())
        m2 = sum(p * S[s] ** 2 for s, p in tab.items())
        acc += w * (m2 - m1 * m1)
    lhs = sum(p * sum(s) for s, p in tab_plus.items())
    rhs = 0.5 * beta * B * acc
    note("block magnetisation is the integrated boundary-induced variance", abs(lhs - rhs) < 1e-9 * max(1.0, abs(lhs)),
         f"E_+[S] = {lhs:.9f} against beta B / 2 times the integral of Var = {rhs:.9f}")


def check_variance_sandwich():
    """GHS monotonicity, and the sandwich between M_n and the two block-spin variances."""
    d, L, alpha = 1, 2, 0.5
    C = total_mass(d, L, alpha)
    for beta in (0.5, 0.8284271, 1.2):
        worst = 0.0
        for n in (2, 3):
            vars_by_t = []
            for t in np.linspace(0.0, 1.0, 11):
                tab, _, _ = ising_block(d, L, n, alpha, beta, boundary=float(t))
                S = {s: sum(s) for s in tab}
                m1 = sum(p * S[s] for s, p in tab.items())
                m2 = sum(p * S[s] ** 2 for s, p in tab.items())
                vars_by_t.append(m2 - m1 * m1)
            rise = max(vars_by_t[i + 1] - vars_by_t[i] for i in range(len(vars_by_t) - 1))
            worst = max(worst, rise)
        note(f"block-spin variance decreases in the boundary field (beta={beta})", worst < 1e-9,
             f"largest rise along t in [0,1]: {worst:.2e}, "
             f"variance from t=0 to t=1: {vars_by_t[0]:.3f} -> {vars_by_t[-1]:.3f}")

        rows = []
        for n in (2, 3):
            mn = L ** (d * n)
            scale = L ** ((d + alpha) * n)
            plus, _, _ = ising_block(d, L, n, alpha, beta, boundary=1.0)
            free, _, _ = ising_block(d, L, n, alpha, beta, boundary=0.0)
            S = {s: sum(s) for s in plus}

            def moments(tab):
                m1 = sum(p * sum(s) for s, p in tab.items())
                m2 = sum(p * sum(s) ** 2 for s, p in tab.items())
                return m1, m2 - m1 * m1

            e_plus, v_plus = moments(plus)
            _, v_free = moments(free)
            Mn = e_plus / mn
            lo = beta * C * v_plus / scale
            hi = beta * C * v_free / scale
            ok = lo <= Mn + 1e-12 and Mn <= hi + 1e-12
            rate = L ** (-(d - alpha) * n) / (beta * C)
            ok = ok and v_plus / mn ** 2 <= rate + 1e-12 and v_free / mn ** 2 >= Mn * rate - 1e-12
            rows.append((n, Mn, lo, hi, v_plus / mn ** 2, rate, v_free / mn ** 2))
        note(f"variance sandwich and concentration rates (beta={beta})",
             all(r[2] <= r[1] + 1e-12 and r[1] <= r[3] + 1e-12 and r[4] <= r[5] + 1e-12
                 and r[6] >= r[1] * r[5] - 1e-12 for r in rows),
             "; ".join(f"n={n}: M_n={Mn:.3f} in [{lo:.3f},{hi:.3f}], Var_+(Y)={vp:.4f} <= {rate:.4f}, "
                       f"Var_free(Y)={vf:.3f} >= {Mn * rate:.4f}"
                       for n, Mn, lo, hi, vp, rate, vf in rows))


def check_finite_volume_magnetisation():
    """Every finite-volume plus state is magnetised, at every positive intensity."""
    d, L, alpha = 1, 2, 0.5
    rows = []
    for beta in (0.05, 0.2, 0.6, 1.5):
        for n in (2, 3):
            tab, V, _ = ising_block(d, L, n, alpha, beta, boundary=1.0)
            m = sum(p * s[0] for s, p in tab.items())
            rows.append((beta, n, m))
    by_n = {}
    for beta, n, m in rows:
        by_n.setdefault(n, []).append(m)
    increasing = all(all(a < b for a, b in zip(v, v[1:])) for v in by_n.values())
    note("finite-volume plus states are magnetised at every intensity",
         all(r[2] > 0 for r in rows) and increasing and rows[0][2] < 0.1,
         "M_n = " + ", ".join(f"beta={b}, n={n}: {m:.2e}" for b, n, m in rows))


def check_free_energy_series():
    """The Gaussian per-scale terms against direct quadrature, and the divergence of the curvature."""
    L, d, alpha = 2, 1, 0.5
    m = L ** d
    xs, ws = np.polynomial.hermite.hermgauss(60)
    worst = 0.0
    for beta in (0.3, 0.7):
        for k in (1, 2):
            mass = (1 - L ** -d) * sum(L ** (-alpha * j) for j in range(1, k))
            v = m ** (k - 1) / (1 - beta * mass)
            b = beta * L ** (-(d + alpha) * k)
            # direct: int int exp(b s1 s2) N(0,v) N(0,v), by Gauss-Hermite (m = 2 children)
            s1 = np.sqrt(2 * v) * xs
            quad = float(np.sum(np.outer(ws, ws) * np.exp(b * np.outer(s1, s1))) / np.pi)
            closed = (1 - b * (m - 1) * v) ** -0.5 * (1 + b * v) ** (-(m - 1) / 2.0)
            worst = max(worst, abs(quad - closed) / closed)
    note("Gaussian per-scale term: closed form against quadrature", worst < 1e-10,
         f"largest relative difference over two intensities and two scales: {worst:.2e}")

    def second(beta, hh):
        return (simulate.free_energy(beta + hh, L, d, alpha) - 2 * simulate.free_energy(beta, L, d, alpha)
                + simulate.free_energy(beta - hh, L, d, alpha)) / hh ** 2

    beta_c = 1 / ((1 - L ** -d) / (L ** alpha - 1))
    low = beta_c ** 2 * second(beta_c * 0.5, 1e-4)
    high = beta_c ** 2 * second(beta_c * 0.95, 1e-4)
    note("the heat capacity grows towards the critical intensity", high > 5 * low > 0,
         f"C at half the critical intensity {low:.3f}, at 0.95 of it {high:.3f}")


def ising_free_energy_fft(beta, n, L=2, d=1, alpha=0.5):
    """F_n for Ising spins by the convolution recursion: the method of the free-energy article."""
    m = L ** d
    N = 1
    law = np.zeros(2 * N + 1)
    law[0] = law[2] = 0.5
    F = 0.0
    for k in range(1, n + 1):
        b = beta * L ** (-(d + alpha) * k)
        S = np.arange(-N, N + 1, dtype=float)
        with np.errstate(divide="ignore"):
            log_t = np.where(law > 0, np.log(np.maximum(law, 1e-300)), -np.inf) - 0.5 * b * S * S
        tilde = np.exp(log_t)
        size = 1
        while size < 2 * len(tilde) - 1:
            size *= 2
        conv = np.fft.irfft(np.fft.rfft(tilde, size) ** 2, size)[:2 * len(tilde) - 1]
        conv = np.maximum(conv, 0.0)
        S2 = np.arange(-2 * N, 2 * N + 1, dtype=float)
        with np.errstate(divide="ignore"):
            log_un = np.where(conv > 0, np.log(conv), -np.inf) + 0.5 * b * S2 * S2
        mx = np.max(log_un)
        logZ = mx + math.log(np.sum(np.exp(log_un - mx)))
        F += m ** (-k) * logZ
        law = np.exp(log_un - logZ)
        N *= 2
    return F


def ising_free_energy_exact(beta, n, L=2, d=1, alpha=0.5):
    """F_n by exact enumeration of the block-spin laws, for small n."""
    m = L ** d
    law = {-1.0: 0.5, 1.0: 0.5}
    F = 0.0
    for k in range(1, n + 1):
        b = beta * L ** (-(d + alpha) * k)
        Z = sum(p * q * math.exp(b * s * t) for s, p in law.items() for t, q in law.items())
        F += m ** (-k) * math.log(Z)
        new = {}
        for s, p in law.items():
            for t, q in law.items():
                u = s + t
                new[u] = new.get(u, 0.0) + p * q * math.exp(b * s * t) / Z
        law = new
    return F


def check_ising_free_energy():
    """The convolution recursion against enumeration, and the table of the free-energy article."""
    worst = max(abs(ising_free_energy_fft(beta, 4) - ising_free_energy_exact(beta, 4))
                for beta in (0.3, 0.8))
    note("Ising free energy: convolution recursion against enumeration", worst < 1e-11,
         f"largest difference at n=4: {worst:.2e}")

    table = re.findall(r"<tr><td>(\d\.\d\d)</td><td>([\d.]+)</td><td>([\d.]+)</td><td>([\d.]+)</td></tr>", 
                       (Path("wiki/articles/hierarchical-free-energy.md")).read_text())
    worst = 0.0
    for beta, f12, f16, f20 in table:
        worst = max(worst, abs(ising_free_energy_fft(float(beta), 12) - float(f12)),
                    abs(ising_free_energy_fft(float(beta), 16) - float(f16)),
                    abs(ising_free_energy_fft(float(beta), 20) - float(f20)))
    note("Ising free energy: the table of the article is what the recursion gives", len(table) == 4 and worst < 1e-7,
         f"{len(table)} rows compared, largest difference {worst:.2e}")


def main() -> int:
    check_variance()
    check_beta_c()
    check_multiplier()
    check_block_identity()
    check_decimation_ising()
    check_triangle()
    check_quartic_generation()
    check_gaussian_spectrum()
    check_boundary_field()
    check_conditional_lipschitz()
    check_free_measure_conditional()
    check_ferromagnetic_phase()
    check_block_average()
    check_variance_sandwich()
    check_finite_volume_magnetisation()
    check_free_energy_series()
    check_ising_free_energy()
    bad = [r for r in RESULTS if not r[1]]
    print(f"\n{len(RESULTS) - len(bad)} passed, {len(bad)} failed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
