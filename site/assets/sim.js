/* Simulations for the hierarchical RG wiki.
 *
 * The pure functions in SIM are the model computations; the code at the bottom only builds
 * widgets for elements of the form <div class="sim" data-sim="NAME"></div>. tools/test_sim.py
 * loads this file in quickjs and checks SIM against tools/simulate.py.
 */
(function (global) {
  "use strict";

  var SIM = {};

  /* ---------------------------------------------------------------- hierarchical geometry */

  SIM.level = function (a, b, d) {
    var out = 0;
    for (var i = 0; i < a.length; i++) if (a[i] !== b[i]) out = Math.floor(i / d) + 1;
    return out;
  };

  SIM.vertices = function (d, L, n) {
    var out = [[]], i, k, next;
    for (k = 0; k < d * n; k++) {
      next = [];
      for (i = 0; i < out.length; i++) for (var a = 0; a < L; a++) next.push(out[i].concat([a]));
      out = next;
    }
    return out;
  };

  /* ---------------------------------------------------------------- Gaussian orbit */

  SIM.varianceOrbit = function (beta, nMax, L, d, alpha, J) {
    L = L || 2; d = d || 1; alpha = alpha === undefined ? 0.5 : alpha; J = J || 1;
    var m = Math.pow(L, d), v = 1.0, out = [1.0], k, b, den;
    for (k = 1; k <= nMax; k++) {
      b = beta * J * Math.pow(L, -(d + alpha) * k);
      den = 1 - b * v * (m - 1);
      if (den <= 0) break;
      v = (m * v) / den;
      out.push(v);
    }
    return out;
  };

  /* ---------------------------------------------------------------- exponents */

  SIM.exponentTable = function (d, L, alpha) {
    var kappa = alpha, nu = 1 / alpha, eta = 2 - kappa;
    var gamma = kappa * nu, betaO = (nu * (d - kappa)) / 2;
    var delta = (d + kappa) / (d - kappa), alphaHy = 2 - d * nu;
    return {
      kappa: kappa, nu: nu, eta: eta, gamma: gamma, betaO: betaO,
      delta: delta, alphaHy: alphaHy,
      fisher: gamma - nu * (2 - eta),
      widom: gamma - betaO * (delta - 1),
      hyperscaling: 2 - alphaHy - d * nu
    };
  };

  /* ---------------------------------------------------------------- percolation */

  /* Deterministic uniform stream, so a reroll is reproducible. */
  SIM.rng = function (seed) {
    var s = seed >>> 0 || 1;
    return function () {
      s = (Math.imul(s, 1664525) + 1013904223) >>> 0;
      return s / 4294967296;
    };
  };

  SIM.openProbability = function (k, beta, L, d, alpha) {
    return 1 - Math.exp(-beta * Math.pow(L, -(d + alpha) * k));
  };

  /* Cluster of vertex 0 for the edge set decided by the supplied uniform bits. */
  SIM.percolateWithBits = function (n, L, d, alpha, beta, bits) {
    var V = SIM.vertices(d, L, n), N = V.length, parent = [], i, j, k, t = 0;
    for (i = 0; i < N; i++) parent.push(i);
    function find(x) { while (parent[x] !== x) { parent[x] = parent[parent[x]]; x = parent[x]; } return x; }
    var edges = [];
    for (i = 0; i < N; i++) {
      for (j = i + 1; j < N; j++) {
        k = SIM.level(V[i], V[j], d);
        var open = bits[t % bits.length] < SIM.openProbability(k, beta, L, d, alpha);
        t++;
        if (open) {
          edges.push([i, j, k]);
          var ra = find(i), rb = find(j);
          if (ra !== rb) parent[ra] = rb;
        }
      }
    }
    var root = find(0), members = [];
    for (i = 0; i < N; i++) if (find(i) === root) members.push(i);
    return { members: members, edges: edges, size: members.length };
  };

  SIM.percolate = function (n, L, d, alpha, beta, seed) {
    var rnd = SIM.rng(seed), V = SIM.vertices(d, L, n), bits = [], i;
    var total = (V.length * (V.length - 1)) / 2;
    for (i = 0; i < total + 8; i++) bits.push(rnd());
    var res = SIM.percolateWithBits(n, L, d, alpha, beta, bits);
    res.bits = bits;
    return res;
  };

  global.SIM = SIM;

  /* ---------------------------------------------------------------- Ising heat bath */

  SIM.isingCouplings = function (n, L, d, alpha) {
    var V = SIM.vertices(d, L, n), N = V.length, J = [], i, j;
    for (i = 0; i < N; i++) { J.push([]); for (j = 0; j < N; j++) J[i].push(0); }
    for (i = 0; i < N; i++) {
      for (j = i + 1; j < N; j++) {
        var w = Math.pow(L, -(d + alpha) * SIM.level(V[i], V[j], d));
        J[i][j] = w; J[j][i] = w;
      }
    }
    return J;
  };

  SIM.isingSweep = function (spins, J, beta, bits, offset) {
    var N = spins.length, i, j;
    for (i = 0; i < N; i++) {
      var h = 0;
      for (j = 0; j < N; j++) if (j !== i) h += J[i][j] * spins[j];
      var pUp = 1 / (1 + Math.exp(-2 * beta * h));
      spins[i] = bits[offset % bits.length] < pUp ? 1 : -1;
      offset++;
    }
    return offset;
  };

  /* ---------------------------------------------------------------- browser widgets */

  if (typeof document === "undefined") return;

  var NS = "http://www.w3.org/2000/svg";
  function el(name, attrs, text) {
    var node = document.createElementNS(NS, name), k;
    for (k in attrs) if (attrs.hasOwnProperty(k)) node.setAttribute(k, attrs[k]);
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function fmt(x, digits) {
    if (x === null || x === undefined || !isFinite(x)) return "—";
    return Number(x).toFixed(digits === undefined ? 3 : digits);
  }
  function svgRoot(w, h) {
    var s = el("svg", { viewBox: "0 0 " + w + " " + h, class: "sim-svg", role: "img" });
    return s;
  }
  function axes(svg, W, H, pad, xTicks, yTicks, xLabel, yLabel) {
    var g = el("g", { class: "axes" });
    g.appendChild(el("line", { x1: pad.l, y1: H - pad.b, x2: W - pad.r, y2: H - pad.b }));
    g.appendChild(el("line", { x1: pad.l, y1: pad.t, x2: pad.l, y2: H - pad.b }));
    xTicks.forEach(function (t) {
      var x = pad.l + t.pos * (W - pad.l - pad.r);
      g.appendChild(el("line", { x1: x, y1: H - pad.b, x2: x, y2: H - pad.b + 4 }));
      g.appendChild(el("text", { x: x, y: H - pad.b + 16, "text-anchor": "middle" }, t.label));
    });
    yTicks.forEach(function (t) {
      var y = H - pad.b - t.pos * (H - pad.t - pad.b);
      g.appendChild(el("line", { x1: pad.l - 4, y1: y, x2: pad.l, y2: y }));
      g.appendChild(el("text", { x: pad.l - 8, y: y + 4, "text-anchor": "end" }, t.label));
    });
    if (xLabel) g.appendChild(el("text", { x: (W + pad.l - pad.r) / 2, y: H - 4, "text-anchor": "middle", class: "axis-label" }, xLabel));
    if (yLabel) g.appendChild(el("text", { x: 12, y: (H - pad.b + pad.t) / 2, "text-anchor": "middle", class: "axis-label", transform: "rotate(-90 12 " + ((H - pad.b + pad.t) / 2) + ")" }, yLabel));
    svg.appendChild(g);
    return g;
  }
  function polyline(svg, pts, cls) {
    if (!pts.length) return;
    var d = pts.map(function (p, i) { return (i ? "L" : "M") + p[0].toFixed(2) + " " + p[1].toFixed(2); }).join(" ");
    svg.appendChild(el("path", { d: d, class: cls, fill: "none" }));
  }

  var widgets = {
    /* -------------------------------------------------- Gaussian orbit */
    "rg-orbit": function (host, data) {
      var W = 640, H = 380, pad = { l: 52, r: 16, t: 16, b: 34 };
      var nMax = data.n_max, bMin = data.betas[0], bMax = data.betas[data.betas.length - 1];
      var yMin = -1, yMax = 0;
      data.curves.forEach(function (c) { c.forEach(function (v) { if (v !== null) { if (v < yMin) yMin = v; if (v > yMax) yMax = v; } }); });
      data.critical.forEach(function (v) { if (v > yMax) yMax = v; });
      yMin = Math.floor(yMin); yMax = Math.ceil(yMax);

      var svg = svgRoot(W, H);
      var xt = [], yt = [], k;
      for (k = 0; k <= nMax; k += 4) xt.push({ pos: k / nMax, label: String(k) });
      var step = Math.max(1, Math.ceil((yMax - yMin) / 6));
      for (k = yMin; k <= yMax; k += step) yt.push({ pos: (k - yMin) / (yMax - yMin), label: String(k) });
      axes(svg, W, H, pad, xt, yt, "scale n", "log10 of the block-spin variance");

      function xOf(n) { return pad.l + (n / nMax) * (W - pad.l - pad.r); }
      function yOf(v) { return H - pad.b - ((v - yMin) / (yMax - yMin)) * (H - pad.t - pad.b); }

      data.critical.forEach(function (v, n) {
        if (n > 0) svg.appendChild(el("line", {
          x1: xOf(n - 1), y1: yOf(data.critical[n - 1]), x2: xOf(n), y2: yOf(v),
          class: "curve-critical"
        }));
      });

      var live = el("path", { class: "curve-live", fill: "none" });
      svg.appendChild(live);

      var slider = document.createElement("input");
      slider.type = "range"; slider.min = bMin.toFixed(4); slider.max = bMax.toFixed(4);
      slider.step = ((bMax - bMin) / 400).toFixed(6); slider.value = (0.92 * data.beta_c).toFixed(4);
      slider.className = "sim-slider";
      var readout = document.createElement("div");
      readout.className = "sim-readout";

      function draw() {
        var beta = parseFloat(slider.value);
        var orbit = SIM.varianceOrbit(beta, nMax, data.L, data.d, data.alpha);
        var pts = orbit.map(function (v, n) { return [xOf(n), yOf(Math.log10(v))]; });
        live.setAttribute("d", pts.map(function (p, i) { return (i ? "L" : "M") + p[0].toFixed(2) + " " + p[1].toFixed(2); }).join(" "));
        var last = orbit[orbit.length - 1];
        var u = beta * Math.pow(data.L, -((data.d + data.alpha) * (orbit.length - 1))) * last;
        readout.innerHTML = "β = " + beta.toFixed(4) + " = " + (beta / data.beta_c).toFixed(3) + " β<sub>c</sub>" +
          " &nbsp;·&nbsp; v<sub>" + (orbit.length - 1) + "</sub> = " + fmt(last, 3) +
          " &nbsp;·&nbsp; u<sub>n</sub> = βJ<sub>n</sub>v<sub>n</sub> = " + fmt(u, 4) +
          " &nbsp;·&nbsp; fixed point u* = " + fmt(data.u_star, 4);
      }
      slider.addEventListener("input", draw);
      var snap = document.createElement("button");
      snap.textContent = "snap to βc"; snap.className = "sim-button";
      snap.addEventListener("click", function () { slider.value = data.beta_c.toFixed(4); draw(); });
      var controls = document.createElement("div");
      controls.className = "sim-controls";
      controls.appendChild(slider); controls.appendChild(snap);
      host.appendChild(svg); host.appendChild(controls); host.appendChild(readout);
      draw();
    },

    /* -------------------------------------------------- exponent calculator */
    "exponents": function (host) {
      var table = document.createElement("table");
      table.className = "sim-table";
      var rows = [["κ", "kappa"], ["ν", "nu"], ["η", "eta"], ["γ", "gamma"], ["β<sub>o</sub>", "betaO"],
                  ["δ", "delta"], ["α<sub>hy</sub>", "alphaHy"]];
      table.innerHTML = "<thead><tr><th>exponent</th><th>value</th></tr></thead><tbody></tbody>";
      var tbody = table.querySelector("tbody");
      var cells = {};
      rows.forEach(function (r) {
        var tr = document.createElement("tr");
        tr.innerHTML = "<td>" + r[0] + "</td><td class='num'>—</td>";
        cells[r[1]] = tr.lastChild; tbody.appendChild(tr);
      });
      var rel = document.createElement("div");
      rel.className = "sim-readout";
      var mk = function (label, min, max, step, value) {
        var wrap = document.createElement("label");
        wrap.className = "sim-field";
        wrap.innerHTML = "<span>" + label + "</span>";
        var inp = document.createElement("input");
        inp.type = "range"; inp.min = min; inp.max = max; inp.step = step; inp.value = value;
        wrap.appendChild(inp); return { wrap: wrap, input: inp };
      };
      var fD = mk("dimension d", 1, 4, 1, 1);
      var fL = mk("scale L", 2, 3, 1, 2);
      var fA = mk("kernel exponent α (must be below d)", 0.05, 3.95, 0.05, 0.5);
      function draw() {
        var d = parseInt(fD.input.value, 10), L = parseInt(fL.input.value, 10), a = parseFloat(fA.input.value);
        if (a >= d) { a = d - 0.05; fA.input.value = a; }
        var t = SIM.exponentTable(d, L, a);
        ["kappa", "nu", "eta", "gamma", "betaO", "delta", "alphaHy"].forEach(function (k) {
          cells[k].textContent = fmt(t[k], 4);
        });
        rel.innerHTML = "d = " + d + ", L = " + L + ", α = " + a.toFixed(2) +
          " · Fisher γ−ν(2−η) = " + t.fisher.toExponential(1) +
          " · Widom γ−β<sub>o</sub>(δ−1) = " + t.widom.toExponential(1) +
          " · hyperscaling 2−α<sub>hy</sub>−dν = " + t.hyperscaling.toExponential(1);
      }
      [fD, fL, fA].forEach(function (f) { f.input.addEventListener("input", draw); });
      host.appendChild(fD.wrap); host.appendChild(fL.wrap); host.appendChild(fA.wrap);
      host.appendChild(table); host.appendChild(rel);
      draw();
    },

    /* -------------------------------------------------- triangle diagram */
    "triangle": function (host, data) {
      var W = 640, H = 340, pad = { l: 56, r: 16, t: 16, b: 34 };
      var svg = svgRoot(W, H);
      var curves = data.curves, nMax = data.n_max;
      var yMin = 1e9, yMax = -1e9;
      curves.forEach(function (c) { c.log10.forEach(function (v) { if (v < yMin) yMin = v; if (v > yMax) yMax = v; }); });
      yMin = Math.floor(yMin); yMax = Math.ceil(yMax);
      var xt = [], yt = [], k;
      for (k = 0; k <= nMax; k += 2) xt.push({ pos: k / nMax, label: String(k) });
      for (k = yMin; k <= yMax; k += Math.max(1, Math.ceil((yMax - yMin) / 6))) yt.push({ pos: (k - yMin) / (yMax - yMin), label: String(k) });
      axes(svg, W, H, pad, xt, yt, "block level N", "log10 of the partial triangle sum");
      function xOf(n) { return pad.l + (n / nMax) * (W - pad.l - pad.r); }
      function yOf(v) { return H - pad.b - ((v - yMin) / (yMax - yMin)) * (H - pad.t - pad.b); }
      var path = el("path", { class: "curve-live", fill: "none" });
      svg.appendChild(path);
      var slider = document.createElement("input");
      slider.type = "range"; slider.min = 0; slider.max = curves.length - 1; slider.step = 1;
      slider.value = Math.max(0, curves.length - 4); slider.className = "sim-slider";
      var readout = document.createElement("div"); readout.className = "sim-readout";
      function draw() {
        var i = parseInt(slider.value, 10), c = curves[i];
        var pts = c.log10.map(function (v, n) { return [xOf(n), yOf(v)]; });
        path.setAttribute("d", pts.map(function (p, j) { return (j ? "L" : "M") + p[0].toFixed(2) + " " + p[1].toFixed(2); }).join(" "));
        var inc = c.S[c.S.length - 1] - c.S[c.S.length - 2];
        readout.innerHTML = "α = " + c.alpha.toFixed(2) + " · 3α − d = " + (3 * c.alpha - data.d).toFixed(2) +
          (3 * c.alpha < data.d ? " (convergent)" : (Math.abs(3 * c.alpha - data.d) < 1e-9 ? " (logarithmic)" : " (divergent)")) +
          " · increment S<sub>" + nMax + "</sub>−S<sub>" + (nMax - 1) + "</sub> = " + fmt(inc, 3) +
          " · predicted ratio L<sup>3α−d</sup> = " + fmt(Math.pow(data.L, 3 * c.alpha - data.d), 3);
      }
      slider.addEventListener("input", draw);
      host.appendChild(svg);
      var controls = document.createElement("div"); controls.className = "sim-controls";
      controls.appendChild(slider);
      host.appendChild(controls); host.appendChild(readout);
      draw();
    },

    /* -------------------------------------------------- Ising block-spin law */
    "ising-block": function (host, data) {
      var W = 620, H = 300, pad = { l: 44, r: 14, t: 14, b: 42 };
      var values = data.values, hist = data.histograms, betas = data.betas;
      var svg = svgRoot(W, H);
      var bw = (W - pad.l - pad.r) / values.length;
      var bars = [], maxP = 0, i, j;
      for (i = 0; i < hist.length; i++) for (j = 0; j < hist[i].length; j++) if (hist[i][j] > maxP) maxP = hist[i][j];
      maxP = Math.max(maxP, 1e-6);
      var yOf = function (p) { return H - pad.b - (p / maxP) * (H - pad.t - pad.b); };
      svg.appendChild(el("line", { x1: pad.l, y1: H - pad.b, x2: W - pad.r, y2: H - pad.b, class: "axes-line" }));
      for (j = 0; j < values.length; j++) {
        if (values[j] % 4 !== 0) continue;
        var x = pad.l + (j + 0.5) * bw;
        svg.appendChild(el("text", { x: x, y: H - pad.b + 15, "text-anchor": "middle" }, String(values[j])));
      }
      svg.appendChild(el("text", { x: (W + pad.l - pad.r) / 2, y: H - 6, "text-anchor": "middle", class: "axis-label" }, "block spin S of a block of 16 sites"));
      for (j = 0; j < values.length; j++) {
        bars.push(el("rect", { x: pad.l + j * bw + 1, y: H - pad.b, width: bw - 2, height: 0, class: "bar" }));
        svg.appendChild(bars[j]);
      }
      var slider = document.createElement("input");
      slider.type = "range"; slider.min = 0; slider.max = betas.length - 1; slider.step = 1;
      slider.value = Math.floor(betas.length * 0.55); slider.className = "sim-slider";
      var readout = document.createElement("div"); readout.className = "sim-readout";
      function draw() {
        var k = parseInt(slider.value, 10), h = hist[k];
        var mean = 0;
        for (var j2 = 0; j2 < values.length; j2++) {
          var y = yOf(h[j2]);
          bars[j2].setAttribute("y", y.toFixed(1));
          bars[j2].setAttribute("height", (H - pad.b - y).toFixed(1));
          mean += Math.abs(values[j2]) * h[j2];
        }
        readout.innerHTML = "β = " + betas[k].toFixed(3) + " = " + (betas[k] / data.beta_c).toFixed(2) + " β<sub>c</sub>" +
          " &nbsp;·&nbsp; E|S|/N = " + (mean / data.N).toFixed(3) +
          " &nbsp;·&nbsp; P(S = 0) = " + h[Math.floor(h.length / 2)].toFixed(3) +
          " &nbsp;·&nbsp; P(|S| = N) = " + h[0].toFixed(3);
      }
      slider.addEventListener("input", draw);
      host.appendChild(svg);
      var controls = document.createElement("div"); controls.className = "sim-controls";
      controls.appendChild(slider);
      host.appendChild(controls); host.appendChild(readout);
      draw();
    },

    /* -------------------------------------------------- Ising Monte Carlo */
    "ising-mc": function (host) {
      var n = 6, L = 2, d = 1, alpha = 0.5, N = Math.pow(L, d * n);
      var J = SIM.isingCouplings(n, L, d, alpha);
      var W = 640, H = 260, pad = { l: 26, r: 14, t: 16, b: 46 };
      var svg = svgRoot(W, H);
      var spins = [], bits = [], off = 0, sweeps = 0, seed = 11, timer = null;
      var cell = (W - pad.l - pad.r) / N;
      function rebuild(keep) {
        var i;
        if (!keep) { spins = []; for (i = 0; i < N; i++) spins.push(1); sweeps = 0; }
        bits = [];
        var rnd = SIM.rng(seed);
        for (i = 0; i < N * 300; i++) bits.push(rnd());
        off = 0;
      }
      rebuild(false);
      var rects = [], i;
      for (i = 0; i < N; i++) {
        rects.push(el("rect", { x: pad.l + i * cell, y: pad.t, width: cell + 0.4, height: 54, class: "cell" }));
        svg.appendChild(rects[i]);
      }
      for (i = 1; i < 7; i++) {
        var x = pad.l + Math.pow(2, i) * cell;
        svg.appendChild(el("line", { x1: x, y1: pad.t, x2: x, y2: pad.t + 54, class: "guide" }));
      }
      // block magnetisation at level 3: eight blocks of eight sites
      var bars = [], nb = 8, bw = (W - pad.l - pad.r) / nb;
      for (i = 0; i < nb; i++) {
        bars.push(el("rect", { x: pad.l + i * bw + 8, y: 120, width: bw - 16, height: 2, class: "bar" }));
        svg.appendChild(bars[i]);
      }
      svg.appendChild(el("text", { x: pad.l, y: 110 }, "block magnetisation of the eight level-3 blocks"));
      var slider = document.createElement("input");
      slider.type = "range"; slider.min = 0.2; slider.max = 1.6; slider.step = 0.01; slider.value = 0.6;
      slider.className = "sim-slider";
      var runBtn = document.createElement("button");
      runBtn.className = "sim-button"; runBtn.textContent = "run";
      var resetBtn = document.createElement("button");
      resetBtn.className = "sim-button"; resetBtn.textContent = "reset";
      var readout = document.createElement("div"); readout.className = "sim-readout";
      var betaC = 1 / ((1 - Math.pow(L, -d)) * Math.pow(L, -alpha) / (1 - Math.pow(L, -alpha)));
      function draw() {
        var beta = parseFloat(slider.value), i2, M = 0;
        for (i2 = 0; i2 < N; i2++) {
          rects[i2].setAttribute("class", spins[i2] > 0 ? "cell up" : "cell down");
          M += spins[i2];
        }
        for (i2 = 0; i2 < nb; i2++) {
          var m = 0;
          for (var j = i2 * (N / nb); j < (i2 + 1) * (N / nb); j++) m += spins[j];
          m /= (N / nb);
          var h = Math.abs(m) * 46, y = 120 + 46 - h;
          bars[i2].setAttribute("y", y.toFixed(1));
          bars[i2].setAttribute("height", Math.max(1, h).toFixed(1));
          bars[i2].setAttribute("class", m > 0 ? "bar" : "bar bar-down");
        }
        readout.innerHTML = "β = " + beta.toFixed(2) + " = " + (beta / betaC).toFixed(2) + " β<sub>c</sub>" +
          " &nbsp;·&nbsp; sweeps " + sweeps +
          " &nbsp;·&nbsp; |M|/N = " + (Math.abs(M) / N).toFixed(3) +
          " &nbsp;·&nbsp; " + N + " sites, couplings at six levels";
      }
      function step() {
        var beta = parseFloat(slider.value), k;
        for (k = 0; k < 2; k++) {
          if (off + N >= bits.length) { seed = (seed * 7 + 13) % 997 + 1; var keep = spins.slice(); rebuild(true); spins = keep; }
          off = SIM.isingSweep(spins, J, beta, bits, off);
          sweeps++;
        }
        draw();
      }
      runBtn.addEventListener("click", function () {
        if (timer) { clearInterval(timer); timer = null; runBtn.textContent = "run"; }
        else { timer = setInterval(step, 90); runBtn.textContent = "pause"; }
      });
      resetBtn.addEventListener("click", function () { rebuild(false); draw(); });
      slider.addEventListener("input", draw);
      host.appendChild(svg);
      var controls = document.createElement("div"); controls.className = "sim-controls";
      controls.appendChild(slider); controls.appendChild(runBtn); controls.appendChild(resetBtn);
      host.appendChild(controls); host.appendChild(readout);
      draw();
    },

    /* -------------------------------------------------- percolation */
    "percolation": function (host) {
      var n = 5, L = 2, d = 1, alpha = 0.5;
      var W = 640, H = 340, pad = { l: 26, r: 16, t: 18, b: 40 };
      var svg = svgRoot(W, H);
      var N = Math.pow(L, d * n);
      function xOf(i) { return pad.l + ((i + 0.5) / N) * (W - pad.l - pad.r); }
      function yOf(k) { return H - pad.b - (k / n) * (H - pad.t - pad.b); }
      var slider = document.createElement("input");
      slider.type = "range"; slider.min = 0.05; slider.max = 2.5; slider.step = 0.01; slider.value = 0.85;
      slider.className = "sim-slider";
      var seedBox = document.createElement("button");
      seedBox.textContent = "reroll"; seedBox.className = "sim-button";
      var readout = document.createElement("div"); readout.className = "sim-readout";
      var seed = 7;
      var palette = ["#8a1c1c", "#1c5a8a", "#4a7a1c", "#8a6a1c", "#6a1c8a", "#1c8a7a", "#8a1c5a"];
      function draw() {
        var beta = parseFloat(slider.value);
        var res = SIM.percolate(n, L, d, alpha, beta, seed);
        while (svg.firstChild) svg.removeChild(svg.firstChild);
        axes(svg, W, H, pad,
             [{ pos: 0, label: "0" }, { pos: 0.5, label: String(N / 2) }, { pos: 1, label: String(N - 1) }],
             [], "vertex", "");
        var k, i;
        for (k = 1; k <= n; k++) {
          svg.appendChild(el("line", { x1: pad.l, y1: yOf(k), x2: W - pad.r, y2: yOf(k), class: "guide" }));
          svg.appendChild(el("text", { x: W - pad.r - 2, y: yOf(k) - 3, "text-anchor": "end", class: "guide-label" }, "level " + k));
        }
        res.edges.forEach(function (e) {
          var x1 = xOf(e[0]), x2 = xOf(e[1]), y = yOf(e[2]);
          svg.appendChild(el("path", {
            d: "M" + x1.toFixed(1) + " " + (H - pad.b) + " L" + x1.toFixed(1) + " " + y.toFixed(1) +
               " L" + x2.toFixed(1) + " " + y.toFixed(1) + " L" + x2.toFixed(1) + " " + (H - pad.b),
            class: "edge", "stroke-width": Math.max(0.4, 1.8 - 0.25 * e[2])
          }));
        });
        var inRoot = {};
        res.members.forEach(function (m) { inRoot[m] = true; });
        for (i = 0; i < N; i++) {
          var c = el("circle", {
            cx: xOf(i), cy: H - pad.b, r: inRoot[i] ? 3.4 : 2.2,
            class: inRoot[i] ? "site-in" : "site-out"
          });
          svg.appendChild(c);
        }
        var V = SIM.vertices(d, L, n);
        var byLevel = {};
        for (i = 0; i < N; i++) if (i !== 0 && inRoot[i]) {
          var lev = SIM.level(V[0], V[i], d);
          byLevel[lev] = (byLevel[lev] || 0) + 1;
        }
        var parts = [];
        Object.keys(byLevel).sort().forEach(function (key) {
          parts.push("τ(0, level " + key + ") = " + byLevel[key] + "/" + (Math.pow(L, d * key) - Math.pow(L, d * (key - 1))));
        });
        readout.innerHTML = "β = " + beta.toFixed(2) + " · |K<sub>0</sub>| = " + res.size + " of " + N +
          " · open bonds " + res.edges.length + " of " + ((N * (N - 1)) / 2) +
          (parts.length ? " · " + parts.join(" · ") : "");
      }
      slider.addEventListener("input", draw);
      seedBox.addEventListener("click", function () { seed = (seed * 7 + 13) % 97 + 1; draw(); });
      host.appendChild(svg);
      var controls = document.createElement("div"); controls.className = "sim-controls";
      controls.appendChild(slider); controls.appendChild(seedBox);
      host.appendChild(controls); host.appendChild(readout);
      draw();
    }
  };

  function init() {
    var hosts = document.querySelectorAll("[data-sim]");
    var data = {};
    var node = document.getElementById("sim-data");
    if (node) { try { data = JSON.parse(node.textContent); } catch (e) { data = {}; } }
    for (var i = 0; i < hosts.length; i++) {
      var host = hosts[i], name = host.getAttribute("data-sim");
      if (!widgets[name]) continue;
      try { widgets[name](host, data[name] || {}); }
      catch (e) { host.textContent = "This figure could not be drawn."; }
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})(typeof window !== "undefined" ? window : this);
