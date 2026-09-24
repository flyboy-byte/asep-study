# Automatic Transmission Image Notes

**Image set reviewed:** 2026-09-22  
**Scope:** 15 supplied screenshots only. The `.txt` file in the older `notes/` directory was deliberately ignored and was not used to create this document.

## What this image set covers

The first 14 screenshots are GM/ACDelco training slides for an illustrated 10-speed automatic transmission. They cover the range-reference clutch chart and power flow in Park, Reverse, Neutral, and 1st through 10th gear. The last screenshot is a general planetary-gear action chart.

These notes organize the visible material into exam-ready patterns. They do not identify the transmission model because the model designation is not visible in the supplied images.

## Main ideas to know first

1. **Start diagnosis with the correct range-reference chart from current Service Information (SI).** The chart tells which friction elements should be applied in each range. The slide text also says that a related chart can show shift-solenoid states and the ratio for each gear.
2. **Every operating range needs an input, an output, and usually a reaction member.** A clutch may connect rotating members or hold a member stationary. The diagrams make more sense when each applied element is labeled as driving, driven, or reacting.
3. **A listed clutch application does not always mean full line-pressure holding force.** The 1st-gear footnote says the 1-2-3-4-6-7-8-10-R clutch is applied with only enough pressure to prevent slip, not with line pressure.
4. **Ratio tells the operating category.** A ratio above 1:1 is reduction and torque multiplication; 1.000:1 is direct drive; a ratio below 1:1 is overdrive.
5. **The one-way clutch changes role as the transmission upshifts.** It holds in 1st and 2nd, overruns in 3rd through 7th, and is not listed as active in 8th through 10th.
6. **Clutch names are functional labels tied to the calibration represented by the chart.** The slide warns that calibration changes can make a clutch's gear-number name inaccurate. Use the chart for the exact vehicle and calibration being diagnosed.

## Range-reference chart

### Clutch abbreviations used below

| Short name | Full clutch name shown in the image |
|---|---|
| C1 | 1-2-3-4-5-6-Reverse clutch |
| C2 | 1-2-8-9-10-Reverse clutch |
| C3 | 2-3-4-5-7-9-10 clutch |
| C4 | 1-2-3-4-6-7-8-10-Reverse clutch |
| C5 | 1-3-5-6-7-8-9 clutch |
| C6 | 4-5-6-7-8-9-10-Reverse clutch |
| OWC | One-way clutch |

### Applications by range

| Range/gear | C1 | C2 | C3 | C4 | C5 | C6 | OWC |
|---|---|---|---|---|---|---|---|
| Park | Applied | Applied | — | — | — | — | — |
| Reverse | Applied | Applied | — | Applied | — | Applied | — |
| Neutral | Applied | Applied | — | Applied | — | — | — |
| 1st | Applied | Applied | — | Applied¹ | Applied | — | Holding |
| 2nd | Applied | Applied | Applied | Applied | — | — | Holding |
| 3rd | Applied | — | Applied | Applied | Applied | — | O/R |
| 4th | Applied | — | Applied | Applied | — | Applied | O/R |
| 5th | Applied | — | Applied | — | Applied | Applied | O/R |
| 6th | Applied | — | — | Applied | Applied | Applied | O/R |
| 7th | — | — | Applied | Applied | Applied | Applied | O/R |
| 8th | — | Applied | — | Applied | Applied | Applied | — |
| 9th | — | Applied | Applied | — | Applied | Applied | — |
| 10th | — | Applied | Applied | Applied | — | Applied | — |

**O/R** means over-running.  
**¹** In 1st, C4 is applied without line pressure. It has only enough pressure to prevent the clutch from slipping.

[Open the original range-reference chart](images/Screenshot_20260920_161143.png)

## Ratio progression

| Range | Approximate ratio shown | Category | Big-picture meaning |
|---|---:|---|---|
| Reverse | 4.866:1 | Reverse reduction | High torque multiplication with reversed output rotation |
| 1st | 4.696:1 | Reduction | Greatest forward torque multiplication in the chart |
| 2nd | 2.985:1 | Reduction | Less multiplication, more output speed |
| 3rd | 2.156:1 | Reduction | Continues the move toward direct drive |
| 4th | 1.779:1 | Reduction | Forward reduction |
| 5th | 1.526:1 | Reduction | Forward reduction |
| 6th | 1.278:1 | Reduction | Last reduction ratio shown before direct drive |
| 7th | 1.000:1 | Direct drive | Input and output speed are equal in ratio terms |
| 8th | 0.854:1 | Overdrive | Output turns faster than input in ratio terms |
| 9th | 0.689:1 | Overdrive | Greater overdrive than 8th |
| 10th | 0.636:1 | Overdrive | Tallest ratio shown; lowest engine speed for a given road speed |

The progression is the key pattern: **high reduction → decreasing reduction → direct drive → increasing overdrive**.

## Park, Neutral, and Reverse

### Park

- The park-pawl actuator engages the park pawl with lugs on the output-carrier assembly.
- Holding the output carrier prevents vehicle movement.
- Internal members can still be driven by the turbine shaft, but the power flow terminates without driving the output.
- C1 and C2 are applied according to the range chart.

[Open the Park image](images/Screenshot_20260920_161204.png)

### Neutral

- The park-pawl actuator is disengaged, and the pawl spring releases the pawl from the output carrier.
- The output carrier is free to rotate, but there is no completed torque path that drives the vehicle.
- C1, C2, and C4 are applied according to the range chart. Applied clutches alone do not prove that output torque exists; the complete drive-and-reaction path matters.

