# bay-gen

Random GM vehicles that could roll into your bay, each with the customer's concern in their own words.
Click **Generate** for one batch, or **Week** for a full work week with a different car count each day.

**Use it in a browser: [flyboy-byte.github.io/asep-study](https://flyboy-byte.github.io/asep-study/)** (works on a phone).

Covers gas vehicles from model years 2013–2026 (no diesel, no EV). Each row has the year, make, model,
engine, mileage, warranty coverage and the concern. It deliberately gives no causes: diagnosing is the
tech's job.

```sh
python3 bay-gen/bay_gen.py                                        # window (tkinter)
python3 bay-gen/bay_gen.py --cli -n 8                             # one batch in the terminal
python3 bay-gen/bay_gen.py --cli --week --sat -n 8                # a week, avg 8 cars/day, plus a Saturday
python3 bay-gen/bay_gen.py --cli --farm 80 --pop 15000 --shop indie   # small farm town, independent shop
```

Needs only Python 3 and tkinter. Created 2026-10-22.

The website in `web/` is a JavaScript port of `bay_gen.py`. Its data (`web/data.js`) is generated from the
Python files: after editing `fleet.py`, `concerns.py` or the knobs, run `python3 bay-gen/export_web.py` and push.
If you change `warranty()` or the generation logic, make the same change in `web/app.js`.

## Controls

| Control | What it does |
|---|---|
| Area (city ↔ farm) | Farm country pushes pickups, especially gas HD trucks, and pulls cars down. It also adds miles per year. |
| City size (5k–1M) | A bigger city means more cars, small SUVs, Cadillac and Buick. A smaller one means more trucks. |
| Peak model year | Where the year spread peaks (default 2019). |
| Model years, brands | Narrow what can show up. |
| Shop | **GM dealer**, **Independent** or **Any**. This changes who walks in (see below). |
| Concern systems | Engine, transmission/driveline, electrical, brakes/steering/suspension, HVAC, body/interior, maintenance/recall. |
| Cars | The batch size, or the average per day for **Week**. |
| Week includes Saturday | Adds a half-day Saturday. |
| Copy | Copies the list to the clipboard, grouped by day for a week. |

Click a row to see its full concern. The bottom line compares the mix on the road with what actually
reaches this shop (average year, median miles, share with coverage).

## How a row is built

1. **Vehicle** (`fleet.py`): 46 models, each with 1–3 engines whose shares change with the generation.
   Weighted by each model's base count per 1,000 vehicles in an ~80k city with farm country around it,
   then adjusted by the area, city-size and year knobs.
2. **Mileage**: age × about 12.5k a year, with more in farm country and on HD trucks and vans, plus random spread.
3. **Coverage**: GM factory warranty for that brand and model year (table below). About 8% of
   out-of-warranty vehicles get a service contract at random.
4. **Concern** (`concerns.py`): 89 concerns written the way customers say them, many with 2–3 wordings.
   Wear and age items get more likely as mileage climbs. Some are weighted toward vehicles with a known
   GM pattern, for example:
   - an engine tick with a flashing check engine light on truck V8s
   - a rumble-strip shudder on 2015–19 V8 trucks
   - "Shift to Park"
   - a 3.6L that rattles on cold start
   - a wet headliner on 2014–18 trucks
5. **Shop filter**: whether this customer would bring this concern to this shop.
   - Covered work goes to the dealer about 95% of the time.
   - Customer-pay work goes to the dealer less as the vehicle ages. Each concern has its own odds (`cp`):
     radio glitches, rattles and stop/start questions show up almost only while they're free, and brakes,
     tires and exhaust mostly go elsewhere once the vehicle is out of warranty.
   - Recalls only ever go to the dealer.

   A rejected draw is drawn again, so dealer traffic skews newer (average about 2021, median about 50k miles)
   and independent traffic skews older (about 2018.5, about 100k).
6. **Week**: each day's count varies around the average (±25%). Monday is busiest, Friday a little slower,
   and Saturday is a half day.

## Warranty terms used (checked 2026-10-22)

| Brand | Model years | Bumper-to-bumper | Powertrain |
|---|---|---|---|
| Chevrolet, GMC | 2013–2015 | 3 yr / 36k | 5 yr / 100k |
| Chevrolet, GMC | 2016+ | 3 yr / 36k | 5 yr / 60k |
| Buick | through 2019 | 4 yr / 50k | 6 yr / 70k |
| Buick | 2020+ | 3 yr / 36k | 5 yr / 60k (the year powertrain changed is inferred) |
| Cadillac | all | 4 yr / 50k | 6 yr / 70k |

Not modeled: the federal 8 yr / 80k emissions warranty, special coverages, CPO, and battery-specific terms.

## Tuning

Every count, share, onset, dealer odds and day factor is an educated guess, not registration or RO data.
They're all plain Python, so edit them freely:

| File | What to edit |
|---|---|
| `fleet.py` | Models, years, engines, engine shares, base counts |
| `concerns.py` | Concerns and their wording, weights, `onset`, `pay` (b2b / pt / wear / recall), `cp`, vehicle filters |
| `bay_gen.py` | Knob strengths (`K_FARM`, `K_CITY`, `K_CITY_BRAND`), `warranty()`, `SERVICE_CONTRACT`, `DAYS` and `DAY_SPREAD`, miles per year |

## Ideas not built yet

- More than one concern per visit
- Comebacks
- "Can't duplicate" intermittents
- Seasons
- Farm-truck aftermarket accessories
- Advisor notes
- A replay seed and CSV export
