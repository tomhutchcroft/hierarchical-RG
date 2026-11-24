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


def main() -> int:
    check_variance()
    check_beta_c()
    check_multiplier()
    check_block_identity()
    check_decimation_ising()
    check_triangle()
    bad = [r for r in RESULTS if not r[1]]
    print(f"\n{len(RESULTS) - len(bad)} passed, {len(bad)} failed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
