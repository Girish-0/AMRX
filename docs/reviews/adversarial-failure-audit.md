# AMRX: adversarial failure audit of the modular AMR proposal

**Project:** SIH26112, Autodesk Fusion hardware challenge  
**Purpose:** Internal engineering criticism before the revised college submission  
**Review date:** 11 September 2026  
**Baseline:** Final seven-slide PPT plus the consolidated 1,614-line technical roadmap  
**Status:** Concept review. No CAD model, solver project, supplier quotation, inspection record, or physical test data was supplied for this audit.

> **Principal finding:** The hybrid chassis and interchangeable conveyor are plausible concepts. The current documents do not establish a buildable, validated design freeze. They combine incompatible configurations, incorrect load calculations, unsupported performance results, and a more elaborate development programme than the official brief requires. Fabricating directly from this roadmap would expose the team to avoidable redesign, misleading simulation results, and a mechanism that may dock on a clean table but fail under load.

This document deliberately concentrates on failure. It is not a replacement design, presentation, compliance certificate, or patent opinion. “Not demonstrated” does not mean “impossible.” Conversely, a claim labelled “verified” in the roadmap is not accepted as verified without the underlying evidence. No document review can enumerate every possible failure; this audit covers the material failure mechanisms visible from the supplied design and identifies the missing evidence needed to discover others.

## 1. Read this first: what can invalidate the submission or its central argument

| Priority | Failure | Consequence |
|---|---|---|
| 1 | Official submission rules prohibit AI-generated content; they require an original Fusion design and its public link. | Attractive generated images and prose cannot substitute for the team’s qualifying work. |
| 2 | The 250 kg aluminium-member PPT is supported by a roadmap largely calculated around 100 kg and carbon-fibre members. | There is no consistent engineering baseline behind the headline capacity. |
| 3 | Whole-payload forces and moments are repeatedly multiplied by four. | Optimisation receives incorrect loads; claimed margins are not trustworthy. |
| 4 | Four rigid support pads are described as an exact-constraint interface without resolving the redundant vertical support. | Rocking, jamming, preload imbalance, plate distortion, and inconsistent location remain possible. |
| 5 | Quick release is specified; safe removal and replacement of a heavy conveyor are not. | A fast latch can produce little or no reduction in real changeover time. |
| 6 | The market argument assumes existing robots cannot perform multiple jobs. | The central commercial comparison is contradicted by existing modular product offerings. |
| 7 | No reproducible Fusion studies or mass records support the claimed performance improvements. | The submission may look decorative rather than engineered under the actual rubric. |
| 8 | Traction, vehicle tipping, and cargo retention are less developed than chassis stress. | The frame can remain intact while the robot slides, tips, or drops the tote. |
| 9 | The “primary validation” report contains demonstrably mismatched source references. | Repeating its confidence labels creates false assurance rather than evidence. |
| 10 | Precision couplings, metal printing, machining, suspension, sensor isolation and automation are all treated as simultaneous essentials. | Integration effort can consume the time needed for the scored Fusion and DfAM work. |

### Evidence and severity notation

- **D — Documented defect:** A contradiction, arithmetic error, or omission directly identifiable in the supplied material.
- **P — Physical risk:** A credible mechanism derived from engineering principles; actual occurrence depends on the eventual geometry and operating conditions.
- **U — Unverified claim:** A statement whose supporting evidence was not supplied or does not substantiate it.
- **B0 — Submission blocker:** Can invalidate eligibility or leave a mandatory deliverable unfulfilled.
- **B1 — Build or safety blocker:** Must be resolved before committing to the affected fabrication or powered test.
- **B2 — Performance/value blocker:** Can make the mechanism unreliable, uneconomic, or irrelevant to its intended advantage.
- **B3 — Credibility defect:** Can undermine the jury’s confidence, even when the underlying concept remains viable.

These are priorities, not numerical failure probabilities. Assigning occurrence scores or a formal FMEA risk-priority number without test and duty-cycle data would invent precision.

## 2. What the official brief actually requires

Source **S1, pages 1–2**, visually inspected because the supplied PDF has no usable text layer.

| Official requirement | Failure exposure in the present proposal |
|---|---|
| Concept design of a universal AMR/AGV chassis supporting multiple interchangeable attachments | A single conveyor bolted or latched to one base does not by itself demonstrate interchangeability. |
| Concept design of any one functional attachment | An entire industrial fleet, three functioning attachments, and a complete navigation product are not stated requirements in this supplied brief. |
| Structural integrity, payload, weight reduction, modularity, manufacturability and maintenance | These must be mutually compatible, rather than separate promises. |
| Use Fusion features such as generative design, topology optimisation, additive build and simulation | Organic-looking render geometry alone does not evidence any of these workflows. |
| Original designs created only using Autodesk Fusion | Imported or generated design geometry can create a direct originality and tool-compliance issue. |
| Public Fusion link and a 5–7-slide PPT for idea submission | Seven slides satisfy the length range; a valid link exposing Part A and Part B remains a separate requirement. |
| AI-generated content is not allowed | This critique is internal AI-assisted analysis. Do not submit it, copy its wording into the deck, or present generated visuals as the team’s qualifying output. The precise permitted boundary for private research assistance needs clarification from the college/SPOC. |
| Faculty/SIH SPOC mandatory form | Shortlisting alone does not establish that this separate requirement was completed. |
| Finale: design in Fusion and print specified components, scaled to machine size, within the allotted period | The roadmap’s insistence on full-size metal production and a fully operational industrial robot is not established by this brief. Finale details are explicitly deferred. |

### Actual scoring

| Criterion | Marks |
|---|---:|
| Design complexity and workability | 20 |
| Design optimisation for 3D printing / DfAM | 20 |
| Innovative design features | 15 |
| Advanced Fusion features | 30 |
| AM process and material selection | 15 |
| **Total** | **100** |

**Failure of interpretation:** The earlier “85% mechanical” shorthand is not an explicit rubric category. The complete rubric concerns design, workability, innovation and manufacturing. There are no separately listed marks for Jetson TOPS, a large battery, proprietary cryptographic module IDs, or a broad revenue forecast. There is also no 250 kg minimum, sub-three-minute swap requirement, or mandated 36-hour duration in these two pages. Those are project choices or unverified event assumptions.

### F01 — AI-content and original-design exposure — B0 / D

**Anchor:** S1 p.2; PPT slides 2–3 and any external/generated robot visuals used in the deck.

The rule is explicit. If the presentation relies on AI-generated product images or copied design geometry, the team may fail the submission requirements regardless of engineering quality. A later recreation does not automatically settle the originality question. The supplied PPT’s asset provenance has not been established in this audit.

