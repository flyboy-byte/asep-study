#!/usr/bin/env python3
"""Bay generator: random GM gas vehicles (2013-2026) with a customer concern, as if they rolled into your bay.

GUI:  python3 bay_gen.py
CLI:  python3 bay_gen.py --cli [-n 8] [--farm 50] [--pop 80000] [--mean 2019] [--shop dealer|indie|any]
      python3 bay_gen.py --cli --week [--sat] -n 8      (a work week, -n = average cars per day)

Vehicle weight = model base (per 1,000) x year curve x farm knob x city-size knob x engine share.
Mileage = age x ~12.5k/yr (more in farm country, HD and vans) with random spread.
Coverage = GM factory warranty by brand/model year (WARRANTY), plus a random share with a service contract.
Concern = picked from concerns.py among those that fit the vehicle, weighted up by mileage for wear items.
Shop filter = whether this customer would bring this concern to a dealer (or an independent shop), given
coverage and vehicle age. Rejected draws are redrawn, which is what skews dealer traffic newer.
"""
import argparse, math, random
from fleet import MODELS, BRANDS, YEARS
from concerns import CONCERNS, SYSTEMS

YEAR_SD = 3.5          # guess: how spread out vehicle ages are around the peak year
PARTIAL_LAST = 0.5     # the newest model year is only partly on the road
DEFAULT_MEAN = 2019
MILES_PER_YEAR = 12_500
TODAY = 2026.8         # for vehicle age; a model year goes into service around the fall before
SERVICE_CONTRACT = 0.08  # guess: share of out-of-warranty vehicles with an extended service contract

# GM factory warranty (years, miles), from in-service date. Checked 2026-10-22 against press coverage:
# Chevy/GMC powertrain dropped 5/100k -> 5/60k for MY2016; Buick B2B 4/50 -> 3/36 for MY2020
# (its powertrain 6/70 -> 5/60 the same year is INFERRED); Cadillac 4/50 + 6/70 throughout.
def warranty(brand, year):
    if brand == "Cadillac" or (brand == "Buick" and year <= 2019):
        return (4, 50_000), (6, 70_000)
    return (3, 36_000), ((5, 100_000) if year <= 2015 and brand != "Buick" else (5, 60_000))

# How strongly each vehicle type responds to the knobs (log-scale multipliers).
K_FARM = {"hd": 1.4, "pickup": 0.9, "fullsuv": 0.3, "van": 0.3, "suv": 0.0, "smallsuv": -0.5, "car": -0.9, "sport": -0.4}
K_CITY = {"hd": -0.8, "pickup": -0.5, "fullsuv": -0.1, "van": 0.2, "suv": 0.1, "smallsuv": 0.5, "car": 0.6, "sport": 0.3}
K_CITY_BRAND = {"Cadillac": 0.6, "Buick": 0.3}
TYPE_NAMES = {"hd": "HD pickup", "pickup": "Pickup", "fullsuv": "Full-size SUV", "van": "Van",
              "suv": "SUV", "smallsuv": "Small SUV", "car": "Car", "sport": "Sports car"}


def year_range(s):
    a, _, b = s.partition("-")
    return range(int(a), int(b or a) + 1)


def curve(y, mean):
    return math.exp(-0.5 * ((y - mean) / YEAR_SD) ** 2) * (PARTIAL_LAST if y == YEARS[1] else 1)


def build_table():
    """Expand fleet.py into (brand, model, type, year, engine, base_weight) at default settings."""
    table = []
    for brand, model, vtype, base, engines in MODELS:
        by_year = {}
        for yrs, eng, share in engines:
            for y in year_range(yrs):
                by_year.setdefault(y, []).append((eng, share))
        rate = base / sum(curve(y, DEFAULT_MEAN) for y in by_year)
        for y, opts in by_year.items():
            total = sum(s for _, s in opts)
            for eng, share in opts:
                table.append((brand, model, vtype, y, eng, rate * share / total))
    return table


TABLE = build_table()


def weights(farm=50, pop=80_000, mean=DEFAULT_MEAN, brands=BRANDS, y_from=YEARS[0], y_to=YEARS[1], **_):
    f = (farm - 50) / 50                  # -1 (all city) .. +1 (deep farm country)
    s = math.log10(max(pop, 1) / 80_000)  # 0 at 80k; +1 = 10x bigger city
    rows, w = [], []
    for brand, model, vtype, y, eng, base in TABLE:
        if brand not in brands or not (y_from <= y <= y_to):
            continue
        k = K_FARM[vtype] * f + (K_CITY[vtype] + K_CITY_BRAND.get(brand, 0)) * s
        rows.append(dict(year=y, brand=brand, model=model, engine=eng, vtype=vtype))
        w.append(base * curve(y, mean) / curve(y, DEFAULT_MEAN) * math.exp(k))
    return rows, w


