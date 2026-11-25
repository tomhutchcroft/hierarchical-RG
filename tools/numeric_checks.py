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

import numpy as np

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
    bad = [r for r in RESULTS if not r[1]]
    print(f"\n{len(RESULTS) - len(bad)} passed, {len(bad)} failed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
