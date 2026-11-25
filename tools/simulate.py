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


def figures() -> dict:
    return {"lattice-children": fig_lattice_children(), "flow": fig_flow(), "decimation": fig_decimation(),
            "exponents-alpha": fig_exponents_alpha(), "thouless": fig_thouless(),
            "boundary": fig_boundary()}


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