**Closure evidence:** Team-authored Fusion history, original renders from that model, and an explicit SPOC clarification of any ambiguous research-assistance boundary. This audit supplies criticism, not permission to override the rule.

### F02 — Missing verifiable Fusion deliverable — B0 / U

**Anchor:** S1 p.2; PPT references slide.

A roadmap, image, or CAD assembly name is not the required accessible Fusion design. The extracted slide text does not show a qualifying Fusion design URL; embedded links or separately submitted links have not been verified. An inaccessible link, absent Part B, or a cosmetic assembly can defeat the submission.

**Closure evidence:** Open the exact submitted link from an unauthenticated browser and inspect both assemblies. Confirm the faculty form separately.

### F03 — Solving a self-invented problem instead of the scored one — B2 / D

**Anchor:** Roadmap Parts 1 and 3, problem formulation and final development target.

The roadmap elevates LiDAR floor strikes, cross-vendor standardisation and three physical attachments into central requirements. The official brief does not. If these consume the development effort while the team cannot demonstrate original Fusion optimisation, printability and workability, the result can fail the challenge despite impressive robotics terminology.

**Closure evidence:** Every major work package must map to an official requirement or a clearly justified design choice. Unsupported claims of mandatory features should disappear.

## 3. Configuration failures: different sections describe different machines

| Variable | Conflicting definitions | Why the conflict matters |
|---|---|---|
| Top load | PPT: 250 kg total top load; roadmap: 100 kg combined load; other passages: 100 kg cargo; universal envelope: 1,000 kg pallet | Changes strength, traction, stability, wheels and braking. |
| Long members | PPT: 6061-T6; roadmap predominantly pultruded carbon fibre | Changes mass, stiffness, joint details and material model. |
| Coupling grid | Earlier 600 × 450 mm; later 400 × 500 mm | Changes force couples and packaging. |
| Conveyor | Four prototype rollers; eight industrial rollers; twelve MDR rollers in Part 3 | Changes length, mass, cost, power and assembly. |
| Taper | 15° included; 30° included with 15° lead-in; wedge angles also mixed into these values | Locating, release and self-locking cannot be calculated consistently. |
| Collar engagement | 60 mm versus 80 mm | Changes slip, bearing and node envelope. |
| Battery | 48 V 30 Ah versus PPT 48 V 60 Ah | Larger pack may invalidate the service corridor and mass properties. |
| Battery opening | 500 × 400 × 160 mm volume versus 450 × 120 mm opening | Extraction route and pack orientation are unresolved. |
| Sensor mounting | Direct to nodes versus a separate flexure-mounted bridge | Different loads, modes and calibration behaviour. |
| Sensor angle target | 0.3°, 0.15°, 0.12°; claimed twist 0.195° | No unique requirement or measurement definition. |
| Lock actuator | Gearmotor/dual shaft, worm drive, stepper lead screw, servo or manual lever | Different geometry, failure states and torque sizing. |
| Utility/ID | GPIO, CANopen, EtherCAT; resistor ID or cryptographic EEPROM | Different interfaces, cost and implementation scope. |

### F04 — No authoritative configuration — B1 / D

**Anchor:** S2 slides 3 and 6; S3 Parts 1–3, particularly Part 2 Tasks 18–20.

Separate teammates can faithfully follow different sections and produce incompatible parts. “Design freeze” currently freezes a family of contradictory descriptions. The final PPT is the latest declared concept, but it is not a complete engineering specification.

**Closure evidence:** One revision-controlled parameter table, coordinate convention and assembly bill defining precisely which older values are superseded.

### F05 — The 250 kg upgrade has not been propagated — B1 / D

**Anchor:** PPT slide 6 versus roadmap load cases.

Changing a capacity label and motor price is not an engineering upgrade. With unchanged geometry and acceleration, forces associated with 250 kg are 2.5 times those for 100 kg. Attachment tare must remain inside the PPT’s total top-load allowance: a 50 kg attachment would leave 200 kg for cargo, before any other top-mounted items. It is not 250 kg cargo plus the attachment.

**Closure evidence:** Recomputed mass ledger, load cases, joint loads, wheel reactions, drivetrain and stability limits for the same frozen configuration.

### F06 — Carbon-to-aluminium substitution invalidates inherited results — B1 / D

The roadmap’s 18.5 kg mass and torsional stiffness are not transferable to the aluminium PPT by renaming the material. Composite axial modulus is not a substitute for its shear/transverse properties. Aluminium section sizing, clamp behaviour and thermal expansion must be reconsidered. Conversely, aluminium must not be rejected merely because one unvalidated comparison called extrusions insufficiently rigid.

**Closure evidence:** CAD mass properties and assembly stiffness for the actual member cross-sections and connections.

## 4. Calculation audit: errors that precede fabrication

These are independent arithmetic and equilibrium checks using the roadmap’s stated assumptions. They are **not** certified design loads or permission to test at these levels.

### F07 — Whole-system load multiplied by four — B1 / D

**Anchor:** S3 Part 1 Task 10 and Part 2 Task 14.

| Roadmap operation | Correct interpretation under its stated inputs |
|---|---|
| 100 kg × 2.5 m/s² = 250 N “per corner”, total 1,000 N | **250 N total.** Equal sharing would be 62.5 N per corner, but actual locator shear sharing may be unequal. |
| 100 kg × 1.5 m/s² = 150 N “per pocket”, total 600 N | **150 N total.** Do not multiply again by the number of interfaces. |
| 100 × 2.5 × 0.15 × 1.5 = 56.25 Nm “per corner”, total 225 Nm | **56.25 Nm total** for that assumed lever arm and factor. Resolve it into reactions once. |
| 100 × 1.5 × 0.65 × 1.3 = 127.5 Nm “per corner”, total 510 Nm | **127.5 Nm total** if 0.65 m is the lever arm from the relevant reference plane. |

Overstating a load does not make the analysis valid: artificial load combinations can grow unnecessary material in the wrong places, obscure real governing modes, and inflate cost. Correct equilibrium is required even for conservative sizing.

### F08 — Static weight and load transfer are conflated — B1 / D

100 kg weighs approximately **981 N**, not 4,000–4,500 N. Dynamic pitching redistributes vertical reactions; it does not independently quadruple total weight. A higher vertical force needs a specified vertical acceleration, additional mass, preload, or impact event. Internal clamp preload must not be counted as additional external vehicle weight.

**Closure evidence:** Separate external weight, inertial loads, internal preload and contact reactions. Confirm the sum of reactions and moments against each free-body diagram.

### F09 — CG reference plane changes between paragraphs — B1 / D

**Anchor:** S3 Part 2 Task 11 and Part 3 specifications.

