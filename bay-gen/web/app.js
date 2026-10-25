// Port of bay_gen.py's generation logic. Data and knobs come from data.js (export_web.py).
const D = BAYGEN;
const LAST_YEAR = D.years[1];

const gauss = () => {
  let u = 0;
  while (!u) u = Math.random();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * Math.random());
};
const pick = arr => arr[Math.floor(Math.random() * arr.length)];
function choices(items, w) {
  let r = Math.random() * w.reduce((a, b) => a + b, 0);
  for (let i = 0; i < items.length; i++) if ((r -= w[i]) < 0) return items[i];
  return items[items.length - 1];
}
function inYears(y, s) {
  const [a, b] = s.split("-").map(Number);
  return y >= a && y <= (b || a);
}
const curve = (y, mean) => Math.exp(-0.5 * ((y - mean) / D.yearSd) ** 2) * (y === LAST_YEAR ? D.partialLast : 1);

// Keep in step with warranty() in bay_gen.py.
function warranty(brand, year) {
  if (brand === "Cadillac" || (brand === "Buick" && year <= 2019)) return [[4, 50000], [6, 70000]];
  return [[3, 36000], year <= 2015 && brand !== "Buick" ? [5, 100000] : [5, 60000]];
}

function weights(s) {
  const f = (s.farm - 50) / 50, k = Math.log10(Math.max(s.pop, 1) / 80000);
  const rows = [], w = [];
  for (const [brand, model, vtype, year, engine, base] of D.table) {
    if (!s.brands.includes(brand) || year < s.yFrom || year > s.yTo) continue;
    const m = D.kFarm[vtype] * f + (D.kCity[vtype] + (D.kCityBrand[brand] || 0)) * k;
    rows.push({ year, brand, model, engine, vtype });
    w.push(base * curve(year, s.mean) / curve(year, D.defaultMean) * Math.exp(m));
  }
  return [rows, w];
}

function addMilesAndCoverage(v, farm) {
  const age = Math.max(0.3, D.today - v.year);
  const perYear = D.milesPerYear * (1 + 0.25 * (farm - 50) / 50) * (v.vtype === "hd" || v.vtype === "van" ? 1.2 : 1);
  const miles = Math.round(age * perYear * Math.exp(0.3 * gauss()) / 1000) * 1000;
  const [[by, bm], [py, pm]] = warranty(v.brand, v.year);
  let coverage, covers;
  if (age <= by && miles <= bm) [coverage, covers] = [`B2B ${by}yr/${bm / 1000}k`, ["b2b", "pt"]];
  else if (age <= py && miles <= pm) [coverage, covers] = [`Powertrain ${py}yr/${pm / 1000}k`, ["pt"]];
  else if (Math.random() < D.serviceContract) [coverage, covers] = ["Service contract", ["b2b", "pt"]];
  else [coverage, covers] = ["Out of warranty", []];
  return { ...v, age, miles, coverage, covers };
}

function fits(c, v) {
  const m = c.match || {};
  if (m.engine && !m.engine.some(e => v.engine.includes(e))) return false;
  if (m.model && !m.model.some(x => v.model.includes(x))) return false;
  if (m.types && !m.types.includes(v.vtype)) return false;
  if (m.years && !inYears(v.year, m.years)) return false;
  return true;
}

function pickConcern(v, systems) {
  const cands = [], w = [];
  for (const c of D.concerns) {
    if (!systems.includes(c.system) || !fits(c, v)) continue;
    const wear = c.onset ? Math.min(2, Math.max(0.01, (v.miles / c.onset) ** 2)) : 1;
    cands.push(c);
    w.push(c.w * wear);
  }
  return cands.length ? choices(cands, w) : null;
}

function shopOdds(v, c, shop) {
  if (shop === "any") return 1;
  if (c.pay === "recall") return shop === "dealer" ? 1 : 0;
  const covered = v.covers.includes(c.pay);
  const loyal = 0.8 * Math.exp(-v.age / 4) + 0.12;
  const dealer = covered ? 0.95 : Math.min(1, loyal * c.cp * 1.6);
  return shop === "dealer" ? dealer : 1 - dealer;
}

function generate(n, s) {
  const [rows, w] = weights(s);
  if (!rows.length || !s.systems.length) return [];
  const out = [];
  while (out.length < n) {
    let v, c, ok = false;
    for (let i = 0; i < 500 && !ok; i++) {
      v = addMilesAndCoverage(choices(rows, w), s.farm);
      c = pickConcern(v, s.systems);
      ok = c && Math.random() < shopOdds(v, c, s.shop);
    }
    if (!ok) return out;                 // filters too narrow for this shop
    out.push({ ...v, concern: Array.isArray(c.say) ? pick(c.say) : c.say, system: c.system });
  }
  return out;
}

function week(avg, saturday, s) {
  const days = saturday ? D.days : D.days.slice(0, 5);
  return days.map(([d, f]) => [d, generate(Math.max(1, Math.round(avg * f + gauss() * avg * f * D.daySpread)), s)]);
}

