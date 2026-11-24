#!/usr/bin/env python3
"""Check the browser simulation code against the Python reference.

Loads wiki/static/sim.js in quickjs (a JS engine, no DOM), calls the pure functions, and compares
them with tools/simulate.py. Needs `pip install quickjs` (or PYTHONPATH to an install of it).

Usage: python3 tools/test_sim.py
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import simulate  # same directory

try:
    import quickjs
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / ".scratch" / "pip"))
    try:
        import quickjs
    except ImportError:
        print("FAIL  quickjs is not installed; cannot test the browser code")
        raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent
FAILS: list[str] = []


def check(name: str, ok: bool, detail: str) -> None:
    print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")
    if not ok:
        FAILS.append(name)


def main() -> int:
    ctx = quickjs.Context()
    ctx.eval((ROOT / "wiki/static/sim.js").read_text())
    check("sim.js loads without a DOM", True,
          "keys " + ",".join(sorted(json.loads(ctx.eval("JSON.stringify(Object.keys(SIM))")))))

    # 1. the Gaussian orbit
    worst = 0.0
    for beta, n_max, L, d, alpha in [(0.3, 10, 2, 1, 0.5), (0.8, 12, 2, 1, 0.5),
                                     (0.15, 8, 3, 2, 1.0), (0.6, 9, 2, 1, 0.9)]:
        py = simulate.variance_orbit(beta, n_max, L, d, alpha)
        js = json.loads(ctx.eval(f"JSON.stringify(SIM.varianceOrbit({beta},{n_max},{L},{d},{alpha}))"))
        if len(py) != len(js):
            check(f"orbit length beta={beta}", False, f"python {len(py)} vs js {len(js)}")
            continue
        worst = max([worst] + [abs(a - b) / max(1e-12, abs(a)) for a, b in zip(py, js)])
    check("Gaussian orbit matches the reference", worst < 1e-12, f"largest relative difference {worst:.2e}")

    # 2. the exponent table
    worst = 0.0
    for point in simulate.sim_exponents()["grid"]:
        js = json.loads(ctx.eval(
            f"JSON.stringify(SIM.exponentTable({point['d']},{point['L']},{point['alpha']}))"))
        for key, value in point["table"].items():
            worst = max(worst, abs(js[key] - value) / max(1e-12, abs(value)))
    check("exponent table matches the reference", worst < 1e-12, f"largest relative difference {worst:.2e}")

    # 3. the percolation cluster, for the same edge decisions
    worst = 0
    for n, L, d, alpha, beta, seed in [(4, 2, 1, 0.5, 1.0, 3), (4, 2, 1, 0.5, 2.0, 11),
                                       (3, 3, 1, 0.4, 1.5, 5)]:
        rnd = simulate_percolate_bits(n, L, d, alpha, beta, seed)
        bits, py_cluster = rnd
        js = json.loads(ctx.eval(
            "JSON.stringify(SIM.percolateWithBits(%d,%d,%d,%s,%s,%s))"
            % (n, L, d, alpha, beta, json.dumps(bits))))
        if sorted(js["members"]) != py_cluster:
            worst += 1
    check("percolation cluster matches the reference", worst == 0,
          "identical clusters for three edge sets" if worst == 0 else f"{worst} mismatch(es)")

    # 4. a live run is a valid cluster
    ctx.eval("var run = SIM.percolate(5,2,1,0.5,1.2,7);")
    size = ctx.eval("run.size")
    has0 = ctx.eval("run.members.indexOf(0) >= 0")
    edges_ok = ctx.eval("run.edges.every(function(e){return e[0]<e[1] && e[2]>=1 && e[2]<=5;})")
    check("live percolation run is consistent", bool(size >= 1 and has0 and edges_ok),
          f"|K_0| = {size}, contains 0 = {has0}, edges valid = {edges_ok}")

    # 5. the data the pages embed
    data = simulate.build()
    for key in ("rg-orbit", "exponents", "triangle"):
        json.dumps(data[key])
    check("simulation data is JSON-serialisable", True,
          f"{len(data['rg-orbit']['curves'])} orbit curves, "
          f"{len(data['exponents']['grid'])} exponent points, "
          f"{len(data['triangle']['curves'])} triangle curves")

    print(f"\n{len(FAILS)} failure(s)" if FAILS else "\nall browser-code checks passed")
    return 1 if FAILS else 0


def simulate_percolate_bits(n, L, d, alpha, beta, seed):
    """The Python side of SIM.percolate: same LCG, same edge order, same decisions."""
    s = seed & 0xFFFFFFFF or 1
    V = simulate.vertices(d, L, n)
    total = len(V) * (len(V) - 1) // 2
    bits = []
    for _ in range(total + 8):
        s = (s * 1664525 + 1013904223) & 0xFFFFFFFF
        bits.append(s / 4294967296)
    cluster = simulate.cluster_of_zero(n, L, d, alpha, bits, beta)
    return bits, cluster


if __name__ == "__main__":
    raise SystemExit(main())