The 0.65 m CG is described both above the floor and above the interface; elsewhere 0.50 m is subtracted. Those interpretations give very different pitch moments. For the PPT’s 250 kg top load and assumed 2.5 m/s² deceleration, total horizontal inertia is **625 N**. It generates **93.75 Nm** about an interface 0.15 m below the CG, or **406.25 Nm** about an interface 0.65 m below it. Neither value includes a dynamic multiplier.

**Closure evidence:** Put the coordinate origin and every CG on one drawing. Distinguish the attachment-interface free body from the whole-vehicle tipping free body.

### F10 — Moment loads can be counted twice — B1 / P

Applying a remote CG force to an interface already transmits its moment. Adding that same moment independently, or imposing both the moment and its complete force-couple equivalent, duplicates it. The roadmap moves between these descriptions without a clear load-application convention.

**Closure evidence:** Each physical action appears exactly once in the solver; reaction-force checks confirm both net force and net moment.

### F11 — Six separate maxima are not a universal capacity certificate — B1 / D/P

**Anchor:** S3 Part 2 Task 12 and ICD.

A component can survive maximum shear alone and maximum overturning alone but fail their combination. The 1,000 kg-derived envelope also does not prove that a 250 kg vehicle can carry a one-tonne pallet. Interface strength, frame strength, stability, traction and actuator ratings are distinct limits.

**Closure evidence:** Physically achievable load combinations, a load reference frame, duration/duty definitions, and separate vehicle-level limits. “Any module within six scalar limits is safe” is not established.

### F12 — Claimed stiffness does not establish the sensor-angle claim — B3 / D

**Anchor:** S3 Part 2 Task 22.

1,200 Nm / 0.0034 rad ≈ **352,941 Nm/rad**, so that arithmetic is reasonable. But **0.0034 rad ≈ 0.195°**, above the claimed 0.12° sensor limit. Chassis twist and scanner pitch need not be equal; proving decoupling requires the missing transfer model. The roadmap supplies neither the FEA dataset nor that relationship. Its claimed 327% increase over 82,000 Nm/rad is also approximately **330%** using those numbers; the missing simulation evidence is far more important than the rounding discrepancy.

### F13 — The LiDAR root-cause claim is not established — B2 / D/U

**Anchor:** S3 Part 1 Task 1; S4 LiDAR correction discussion.

For a point ray over a flat floor, intersection distance is **d = h / tan(θ)**. At h = 0.15 m and θ = 0.5°, d ≈ **17.2 m**, not within 5.5 m. Intersection at 5.5 m would require approximately **1.56°** of downward angle. Beam spread, floor irregularity and mounting errors can change this, but must be specified from the selected scanner and site. A warning-field event must also not automatically be equated with a protective stop or emergency stop.

**Closure evidence:** Scanner-specific optical data, configured field distances, floor profile and measured orientation. The SICK manual could not be retrieved during this audit, so no scanner-specific divergence or safety threshold is certified here. The claim that floor striking is the dominant industry problem remains unproven.

### F14 — Conveyor power contradicts the stated acceleration — B1 / D/P

**Anchor:** S3 Part 2 Task 11: one 45 W MDR, 50 kg tote, 1.2 m/s in 0.15 s.

That acceleration is 8 m/s² and requires 400 N ignoring losses. Kinetic energy is **36 J**; achieving it in 0.15 s requires **240 W average mechanical power**, reaching **480 W instantaneous mechanical power** at the end of a constant-acceleration ramp. A 45 W continuous rating alone cannot substantiate this manoeuvre. Decelerating against a hard stop creates a different impact problem and does not rescue the acceleration claim.

**Closure evidence:** Selected drive’s torque-speed and transient limits, gearing, belt traction, tote-bottom friction and a slower justified motion profile if necessary.

## 5. Mechanical interface failure mechanisms

### F15 — Four hard Z supports are not automatically exact constraint — B1 / D/P

**Anchor:** S3 Part 1 Tasks 7–8, Part 2 Task 18, Part 3 Q1.

A round and diamond locator can avoid redundant in-plane location. They do not remove the redundant fourth vertical support. Three non-collinear support points define a plane; a fourth rigid pad can create rocking or assembly strain when flatness differs. Four clamped stations are entirely possible, but require an explicit tolerance/compliance/load-sharing treatment. MIT’s constraint-design material distinguishes exact and quasi-kinematic constraint; this audit’s application to the proposed pads is an engineering deduction. [E3]

**Closure evidence:** Identify the three primary plane-defining supports and treatment of the fourth, or model and test a deliberately compliant/elastic-averaging four-support arrangement. Do not claim all overconstraint has been eliminated.

### F16 — Taper and flat shoulder can fight each other — B1 / P

If the taper seats before the shoulder, the flat pad may remain unloaded. If the shoulder seats first, the taper may not locate tightly. Angle error and axial stack-up can concentrate contact at an edge. A lead-in chamfer, locating taper and retaining wedge are different features, despite being conflated in the roadmap.

**Closure evidence:** A sectioned drawing with contact sequence, controlled stand-off, tolerances, intended compliance and release clearance.

### F17 — Four 5 kN clamps do not necessarily apply equal preload — B1 / P

One shaft or actuator can reach its stop while another corner remains partly seated. Shaft twist, linkage tolerances, debris and plate deflection change individual clamp loads. A motor-current threshold or one “locked” switch cannot establish all four local states.

**Closure evidence:** Per-station seating/retention assessment and a means of equalising or tolerating preload variation. Measure each station in a restrained fixture before automating it.

### F18 — Self-locking reasoning mixes geometry and friction — B1 / D

**Anchor:** S3 Part 3 Q7 and technical risk 3.

The roadmap alternately describes 15° as below and above a 7° friction limit, while also changing included angle and wedge angle. For a simple friction wedge, a condition such as tan(α) < μ depends on its actual force geometry and friction; it is not a universal 7° rule. An over-centre linkage is a separate positive-retention mechanism whose travel, stop and reverse-loading behaviour must be defined.

**Closure evidence:** One mechanism drawing with angles, spring direction, hard stops, force balance, tolerances and behaviour under reverse load and power loss.

### F19 — Locked-on-power-loss is not the only failure state — B1 / P

Power can fail during partial insertion or release. A stud may be caught but not seated; a spring can break; a jammed shaft can leave two corners locked. “Normally closed” does not establish safe operation from every intermediate state.

**Closure evidence:** State transitions for absent, partly seated, fully seated, retained, releasing and faulted. Motion must depend on established attachment state, not just the release command being inactive.

### F20 — Pull studs, groove roots and cartridge retention can fail first — B1 / P

The stud’s reduced groove section sees stress concentration, bending and repeated loads. A broad aluminium seat does not protect a small retention screw from pull-out or prying. The cartridge’s upward retention path is not established merely by specifying four countersunk M5 screws.