def add_miles_and_coverage(v, farm):
    age = max(0.3, TODAY - v["year"])
    per_year = MILES_PER_YEAR * (1 + 0.25 * (farm - 50) / 50) * (1.2 if v["vtype"] in ("hd", "van") else 1)
    miles = int(round(age * per_year * random.lognormvariate(0, 0.3), -3))
    (by, bm), (py, pm) = warranty(v["brand"], v["year"])
    if age <= by and miles <= bm:
        cov, covers = f"B2B {by}yr/{bm // 1000}k", {"b2b", "pt"}
    elif age <= py and miles <= pm:
        cov, covers = f"Powertrain {py}yr/{pm // 1000}k", {"pt"}
    elif miles <= 150_000 and random.random() < SERVICE_CONTRACT:   # contracts rarely run past ~150k
        cov, covers = "Service contract", {"b2b", "pt"}
    else:
        cov, covers = "Out of warranty", set()
    return dict(v, age=age, miles=miles, coverage=cov, covers=covers)


def fits(c, v):
    m = c.get("match", {})
    if "engine" in m and not any(e in v["engine"] for e in m["engine"]):
        return False
    if "model" in m and not any(x in v["model"] for x in m["model"]):
        return False
    if "types" in m and v["vtype"] not in m["types"]:
        return False
    if "years" in m and v["year"] not in year_range(m["years"]):
        return False
    return True


def pick_concern(v, systems):
    cands, w = [], []
    for c in CONCERNS:
        if c["system"] in systems and fits(c, v):
            # Wear/age items: rare on low miles, common past onset (squared so a 10k-mile truck rarely gets one).
            wear = min(2.0, max(0.01, (v["miles"] / c["onset"]) ** 2)) if "onset" in c else 1
            cands.append(c)
            w.append(c["w"] * wear)
    return random.choices(cands, weights=w)[0] if cands else None


def shop_odds(v, c, shop):
    """Chance this customer brings this concern to this kind of shop."""
    if shop == "any":
        return 1.0
    if c["pay"] == "recall":
        return 1.0 if shop == "dealer" else 0.0
    covered = c["pay"] in v["covers"]
    # Customer-pay loyalty to the dealer fades with age: ~0.9 new, ~0.35 at 5 yr, ~0.2 at 10 yr.
    loyal = 0.8 * math.exp(-v["age"] / 4) + 0.12
    dealer = 0.95 if covered else min(1.0, loyal * c["cp"] * 1.6)
    return dealer if shop == "dealer" else 1 - dealer


def generate(n=8, systems=SYSTEMS, shop="dealer", **kw):
    rows, w = weights(**kw)
    if not rows or not systems:
        return []
    out = []
    while len(out) < n:
        for _ in range(500):
            v = add_miles_and_coverage(random.choices(rows, weights=w)[0], kw.get("farm", 50))
            c = pick_concern(v, systems)
            if c and random.random() < shop_odds(v, c, shop):
                break
        else:
            return out                    # filters too narrow for this shop; return what we have
        v["concern"] = random.choice(c["say"]) if isinstance(c["say"], list) else c["say"]
        v["system"] = c["system"]
        out.append(v)
    return out


DAYS = [("Mon", 1.15), ("Tue", 1.0), ("Wed", 1.0), ("Thu", 0.95), ("Fri", 0.9), ("Sat", 0.5)]
DAY_SPREAD = 0.25      # guess: day-to-day variation in car count (25% of that day's average)


def week(avg=8, saturday=False, **kw):
    """A work week: each day's car count varies around avg (Monday busiest, Saturday a half day)."""
    days = DAYS if saturday else DAYS[:5]
    return [(d, generate(max(1, round(random.gauss(avg * f, avg * f * DAY_SPREAD))), **kw)) for d, f in days]


