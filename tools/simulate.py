#!/usr/bin/env python3
"""Data for the wiki's simulations.

Every figure on the site is driven by numbers computed here, in Python, and embedded in the page
as JSON; the browser code in wiki/static/sim.js only draws them, except for the exponent
calculator and the percolation model, whose arithmetic is in the page and is tested against the
reference functions in this file by tools/test_sim.py.

Usage: python3 tools/simulate.py            # summary
       from simulate import build; build()  # dict of every simulation's data
"""
from __future__ import annotations

import itertools
import json
import math

# ---------------------------------------------------------------- hierarchical geometry


def children_index(x, y, d):
    """Level of the pair (x, y): the index of the last coordinate at which they differ."""
    out = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            out = i // d + 1
    return out


def vertices(d, L, n):
    return list(itertools.product(range(L), repeat=d * n))


# ---------------------------------------------------------------- 1. Gaussian renormalisation orbit


def flat_params(L=2, d=1, alpha=0.5, J=1.0):
    m = L ** d
    row = J * (1 - L ** (-d)) * L ** (-alpha) / (1 - L ** (-alpha))
    return m, row


def variance_orbit(beta, n_max=24, L=2, d=1, alpha=0.5, J=1.0):
    """v_n for the Gaussian block-spin recursion, stopping at the first non-positive v."""
    m = L ** d
    v, out = 1.0, [1.0]
    for k in range(1, n_max + 1):
        b = beta * J * L ** (-(d + alpha) * k)
        denom = 1 - b * v * (m - 1)
        if denom <= 0:
            break
        v = m * v / denom
        out.append(v)
    return out


def sim_rg_orbit(L=2, d=1, alpha=0.5, n_max=24, n_beta=25):
    m, row = flat_params(L, d, alpha)
    beta_c = 1.0 / row
    betas = [beta_c * (0.15 + 1.15 * i / (n_beta - 1)) for i in range(n_beta)]
    curves = []
    for b in betas:
        v = variance_orbit(b, n_max, L, d, alpha)
        v = v + [None] * (n_max + 1 - len(v))
        curves.append([None if x is None or x <= 0 else round(math.log10(x), 6) for x in v])
    crit = variance_orbit(beta_c, n_max, L, d, alpha)
    crit = [round(math.log10(x), 6) for x in crit]
    u_star = m * (L ** alpha - 1) / (m - 1)
    return {"beta_c": beta_c, "u_star": u_star, "betas": [round(b, 6) for b in betas],
            "curves": curves, "critical": crit, "alpha": alpha, "L": L, "d": d, "m": m,
            "n_max": n_max,
            "theory": {"nu": 1 / alpha, "theta": (d + alpha) / 2}}


# ---------------------------------------------------------------- 2. exponents


def exponent_table(d, L, alpha):
    """The classical (Gaussian fixed point) exponents and the scaling relations."""
    kappa = alpha
    nu = 1 / alpha
    eta = 2 - kappa
    gamma = kappa * nu
    beta_o = nu * (d - kappa) / 2
    delta = (d + kappa) / (d - kappa)
    alpha_hy = 2 - d * nu
    return {"kappa": kappa, "nu": nu, "eta": eta, "gamma": gamma,
            "betaO": beta_o, "delta": delta, "alphaHy": alpha_hy,
            "fisher": gamma - nu * (2 - eta),
            "widom": gamma - beta_o * (delta - 1),
            "hyperscaling": 2 - alpha_hy - d * nu}


def sim_exponents():
    grid = []
    for d in (1, 2, 3):
        for L in (2, 3):
            for alpha in (0.2, 0.4, 0.6, 0.9, 0.95):
                if alpha >= d:
                    continue
                grid.append({"d": d, "L": L, "alpha": alpha, "table": exponent_table(d, L, alpha)})
    return {"grid": grid}


# ---------------------------------------------------------------- 3. the triangle diagram


def tau_kernel(level, d=1.0, L=2.0, alpha=0.5):
    return 1.0 if level == 0 else L ** (-(d - alpha) * level)


def triangle_partials(alpha, n_max=11, d=1, L=2):
    """S_N = sum over pairs in the block of the three point product; the increments are
    of order L^((3 alpha - d) N), which is the statement the article proves."""
    out = []
    for n in range(0, n_max + 1):
        V = vertices(d, L, n)
        c = [tau_kernel(0)] + [tau_kernel(k, d, L, alpha) for k in range(1, n + 1)]
        total = 0.0
        for x in V:
            cx = c[children_index(tuple([0] * (d * n)), x, d)]
            for y in V:
                total += cx * c[children_index(x, y, d)] * c[children_index(tuple([0] * (d * n)), y, d)]
        out.append(total)
    return out


def sim_triangle(n_max=9, d=1, L=2):
    alphas = [0.05 + 0.05 * i for i in range(13)]      # 0.05 .. 0.65, threshold at 1/3 for d=1
    curves = []
    for a in alphas:
        S = triangle_partials(a, n_max, d, L)
        curves.append({"alpha": round(a, 4),
                       "S": [round(x, 8) for x in S],
                       "log10": [round(math.log10(max(x, 1e-12)), 6) for x in S]})
    return {"d": d, "L": L, "threshold": d / 3.0, "n_max": n_max, "curves": curves}


# ---------------------------------------------------------------- 4. percolation (reference)