**Closure evidence:** Trace upward and downward loads separately through shoulders, stud root, wedge, cartridge flange and node. Check net sections, threads, edge distances and fatigue at the actual geometry.

### F21 — Hard wear inserts reduce wear; they do not eliminate it — B2 / U/P

**Anchor:** S3 materials tables and repeated “zero wear” claims.

Hardness cannot guarantee freedom from fretting, edge chipping, corrosion, debris indentation or datum drift. A2 at a selected hardness needs a toughness and finish rationale. Replacing a cartridge can itself move the datum if its locating seat is not repeatable.

**Closure evidence:** Defined allowable wear and repeatability, contamination conditions, lubrication/cleaning policy, replacement datum procedure and cycle tests under representative loading.

### F22 — Dust and approach error can defeat precision docking — B2 / P

The ±1.5 mm capture value addresses only part of docking error. Pitch, roll and yaw can make the first stud bind before the others enter. A small chip on a support pad can produce a large angular error even with perfect pin-centre tolerances. A 50 μm repeatability claim must include measurement setup and cleanliness.

**Closure evidence:** A translational and angular capture envelope, controlled dirty-interface trials, contact inspection and repeatability measurements at the actual functional datum.

### F23 — Heavy attachment exchange is mechanically incomplete — B2 / D/P

**Anchor:** S3 excludes autonomous exchange stations but promises rapid swaps; attachment tare is stated as 50 kg in one configuration.

The locks cannot lift or support the conveyor after release. Manual handling, a hoist, lift table, trolley, parking cradle or another transfer method remains necessary. If the operator needs a forklift and realignment, the latch stroke contributes little to end-to-end changeover savings.

**Closure evidence:** An unloaded-module exchange sequence with support at every step, access for the handling device and timing from “stop old task” to “ready for new task.” A powered change station is not mandatory, but a credible handling method is.

## 6. Chassis, ground contact and stability

### F24 — An open rectangle can rack even with strong corner nodes — B1 / P

**Anchor:** S3 chassis freeze; PPT slide 4.

Strong nodes do not automatically make the whole frame torsionally stiff. Long members and semi-rigid clamps can dominate compliance. A visually triangulated node may not triangulate the chassis. Closing the load path using the removable module can make base stiffness depend on which module is fitted.

**Closure evidence:** Compare bare-base and module-fitted stiffness, including joint compliance. Show structural bracing around the service volume in the complete assembly.

### F25 — Local node optimisation can miss the real drive-wheel load path — B1 / P

Four corner hubs cannot directly contain both corner caster mounts and centrally located drive pivots unless the actual intervening structure is modelled. Loads may travel through tube bending and additional brackets absent from a simplified node-only study.

**Closure evidence:** Full assembly free-body diagram and boundary conditions transferred from global analysis into local node studies, with stiffness compatibility checked.

### F26 — Split collars can slip, crush members or lose preload — B1 / P

Short collar engagement, thin tube walls, bolt scatter and vibration can cause axial movement or rotation. Pin holes introduce stress concentrations. Carbon-specific clamp assumptions must not be retained uncritically for the aluminium version, and nylon prototype collars can relax over time.

**Closure evidence:** A joint specimen tested for axial pull-out, torsion and cyclic relaxation at restrained low-risk loads before it becomes a structural dependency.

### F27 — A heavy robot can have inadequate drive-wheel traction — B1 / P

The load carried by passive casters does not contribute directly to drive-wheel traction. With total mass M, driven normal load Nd and friction μ, available driven traction is approximately μNd. The necessary condition for acceleration a on a level surface is μNd ≥ Ma before additional resistance. At μ = 0.6 and a = 2.5 m/s², the driven wheels would need at least **42.5% of total weight** in this idealised case. Motor wattage cannot compensate for wheel unloading.

**Closure evidence:** Wheel-load measurements or a validated suspension model for empty, loaded, offset-CG, braking and uneven-floor states. The numerical example is not a guaranteed friction coefficient.

### F28 — Six contact points do not guarantee stable support — B1 / P

Two drive wheels plus four casters create load sharing that depends on tyre compliance, suspension preload and floor flatness. A rigid simplification may lift a drive wheel or overload one caster. The stated ±5 mm suspension travel and a 10 mm ditch case are not reconciled. Caster swivel envelopes can also collide with the frame.

**Closure evidence:** Contact-state model, actual wheel/spring specifications, travel stops, clearances and low-speed uneven-floor trials.

### F29 — Vehicle tipping is not checked by clamp separation margin — B1 / D/P

An interface may remain clamped while the complete robot tips about a ground-contact edge. Use the combined CG of base, battery, module and cargo, and the active wheel support polygon. The 400 × 500 mm interface rectangle is not the ground support polygon.

For a simplified rigid vehicle on a level floor, lateral tipping onset under quasi-static acceleration is approximately **a = g b / h**, where b is the horizontal CG distance to the tipping edge and h the combined CG height. Suspension, slope, impacts and moving cargo require further treatment.

**Closure evidence:** Stability margins for braking, cornering, off-centre cargo and transfer. No numerical tipping rating can be established from the supplied data.

### F30 — Removing the battery changes stability and support — B1 / P

A low battery may act as stabilising mass. Sliding it sideways shifts CG; removing it changes wheel loading, potentially while a heavy module remains installed. An “unobstructed” battery cavity says nothing about drawer retention, stops, supported extraction or electrical isolation.

**Closure evidence:** Service-state CG analysis, drawer support and retention, and a specified unloaded/loaded service policy.

### F31 — Motor power does not prove torque, braking or thermal capability — B1 / U

**Anchor:** PPT slide 6: two 750 W drives and 1.8 m/s.

Selection requires wheel radius, ratio, efficiency, torque-speed curve, continuous and peak current, caster scrub, slope and duty cycle. The drive’s brake may have different holding and dynamic ratings. Energy regenerated into a full battery can also require a managed dissipation path.

**Closure evidence:** Operating points on actual drive curves, controller/BMS limits and a braking-energy assessment. Do not infer a safe stopping distance from nameplate power.

### F32 — A sensor bridge adds its own modes and error sources — B2 / P

Flexures can isolate selected strains while introducing compliance in other directions. “Non-deflecting wheel uprights” are an idealisation; wheel mounts move under tyre and suspension compliance. Multiple moving anchors can distort the bridge or change its orientation. Isolation does not establish a fixed scan plane.

**Closure evidence:** Degrees-of-freedom map, modal and orientation response of the actual bridge, and a comparison showing that it is needed over simpler rigid mounting.

## 7. Conveyor and warehouse-task failures

### F33 — Roller count and envelope are incompatible across revisions — B1 / D