def mix_summary(**kw):
    """Vehicles on the road vs what actually shows up at this shop (sampled)."""
    rows, w = weights(**kw)
    tot = sum(w) or 1
    by = {}
    for r, x in zip(rows, w):
        by[TYPE_NAMES[r["vtype"]]] = by.get(TYPE_NAMES[r["vtype"]], 0) + x
    road = ", ".join(f"{t} {v / tot:.0%}" for t, v in sorted(by.items(), key=lambda kv: -kv[1])[:5])
    s = generate(400, **kw)
    if not s:
        return f"On the road: {road}"
    yr = sum(v["year"] for v in s) / len(s)
    mi = sorted(v["miles"] for v in s)[len(s) // 2]
    cov = sum(v["coverage"] != "Out of warranty" for v in s) / len(s)
    return f"On the road: {road}  |  At this shop: avg year {yr:.1f}, median {mi:,} mi, {cov:.0%} with some coverage"


def gui():
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("Bay Generator")
    root.geometry("1400x660")
    ctl = ttk.Frame(root, padding=10)
    ctl.pack(side="left", fill="y")
    out = ttk.Frame(root, padding=(0, 10, 10, 10))
    out.pack(side="left", fill="both", expand=True)

    farm = tk.IntVar(value=50)
    pop = tk.DoubleVar(value=math.log10(80_000))
    mean = tk.IntVar(value=DEFAULT_MEAN)
    y_from, y_to = tk.IntVar(value=YEARS[0]), tk.IntVar(value=YEARS[1])
    count = tk.IntVar(value=8)
    saturday = tk.BooleanVar(value=False)
    shop = tk.StringVar(value="dealer")
    brand_on = {b: tk.BooleanVar(value=True) for b in BRANDS}
    sys_on = {s: tk.BooleanVar(value=True) for s in SYSTEMS}
    farm_lbl, pop_lbl, mean_lbl = tk.StringVar(), tk.StringVar(), tk.StringVar()
    mix = tk.StringVar()
    current = []

    def settings():
        return dict(farm=farm.get(), pop=10 ** pop.get(), mean=mean.get(), shop=shop.get(),
                    brands=[b for b, v in brand_on.items() if v.get()],
                    systems=[s for s, v in sys_on.items() if v.get()],
                    y_from=min(y_from.get(), y_to.get()), y_to=max(y_from.get(), y_to.get()))

    def labels(*_):
        farm_lbl.set(f"Area: {'city' if farm.get() < 35 else 'farm country' if farm.get() > 65 else 'mixed'} ({farm.get()})")
        pop_lbl.set(f"City size: {round(10 ** pop.get(), -3):,.0f} people")
        mean_lbl.set(f"Peak model year: {mean.get()}")

    def row(label_var, widget):
        ttk.Label(ctl, textvariable=label_var).pack(anchor="w", pady=(6, 0))
        widget.pack(fill="x")

    row(farm_lbl, ttk.Scale(ctl, from_=0, to=100, variable=farm, length=220,
                            command=lambda v: (farm.set(round(float(v))), labels())))
    row(pop_lbl, ttk.Scale(ctl, from_=math.log10(5_000), to=math.log10(1_000_000), variable=pop, command=labels))
    row(mean_lbl, ttk.Scale(ctl, from_=2015, to=2023, variable=mean,
                            command=lambda v: (mean.set(round(float(v))), labels())))

    ttk.Label(ctl, text="Model years").pack(anchor="w", pady=(6, 0))
    yr = ttk.Frame(ctl)
    yr.pack(fill="x")
    for var in (y_from, y_to):
        ttk.Spinbox(yr, from_=YEARS[0], to=YEARS[1], textvariable=var, width=6).pack(side="left", padx=(0, 6))

    ttk.Label(ctl, text="Shop").pack(anchor="w", pady=(6, 0))
    sh = ttk.Frame(ctl)
    sh.pack(fill="x")
    for val, txt in (("dealer", "GM dealer"), ("indie", "Independent"), ("any", "Any")):
        ttk.Radiobutton(sh, text=txt, value=val, variable=shop).pack(side="left", padx=(0, 6))

    def checks(title, vars_):
        ttk.Label(ctl, text=title).pack(anchor="w", pady=(6, 0))
        for name, v in vars_.items():
            ttk.Checkbutton(ctl, text=name, variable=v).pack(anchor="w")

    checks("Brands", brand_on)
    checks("Concern systems", sys_on)

    cnt = ttk.Frame(ctl)
    cnt.pack(fill="x", pady=(6, 0))
    ttk.Label(cnt, text="Cars (avg per day for Week)").pack(side="left")
    ttk.Spinbox(cnt, from_=1, to=50, textvariable=count, width=5).pack(side="left", padx=6)
    ttk.Checkbutton(ctl, text="Week includes Saturday (half day)", variable=saturday).pack(anchor="w")

    cols = ("Day", "#", "Year", "Make", "Model", "Engine", "Miles", "Coverage", "Concern")
    tbl = ttk.Frame(out)
    tbl.pack(fill="both", expand=True)
    tree = ttk.Treeview(tbl, columns=cols, show="headings", height=16)
    sb = ttk.Scrollbar(tbl, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y")
    for c, wdt in zip(cols, (40, 28, 48, 75, 150, 165, 70, 135, 420)):
        tree.heading(c, text=c)
        tree.column(c, width=wdt, anchor="w", stretch=c == "Concern")
    tree.pack(side="left", fill="both", expand=True)
    detail = tk.StringVar(value="Click a row to see the full concern.")
    ttk.Label(out, textvariable=detail, wraplength=1000, font=("TkDefaultFont", 11)).pack(anchor="w", pady=(6, 0))
    ttk.Label(out, textvariable=mix, wraplength=1000, foreground="#555").pack(anchor="w", pady=(6, 0))

    def on_select(_=None):
        sel = tree.selection()
        if sel:
            day, v = current[tree.index(sel[0])]
            detail.set(f"{day + ': ' if day else ''}{v['year']} {v['brand']} {v['model']} {v['engine']}, {v['miles']:,} mi, "
                       f"{v['coverage']}:  \"{v['concern']}\"")

    tree.bind("<<TreeviewSelect>>", on_select)

    def show(days):
        """days = [(day label, [vehicles])]; a single batch uses day label ''."""
        current[:] = [(d, v) for d, vs in days for v in vs]
        tree.delete(*tree.get_children())
        for d, vs in days:
            for i, v in enumerate(vs, 1):
                tree.insert("", "end", values=(d if i == 1 else "", i, v["year"], v["brand"], v["model"], v["engine"],
                                               f"{v['miles']:,}", v["coverage"], v["concern"]))
        if not current:
            detail.set("Nothing fits those filters at this shop. Loosen brands, years or systems.")
        elif days[0][0]:
            detail.set("Week: " + ", ".join(f"{d} {len(vs)}" for d, vs in days) + f"  (total {len(current)})")
        else:
            detail.set("Click a row to see the full concern.")
        mix.set(mix_summary(**settings()))

    def do_generate(*_):
        show([("", generate(max(1, count.get()), **settings()))])

    def do_week():
        show(week(max(1, count.get()), saturday.get(), **settings()))

    def do_copy():
        lines, last = [], None
        for d, v in current:
            if d and d != last:
                lines.append(f"\n{d}")
                last, i = d, 0
            i = (i + 1) if d else len(lines) + 1
            lines.append(f"{i}. {v['year']} {v['brand']} {v['model']} {v['engine']}, {v['miles']:,} mi, "
                         f"{v['coverage']} - \"{v['concern']}\"")
        root.clipboard_clear()
        root.clipboard_append("\n".join(lines).strip())

    btns = ttk.Frame(ctl)
    btns.pack(fill="x", pady=(10, 0))
    ttk.Button(btns, text="Generate", command=do_generate).pack(side="left")
    ttk.Button(btns, text="Week", command=do_week).pack(side="left", padx=6)
    ttk.Button(btns, text="Copy", command=do_copy).pack(side="left")
    root.bind("<Return>", do_generate)

    labels()
    do_generate()
    root.mainloop()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cli", action="store_true", help="print vehicles instead of opening the window")
    ap.add_argument("-n", type=int, default=8)
    ap.add_argument("--farm", type=int, default=50, help="0 = city, 100 = deep farm country")
    ap.add_argument("--pop", type=int, default=80_000)
    ap.add_argument("--mean", type=int, default=DEFAULT_MEAN)
    ap.add_argument("--shop", choices=["dealer", "indie", "any"], default="dealer")
    ap.add_argument("--week", action="store_true", help="a work week; -n is the average cars per day")
    ap.add_argument("--sat", action="store_true", help="with --week: include a Saturday half day")
    a = ap.parse_args()
    if a.cli:
        kw = dict(farm=a.farm, pop=a.pop, mean=a.mean, shop=a.shop)
        days = week(a.n, a.sat, **kw) if a.week else [("", generate(a.n, **kw))]
        for d, vs in days:
            if d:
                print(f"\n{d} ({len(vs)} cars)")
            for i, v in enumerate(vs, 1):
                print(f"{i:2}. {v['year']} {v['brand']} {v['model']} - {v['engine']}, {v['miles']:,} mi [{v['coverage']}]")
                print(f"     \"{v['concern']}\"")
        print(mix_summary(**kw))
    else:
        gui()