def percolation_edges(n, L, d, alpha, bits, beta):
    """Open edges of the hierarchical block of level n, decided by the given bits."""
    J = lambda k: L ** (-(d + alpha) * k)
    p = lambda k: 1 - math.exp(-beta * J(k))
    V = vertices(d, L, n)
    edges = []
    i = 0
    for a in range(len(V)):
        for b in range(a + 1, len(V)):
            k = children_index(V[a], V[b], d)
            edges.append((a, b, k, bits[i % len(bits)] < p(k)))
            i += 1
    return edges


def cluster_of_zero(n, L, d, alpha, bits, beta):
    """Cluster of vertex 0 under the edge set, by union-find (the reference for sim.js)."""
    V = vertices(d, L, n)
    parent = list(range(len(V)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b, k, open_ in percolation_edges(n, L, d, alpha, bits, beta):
        if open_:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
    r = find(0)
    return [i for i in range(len(V)) if find(i) == r]


def build() -> dict:
    return {"rg-orbit": sim_rg_orbit(), "exponents": sim_exponents(), "triangle": sim_triangle(),
            "ising-block": ising_block()}


if __name__ == "__main__":
    data = build()
    orbit = data["rg-orbit"]
    print(f"rg-orbit: beta_c={orbit['beta_c']:.6f}, {len(orbit['betas'])} curves, "
          f"critical log10 v_{orbit['n_max']}={orbit['critical'][-1]:.3f}")
    print(f"exponents: {len(data['exponents']['grid'])} parameter points")
    tri = data["triangle"]
    print(f"triangle: {len(tri['curves'])} exponents, threshold {tri['threshold']:.3f}, "
          f"alpha={tri['curves'][0]['alpha']}: S_11={tri['curves'][0]['S'][-1]:.3f}, "
          f"alpha={tri['curves'][-1]['alpha']}: S_11={tri['curves'][-1]['S'][-1]:.3f}")
    print("percolation reference: |K_0| =", len(cluster_of_zero(4, 2, 1, 0.5, [0.5] * 2000, 1.2)))


# ---------------------------------------------------------------- static figures (inline SVG)

SVG_HEAD = '<svg viewBox="0 0 {w} {h}" class="fig-svg" role="img" aria-label="{label}">'


def _svg(w, h, label, body):
    return f'<svg viewBox="0 0 {w} {h}" class="fig-svg" role="img" aria-label="{label}">' + body + "</svg>"


def fig_lattice_children():
    """A level-2 block of the hierarchical lattice with L=2, d=1: two children, two levels."""
    W, H = 560, 250
    sites = [70 + 110 * i for i in range(4)]
    y0 = 190
    parts = [f'<line x1="30" y1="{y0}" x2="{W-30}" y2="{y0}" class="fg-axis"/>']
    for i, x in enumerate(sites):
        parts.append(f'<circle cx="{x}" cy="{y0}" r="7" class="fg-site"/>')
        parts.append(f'<text x="{x}" y="{y0+26}" text-anchor="middle">{i}</text>')
    # children of the level-2 block
    for lo, hi in ((0, 1), (2, 3)):
        x1, x2 = sites[lo] - 26, sites[hi] + 26
        parts.append(f'<rect x="{x1}" y="{y0-30}" width="{x2-x1}" height="60" class="fg-box"/>')
    parts.append('<text x="125" y="' + str(y0 + 58) + '" text-anchor="middle" class="fg-small">child 1 (a coset of the level-1 block)</text>')
    parts.append('<text x="435" y="' + str(y0 + 58) + '" text-anchor="middle" class="fg-small">child 2</text>')
    # level-1 pairs and level-2 pairs
    parts.append(f'<path d="M{sites[0]} {y0-34} V110 H{sites[1]} V{y0-34}" class="fg-level1"/>')
    parts.append(f'<path d="M{sites[2]} {y0-34} V110 H{sites[3]} V{y0-34}" class="fg-level1"/>')
    parts.append(f'<path d="M{sites[0]} 96 V60 H{sites[3]} V96" class="fg-level2"/>')
    parts.append('<text x="125" y="105" text-anchor="middle" class="fg-small">level 1: distance L</text>')
    parts.append('<text x="280" y="52" text-anchor="middle" class="fg-small">level 2: every cross pair has distance L²</text>')
    return _svg(W, H, "children of a block", "".join(parts))


def fig_flow():
    """The flow of the two-coupling truncation: two fixed points and the critical trajectory."""
    W, H = 560, 300
    p = [f'<line x1="60" y1="{H-50}" x2="{W-24}" y2="{H-50}" class="fg-axis"/>',
         f'<line x1="60" y1="{H-50}" x2="60" y2="30" class="fg-axis"/>',
         f'<text x="{W-30}" y="{H-22}" text-anchor="end" class="fg-small">quartic coupling</text>',
         '<text x="16" y="40" class="fg-small" transform="rotate(-90 16 40)">mass</text>']
    p.append('<circle cx="110" cy="120" r="6" class="fg-fp"/>')
    p.append('<text x="122" y="118" class="fg-small">Gaussian fixed point</text>')
    p.append('<circle cx="400" cy="90" r="6" class="fg-fp"/>')
    p.append('<text x="412" y="88" class="fg-small">nontrivial fixed point</text>')
    p.append('<path d="M110 120 C 200 116, 320 104, 400 90" class="fg-critical"/>')
    for t in (0.12, 0.32, 0.55, 0.8):
        x = 110 + t * 290
        y = 120 - t * 30 - 8 * math.sin(3.14 * t)
        p.append(f'<path d="M{x} {y} l10 -1" class="fg-arrow"/>')
    p.append('<text x="250" y="70" class="fg-small">critical trajectory: one relevant direction along it</text>')
    for x0 in (150, 200, 250, 300, 350):
        p.append(f'<path d="M{x0} {H-55} C {x0+10} {H-110}, {x0-20} 200, 80 190" class="fg-flow"/>')
    p.append(f'<text x="150" y="{H-64}" class="fg-small">flow below criticality: to the disordered side</text>')
    return _svg(W, H, "flow diagram", "".join(p))


def fig_decimation():
    """One decimation step: m children, the tilt, and the block spin."""
    W, H = 560, 220
    p = []
    xs = [90, 190, 290, 390]
    for i, x in enumerate(xs):
        p.append(f'<rect x="{x-34}" y="120" width="68" height="60" rx="6" class="fg-box"/>')
        p.append(f'<text x="{x}" y="156" text-anchor="middle">child {i+1}</text>')
        p.append(f'<text x="{x}" y="196" text-anchor="middle" class="fg-small">law μ</text>')
    p.append('<text x="240" y="108" text-anchor="middle" class="fg-small">independent, tilted by exp(b Σ sᵢsⱼ)</text>')
    for x in xs:
        p.append(f'<path d="M{x} 120 C {x} 80, 240 70, 250 52" class="fg-flow"/>')
    p.append('<rect x="196" y="20" width="110" height="34" rx="6" class="fg-result"/>')
    p.append('<text x="251" y="42" text-anchor="middle">block spin S</text>')
    p.append('<text x="320" y="34" class="fg-small">law 𝒯_b μ</text>')
    return _svg(W, H, "one decimation step", "".join(p))


def fig_boundary():
    """The coupling of a block to its complement: decaying per vertex, growing in total below alpha = d."""
    d, L, J = 1, 2, 1.0
    alphas = [(0.4, "#1c5a8a"), (0.8, "#4a7a1c"), (1.2, "#8a1c1c")]
    W, H = 560, 290
    pad = {"l": 56, "r": 126, "t": 30, "b": 42}
    n_max = 8
    ymin, ymax = 0.03, 80.0

    def X(n):
        return pad["l"] + n / n_max * (W - pad["l"] - pad["r"])

    def Y(v):
        t = (math.log(v) - math.log(ymin)) / (math.log(ymax) - math.log(ymin))
        return H - pad["b"] - t * (H - pad["t"] - pad["b"])

    def path(values, colour, width, dash=""):
        """Polyline, broken where it leaves the frame, so that no curve is drawn flat on the axis."""
        pts, out = [], []
        for n, v in enumerate(values):
            if v < ymin:
                if len(pts) > 1:
                    out.append(f'<path d="{" ".join(pts)}" fill="none" stroke="{colour}" '
                               f'stroke-width="{width}"{dash}/>')
                pts = []
                continue
            pts.append(("M" if not pts else "L") + f"{X(n):.1f} {Y(min(v, ymax)):.1f}")
        if len(pts) > 1:
            out.append(f'<path d="{" ".join(pts)}" fill="none" stroke="{colour}" stroke-width="{width}"{dash}/>')
        return "".join(out)

    p = [f'<line x1="{pad["l"]}" y1="{H-pad["b"]}" x2="{W-pad["r"]}" y2="{H-pad["b"]}" class="fg-axis"/>',
         f'<line x1="{pad["l"]}" y1="{pad["t"]}" x2="{pad["l"]}" y2="{H-pad["b"]}" class="fg-axis"/>']
    for v, label in ((0.1, "0.1"), (1.0, "1"), (10.0, "10")):
        p.append(f'<line x1="{pad["l"]}" y1="{Y(v):.1f}" x2="{W-pad["r"]}" y2="{Y(v):.1f}" '
                 f'stroke="#e3e3e6" stroke-width="1"/>')
        p.append(f'<text x="{pad["l"]-8}" y="{Y(v)+4:.1f}" text-anchor="end" class="fg-small">{label}</text>')
    for n in range(0, n_max + 1, 2):
        p.append(f'<text x="{X(n):.1f}" y="{H-pad["b"]+18}" text-anchor="middle" class="fg-small">{n}</text>')
    p.append(f'<text x="{(pad["l"]+W-pad["r"])/2:.0f}" y="{H-8}" text-anchor="middle" class="fg-small">'
             f'block level n</text>')
    p.append(f'<text x="{pad["l"]}" y="{pad["t"]-10}" class="fg-small">'
             f'solid: |\u039b\u2099| B\u2099 (total)   dashed: B\u2099 (per vertex)   d = 1, L = 2</text>')
    legend = []
    for i, (alpha, colour) in enumerate(alphas):
        row = J * (1 - L ** (-d)) * L ** (-alpha) / (1 - L ** (-alpha))
        per = [row * L ** (-alpha * n) for n in range(0, n_max + 1)]
        tot = [per[n] * L ** (d * n) for n in range(0, n_max + 1)]
        p.append(path(tot, colour, 2))
        p.append(path(per, colour, 1.6, ' stroke-dasharray="5 4"'))
        ly = pad["t"] + 10 + 22 * i
        legend.append(f'<path d="M{W-pad["r"]+10} {ly} l18 0" stroke="{colour}" stroke-width="2"/>')
        legend.append(f'<path d="M{W-pad["r"]+10} {ly+8} l18 0" stroke="{colour}" stroke-width="1.6" '
                      f'stroke-dasharray="5 4"/>')
        legend.append(f'<text x="{W-pad["r"]+34}" y="{ly+6}" class="fg-small">alpha = {alpha}</text>')
    return _svg(W, H, "the boundary field of a block", "".join(p + legend))


# ---------------------------------------------------------------- 5. percolation tail (sampled twice)

def percolation_bits(n, L, d, seed):
    """The uniform stream of sim.js's SIM.rng for one realisation, in the same order."""
    total = len(vertices(d, L, n)) * (len(vertices(d, L, n)) - 1) // 2
    state = (seed & 0xFFFFFFFF) or 1
    out = []
    for _ in range(total + 8):
        state = (state * 1664525 + 1013904223) & 0xFFFFFFFF
        out.append(state / 4294967296)
    return out


def percolation_clusters(n, L, d, alpha, beta, seed):
    """Sizes of every cluster of the block for one realisation: the twin in sim.js is SIM.percolationClusters."""
    V = vertices(d, L, n)
    size = len(V)
    bits = percolation_bits(n, L, d, seed)
    parent = list(range(size))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    t = 0
    for i in range(size):
        for j in range(i + 1, size):
            k = children_index(V[i], V[j], d)
            if bits[t % len(bits)] < 1 - math.exp(-beta * L ** (-(d + alpha) * k)):
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
            t += 1
    counts = {}
    for i in range(size):
        r = find(i)
        counts[r] = counts.get(r, 0) + 1
    return sorted(counts.values(), reverse=True)


def percolation_cluster_sizes(n, L, d, alpha, beta, seeds):
    """The list of cluster sizes of each realisation, for the seeds given."""
    return [percolation_clusters(n, L, d, alpha, beta, s) for s in seeds]


def percolation_density(sizes, N):
    """n_s: the number of clusters of size s per vertex, for s = 1..N."""
    out = [0] * (N + 1)
    for real in sizes:
        for sz in real:
            out[sz] += 1
    return [c / (N * len(sizes)) for c in out]


def percolation_mean_cluster(sizes, N):
    """The mean size of the finite cluster of a random vertex, the largest cluster excluded.

    Excluding the largest cluster is what makes this a susceptibility proxy: with it included the
    statistic is maximised by the fully connected block rather than at the transition.
    """
    tot = 0.0
    for real in sizes:
        finite = real[1:] if len(real) > 1 else []
        tot += sum(sz * sz for sz in finite) / N
    return tot / len(sizes)


def percolation_threshold(n, L, d, alpha, seeds):
    """The intensity maximising the sampled mean cluster size: a finite-block pseudocritical intensity."""
    N = L ** (d * n)
    best, best_beta = -1.0, 1.0
    lo, hi, steps = 0.2, 6.0, 3
    for _ in range(steps):
        for beta in (lo + (hi - lo) * i / 4 for i in range(5)):
            chi = percolation_mean_cluster(percolation_cluster_sizes(n, L, d, alpha, beta, seeds), N)
            if chi > best:
                best, best_beta = chi, beta
        lo, hi = max(0.05, best_beta - (hi - lo) / 4), best_beta + (hi - lo) / 4
    return best_beta


def fig_percolation_tail():
    """The sampled cluster-size distribution on a level-6 block at three intensities, with the predicted slope."""
    n, L, d, alpha = 6, 2, 1, 0.5
    N = L ** (d * n)
    seeds = list(range(1, 201))
    beta_c = percolation_threshold(n, L, d, alpha, list(range(1, 61)))
    curves = [(beta_c / 2, "#1c5a8a", "beta = beta*/2"), (beta_c, "#8a1c1c", "beta = beta*"),
              (2 * beta_c, "#4a7a1c", "beta = 2 beta*")]
    W, H = 560, 330
    pad = {"l": 62, "r": 150, "t": 34, "b": 46}
    xmax = float(N)
    floor = 1.0 / (N * len(seeds))

    def X(k):
        return pad["l"] + math.log(k) / math.log(xmax) * (W - pad["l"] - pad["r"])

    def Y(v):
        v = max(min(v, 1.0), floor)
        t = (math.log(v) - math.log(floor)) / (0.0 - math.log(floor))
        return H - pad["b"] - t * (H - pad["t"] - pad["b"])

    p = [f'<line x1="{pad["l"]}" y1="{H-pad["b"]}" x2="{W-pad["r"]}" y2="{H-pad["b"]}" class="fg-axis"/>',
         f'<line x1="{pad["l"]}" y1="{pad["t"]}" x2="{pad["l"]}" y2="{H-pad["b"]}" class="fg-axis"/>']
    for v, label in ((1.0, "1"), (0.1, "0.1"), (0.01, "0.01"), (1e-3, "0.001")):
        if v < floor:
            continue
        p.append(f'<line x1="{pad["l"]}" y1="{Y(v):.1f}" x2="{W-pad["r"]}" y2="{Y(v):.1f}" '
                 f'stroke="#e3e3e6" stroke-width="1"/>')
        p.append(f'<text x="{pad["l"]-8}" y="{Y(v)+4:.1f}" text-anchor="end" class="fg-small">{label}</text>')
    for k in (1, 2, 4, 8, 16, 32, 64):
        p.append(f'<text x="{X(k):.1f}" y="{H-pad["b"]+18}" text-anchor="middle" class="fg-small">{k}</text>')
    p.append(f'<text x="{(pad["l"]+W-pad["r"])/2:.0f}" y="{H-8}" text-anchor="middle" class="fg-small">'
             f'cluster size s</text>')
    p.append(f'<text x="{pad["l"]}" y="{pad["t"]-14}" class="fg-small">clusters of size s per vertex</text>')

    legend, dens = [], {}
    for beta, colour, label in curves:
        ns = percolation_density(percolation_cluster_sizes(n, L, d, alpha, beta, seeds), N)
        dens[beta] = ns
        pts = [(k, ns[k]) for k in range(1, N + 1) if ns[k] > 0]
        path = " ".join(("M" if i == 0 else "L") + f"{X(k):.1f} {Y(v):.1f}" for i, (k, v) in enumerate(pts))
        p.append(f'<path d="{path}" fill="none" stroke="{colour}" stroke-width="2"/>')
        y = pad["t"] + 6 + 22 * len(legend)
        legend.append(f'<path d="M{W-pad["r"]+8} {y} l18 0" stroke="{colour}" stroke-width="2"/>')
        legend.append(f'<text x="{W-pad["r"]+32}" y="{y+4}" class="fg-small">{label}</text>')

    # the predicted slope of n_s, anchored on the critical curve at s = 3
    tau = 2.0 * d / (d + alpha)
    k0, k1 = 2.0, 32.0
    v0 = dens[curves[1][0]][3]
    v1 = v0 * (k1 / 3.0) ** (-tau)
    p.append(f'<path d="M{X(3.0):.1f} {Y(v0):.1f} L{X(k1):.1f} {Y(v1):.1f}" stroke="#8a8f99" '
             f'stroke-width="1.6" stroke-dasharray="6 4"/>')
    p.append(f'<text x="{X(k1)-6:.1f}" y="{Y(v1)+16:.1f}" text-anchor="end" class="fg-small">'
             f'slope -{tau:.2f}, the predicted n_s ~ s^-2d/(d+alpha)</text>')
    p.append(f'<line x1="{X(N):.1f}" y1="{pad["t"]}" x2="{X(N):.1f}" y2="{H-pad["b"]}" '
             f'stroke="#8a8a8a" stroke-width="1" stroke-dasharray="3 3"/>')
    p.append(f'<text x="{X(N)-4:.1f}" y="{pad["t"]+10}" text-anchor="end" class="fg-small">block size</text>')
    return _svg(W, H, "sampled cluster-size distribution", "".join(p + legend))


# ---------------------------------------------------------------- 6. block-spin laws (exact)

def block_spin_laws(n, L, d, alpha, beta):
    """Exact law of the block spin under the plus, free and minus boundary conditions, by enumeration.

    The twin in sim.js is SIM.blockSpinLaws; the article on the magnetised phase displays the three.
    """
    V = vertices(d, L, n)
    N = len(V)
    B = (1 - L ** (-d)) / (L ** alpha - 1) * L ** (-alpha * n)
    out = {}
    for name, t in (("minus", -1.0), ("free", 0.0), ("plus", 1.0)):
        weights = {}
        for s in itertools.product([-1, 1], repeat=N):
            e = 0.0
            for a in range(N):
                for b in range(a + 1, N):
                    e += L ** (-(d + alpha) * children_index(V[a], V[b], d)) * s[a] * s[b]
                e += t * B * s[a]
            weights[s] = math.exp(beta * e)
        Z = sum(weights.values())
        law = {}
        for s, w in weights.items():
            law[sum(s)] = law.get(sum(s), 0.0) + w / Z
        out[name] = {"law": {str(k): law[k] for k in sorted(law)},
                     "mean": sum(k * v for k, v in law.items())}
    return out


# ---------------------------------------------------------------- 7. free energy (Gaussian)

def free_energy_term(k, L, d, alpha, beta):
    """The level-k contribution to the Gaussian free energy, in closed form.

    The tilt is a quadratic form whose matrix has eigenvalue (m-1)/2 along the diagonal direction
    and -1/2 on its complement, so in an orthonormal eigenbasis the Gaussian integral factorises.
    """
    m = L ** d
    mass = (1 - L ** (-d)) * sum(L ** (-alpha * j) for j in range(1, k))   # mass up to level k-1
    v = m ** (k - 1) / (1 - beta * mass)
    Jk = L ** (-(d + alpha) * k)
    a = 1 - beta * Jk * (m - 1) * v      # eigenvalue (m-1)/2 of the tilt, twice
    b = 1 + beta * Jk * v                # eigenvalue -1/2, m-1 times
    if a <= 0:
        return float("inf")
    return m ** (-k) * (-0.5 * math.log(a) - ((m - 1) / 2) * math.log(b))


def free_energy(beta, L=2, d=1, alpha=0.5, terms=80):
    """The Gaussian free energy per site: the sum of the per-scale terms."""
    return sum(free_energy_term(k, L, d, alpha, beta) for k in range(1, terms + 1))


def free_energy_curvature(beta, L=2, d=1, alpha=0.5, terms=80, h=2e-4):
    """The heat capacity beta^2 F'' of the Gaussian model, by central differences with a Richardson step."""
    def second(hh):
        return (free_energy(beta + hh, L, d, alpha, terms)
                - 2 * free_energy(beta, L, d, alpha, terms)
                + free_energy(beta - hh, L, d, alpha, terms)) / hh ** 2
    d2 = (4 * second(h / 2) - second(h)) / 3
    return beta ** 2 * d2


def fig_free_energy():
    """The Gaussian free energy and its curvature against the intensity, with the critical one marked."""
    L, d, alpha = 2, 1, 0.5
    C = (1 - L ** (-d)) / (L ** alpha - 1)
    beta_c = 1 / C
    W, H = 560, 320
    pad = {"l": 56, "r": 150, "t": 24, "b": 46}
    betas = [beta_c * (i / 40.0) for i in range(1, 40)]

    def X(b):
        return pad["l"] + b / beta_c * (W - pad["l"] - pad["r"])

    fvals = [free_energy(b, L, d, alpha) for b in betas]
    cvals = [free_energy_curvature(b, L, d, alpha) for b in betas]
    fmax = max(fvals) * 1.05
    cmax = max(cvals) * 1.05
    p = [f'<line x1="{pad["l"]}" y1="{H-pad["b"]}" x2="{W-pad["r"]}" y2="{H-pad["b"]}" class="fg-axis"/>',
         f'<line x1="{pad["l"]}" y1="{pad["t"]}" x2="{pad["l"]}" y2="{H-pad["b"]}" class="fg-axis"/>']
    for frac in (0.25, 0.5, 0.75, 1.0):
        p.append(f'<text x="{X(beta_c * frac):.1f}" y="{H-pad["b"]+18}" text-anchor="middle" class="fg-small">'
                 f'{frac:.2f}</text>')
    p.append(f'<text x="{(pad["l"]+W-pad["r"])/2:.0f}" y="{H-10}" text-anchor="middle" class="fg-small">'
             f'intensity as a fraction of the critical one</text>')
    p.append(f'<text x="{pad["l"]}" y="{pad["t"]-8}" class="fg-small">free energy F (blue, left) '
             f'and heat capacity (red, scaled)</text>')
    fpath = " ".join(("M" if i == 0 else "L") +
                     f"{X(b):.1f} {H-pad['b'] - (f / fmax) * (H-pad['t']-pad['b']):.1f}"
                     for i, (b, f) in enumerate(zip(betas, fvals)))
    p.append(f'<path d="{fpath}" fill="none" stroke="#1c5a8a" stroke-width="2"/>')
    cpath = " ".join(("M" if i == 0 else "L") +
                     f"{X(b):.1f} {H-pad['b'] - (c / cmax) * (H-pad['t']-pad['b']):.1f}"
                     for i, (b, c) in enumerate(zip(betas, cvals)))
    p.append(f'<path d="{cpath}" fill="none" stroke="#8a1c1c" stroke-width="2"/>')
    p.append(f'<line x1="{X(beta_c):.1f}" y1="{pad["t"]}" x2="{X(beta_c):.1f}" y2="{H-pad["b"]}" '
             f'stroke="#8a8a8a" stroke-width="1" stroke-dasharray="3 3"/>')
    p.append(f'<text x="{X(beta_c)-4:.1f}" y="{pad["t"]+4}" text-anchor="end" class="fg-small">critical</text>')
    p.append(f'<text x="{W-pad["r"]+10}" y="{pad["t"]+16}" class="fg-small">F({betas[-1]:.2f}) = '
             f'{fvals[-1]:.4f}</text>')
    p.append(f'<text x="{W-pad["r"]+10}" y="{pad["t"]+32}" class="fg-small">C near it = '
             f'{cvals[-1]:.1f}</text>')
    return _svg(W, H, "free energy and heat capacity", "".join(p))


def fig_volume_exponent():
    """The cluster-volume exponent against the kernel exponent, with the upper critical dimension marked."""
    d = 1
    W, H = 560, 300
    pad = {"l": 58, "r": 26, "t": 30, "b": 46}
    lo, hi = 0.02, 0.99 * d

    def X(a):
        return pad["l"] + (a - lo) / (hi - lo) * (W - pad["l"] - pad["r"])

    ymax = 6.0

    def Y(v):
        return H - pad["b"] - min(v, ymax) / ymax * (H - pad["t"] - pad["b"])

    p = [f'<line x1="{pad["l"]}" y1="{H-pad["b"]}" x2="{W-pad["r"]}" y2="{H-pad["b"]}" class="fg-axis"/>',
         f'<line x1="{pad["l"]}" y1="{pad["t"]}" x2="{pad["l"]}" y2="{H-pad["b"]}" class="fg-axis"/>']
    for v in (1, 2, 3, 4, 5, 6):
        p.append(f'<line x1="{pad["l"]}" y1="{Y(v):.1f}" x2="{W-pad["r"]}" y2="{Y(v):.1f}" '
                 f'stroke="#e3e3e6" stroke-width="1"/>')
        p.append(f'<text x="{pad["l"]-8}" y="{Y(v)+4:.1f}" text-anchor="end" class="fg-small">{v:g}</text>')
    for a in (0.2, 1 / 3.0, 0.5, 0.7, 0.9):
        p.append(f'<text x="{X(a):.1f}" y="{H-pad["b"]+18}" text-anchor="middle" class="fg-small">'
                 f'{a:.2f}</text>')
    ac = d / 3.0
    p.append(f'<line x1="{X(ac):.1f}" y1="{pad["t"]}" x2="{X(ac):.1f}" y2="{H-pad["b"]}" '
             f'stroke="#8a1c1c" stroke-width="1.4" stroke-dasharray="4 4"/>')
    p.append(f'<text x="{X(ac)+6:.1f}" y="{pad["t"]+12}" class="fg-small">alpha = d/3</text>')
    mean = [X(a) for a in (lo, ac)]
    p.append(f'<path d="M{mean[0]:.1f} {Y(2):.1f} L{mean[1]:.1f} {Y(2):.1f}" stroke="#4a7a1c" stroke-width="2.4"/>')
    pts = []
    steps = 200
    for i in range(steps + 1):
        a = ac + (hi - ac) * i / steps
        v = (d + a) / (d - a)
        if v > ymax:
            break
        pts.append((X(a), Y(v)))
    p.append('<path d="' + " ".join(("M" if i == 0 else "L") + f"{x:.1f} {y:.1f}"
                                    for i, (x, y) in enumerate(pts)) + '" fill="none" stroke="#1c5a8a" stroke-width="2.4"/>')

    p.append(f'<text x="{pad["l"]}" y="{pad["t"]-12}" class="fg-small">'
             f'green: 2 for d &gt; 3 alpha    blue: (d+alpha)/(d-alpha) for d &lt; 3 alpha    d = 1</text>')
    p.append(f'<text x="{(pad["l"]+W-pad["r"])/2:.0f}" y="{H-8}" text-anchor="middle" class="fg-small">'
             f'kernel exponent alpha</text>')
    return _svg(W, H, "the volume exponent against the kernel exponent", "".join(p))


# ---------------------------------------------------------------- what each one computes

#: One line per generated figure: what it computes, and what checks that computation.
FIGURE_NOTES = {
    "lattice-children": ("The children of a level-2 block with $L=2$, $d=1$, with the pairs at each "
                         "level drawn.", "schematic: geometry only"),
    "flow": ("The two-coupling truncation, with the Gaussian and nontrivial fixed points and the "
             "critical trajectory between them.", "schematic: it illustrates the truncation of the "
             "phi-fourth article, not a computed flow"),
    "decimation": ("One decimation step: the children, the tilt and the block spin.",
                   "schematic: the identity it illustrates is checked by numeric_checks.py"),
    "exponents-alpha": ("The classical exponents against the kernel exponent, with the crossover at "
                        "$\\alpha=d/2$ marked.", "the formulas of the exponent dictionary, checked "
                        "by test_sim.py against SIM.exponentTable"),
    "thouless": ("The direction of the block spin below, at and above the critical intensity, which "
                 "is the phenomenon of Bleher and Major.", "schematic: three unit circles of directions"),
    "boundary": ("The coupling of a block to its complement: the field at one vertex, which decays, "
                 "and its sum over the block, which grows below $\\alpha=d$.",
                 "the closed form, checked against direct summation in numeric_checks.py"),
    "percolation-tail": ("The sampled cluster-size distribution on a block of 64 sites at three "
                         "intensities, with the predicted slope as a guide.",
                         "sampled, and the sampler is written twice and compared in test_sim.py"),
    "free-energy": ("The Gaussian free energy per site and its curvature against the intensity, with "
                    "the critical intensity marked.",
                    "the closed-form per-scale terms, checked against direct quadrature in "
                    "numeric_checks.py"),
    "volume-exponent": ("The cluster-volume exponent against the kernel exponent, mean field on one "
                        "side of d = 3 alpha and (d+alpha)/(d-alpha) on the other.",
                        "arithmetic: the two formulas joined at the upper critical dimension"),
}

#: One line per interactive figure.
SIM_NOTES = {
    "rg-orbit": ("The Gaussian orbit of the variance recursion for a range of intensities, against "
                 "the critical one.", "the closed form, computed in Python and served as data"),
    "exponents": ("The exponent table over a grid of kernel exponents.", "SIM.exponentTable, "
                  "checked against the reference in test_sim.py"),
    "triangle": ("The triangle diagram at criticality against its truncation level.",
                 "the sum of the article, computed in Python and checked in numeric_checks.py"),
    "ising-block": ("The exact law of the block spin of sixteen sites, by enumeration.",
                    "exact enumeration, served as data"),
    "ising-mc": ("A heat bath for the Ising model on sixty-four sites.",
                 "SIM.isingSweep, checked bit for bit against the Python twin in test_sim.py"),
    "percolation": ("A percolation realisation on a block, drawn level by level.",
                    "SIM.percolate, checked against the reference clusters in test_sim.py"),
    "domination": ("The exact block-spin laws of the plus, free and minus boundary conditions.",
                   "SIM.blockSpinLaws, checked against the reference in test_sim.py"),
}


def figures() -> dict:
    return {"lattice-children": fig_lattice_children(), "flow": fig_flow(), "decimation": fig_decimation(),
            "exponents-alpha": fig_exponents_alpha(), "thouless": fig_thouless(),
            "boundary": fig_boundary(), "percolation-tail": fig_percolation_tail(),
            "free-energy": fig_free_energy(), "volume-exponent": fig_volume_exponent()}


def fig_exponents_alpha():
    """The classical exponents against the kernel exponent, with the crossover at alpha = d/2."""
    W, H = 560, 300
    pad = {"l": 46, "r": 120, "t": 18, "b": 34}
    lo, hi, ymax, d = 0.12, 0.95, 5.0, 1

    def X(a):
        return pad["l"] + (a - lo) / (hi - lo) * (W - pad["l"] - pad["r"])

    def Y(y):
        return H - pad["b"] - min(y, ymax) / ymax * (H - pad["t"] - pad["b"])

    p = [f'<line x1="{pad["l"]}" y1="{H-pad["b"]}" x2="{W-pad["r"]}" y2="{H-pad["b"]}" class="fg-axis"/>',
         f'<line x1="{pad["l"]}" y1="{pad["t"]}" x2="{pad["l"]}" y2="{H-pad["b"]}" class="fg-axis"/>']
    for a in (0.2, 0.4, 0.6, 0.8):
        p.append(f'<text x="{X(a):.1f}" y="{H-pad["b"]+16}" text-anchor="middle" class="fg-small">{a}</text>')
    for y in (0, 1, 2, 3, 5):
        p.append(f'<text x="{pad["l"]-8}" y="{Y(y)+4:.1f}" text-anchor="end" class="fg-small">{y}</text>')
    p.append(f'<text x="{(pad["l"]+W-pad["r"])/2:.0f}" y="{H-4}" text-anchor="middle" class="fg-small">kernel exponent alpha  (d = 1)</text>')
    xc = X(d / 2)
    p.append(f'<line x1="{xc:.1f}" y1="{pad["t"]}" x2="{xc:.1f}" y2="{H-pad["b"]}" stroke="#8a1c1c" stroke-width="1.4" stroke-dasharray="4 4"/>')
    p.append(f'<text x="{xc+6:.1f}" y="{pad["t"]+12}" class="fg-small">alpha = d/2</text>')
    curves = [("nu = 1/alpha", lambda a: 1 / a, "#1c5a8a"),
              ("delta", lambda a: (d + a) / (d - a), "#8a1c1c"),
              ("beta_o", lambda a: (d - a) / (2 * a), "#4a7a1c"),
              ("gamma = 1", lambda a: 1.0, "#8a8f99")]
    for label, f, colour in curves:
        pts, a, step = [], lo, (hi - lo) / 160.0
        while a <= hi:
            y = f(a)
            if y <= ymax:
                pts.append((X(a), Y(y)))
            a += step
        if len(pts) > 1:
            p.append('<path d="M' + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) +
                     f'" fill="none" stroke="{colour}" stroke-width="1.8"/>')
    ylab = pad["t"] + 14
    for label, f, colour in curves:
        p.append(f'<text x="{W-pad["r"]+12}" y="{ylab}" fill="{colour}" class="fg-small">{label}</text>')
        ylab += 16
    return _svg(W, H, "exponents against the kernel exponent", "".join(p))


def fig_thouless():
    """The direction of the block spin below, at and above the critical temperature."""
    W, H = 560, 210
    p = ['<text x="280" y="18" text-anchor="middle" class="fg-small">direction of the block spin, two components</text>']
    centres = [(104, 96), (280, 96), (456, 96)]
    titles = ["T below Tc: concentrated", "T = Tc: uniform", "T above Tc: uniform"]
    r = 58
    for (cx, cy), title, spread in zip(centres, titles, [0.5, 1.0, 1.0]):
        p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#dcdfe4" stroke-width="1.2"/>')
        p.append(f'<circle cx="{cx}" cy="{cy}" r="2" fill="#17181a"/>')
        for i in range(36):
            ang = (i / 36.0 - 0.5) * spread * 2 * math.pi if spread < 0.9 else (i / 36.0) * 2 * math.pi
            if spread < 0.9:
                ang = (i / 36.0 - 0.5) * 0.55
            p.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r*0.9*math.cos(ang):.1f}" '
                     f'y2="{cy - r*0.9*math.sin(ang):.1f}" stroke="#8a1c1c" stroke-width="1" opacity="0.45"/>')
        p.append(f'<text x="{cx}" y="{cy+r+22}" text-anchor="middle" class="fg-small">{title}</text>')
    return _svg(W, H, "direction of the block spin", "".join(p))


