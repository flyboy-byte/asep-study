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
  else if (miles <= 150000 && Math.random() < D.serviceContract) [coverage, covers] = ["Service contract", ["b2b", "pt"]];
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

const MAX_REPEAT = 5;   // the same concern shows up at most this many times in one week

function pickConcern(v, systems, pool = D.concerns, used = new Map()) {
  const cands = [], w = [];
  for (const c of pool) {
    if (!systems.includes(c.system) || !fits(c, v) || (used.get(c) || 0) >= MAX_REPEAT) continue;
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

// warranty = the factory warranty or a service contract would pay for this concern (recalls always).
// A repeated concern gets a wording not used yet this week when there is one.
function finish(v, c, used = new Map(), said = new Set()) {
  const says = Array.isArray(c.say) ? c.say : [c.say], fresh = says.filter(x => !said.has(x));
  const concern = pick(fresh.length ? fresh : says);
  used.set(c, (used.get(c) || 0) + 1);
  said.add(concern);
  return { ...v, ref: c, concern, system: c.system, notes: c.notes || [], warranty: c.pay === "recall" || v.covers.includes(c.pay) };
}

// The diag of the week: one vehicle with a harder scenario from D.hard, through the same shop filter.
function genDiag(s) {
  const [rows, w] = weights(s);
  if (!rows.length || !s.systems.length) return null;
  for (let i = 0; i < 3000; i++) {
    const v = addMilesAndCoverage(choices(rows, w), s.farm);
    const c = pickConcern(v, s.systems, D.hard);
    if (c && Math.random() < shopOdds(v, c, s.shop)) return { ...finish(v, c), diag: true };
  }
  return null;
}

function generate(n, s, used = new Map(), said = new Set()) {
  const [rows, w] = weights(s);
  if (!rows.length || !s.systems.length) return [];
  const out = [];
  while (out.length < n) {
    let v, c, ok = false;
    for (let i = 0; i < 500 && !ok; i++) {
      v = addMilesAndCoverage(choices(rows, w), s.farm);
      c = pickConcern(v, s.systems, D.concerns, used);
      ok = c && Math.random() < shopOdds(v, c, s.shop);
    }
    if (!ok) return out;                 // filters too narrow for this shop
    out.push(finish(v, c, used, said));
  }
  return out;
}

function week(avg, saturday, s) {
  const days = saturday ? D.days : D.days.slice(0, 5);
  const used = new Map(), said = new Set();   // shared across the week for the repeat cap
  return days.map(([d, f]) => [d, generate(Math.max(1, Math.round(avg * f + gauss() * avg * f * D.daySpread)), s, used, said)]);
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
// State: the week (days of cars) and the diag car, which always sits in one of those days.
// New week keeps the diag car (dropped into a random slot); New diag swaps it for a fresh one.
const $ = id => document.getElementById(id);
const esc = t => String(t).replace(/[&<>"]/g, ch => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]));
const FULL_DAY = { Mon: "Monday", Tue: "Tuesday", Wed: "Wednesday", Thu: "Thursday", Fri: "Friday", Sat: "Saturday" };
const S = { days: [], diag: null, day: "Mon", sort: { key: "order", dir: 1 } };

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
  $("popLbl").textContent = (Math.round(10 ** +$("pop").value / 1000) * 1000).toLocaleString();
  $("meanLbl").textContent = $("mean").value;
}

const count = () => Math.max(1, Math.min(50, +$("count").value || 5));
const stillFits = (v, s) => s.brands.includes(v.brand) && v.year >= s.yFrom && v.year <= s.yTo && s.systems.includes(v.system);

function findDiag() {
  for (const [d, cars] of S.days) {
    const i = cars.indexOf(S.diag);
    if (i >= 0) return [d, cars, i];
  }
  return null;
}

// Concern counts for the repeat cap, from every ordinary car outside `skipDay`.
function usage(skipDay) {
  const used = new Map(), said = new Set();
  for (const [d, cs] of S.days) if (d !== skipDay) for (const v of cs) {
    if (!v.diag) { used.set(v.ref, (used.get(v.ref) || 0) + 1); said.add(v.concern); }
  }
  return [used, said];
}

// Put the diag car in a random slot (replacing an ordinary car), on `day` if given.
function placeDiag(day) {
  const [, cars] = day ? S.days.find(([d]) => d === day) : choices(S.days, S.days.map(([, c]) => c.length || 0.5));
  cars.splice(Math.floor(Math.random() * (cars.length + 1)), cars.length ? 1 : 0, S.diag);
}

function newDiag() {
  const s = settings(), d = genDiag(s);
  if (!d) return render("Nothing fits those filters at this shop. Loosen brands, years or systems.");
  const at = findDiag();
  if (at) {                                   // the old diag car's slot gets an ordinary car
    const [, cars, i] = at, fill = generate(1, s, ...usage());
    fill.length ? cars.splice(i, 1, fill[0]) : cars.splice(i, 1);
  }
  S.diag = d;
  placeDiag();
  render();
}

function newWeek() {
  const s = settings();
  S.days = week(count(), $("sat").checked, s);
  if (!S.days.some(([, c]) => c.length)) { S.diag = null; return render("Nothing fits those filters at this shop. Loosen brands, years or systems."); }
  if (S.day !== "All" && !S.days.some(([d]) => d === S.day)) S.day = "Mon";
  if (S.diag && stillFits(S.diag, s)) { placeDiag(); render(); }
  else { S.diag = null; newDiag(); }
}

// Rebuild only the selected day. If the diag car was on it, it stays on that day.
function newDay() {
  const s = settings(), entry = S.days.find(([d]) => d === S.day);
  if (!entry) return;
  const f = D.days.find(([d]) => d === S.day)[1], avg = count();
  const hadDiag = S.diag && entry[1].includes(S.diag);
  entry[1] = generate(Math.max(1, Math.round(avg * f + gauss() * avg * f * D.daySpread)), s, ...usage(S.day));
  if (!hadDiag) return render();
  if (!stillFits(S.diag, s)) { S.diag = null; return newDiag(); }
  placeDiag(S.day);
  render();
}

const SORTS = {
  order: null,
  year: v => v.year, make: v => `${v.brand} ${v.model}`, engine: v => v.engine,
  miles: v => v.miles, warranty: v => (v.warranty ? 0 : 1), concern: v => v.concern,
};

function rows() {
  let list = S.days.flatMap(([d, cars]) => cars.map((v, i) => ({ d, i: i + 1, v })));
  if (S.day !== "All") list = list.filter(r => r.d === S.day);
  const f = SORTS[S.sort.key];
  if (f) list.sort((a, b) => { const x = f(a.v), y = f(b.v); return (x < y ? -1 : x > y ? 1 : 0) * S.sort.dir; });
  else if (S.sort.dir < 0) list.reverse();
  return list;
}

let shown = [];                               // cars in the table, in display order (for the row copy buttons)
const textLine = v => `${v.year} ${v.brand} ${v.model}: ${v.concern}`;   // ready to paste into a text message
const copyBtn = i => `<button class="cp" data-copy="${i}" title="Copy for a text message" aria-label="Copy">Copy</button>`;

function copyText(text, btn, label = "Copy") {
  const done = () => { btn.textContent = "Copied"; setTimeout(() => (btn.textContent = label), 1200); };
  if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, () => prompt("Copy this:", text));
  else prompt("Copy this:", text);
}

const wChip = w => `<span class="chip ${w ? "yes" : "no"}">${w ? "Yes" : "No"}</span>`;

function render(msg) {
  // Diag of the week
  const at = S.diag && findDiag();
  if (!S.diag || !at) {
    $("diagBody").innerHTML = `<p class="empty">${esc(msg || "No diag yet.")}</p>`;
    $("diagDay").hidden = true;
  } else {
    const v = S.diag;
    $("diagDay").hidden = false;
    $("diagDay").textContent = `Comes in ${FULL_DAY[at[0]]}`;
    $("diagBody").innerHTML = `
      <div class="dhead"><div class="dveh">${v.year} ${esc(v.brand)} ${esc(v.model)}</div>${copyBtn("diag")}</div>
      <div class="dmeta"><span>${esc(v.engine)}</span><span>${v.miles.toLocaleString()} mi</span>
        <span>Warranty ${wChip(v.warranty)}</span><span>${esc(v.system)}</span></div>
      <blockquote>“${esc(v.concern)}”</blockquote>
      ${v.notes.length ? `<ul class="notes">${v.notes.map(n => `<li>${esc(n)}</li>`).join("")}</ul>` : ""}`;
  }

  // Day buttons
  const total = S.days.reduce((a, [, c]) => a + c.length, 0);
  const btn = (key, label, n) => `<button class="dayBtn" data-day="${key}" aria-pressed="${S.day === key}">
      <span>${label}</span><b>${n}</b>${at && at[0] === key ? '<i title="Technical report">●</i>' : ""}</button>`;
  $("days").innerHTML = S.days.map(([d, c]) => btn(d, d, c.length)).join("") + btn("All", "All", total);
  $("newDay").hidden = S.day === "All";
  $("newDay").textContent = `New ${S.day}`;
  $("weekTitle").textContent = S.day === "All" ? `Whole week, ${total} cars` : `${FULL_DAY[S.day]}, ${S.days.find(([d]) => d === S.day)?.[1].length || 0} cars`;

  // Table (cards on a phone)
  const all = S.day === "All", list = rows();
  shown = list.map(r => r.v);
  const cols = [["order", "#"], ...(all ? [["day", "Day"]] : []), ["year", "Year"], ["make", "Vehicle"], ["engine", "Engine"],
    ["miles", "Miles"], ["warranty", "Warranty"], ["concern", "Concern"], ["copy", ""]];
  const arrow = k => S.sort.key === k ? (S.sort.dir > 0 ? " ▲" : " ▼") : "";
  $("thead").innerHTML = "<tr>" + cols.map(([k, t]) =>
    k === "day" || k === "copy" ? `<th>${t}</th>` : `<th><button data-sort="${k}">${t}${arrow(k)}</button></th>`).join("") + "</tr>";
  $("tbody").innerHTML = list.length ? list.map(({ d, i, v }, n) => `<tr class="${v.diag ? "isDiag" : ""}">
      <td class="c-num">${i}</td>${all ? `<td class="c-day">${d}</td>` : ""}
      <td class="c-year">${v.year}</td>
      <td class="c-veh">${esc(v.brand)} ${esc(v.model)}${v.diag ? ' <span class="tag">REPORT</span>' : ""}</td>
      <td class="c-eng">${esc(v.engine)}</td>
      <td class="c-mi">${v.miles.toLocaleString()}<span class="u"> mi</span></td>
      <td class="c-w"><span class="lbl">Warranty </span>${wChip(v.warranty)}</td>
      <td class="c-say">“${esc(v.concern)}”</td><td class="c-cp">${copyBtn(n)}</td></tr>`).join("")
    : `<tr><td colspan="${cols.length}" class="empty">${esc(msg || "No cars.")}</td></tr>`;
  $("sortSel").value = `${S.sort.key}:${S.sort.dir}`;
}

function setSort(key, dir) {
  S.sort = { key, dir: dir ?? (S.sort.key === key ? -S.sort.dir : 1) };
  render();
}

function copy() {
  const line = v => `${v.year} ${v.brand} ${v.model} ${v.engine}, ${v.miles.toLocaleString()} mi, warranty ${v.warranty ? "yes" : "no"} - "${v.concern}"`;
  const out = [];
  if (S.diag) out.push(`TECHNICAL REPORT: ${line(S.diag)}`, ...S.diag.notes.map(n => `  - ${n}`));
  for (const [d, cars] of S.days) {
    out.push(`\n${FULL_DAY[d]}`);
    cars.forEach((v, i) => out.push(`${i + 1}. ${line(v)}${v.diag ? "  [REPORT]" : ""}`));
  }
  copyText(out.join("\n").trim(), $("copy"), "Copy week");
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
  $("newWeek").onclick = newWeek;
  $("newDiag").onclick = newDiag;
  $("newDay").onclick = newDay;
  $("copy").onclick = copy;
  document.addEventListener("click", e => {
    const b = e.target.closest("[data-copy]");
    if (b) copyText(textLine(b.dataset.copy === "diag" ? S.diag : shown[+b.dataset.copy]), b);
  });
  $("diagDay").onclick = () => { const at = findDiag(); if (at) { S.day = at[0]; render(); $("weekBox").scrollIntoView({ behavior: "smooth" }); } };
  $("days").onclick = e => { const b = e.target.closest("[data-day]"); if (b) { S.day = b.dataset.day; render(); } };
  $("thead").onclick = e => { const b = e.target.closest("[data-sort]"); if (b) setSort(b.dataset.sort); };
  $("sortSel").onchange = e => { const [k, d] = e.target.value.split(":"); setSort(k, +d); };
  const toggle = open => { document.body.classList.toggle("open", open); $("toggle").setAttribute("aria-expanded", open); };
  $("toggle").onclick = () => toggle(!document.body.classList.contains("open"));
  $("done").onclick = () => toggle(false);
  $("mixBtn").onclick = () => { $("mix").textContent = mixSummary(settings()); };
  labels();
  newWeek();
}
init();