function mixSummary(s) {
  const [rows, w] = weights(s);
  const tot = w.reduce((a, b) => a + b, 0) || 1, by = {};
  rows.forEach((r, i) => { const t = D.typeNames[r.vtype]; by[t] = (by[t] || 0) + w[i]; });
  const pct = x => Math.round(x * 100) + "%";
  const road = Object.entries(by).sort((a, b) => b[1] - a[1]).slice(0, 5).map(([t, x]) => `${t} ${pct(x / tot)}`).join(", ");
  const smp = generate(400, s);
  if (!smp.length) return `On the road: ${road}`;
  const yr = smp.reduce((a, v) => a + v.year, 0) / smp.length;
  const mi = smp.map(v => v.miles).sort((a, b) => a - b)[smp.length >> 1];
  const cov = smp.filter(v => v.coverage !== "Out of warranty").length / smp.length;
  return `On the road: ${road}. At this shop: avg year ${yr.toFixed(1)}, median ${mi.toLocaleString()} mi, ${pct(cov)} with some coverage.`;
}

// ---------------- UI ----------------
const $ = id => document.getElementById(id);
const esc = t => String(t).replace(/[&<>"]/g, ch => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]));
let current = [];

function checks(el, names, cls) {
  el.innerHTML = names.map(n => `<label><input type="checkbox" class="${cls}" value="${esc(n)}" checked> ${esc(n)}</label>`).join("");
}

function settings() {
  const a = +$("yFrom").value, b = +$("yTo").value;
  return {
    farm: +$("farm").value, pop: 10 ** +$("pop").value, mean: +$("mean").value,
    shop: document.querySelector("input[name=shop]:checked").value,
    brands: [...document.querySelectorAll(".brand:checked")].map(x => x.value),
    systems: [...document.querySelectorAll(".sys:checked")].map(x => x.value),
    yFrom: Math.min(a, b), yTo: Math.max(a, b),
  };
}

function labels() {
  const f = +$("farm").value;
  $("farmLbl").textContent = `${f < 35 ? "City" : f > 65 ? "Farm country" : "Mixed"} (${f})`;
  $("popLbl").textContent = (Math.round(10 ** +$("pop").value / 1000) * 1000).toLocaleString() + " people";
  $("meanLbl").textContent = $("mean").value;
}

const line = v => `${v.year} ${v.brand} ${v.model} ${v.engine}, ${v.miles.toLocaleString()} mi, ${v.coverage}`;

function show(days) {
  current = days.flatMap(([d, vs]) => vs.map(v => [d, v]));
  const covCls = c => c.startsWith("B2B") ? "b2b" : c.startsWith("Power") ? "pt" : c.startsWith("Service") ? "sc" : "ow";
  let html = "";
  for (const [d, vs] of days) {
    if (d) html += `<h3 class="day">${d} <span>${vs.length} car${vs.length === 1 ? "" : "s"}</span></h3>`;
    html += vs.map((v, i) => `<li class="car">
      <div class="num">${i + 1}</div>
      <div class="body">
        <div class="veh"><b>${v.year} ${esc(v.brand)} ${esc(v.model)}</b> <span class="eng">${esc(v.engine)}</span></div>
        <div class="meta">${v.miles.toLocaleString()} mi <span class="cov ${covCls(v.coverage)}">${esc(v.coverage)}</span></div>
        <div class="say">“${esc(v.concern)}”</div>
      </div></li>`).join("");
  }
  $("list").innerHTML = current.length ? html : `<p class="empty">Nothing fits those filters at this shop. Loosen brands, years or systems.</p>`;
  $("status").textContent = days[0] && days[0][0]
    ? `Week: ${days.map(([d, vs]) => `${d} ${vs.length}`).join(", ")} (total ${current.length})` : "";
  setTimeout(() => { $("mix").textContent = mixSummary(settings()); }, 0);
}

const count = () => Math.max(1, Math.min(50, +$("count").value || 8));

function copy() {
  const lines = [];
  let last = null, i = 0;
  for (const [d, v] of current) {
    if (d && d !== last) { lines.push(`\n${d}`); last = d; i = 0; }
    lines.push(`${++i}. ${line(v)} - "${v.concern}"`);
  }
  const text = lines.join("\n").trim();
  const done = () => { $("copy").textContent = "Copied"; setTimeout(() => ($("copy").textContent = "Copy"), 1200); };
  if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, () => prompt("Copy this:", text));
  else prompt("Copy this:", text);
}

function init() {
  for (const id of ["yFrom", "yTo"]) {
    $(id).innerHTML = Array.from({ length: LAST_YEAR - D.years[0] + 1 }, (_, i) => D.years[0] + i)
      .map(y => `<option>${y}</option>`).join("");
  }
  $("yFrom").value = D.years[0];
  $("yTo").value = LAST_YEAR;
  $("mean").value = D.defaultMean;
  checks($("brands"), D.brands, "brand");
  checks($("systems"), D.systems, "sys");
  for (const id of ["farm", "pop", "mean"]) $(id).addEventListener("input", labels);
  $("gen").onclick = () => show([["", generate(count(), settings())]]);
  $("week").onclick = () => show(week(count(), $("sat").checked, settings()));
  $("copy").onclick = copy;
  $("toggle").onclick = () => document.body.classList.toggle("open");
  labels();
  $("gen").click();
}
init();