# ---------------------------------------------------------------- 5. Ising block spin (exact)


def ising_block(n=4, L=2, d=1, alpha=0.5, n_beta=18):
    """Exact law of the block spin of the Ising model on a block of 2^n sites, free boundary.

    With 2^n = 16 there are 65536 configurations, so the histogram is exact, not sampled.
    """
    V = vertices(d, L, n)
    N = len(V)
    pairs = []
    for i in range(N):
        for j in range(i + 1, N):
            k = children_index(V[i], V[j], d)
            pairs.append((i, j, L ** (-(d + alpha) * k)))
    configs = list(itertools.product([-1, 1], repeat=N))
    energies = []
    for cfg in configs:
        energies.append(sum(w * cfg[i] * cfg[j] for i, j, w in pairs))
    spins = [sum(cfg) for cfg in configs]
    _, row = flat_params(L, d, alpha)
    beta_max = 1.6 / row
    betas = [beta_max * (i + 1) / n_beta for i in range(n_beta)]
    histograms = []
    for beta in betas:
        weights = [math.exp(beta * e) for e in energies]
        Z = sum(weights)
        counts = {v: 0.0 for v in range(-N, N + 1, 2)}
        for w, s in zip(weights, spins):
            counts[s] += w / Z
        histograms.append([round(counts[v], 8) for v in range(-N, N + 1, 2)])
    return {"n": n, "N": N, "values": list(range(-N, N + 1, 2)),
            "betas": [round(b, 6) for b in betas], "beta_c": 1 / row,
            "histograms": histograms, "alpha": alpha, "L": L, "d": d}


