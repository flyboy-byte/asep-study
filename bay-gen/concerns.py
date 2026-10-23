"""Customer concerns, in the customer's words. No causes: diagnosing is the tech's job.

Each concern is a dict:
  system  one of SYSTEMS (GUI checkboxes)
  say     what the customer says; a list = random wording each time
  w       how common, relative to the others
  onset   optional: miles where it becomes common; weight rises with mileage (wear, age)
  pay     what usually pays when the vehicle is covered:
            "b2b" = bumper-to-bumper only, "pt" = also powertrain coverage, "wear" = never warranty,
            "recall" = always free and dealer-only
  cp      how likely a *customer-pay* owner brings it to a dealer (0 = never, 1 = always).
          Low cp + "b2b" = the stuff people only bring in while it's free (rattles, radio glitches).
  match   optional filters (all must pass): engine=[substrings], model=[substrings], types={...}, years="2014-2018"

Concerns with a match filter are weighted toward vehicles with a known GM pattern for that symptom
(e.g. AFM V8 ticking/misfire, 3.6L cold-start rattle, 8-speed shudder). All weights are guesses.
"""

SYSTEMS = ["Engine / driveability", "Transmission / driveline", "Electrical", "Brakes / steering / suspension",
           "HVAC", "Body / interior", "Maintenance / recall"]

V8 = ["5.3L", "6.2L", "4.8L", "6.0L"]
GEN5_V8 = ["L83", "L86", "L84", "L87"]
DI = GEN5_V8 + ["Turbo", "3.6L V6", "2.5L I4"]     # direct-injected (2014+ filter applied where used)
TRUCKISH = {"pickup", "hd", "fullsuv"}

E, T, EL, B, H, BI, M = SYSTEMS