**Anchor:** S3 Part 2 Task 11 versus Part 3 Part B.

At 75 mm pitch, twelve roller centres span **825 mm**, before end radius and end structure. That does not fit inside an 800 mm direction without overhang or a changed layout. Eight centres span **525 mm**; twelve powered rollers are also a fundamentally different system from one powered plus seven slave rollers.

**Closure evidence:** One roller count, pitch, axis direction, usable width, overall module envelope and corresponding mass/power model.

### F34 — The roller orientation may transfer in the wrong direction — B2 / P

Cargo motion is perpendicular to roller axes. Calling a conveyor “transverse” is insufficient if the CAD render places the roller axes the wrong way. Transfer faces, side rails and powered belt routing must match the warehouse dock.

**Closure evidence:** Annotated top view showing AMR travel, roller axes, cargo motion, entry/exit sides and dock location.

### F35 — The tote can roll or slide off during travel — B1 / P

Turning off an MDR does not necessarily restrain the tote. Roller inertia, backdriving, low friction and base acceleration can cause unintended cargo movement. Fixed end stops can obstruct transfer; movable stops require safe sequencing.

**Closure evidence:** A cargo-retention mechanism and failure-state sequence covering travel, transfer, loss of power and incomplete loading. No loaded mobile test should rely on unverified roller friction alone.

### F36 — Robot-to-station error can dominate coupling precision — B2 / P

A repeatable top-to-base coupling does not correct AMR position error, floor variation, roller elevation change under suspension deflection or the physical gap to the stationary conveyor. Totes can snag or tip at the transition even when the module’s locating pins repeat perfectly.

**Closure evidence:** A complete alignment-error budget and an actual or representative transfer station. Define acceptable gap, height mismatch, yaw and tote-bottom geometry.

### F37 — Load sharing among rollers is not uniform — B1 / P

Flexible tote bottoms, ribs and overhanging loads can concentrate force on fewer rollers than assumed. Roller bending, bearing loads and side-frame deformation can then govern. “250 kg top load” does not certify individual rollers, shafts, bearings or tote geometry.

**Closure evidence:** Worst supported tote footprint and entry/exit cases, selected roller ratings and frame-deflection checks. Treat side-stop impact separately.

### F38 — Part B may contribute little additive-design evidence — B2 / D/P

**Anchor:** PPT slide 2; roadmap’s largely conventional conveyor frame.

A catalogue conveyor on a generic plate can appear weak as the mandatory attachment concept, especially if virtually all design optimisation occurs in Part A. A generative base does not automatically demonstrate that Part B has been re-imagined for the stated task.

**Closure evidence:** An original functional Part B design decision supported by Fusion work and manufacturability reasoning, rather than decorative printed covers.

## 8. Manufacturing and prototype failures

### F39 — “Support-free LPBF” is not established by a 45° setting — B2 / U

**Anchor:** PPT slide 5; roadmap DfAM sections.

Geometric overhang limits do not establish heat removal, residual-stress control, recoater clearance, build-plate attachment or support accessibility. Autodesk provides manufacturing constraints, but selecting them does not certify production printability. [E2]

**Closure evidence:** A supplier-reviewed orientation and support plan for the actual node, including removal access and machining fixtures.

### F40 — Supplier-specific properties have become universal constants — B1 / U

The roadmap assigns one heat treatment, yield strength, ductility and fatigue value to AlSi10Mg. Actual allowable properties must match machine, process, orientation, heat treatment, surface and quality control. EOS itself provides material/process-specific information and identifies heat treatment as modifying properties. [E4]

**Closure evidence:** The selected supplier’s process datasheet and inspection assumptions. Do not borrow a convenient yield value from a different material condition.

### F41 — Static FoS does not establish infinite fatigue life — B1 / D/U

**Anchor:** S3 Tasks 11/21 and Part 3 Q6/Q12.

Local average compression below a stated fatigue number cannot prove infinite life of the full node. Stress range, mean stress, notches, pores, roughness and cycle count matter. Ten million cycles is a finite endurance statement, not infinity. A static FoS of two does not establish a fatigue factor of safety.

**Closure evidence:** A defined duty spectrum and finite-life assessment at the governing features, with process-appropriate data. Withdraw “permanent survival” and “zero fatigue failure.”

### F42 — Post-machining may dominate node cost and lead time — B2 / P

Precision cups, flatness and H7 bores require datum establishment, workholding and tool access after printing and heat treatment. Organic geometry can be difficult to clamp without distortion. An ambiguous “oversize 1.2 mm” instruction can even remove rather than leave machining stock on an internal bore.

**Closure evidence:** Machining drawing, stock convention, accessible datum surfaces, process sequence and a quotation including finishing and inspection.

### F43 — Thin members, sockets and inserts create local failure modes — B1 / P

Global node stress may look acceptable while a tube buckles, a collar lug splits, an insert pulls out, or a countersink leaves insufficient ligament. A single minimum wall setting does not ensure adequate material around holes, powder drains and contact shoulders.

**Closure evidence:** Local sections and load paths checked at final tolerances, including manufacturing stock and support-removal damage allowances.

### F44 — Polymer prototype similarity is being overinterpreted — B1 / D/P

FDM proves fit and motion only within its tested load range. Layer strength, creep and brass inserts do not reproduce LPBF metal behaviour. Continuous-fibre capability must not be assumed from a chopped-fibre filament or an ordinary desktop printer. Applying the industrial 5 kN clamp preload to a small printed mock-up can break it before useful testing.

**Closure evidence:** A separately rated prototype, printer/material-specific settings and restricted demonstrator loads. State explicitly which observations transfer to the full-scale concept and which do not.

### F45 — Scaling is not mechanically neutral — B1 / P

Under geometric scale s, area scales as s² and volume as s³. A geometrically scaled mass under gravity therefore does not preserve stress automatically. Standard screws, springs, layer heights and contact surfaces also do not scale continuously. A small model’s easy docking is not evidence for a 250 kg assembly’s handling.

**Closure evidence:** Separate full-scale analysis from scaled workability demonstration; do not invent a full-scale capacity conversion from model size alone.

### F46 — Printing and procurement can exceed the available window — B2 / U/P

**Anchor:** S3 100% infill and high-resolution printing prescriptions.

Four solid nodes, several retries, drying, supports and assembly can exceed one printer’s time budget. Heat treatment, precision machining, tool steel hardening and bought-in drives involve external lead times. The actual machine envelope and finalist fabrication rules are not established by the roadmap.

**Closure evidence:** Slice the actual demonstrator parts, record estimated time/material, reserve machine access and identify supplier availability before freezing the fabrication scope.