# ---------------------------------------------------------------- 6. Ising Monte Carlo (reference)


def ising_couplings(n, L=2, d=1, alpha=0.5):
    """The coupling matrix of the hierarchical Ising model on a block of 2^n sites."""
    V = vertices(d, L, n)
    N = len(V)
    J = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            k = children_index(V[i], V[j], d)
            w = L ** (-(d + alpha) * k)
            J[i][j] = J[j][i] = w
    return J


def ising_sweep(spins, J, beta, bits, offset):
    """One heat-bath sweep: site i becomes +1 with probability 1/(1+exp(-2 beta h_i)).

    Returns the new offset into the uniform stream. The browser code in wiki/static/sim.js
    reproduces this function exactly; tools/test_sim.py checks the two against each other.
    """
    N = len(spins)
    for i in range(N):
        h = 0.0
        row = J[i]
        for j in range(N):
            if j != i:
                h += row[j] * spins[j]
        p_up = 1.0 / (1.0 + math.exp(-2.0 * beta * h))
        spins[i] = 1 if bits[offset % len(bits)] < p_up else -1
        offset += 1
    return offset


def lcg_stream(seed, count):
    s = seed & 0xFFFFFFFF or 1
    out = []
    for _ in range(count):
        s = (s * 1664525 + 1013904223) & 0xFFFFFFFF
        out.append(s / 4294967296)
    return out