[Open the Neutral image](images/Screenshot_20260920_161225.png)

### Reverse

- Reverse uses gear reduction and reverses output rotation at approximately 4.866:1.
- The visible description routes power from the turbine shaft through the input carrier and direct-overdrive sun-gear shaft.
- C4 holds the direct-overdrive carrier, while C6 holds the output-carrier internal-gear transfer-shell path. Together with C1 and C2, these applied elements establish the reverse power path.
- For diagnosis, compare a loss of Reverse with other ranges that share C1, C2, C4, or C6 rather than condemning a part from the Reverse symptom alone.

[Open the Reverse image](images/Screenshot_20260920_161214.png)

## Forward gears

The diagrams repeatedly use the turbine shaft, input carrier and pinions, direct-overdrive sun gear and shaft, output sun gear and pinions, internal gears, carriers, transfer shell, and the six clutch groups. The exact path changes with the applied and released elements.

| Gear | What changes from the previous forward gear | OWC state | Source image |
|---|---|---|---|
| 1st | Starting state: C1, C2, low-pressure C4, and C5 applied | Holding | [1st](images/Screenshot_20260920_161234.png) |
| 2nd | C3 applies; C5 releases; C4 is shown fully applied | Holding | [2nd](images/Screenshot_20260920_161245.png) |
| 3rd | C2 releases; C5 applies | Over-running | [3rd](images/Screenshot_20260920_161253.png) |
| 4th | C5 releases; C6 applies | Over-running | [4th](images/Screenshot_20260920_161300.png) |
| 5th | C4 releases; C5 applies | Over-running | [5th](images/Screenshot_20260920_161310.png) |
| 6th | C3 releases; C4 applies | Over-running | [6th](images/Screenshot_20260920_161318.png) |
| 7th | C1 releases; C3 applies; ratio becomes 1.000:1 | Over-running | [7th](images/Screenshot_20260920_161328.png) |
| 8th | C3 releases; C2 applies; first overdrive ratio | Not listed | [8th](images/Screenshot_20260920_161337.png) |
| 9th | C4 releases; C3 applies | Not listed | [9th](images/Screenshot_20260920_161345.png) |
| 10th | C5 releases; C4 applies | Not listed | [10th](images/Screenshot_20260920_161352.png) |

This shift-change table is useful for fault isolation. If two affected ranges share an applied element, that shared element becomes a candidate; if an unaffected range also depends on it, the diagnosis needs more evidence. Solenoid commands, pressure tests, speed-sensor data, ratio-error information, and the exact SI chart are the evidence that separates a hydraulic, mechanical, or control cause.

### First and second gear

- 1st provides the greatest forward torque multiplication, approximately 4.696:1.
- C5 holds the output sun gear in 1st. The OWC holds, and C4 has the special low-pressure application noted in the chart.
- 2nd remains a reduction ratio at approximately 2.985:1. The visible text shows input-carrier pinions driving the direct-overdrive sun-gear shaft and the input internal gear.
- The 1–2 shift changes the reaction path by applying C3 and releasing C5 while the OWC continues to hold.

### Third through sixth gear

- These ranges remain in reduction, but torque multiplication decreases each time vehicle speed rises.
- 3rd applies C5 again and releases C2; the OWC begins overrunning.
- 4th exchanges C5 for C6.
- 5th exchanges C4 for C5.
- 6th exchanges C3 for C4.
- The repeated one-element exchange is the pattern to recognize. Each change redirects which member is driven or held while maintaining a continuous path through the compound gearset.

### Seventh through tenth gear

- 7th is direct drive at 1.000:1.
- 8th, 9th, and 10th are overdrive ratios of approximately 0.854:1, 0.689:1, and 0.636:1.
- The 8th-, 9th-, and 10th-gear slides state that the OWC is not used to drive the vehicle. With no element available to overrun for free coasting, engine compression slows the vehicle when the throttle is released until the transmission downshifts to the next lower gear.
- Overdrive lowers engine speed at a given road speed. It does not mean torque multiplication is increasing.

## General planetary-gear rules

The final screenshot gives these broad relationships:

| Result | Condition shown in the chart |
|---|---|
| Neutral | No driving member or reaction member |
| Forward direct drive, 1:1 | Two members are driven |
| Forward reduction | Carrier is the output |
| Forward overdrive | Carrier is the input |
| Reverse, reduction or overdrive | Carrier is the reaction member |
| Forward or reverse overdrive | Sun gear is the output |
| Forward or reverse reduction | Sun gear is the input |
| Reverse rotation | One external gear drives another external gear |
| Same-direction rotation | An external gear drives an internal gear, or vice versa |

Treat these as recognition rules, then identify the actual **input, reaction, and output** members in the diagram before choosing the result.

[Open the planetary-gear fundamentals chart](images/Screenshot_20260922_144553.png)

## Fast recall

- **P:** output mechanically locked by the park pawl.
- **N:** no completed output-torque path.
- **R:** 4.866:1 reduction with reversed output.
- **1–6:** reduction.
- **7:** direct, 1.000:1.
- **8–10:** overdrive.
- **OWC:** holds in 1–2, overruns in 3–7, not listed in 8–10.
- **Use the exact SI range chart:** calibration and clutch-label details can change.
- **Diagnose patterns across ranges:** shared applied elements narrow the search; command and test data confirm it.