**Related software dependency:** PPT slide 4 claims “Zero Software Feasibility Gap.” Free Fusion access does not, by itself, demonstrate that this team's account can execute every proposed cloud study, simulation type and additive workflow on its available computers. Verify login, supported operating environment, required entitlements, a small successful solve, export and sharing before making that claim. This audit did not verify the team's account or establish that access is unavailable.

## 9. Electrical, control and test failures

### F47 — Blind-mate electrical docking is under-specified — B1 / P

A nominal 40 A contact rating is insufficient without connector temperature rise, contact resistance, mating life, environment and live-mating capability. Inrush can damage contacts; partial engagement can energise an unsecured module. Generic pogo pins should not be assumed suitable for industrial power or high-speed data.

**Closure evidence:** Selected connector datasheets, power isolation/precharge if needed, fuse protection, mating sequence, strain relief and fault tests. Mechanical capture must protect the electrical contacts.

### F48 — The battery bus is not defined by “48 V” — B1 / U

**Anchor:** PPT battery selection; roadmap’s 41–54 V bus range.

Maximum charge voltage depends on the selected cell count and charger. Converter input limits must cover the actual pack and transients. Capacity in Ah does not establish discharge current, thermal performance or safe regeneration acceptance. The 60 Ah battery’s dimensions and mass remain unverified.

**Closure evidence:** Exact pack/BMS/charger specifications and a compatible electrical architecture, rather than a nominal-voltage shopping list.

### F49 — STO, emergency stop and ordinary GPIO are conflated — B1 / D

The roadmap alternates industrial safety terminology with simple relay or controller implementations. Removing drive torque does not necessarily produce the required deceleration or hold a load. Ordinary software or dual wires do not, by themselves, demonstrate a validated safety function. ISO’s catalogue identifies the 2020 edition as revised by 2023; exact clause claims need the applicable full standard, which was not audited here. [E5]

**Closure evidence:** Clearly distinguish a supervised demonstration stop circuit from an industrial safety implementation. Specify actual stop behaviour, fault handling and restart inhibition without claiming certification.

### F50 — Module identity is not payload knowledge — B1 / P

A resistor or EEPROM identifies a module type, not actual cargo mass, CG, damage or whether all locks have seated. A correctly identified conveyor can still be overloaded. Unknown-module behaviour is inconsistently described as derating rather than preventing operation.

**Closure evidence:** Define known-module limits, loading restrictions, independent seating/retention checks and explicit behaviour for absent, unreadable or implausible ID data.

### F51 — Protected wiring can become unserviceable wiring — B2 / P

Internal conduits may not pass connector bodies, respect bend radius or allow harness replacement. Power noise can disturb low-level signalling. A hollow node does not establish IP65 protection; every opening and moving joint matters. Aluminium/steel interfaces and exposed tool steel also require environmental consideration.

**Closure evidence:** Route actual cable and connector envelopes, include pulling/replacement access, and define the intended indoor environment without unsupported ingress claims.

### F52 — Software scope can still block the physical demonstration — B2 / P

Avoiding custom SLAM is sensible scope control, but “use ROS2” is not an integration plan. Drives, encoders, odometry, stop inputs, transfer logic and sensors still need working interfaces. High compute capability cannot compensate for missing state handling or docking reliability.

**Closure evidence:** The smallest deterministic demonstration sequence with selected hardware interfaces. Mechanical and Fusion evidence should not depend on finishing a full navigation product.

### F53 — The proposed first powered test is premature — B1 / D/P

**Anchor:** S3 Part 3 validation experiment 2: loaded travel at 1.8 m/s followed by emergency braking.

This test combines unknown braking, traction, cargo restraint and frame strength. It is a late-stage system test, not a first validation experiment. A successful run also cannot establish fatigue life or safe operation across modules.

**Closure evidence:** Progress through dimensional inspection, restrained joint tests, unpowered fit checks and controlled low-speed unloaded trials before any loaded dynamic test. Full-load tests need competent supervision, rated containment and documented release criteria.

## 10. Simulation and evidence failures

### F54 — Numerical results are presented without reproducible analyses — B3 / U

**Anchor:** S3 Part 2 Tasks 13 and 22; final freeze declaration.

The roadmap describes measured FEA twist, 65 MPa stress, 18.5 kg mass and validated compliance but supplies no model revision, mesh, contacts, solver output or reaction summary. The absence of those files in this review does not prove no analysis exists; it means these results cannot be relied on here.

**Closure evidence:** Native Fusion studies tied to a specific CAD revision, material assignments, load definitions and exported results. Until then, mark numerical outcomes as unverified, not achieved.

### F55 — Fixed supports and bonded contacts can manufacture stiffness — B1 / P

**Anchor:** S3 FEA boundary setups.

Fixing several tyre contact regions and bonding bolted joints can suppress slip, tyre compliance, uplift and local joint rotation. “Pinned fixed” is not a sufficient boundary-condition definition. Removing a payload-interface reaction is also not equivalent to removing a wheel’s floor contact.

**Closure evidence:** Separate interface contacts from ground contacts, model realistic release/compliance, and compare a justified simplified model with sensitivity cases.

### F56 — Mesh, resonance and failure metrics are not validated — B2 / U/P

A prescribed 15 mm global mesh and 1.5 mm local mesh do not establish convergence or accurate thin-wall behaviour. A >35 Hz mode is not automatically safe when wheel, motor and belt excitation varies with speed and loading. A single von Mises plot does not evaluate buckling, separation, slip, fatigue or functional deflection.

**Closure evidence:** Targeted convergence on decision-critical quantities, reaction checks, assembly modes with appropriate masses/supports, and separate acceptance criteria for each governing failure mode.

### F57 — The cited evidence chain is unreliable — B3 / D/U

**Anchor:** S4 body and Works cited; S3 bibliographies.

The document’s title is not evidence that it contains only primary validation. Concrete examples from its own reference mapping:

| S4 reference | What the bibliography actually identifies | Failure of support |
|---|---|---|
| 5 | A generative-design software comparison blog | Not Autodesk’s engineering manual for the numerical setup attributed to it. |
| 7 | A patent on adjustable traction weights | Not a general zero-point contact/preload manual. |
| 8 | A third-party blog explaining ISO 3691-4 | Not the standard text supporting claimed exact limits. |
| 12 | A robotics podcast | Not a primary keep-out or manufacturing specification. |
| 3 | ROEQ TMC300 cart-system product page | Not a conveyor manual proving the roadmap’s tote speed, shock factors and motor sizing. |

The directly checked TMC300 page describes a cart system. [E6] The roadmap also gives a paraphrased title for US20230324882A1 that differs from the publication’s actual subject: shape optimisation with singularities and disconnection prevention. This does not prove the patent contains no relevant constraint discussion; it does mean its asserted maintenance-specific interpretation needs passage-level verification. [E7]