CONCERNS = [
    # ---------------- Engine / driveability ----------------
    dict(system=E, w=14, onset=60_000, pay="b2b", cp=0.5,
         say=["Check engine light came on, drives fine", "Engine light on since last week, nothing feels different",
              "Check engine light is on, wants to know if it's safe to drive"]),
    dict(system=E, w=6, onset=90_000, pay="b2b", cp=0.5,
         say=["Shakes and stumbles when accelerating, engine light flashing", "Misses under load, check engine light blinking"]),
    dict(system=E, w=6, onset=90_000, pay="pt", cp=0.8, match=dict(engine=["5.3L", "6.2L"], types=TRUCKISH),
         say=["Ticking from the engine and the check engine light is flashing", "Truck shakes at idle and there's a tick"]),
    dict(system=E, w=5, onset=70_000, pay="b2b", cp=0.5, say=["Runs rough at idle", "Idles rough, shakes at stop lights"]),
    dict(system=E, w=4, onset=80_000, pay="b2b", cp=0.5, say=["Hesitates when you step on it", "Stumbles taking off from a stop"]),
    dict(system=E, w=4, onset=60_000, pay="b2b", cp=0.5,
         say=["Check engine light came on right after I got gas", "Hard to start right after filling up"]),
    dict(system=E, w=3, onset=80_000, pay="b2b", cp=0.3, say=["Gas mileage dropped off", "Getting worse fuel mileage than it used to"]),
    dict(system=E, w=4, onset=100_000, pay="b2b", cp=0.6, say=["Cranks but won't start", "Turns over, won't fire (towed in)"]),
    dict(system=E, w=2, onset=100_000, pay="b2b", cp=0.7, say=["Died while driving and won't restart", "Stalled on the highway"]),
    dict(system=E, w=2, onset=90_000, pay="b2b", cp=0.6, say=["Stalls when coming to a stop", "Dies at idle sometimes"]),
    dict(system=E, w=3, onset=70_000, pay="b2b", cp=0.7, say=["Reduced engine power message came on", "Went into limp mode, no power"]),
    dict(system=E, w=3, onset=90_000, pay="b2b", cp=0.5, say=["Running hot in traffic", "Temp gauge climbs when sitting at idle"]),
    dict(system=E, w=3, onset=60_000, pay="b2b", cp=0.5, say=["Heater blows lukewarm, temp gauge barely moves"]),
    dict(system=E, w=4, onset=70_000, pay="b2b", cp=0.5, say=["Low coolant light keeps coming on", "Keeps losing coolant"]),
    dict(system=E, w=4, onset=50_000, pay="b2b", cp=0.6, match=dict(engine=["1.4L Turbo", "1.8L I4", "1.5L Turbo", "3.6L V6"]),
         say=["Low coolant light keeps coming on", "Smells like coolant, sweet smell"]),
    dict(system=E, w=5, onset=90_000, pay="pt", cp=0.7, match=dict(engine=["3.6L V6"], years="2013-2017"),
         say=["Check engine light and a rattle for a second when it first starts"]),
    dict(system=E, w=5, onset=80_000, pay="pt", cp=0.7, match=dict(engine=["2.4L I4"], years="2013-2015"),
         say=["Oil light came on, it was two quarts low", "Using oil, no leaks"]),
    dict(system=E, w=3, onset=90_000, pay="pt", cp=0.7, match=dict(engine=["5.3L"], years="2013"),
         say=["Has to add a quart of oil every 2,000 miles, no leaks"]),
    dict(system=E, w=2, onset=120_000, pay="pt", cp=0.5, say=["Burning oil between changes", "Blue smoke on startup"]),
    dict(system=E, w=6, onset=40_000, pay="b2b", cp=0.6, match=dict(engine=["1.4L Turbo"]),
         say=["Whistling noise at idle and the check engine light is on", "Howling sound from the engine, runs rough"]),
    dict(system=E, w=4, onset=60_000, pay="pt", cp=0.6, match=dict(engine=["Turbo I4", "Turbo I3"]),
         say=["Feels down on power, check engine light", "No power going up hills"]),
    dict(system=E, w=4, onset=100_000, pay="pt", cp=0.4, match=dict(engine=V8, types=TRUCKISH | {"van"}),
         say=["Ticking noise on cold start, goes away when it warms up"]),
    dict(system=E, w=3, onset=80_000, pay="b2b", cp=0.5, match=dict(engine=["L83", "L86"]),
         say=["Oil leak at the back of the engine"]),
    dict(system=E, w=3, onset=100_000, pay="pt", cp=0.35, say=["Oil spots on the driveway", "Leaking oil"]),
    dict(system=E, w=3, pay="b2b", cp=0.2, match=dict(years="2014-2026", engine=DI),
         say=["Engine makes a ticking noise, worried about it"]),            # often normal DI noise
    dict(system=E, w=3, pay="b2b", cp=0.1, match=dict(years="2016-2026", types={"car", "suv", "smallsuv", "pickup"}),
         say=["Engine shuts off at stop lights", "Engine turns off by itself at red lights"]),   # often auto stop/start
    dict(system=E, w=4, onset=90_000, pay="wear", cp=0.15, say=["Rattle from under the vehicle", "Exhaust sounds loud"]),
    dict(system=E, w=1, onset=90_000, pay="b2b", cp=0.6, say=["Smells like exhaust inside the cab"]),
    # ---------------- Transmission / driveline ----------------
    dict(system=T, w=6, onset=30_000, pay="pt", cp=0.9, match=dict(years="2015-2019", types={"pickup", "fullsuv"}, engine=["5.3L", "6.2L"]),
         say=["Feels like driving over rumble strips around 40-50 mph", "Shudders at light throttle on the highway"]),
    dict(system=T, w=3, onset=30_000, pay="pt", cp=0.9, match=dict(years="2017-2019", model=["Colorado", "Canyon"], engine=["3.6L"]),
         say=["Feels like driving over rumble strips around 40-50 mph"]),
    dict(system=T, w=5, onset=30_000, pay="b2b", cp=0.9, match=dict(model=["Malibu", "Traverse", "Blazer", "Acadia", "Enclave"], years="2016-2023"),
         say=["Says 'Shift to Park' and won't shut off"]),
    dict(system=T, w=3, onset=100_000, pay="pt", cp=0.8, match=dict(years="2013-2016", engine=["3.6L V6"], model=["Traverse", "Acadia", "Enclave"]),
         say=["No reverse", "Won't go into reverse, drives forward fine"]),
    dict(system=T, w=1, onset=120_000, pay="pt", cp=0.7, say=["No reverse"]),
    dict(system=T, w=4, onset=60_000, pay="pt", cp=0.7, say=["Shifts hard, especially when it's cold", "Bangs into gear"]),
    dict(system=T, w=3, onset=100_000, pay="pt", cp=0.7, say=["Slips, engine revs up between gears", "Flares on the 2-3 shift"]),
    dict(system=T, w=2, onset=100_000, pay="pt", cp=0.7, say=["Takes a few seconds to go into drive in the morning"]),
    dict(system=T, w=2, onset=80_000, pay="pt", cp=0.5, say=["Leaking red fluid under the front"]),
    dict(system=T, w=3, onset=100_000, pay="pt", cp=0.4, match=dict(types=TRUCKISH | {"van"}), say=["Clunk when shifting into drive"]),
    dict(system=T, w=4, onset=30_000, pay="b2b", cp=0.4, say=["Vibration at highway speed", "Shakes at 65-70 mph"]),
    dict(system=T, w=3, onset=70_000, pay="pt", cp=0.6, match=dict(types=TRUCKISH),
         say=["Service 4WD light, won't go into four-wheel drive"]),
    dict(system=T, w=1, onset=100_000, pay="pt", cp=0.5, match=dict(types=TRUCKISH), say=["Clicking from the front when turning in 4WD"]),
    dict(system=T, w=1, onset=120_000, pay="pt", cp=0.5, match=dict(types=TRUCKISH | {"van"}), say=["Whine from the rear that changes with speed"]),
    # ---------------- Electrical ----------------
    dict(system=EL, w=6, onset=40_000, pay="b2b", cp=0.3, say=["Slow to start in the morning", "Cranks slow when it's cold"]),
    dict(system=EL, w=4, pay="b2b", cp=0.7, say=["Battery goes dead after sitting a couple days", "Dead battery again"]),
    dict(system=EL, w=2, onset=110_000, pay="b2b", cp=0.4, say=["Battery light is on, lights flicker"]),
    dict(system=EL, w=2, onset=120_000, pay="b2b", cp=0.35, say=["Clicks but won't crank"]),
    dict(system=EL, w=3, pay="b2b", cp=0.3, match=dict(years="2016-2026"), say=["Radio screen freezes and reboots", "Touchscreen stops responding"]),
    dict(system=EL, w=2, pay="b2b", cp=0.3, match=dict(years="2014-2026"), say=["Backup camera goes black"]),
    dict(system=EL, w=2, pay="b2b", cp=0.15, match=dict(years="2014-2026"), say=["Phone won't connect", "Bluetooth keeps dropping calls"]),
    dict(system=EL, w=2, pay="b2b", cp=0.25, say=["Remote start doesn't work"]),
    dict(system=EL, w=2, pay="b2b", cp=0.5, match=dict(years="2014-2026"), say=["'No remote detected' message, have to put the fob in the cupholder"]),
    dict(system=EL, w=2, pay="b2b", cp=0.9, say=["A bunch of warning lights came on at once", "Gauges went dead for a second and all the lights came on"]),
    dict(system=EL, w=2, pay="b2b", cp=0.5, say=["Cruise control won't set"]),
    dict(system=EL, w=3, pay="wear", cp=0.15, say=["Headlight is out", "Brake light out"]),
    dict(system=EL, w=1, onset=100_000, pay="b2b", cp=0.8, say=["Airbag light is on"]),
    dict(system=EL, w=2, onset=60_000, pay="b2b", cp=0.6, say=["Service StabiliTrak message", "Traction control light stays on"]),
    dict(system=EL, w=1, pay="b2b", cp=0.7, match=dict(years="2017-2026"), say=["'Front camera unavailable', lane keep doesn't work"]),
    # ---------------- Brakes / steering / suspension ----------------
    dict(system=B, w=7, onset=35_000, pay="wear", cp=0.3, say=["Brakes squeal", "Squeaking when I stop"]),
    dict(system=B, w=5, onset=50_000, pay="wear", cp=0.3, say=["Grinding when braking", "Metal-on-metal noise when stopping"]),
    dict(system=B, w=5, onset=45_000, pay="wear", cp=0.35, say=["Steering wheel shakes when braking on the highway"]),
    dict(system=B, w=1, onset=80_000, pay="b2b", cp=0.6, say=["Brake pedal feels low and soft"]),
    dict(system=B, w=4, onset=70_000, pay="b2b", cp=0.5, say=["ABS and traction lights are on"]),
    dict(system=B, w=4, onset=20_000, pay="b2b", cp=0.7, match=dict(types=TRUCKISH, years="2014-2019"),
         say=["Clunk in the steering wheel when turning in a parking lot"]),
    dict(system=B, w=4, onset=80_000, pay="b2b", cp=0.35, say=["Clunk over bumps", "Knocking from the front end on rough roads"]),
    dict(system=B, w=4, onset=70_000, pay="b2b", cp=0.4, say=["Humming noise that gets louder with speed"]),
    dict(system=B, w=3, pay="wear", cp=0.3, say=["Pulls to the right", "Steering wheel is off center"]),
    dict(system=B, w=4, onset=20_000, pay="wear", cp=0.25, say=["Tire pressure light is on"]),
    dict(system=B, w=3, onset=60_000, pay="b2b", cp=0.2, say=["Squeak from the front end over bumps"]),
    dict(system=B, w=1, onset=80_000, pay="b2b", cp=0.7, say=["Steering got heavy, power steering message"]),
    dict(system=B, w=1, onset=60_000, pay="b2b", cp=0.7, match=dict(model=["Escalade", "Yukon"], years="2015-2026"),
         say=["Rear end is sitting low, suspension message on the dash"]),
    # ---------------- HVAC ----------------
    dict(system=H, w=6, onset=50_000, pay="b2b", cp=0.5, say=["A/C blows warm", "A/C isn't cold anymore"]),
    dict(system=H, w=4, onset=40_000, pay="b2b", cp=0.5, match=dict(types=TRUCKISH, years="2014-2018"), say=["A/C blows warm"]),
    dict(system=H, w=2, onset=60_000, pay="b2b", cp=0.4, say=["Blower only works on high"]),
    dict(system=H, w=3, pay="b2b", cp=0.3, say=["Clicking behind the dash when I change the temperature"]),
    dict(system=H, w=1, pay="b2b", cp=0.4, say=["Heat only blows hot on one side"]),
    dict(system=H, w=2, pay="wear", cp=0.3, say=["Musty smell from the vents"]),
    # ---------------- Body / interior ----------------
    dict(system=BI, w=2, pay="b2b", cp=0.6, say=["Water on the passenger floor"]),
    dict(system=BI, w=2, pay="b2b", cp=0.6, match=dict(types={"pickup", "hd"}, years="2014-2018"),
         say=["Water dripping from the headliner by the back window"]),
    dict(system=BI, w=3, onset=60_000, pay="b2b", cp=0.5, say=["Window won't roll up", "Window fell down into the door"]),
    dict(system=BI, w=2, pay="b2b", cp=0.15, say=["Wind noise from the driver door on the highway"]),
    dict(system=BI, w=3, pay="b2b", cp=0.1, say=["Rattle in the dash", "Squeak from the back seat area"]),
    dict(system=BI, w=1, pay="b2b", cp=0.2, say=["Heated seat doesn't work"]),
    dict(system=BI, w=1, pay="b2b", cp=0.4, match=dict(types={"suv", "fullsuv"}, years="2015-2026"), say=["Power liftgate won't open"]),
    dict(system=BI, w=1, pay="b2b", cp=0.4, say=["Door won't lock with the fob"]),
    # ---------------- Maintenance / recall ----------------
    dict(system=M, w=10, pay="wear", cp=0.45, say=["Oil change", "Oil life is at 0%"]),
    dict(system=M, w=3, onset=45_000, pay="wear", cp=0.4, say=["Due for scheduled maintenance", "Whatever the next service is"]),
    dict(system=M, w=2, pay="wear", cp=0.3, say=["Wants it looked over before a long trip"]),
    dict(system=M, w=3, onset=40_000, pay="wear", cp=0.15, say=["Needs tires and an alignment"]),
    dict(system=M, w=3, pay="recall", cp=1.0, say=["Got a recall letter in the mail", "Open recall, customer waiting"]),
]
