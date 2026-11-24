/* Filter the article list from search-index.json. No dependencies, no network beyond the file. */
(function () {
  "use strict";
  var input = document.getElementById("q");
  if (!input) return;
  var list = document.getElementById("results");
  var index = null;
  function load() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "search-index.json");
    xhr.onload = function () {
      try { index = JSON.parse(xhr.responseText); } catch (e) { index = []; }
      if (input.value) run();
    };
    xhr.send();
  }
  function run() {
    if (!index) return;
    var q = input.value.trim().toLowerCase();
    list.innerHTML = "";
    if (q.length < 2) return;
    var shown = 0;
    index.forEach(function (entry) {
      if (shown >= 8) return;
      var hay = (entry.title + " " + entry.subtitle + " " + entry.summary + " " + entry.text).toLowerCase();
      var at = hay.indexOf(q);
      if (at < 0) return;
      shown++;
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = entry.url; a.textContent = entry.title;
      var snip = document.createElement("span");
      snip.className = "snippet";
      var from = Math.max(0, at - 40);
      snip.textContent = (from > 0 ? "… " : "") + hay.slice(from, at + 90).replace(/\s+/g, " ") + " …";
      li.appendChild(a); li.appendChild(snip); list.appendChild(li);
    });
    if (!shown) {
      var li = document.createElement("li");
      li.className = "snippet";
      li.textContent = "no match";
      list.appendChild(li);
    }
  }
  input.addEventListener("input", run);
  input.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { input.value = ""; run(); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== input) { e.preventDefault(); input.focus(); }
  });
  load();
})();