**Closure evidence:** For each retained claim, record the real source, revision/page, supporting passage and whether the number is measured, supplier-rated, calculated or assumed. Do not describe every suspect reference as fabricated without checking it.

### F58 — Claimed freedom to operate is not established — B3 / U

**Anchor:** S3 patent matrix and Part 3 Q3; S5 patent landscape.

“Different actuator,” “different material,” or “four-corner layout” is not an element-by-element claim analysis. Publication numbers, family mappings, legal status and jurisdictions require verification. Neither this audit nor the supplied comparison establishes absolute freedom to operate, and no conclusion about infringement is made here.

**Closure evidence:** Keep the landscape as prior-art research with explicit uncertainty. Withdraw blanket legal clearance and “first-ever” claims unless independently supported by appropriate review.

## 11. Ways the solution can work mechanically and still lose its value

### F59 — Existing modularity defeats the current market narrative — B2 / D

**Anchor:** PPT slide 5.

The assertion that operators must buy a separate dedicated AMR for every workflow is too broad. MiR’s own product page describes different top modules and applications on its common base. This does not establish rapid powered-superstructure exchange, but it does invalidate generic “one base, many jobs” as a unique advantage. [E1]

**Closure evidence:** Define the narrower unresolved exchange problem and compare against a specific existing integration method, with measured or documented changeover steps.

### F60 — The cost comparison uses unequal system boundaries — B2 / D/U

**Anchor:** PPT slides 5–6.

An estimated student BOM is compared with a commercial robot’s sale price, while a chassis-only mass is compared with a complete robot’s tare. Commercial safety hardware, software, integration, service, warranty and margin are not interchangeable with raw parts. The stated ₹5–6 lakh, ₹45–55 lakh benchmark, 28–40% fleet savings and 40–50% gross margins were not substantiated by quotations or a cost model in the supplied files.

**Closure evidence:** Compare frame to frame, interface to interface, and complete system to complete system. Include machining, inspection, failed prints, purchased parts, assembly and integration. No replacement price is invented in this audit.

### F61 — Swapping cannot replace simultaneous capacity — B2 / P

One base cannot execute a conveyor task and a lifting task concurrently. If workloads overlap or travel capacity is already saturated, several dedicated robots may still be necessary. If modules change only once per quarter, seconds saved at the latch may never repay extra hardware and maintenance.

**Closure evidence:** A target workflow with task timing, actual exchange frequency, utilisation and cost of the handling/staging system. Evaluate total available working time after exchange and recovery overhead.

### F62 — Lightweighting can erase its own stability benefit — B2 / P

Reducing low-mounted base mass can increase combined CG height and reduce restoring moment. Larger batteries or added ballast may then be needed, recovering the mass allegedly saved. Lower chassis mass also need not materially reduce energy if auxiliary electronics, conveyor power or duty-cycle losses dominate.

**Closure evidence:** Compare complete vehicle mass, stability and duty-cycle energy together. A percentage reduction in frame mass is not the same percentage reduction in robot energy.

### F63 — Precision is not valuable without a task-level requirement — B2 / P

An expensive 50 μm docking target can be irrelevant if station alignment tolerates millimetres and the wheel/floor system dominates the error budget. Conversely, a loose coupling may be insufficient for a precise transfer. The required functional tolerance has not been derived from the warehouse task.

**Closure evidence:** Allocate permissible transfer error across station, vehicle, suspension, coupling and module. Size precision to that budget before paying for it.

### F64 — A simpler architecture may equal or outperform the proposal — B2 / U

**Anchor:** S3 rejects welded, extruded and alternative coupling architectures as categorically inferior.

An honestly designed aluminium tube frame with machined brackets, or a fabricated sheet structure with standard clamps, might provide equivalent stiffness and service access at lower cost. That is a counter-hypothesis, not an established result. Printed nodes remain justified only if their integration or geometry offers measurable value under the same constraints.

**Closure evidence:** A fair baseline with the same payload, envelope, access corridors, load cases and manufacturing boundary. If the hybrid loses, narrow the printed scope or revise the concept rather than inventing poor baseline performance.

### F65 — “Universal” may mean only your own two matching parts — B2 / U

A common pin pattern does not resolve power, CG limits, safety behaviour, physical clearance, transfer height or supplier tolerances. A towing module also creates different braking and articulation loads from a conveyor; a robot arm can exceed stability limits at low mass.

**Closure evidence:** A bounded interface specification and at least a second independently modelled attachment mating to the unchanged base. One physical functional attachment can satisfy Part B; broader universality remains a claim requiring broader evidence.

## 12. Failure chains worth testing first

Individual risks interact. These are particularly credible chains for this architecture:

1. **Fourth pad sits high → uneven clamp preload → local plate bending → fretting → locator drift → tote-transfer misalignment.** A successful clean initial fit will not reveal the whole chain.
2. **Corner-supported payload unloads driven wheels → available friction falls → stopping distance grows → cargo shifts → stability margin collapses.** Stronger motors and stronger nodes do not resolve it.
3. **Larger battery narrows the service route → cross-member is moved → torsional stiffness falls → added bracing blocks extraction.** Packaging and optimisation must be iterated together.
4. **Unverified load table enters Fusion → visually convincing node is printed → real joint compliance was omitted → assembly deflects despite a favourable stress plot.** The input model is the root problem.
5. **Fast clamp release → heavy module needs external lifting → exchange time remains long → claimed fleet savings disappear.** A functional latch is not a validated business case.
6. **Feature-rich roadmap → insufficient time for original Fusion studies → generated render fills the gap → originality and scoring requirements become exposed.** Scope inflation becomes a submission risk.

## 13. What must be corrected before tomorrow’s PPT submission

This is a critique-driven correction checklist, not slide copy. The team must author its own submission and verify the findings.

| Required correction | Why it cannot wait |
|---|---|
| Resolve original-design/AI-content requirements and verify the Fusion submission link | Eligibility precedes technical persuasion. |
| State 250 kg as a **design target for total top load**, unless actual validation supports more | Prevents implying tested cargo capacity. |
| Freeze 6061-T6 members and remove inherited carbon-fibre results | Avoids describing incompatible machines. |
| Replace “validated design freeze” with the actual evidence status | No supplied solver or test records substantiate the existing declaration. |
| Remove “first to combine,” “no existing modular solutions,” and guaranteed commercial superiority | These claims exceed the evidence and invite easy rebuttal. |
| Remove or qualify exact savings, margins, mass, stress, stiffness, life and timing figures | None should appear as achieved without a traceable basis. |
| Correct the fourfold force/moment errors before showing any FEA-derived claim | Incorrect loads invalidate the apparent rigour. |
| Stop calling the four rigid pads automatically exact constraint | The unresolved vertical support issue is real. |
| Show how the unloaded attachment is physically supported during exchange | Otherwise the principal benefit remains incomplete. |
| Distinguish full-scale concept from the scaled printed workability model | Avoids claiming that plastic demonstrates 250 kg capability. |
| Focus Part A and Part B evidence on actual Fusion and DfAM work | These are the documented scoring priorities. |

## 14. Minimum evidence needed before committing to fabrication

Passing these checks would close specific criticisms. It would not automatically certify the whole robot.

| Gate | Required evidence | Do not proceed with the affected build if… |
|---|---|---|
| G1: One configuration | Parameter sheet, coordinate drawing, mass breakdown and chosen component envelopes | Capacity, material or interface dimensions still contradict each other. |
| G2: Physical packaging | Complete base/module assembly and swept service/handling volumes | Battery, motor, caster, tool or module-removal path collides. |
| G3: Equilibrium | Free-body diagrams and independently checked forces/moments | Reactions do not balance or force/moment application is ambiguous. |
| G4: Coupling coupon | Sectioned mechanism, tolerance stack and restrained seating/retention test | Four stations cannot reliably seat or retention depends on guessed friction. |
| G5: Ground support | Wheel-load and stability assessment across load cases | Drive wheels unload or the effective load resultant leaves the support polygon. |
| G6: Honest comparison | Same-boundary baseline and proposed mass/stiffness/manufacturing comparison | The proposed complexity has no demonstrated benefit. |
| G7: Manufacturing | Slice/build plan, machine availability, machining route and realistic lead times | Critical tolerances or processes have no feasible production route. |
| G8: Controlled demonstration | Restricted-load protocol, cargo retention and stop behaviour | The first useful test requires an uncontrolled full-speed loaded run. |

The most informative early physical experiment is a **restrained interface specimen or small mating assembly**, because it tests the mechanism underlying the proposal’s distinctiveness before the team buys a complete robot. This is a test-priority judgment, not a claim that the rest of the design can be ignored.

## 15. Conditions under which the present solution should be substantially revised

- If the team cannot produce original Fusion design and manufacturing evidence, the present presentation approach does not meet the supplied challenge requirements.
- If four-station seating and retention cannot be made reliable within available machining tolerances, the interface implementation must change.
- If the complete 250 kg concept cannot satisfy traction and stability within its envelope, either the target or the vehicle layout must change; thicker nodes alone cannot solve it.
- If exchange requires lengthy lifting and alignment, the quick-change advantage must be narrowed or the handling architecture redesigned.
- If a matched conventional baseline achieves the same useful performance more simply, printed-node complexity needs a narrower justification.
- If customers seldom change tasks or need concurrent capacity, the claimed fleet-reduction business case should be abandoned for that segment.
- If the 250 kg headline prevents a credible, original and printable concept from being completed, it is a self-imposed constraint rather than a requirement established by the supplied official brief.

**Overall disposition:** Retain the hybrid base plus detachable conveyor as a candidate. Reopen the detailed design freeze. The concept’s plausibility survives this audit; the current claims of validated loads, exact constraint, production readiness, universal compatibility, guaranteed savings and legal clearance do not.

## 16. Source register and limits

### Supplied sources used

- **S1:** `SIH26112.pdf`, both pages visually inspected. Authoritative for the supplied competition requirements, not evidence of later amendments.
- **S2:** `SIH26112_Final_Modular_AMR_SIH2026 (1).pptx`, text/tables from all seven slides inspected. Latest declared configuration. Asset authorship and any separately submitted Fusion links were not verified.
- **S3:** `modular-amr-technical-roadmap(3).md`, consolidated Parts 1–3. Section anchors identify the challenged statements; duplicated task numbers are qualified by part.
- **S4:** `Primary Source Acquisition and Architectural Validation for Modular AMR Platform-1.pdf`, architecture assertions and bibliography inspected. Treated as a secondary synthesis whose references require checking, not as independent validation.
- **S5:** `Modular AMR Patent Landscape Architecture.md`, relevant patent table/reference mappings inspected. No complete legal claim audit performed.

The separate design-freeze/adversarial documents and earlier exploration reports were available, but this audit does not claim a new exhaustive reread of all ten attachments. The consolidated roadmap is the primary engineering object under review. No actual Fusion project, CAD measurements, safety implementation, quotations or laboratory results were inspected.

### External primary-source spot checks

Accessed 11 September 2026. These support only the associated narrow findings, not the roadmap’s entire numerical design.

- **E1 — MiR250 manufacturer page:** Confirms a common base with multiple module/application options. It does not prove a specific powered-module exchange time. [MiR250](https://mobile-industrial-robots.com/products/robots/mir250)
- **E2 — Autodesk manufacturing constraints:** Confirms Fusion offers manufacturing-method constraints; does not certify that this node is support-free or that the team’s account has every required entitlement. [Specify manufacturing methods](https://help.autodesk.com/view/fusion360/ENU/?contextId=GD-SPECIFY-MFG-METHOD)
- **E3 — MIT constraint-design lecture:** Supports the distinction between independent exact constraints and other coupling strategies. The four-pad diagnosis is this audit’s application of that principle. [Design of Constraints in Precision Systems](https://ocw.mit.edu/courses/2-75-precision-machine-design-fall-2001/962f560f763715a81e775af536b5e3f8_constraint_lecture_part_I.pdf)
- **E4 — EOS aluminium materials:** Provides material/process information and identifies heat-treatment dependence. No generic web property was adopted as a design allowable here. [EOS aluminium materials](https://www.eos.info/metal-solutions/metal-materials/aluminium)
- **E5 — ISO catalogue:** Identifies ISO 3691-4:2020 as withdrawn and revised by the 2023 edition. Full normative clauses were not inspected. [ISO 3691-4 catalogue entry](https://www.iso.org/standard/70660.html)
- **E6 — ROEQ TMC300 listing:** Identifies the cited product as a cart system, undermining its use as support for the roadmap’s particular conveyor calculations. [TMC300](https://mobile-industrial-robots.com/products/mir-go/roeq-tmc300)
- **E7 — Published Autodesk patent text:** Confirms the publication’s actual title and subject. No infringement, validity or jurisdictional conclusion is inferred. [US20230324882A1](https://patents.google.com/patent/US20230324882A1/en)

Some broad web searches returned irrelevant results, so they were excluded. Direct primary pages were used instead. The SICK manual and requested Interroll page were not successfully retrieved; scanner-specific thresholds, motor curves and catalogue prices therefore remain unverified. The engineering calculations above are transparent deductions from explicitly stated inputs, not substituted supplier specifications.
