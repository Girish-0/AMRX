# AMRX — Revised Engineering Roadmap v2.0

**Project:** SIH26112 — Modular AMR Platform for Smart Warehouse Automation  
**Team:** AMRX · AU/SIH/26-126  
**Date:** 11 September 2026  
**Status:** Revised development baseline; detailed design and fabrication release remain open.  
**Purpose:** Internal engineering roadmap for refining the shortlisted university proposal. This is not a replacement PPT, a completed Fusion design, or a statement of tested capacity.

> **Recommended direction:** Develop an original Fusion-designed hybrid aluminium chassis with a bounded interchangeable-module interface, a powered tote conveyor, and a simple passive carrier demonstrating reuse of the same base. Concentrate additive design on structural junctions where integration has measurable value. Use manual, positively retained clamps and a supported, power-isolated exchange procedure first. Prove fit, load paths, service access and manufacturability before automating the exchange or purchasing a complete industrial robot.

A rewrite cannot eliminate physical failures. It can remove contradictory requirements, replace avoidable mechanisms, and define evidence that must exist before a risk is considered closed. This roadmap does all three. **No physical audit finding is marked experimentally closed by this document.**

## 1. Authority, evidence and what this revision supersedes

### 1.1 Inputs actually reviewed

| Source | Role in this revision | Limits |
|---|---|---|
| `AMRX_AMR_Adversarial_Failure_Audit.md` | Failure register F01–F65; reported extraction of the official brief and rubric | Its cited official PDF, validation reports and patent landscape were not separately attached to this request. Their contents are not treated as independently reverified here. |
| `SIH26112_Final_Modular_AMR_SIH2026 (1).pptx` | Text and tables from all seven slides; latest declared 250 kg/aluminium concept | No native Fusion project, measurement files or quotations accompany the deck. Asset provenance has not been established. |
| `modular-amr-technical-roadmap.md` | Original 1,614-line consolidated roadmap, architecture and calculations | Inconsistent configurations and unsupported outcomes are superseded, not inherited as results. |
| Primary pages listed in §18 | Narrow checks on existing modular products, Fusion manufacturing options, constraint design and material-process dependence | They do not validate AMRX geometry, capacity, costs or performance. |

**Precedence:** Current official challenge instructions and written organizer clarification → team-approved requirements → this revised baseline → historical slides/roadmap. The official brief itself must be placed in the team's controlled project folder at Gate G0. Public search in this review did not establish an authoritative replacement copy.

### 1.2 Evidence labels

- **Reported requirement:** A requirement reproduced by the supplied audit, pending direct team confirmation against the official document.
- **Decision:** The development choice recommended here.
- **Target:** A desired outcome; not an achieved result or released operating limit.
- **Assumption:** A numerical input that must be replaced or justified.
- **Calculated example:** Arithmetic under stated assumptions; not a component rating.
- **Verified result:** Reserved for a specific reproducible CAD study, supplier record, inspection or physical test.

All dimensions below are concept parameters unless explicitly tied to released drawings. The word “freeze” applies only to the scope and conventions at this stage.

### 1.3 Withdrawn legacy claims

Retire the inherited 100 kg/carbon-fibre configuration, one-tonne universal envelope, fixed 5 kN-per-clamp preload, competing taper definitions, 12-roller conveyor and synchronized wedge mechanism. Retire the claimed 18.5 kg frame mass, 65 MPa result, 327% stiffness improvement, 0.12° scanner guarantee, infinite fatigue life, zero wear, support-free LPBF, universal compatibility, absolute freedom to operate, and guaranteed commercial savings.

The previous 48 V 60 Ah battery, two 750 W motors, Jetson and 1.8 m/s speed become **unselected candidates**, not purchase instructions. Their names and prices cannot substitute for packaging, duty-cycle and braking calculations.

## 2. Solve the challenge at the correct level

### 2.1 Engineering problem

A common AMR base must accept attachments with different masses, centres of gravity and task reactions while preserving structural integrity, usable payload, service access and a credible manufacturing route. The attachment must actually perform its selected warehouse task. Lightweighting is valuable only when the resulting assembly still meets these requirements.

The project investigates whether **selectively printed structural junctions, conventional aluminium spans, replaceable interface wear parts and explicit service envelopes** can achieve that balance better than a matched conventional design.

This is a bounded engineering contribution. It does not require proving that commercial modular AMRs are absent or that LiDAR floor strikes are the dominant industry failure.

### 2.2 Requirement-to-deliverable map

The requirements and marks here are **reported by the supplied audit**, not independently extracted from the official PDF in this turn.

| Reported requirement / criterion | AMRX response | Evidence required |
|---|---|---|
| Part A: universal AMR/AGV chassis for interchangeable attachments | One unchanged base; common interface specification; conveyor and passive carrier | Both attachments assembled onto the same base in Fusion; no new base drilling, welding or bracket relocation |
| Part B: one functional attachment | Powered, bidirectional single-tote roller conveyor | Original attachment structure, mechanism, load calculations and workability demonstration |
| Complexity and workability: 20 marks | Resolve support, retention, handling, cargo transfer and service access | Sections, assembly motion and physical fit/transfer observations |
| DfAM: 20 marks | Design selected structural junctions for a declared additive process | Orientation, supports, machining access, build-time and material records |
| Innovative design features: 15 marks | Investigate integration of load paths, replaceable wear datums and service access | Measured comparison with a fair baseline; no unsupported priority claim |
| Advanced Fusion features: 30 marks | Parametric assemblies, generative studies, simulation and additive preparation as available | Original project history, actual study setup and results, manufacturing setup |
| AM process/material selection: 15 marks | Distinct full-scale metal concept and scaled polymer demonstrator | Process-specific rationale, limitations and credible supplier/printer route |
| Original Fusion design; public Fusion link; 5–7 slides; faculty/SPOC form | Team-produced submission artifacts and access check | Confirm exact current requirements and completion |

**Submission constraint reported by the audit:** AI-generated content is prohibited. Use this document as internal critique and planning assistance; the team must establish the permitted boundary with the SPOC and author its qualifying Fusion work and submission. Do not assume private research assistance and required Fusion generative design are treated identically. This issue does not prevent preparation of the requested internal roadmap.

### 2.3 Scope discipline

**Required development core:** Part A and Part B CAD, baseline comparison, interface specimen, service/handling proof, DfAM evidence, and a scaled workability model consistent with confirmed event rules.

**Useful second module:** A low-profile passive tray/carrier. It tests geometric interchangeability without introducing lifting, towing articulation or robot-arm reactions. Model it independently using the interface drawing. Build a lightweight version if time permits.

**Deferred:** Autonomous module changing, custom SLAM, fleet software, cryptographic IDs, blind-mate high-current connectors, sensor isolation bridge, industrial certification programme and a third powered module. A low-speed mobile demonstration is an extension after mechanical gates, not a dependency of the scored design evidence.

## 3. One configuration and one coordinate system

### 3.1 Concept baseline

| Parameter | v2 decision / target | Status and release condition |
|---|---|---|
| Base plan envelope | 800 mm X × 600 mm Y | Retained packaging target; increase if credible hardware cannot fit |
| Interface height above floor | Start packaging at 350 mm | New assumption to reduce height; replaces fixed 500 mm. Revise against wheels, battery and transfer station. |
| Interface station spacing | 500 mm X × 400 mm Y | Retained grid, with axes made unambiguous |
| Total top load | 250 kg, including attachment, cargo and everything above the interface | Full-scale base structural design target; no physical capacity established |
| Primary attachment | One 50 kg-cargo tote conveyor | Attachment design target; does not inherit a 250 kg cargo rating |
| Top-load CG domain for first structural studies | X and Y offsets each within ±50 mm; height ≤300 mm above interface | Restrictive initial assumption. Transfer states are assessed separately and can exceed these offsets. |
| Structural members | 6061-T6 rectangular hollow sections, bolted joints | Start section study at 40 × 40 × 3 mm; increase/change based on results. No carbon-fibre structural members. |
| Primary nodes | Selective AlSi10Mg LPBF concept | Supplier/process-dependent; not mandatory metal fabrication for the first demonstrator |
| Module attachment | Four accessible manual draw clamps with positive secondary retention | Exact part number and mounting rating remain open |
| Location and Z support | Round/diamond location; three primary pads plus adjustable fourth support | Detailed sequence and limitations in §5 |
| Base ground support | Two central sprung drive pods and four passive casters | Candidate retained; wheel-load gate is mandatory, not solved by this label |
| Conveyor rollers | Exactly eight, axes parallel to X, cargo travel along ±Y | Geometry in §7 |
| Utilities | Power-isolated, keyed manual connector; separate module enable/identity signals | No live exchange; demonstrator uses a current-limited low-voltage supply |
| Service policy | Remove cargo and module; isolate power before battery or drive service | Sacrifices under-load servicing to simplify structure and stability |
| Initial environment | Supervised indoor operation on characterized, dry, level floor | No outdoor, ingress-protection or threshold-crossing claim |

Define **O_G** at floor level below the centre of the interface. X is forward, Y left, Z up. Define **O_I** at the interface centre, so O_I = (0,0,h_I) in the floor frame. All interface moments are about O_I. Whole-vehicle stability uses O_G and actual ground-contact positions.

### 3.2 Mass boundaries

Maintain separate ledgers:

1. **Structural chassis:** Nodes, tubes, braces, structural joints and wheel-mount brackets.
2. **Base-mounted interface:** Pads, locators, clamps, support mechanism and fasteners.
3. **Complete base tare:** Items 1–2 plus wheels, suspension, drives, battery, controls, sensors, covers and wiring.
4. **Attachment tare:** Complete removable module, including its mating hardware, restraints and connector.
5. **Cargo:** Material carried by the attachment.

Total top load = attachment tare + cargo. Complete moving mass = complete base tare + total top load.

For a hypothetical 40 kg conveyor, 50 kg cargo gives 90 kg top load. The base's remaining structural headroom does **not** authorize putting 210 kg on that conveyor. A future 210 kg cargo carrier would require its own structure, CG and vehicle-level validation.

Report both cargo/complete-unloaded-vehicle mass and top-load/base-tare ratio with their denominators written out. Chassis-only mass ratios are a separate structural comparison.

## 4. Part A: practical hybrid structure

### 4.1 Structural arrangement

Use two longitudinal side structures, front/rear transverse members, and permanent gussets or diagonals outside the service envelopes. Make the bare base resist racking without relying on the removable conveyor as a shear panel.

The four corner nodes integrate member connections, interface support lands and caster brackets where geometry permits. **Central drive loads enter dedicated mid-span brackets and the side structures.** Do not pretend the central wheels attach directly to corner nodes. Include these intervening members in the global model.

At each module station, compression passes through a replaceable steel support pad into a broad node land. Uplift passes through the clamp keeper, clamp body and structural backing into the node/frame. Shear passes principally through the designated round and diamond locators. The load paths are distinct but mechanically coupled; none is assumed perfectly pure.

### 4.2 Member joints

Replace friction-only circular split collars with rectangular sockets or flanged joints having positive axial retention and an anti-rotation path. A starting candidate is a through-bolted socket with an internal crush sleeve and suitable end engagement. Determine hole positions, edge distance, wall bearing, tear-out, net-section stress and bolt preload before releasing dimensions.

Use accessible nuts or qualified threaded inserts in metal. Do not select bolt grade or tightening torque by copying the old roadmap. Galvanic protection and finishes must preserve the designed metal compression path rather than inserting an uncontrolled soft layer under a highly loaded joint.

The first physical joint specimen must reproduce the actual tube wall, sleeve, fastener and socket geometry. Test restrained axial and torsional loading, then inspect for slip, ovalization and preload loss.

### 4.3 Service access with less structural penalty

Adopt **top battery removal after unloading and removing the attachment** for v2. This removes the need for a large lateral tunnel through the primary side structure. Preserve a lifting/tool envelope above the actual pack and clearance for connectors and straps. Battery mass still requires a rated handling aid when appropriate.

Specify drive-pod removal only while the unloaded base is on rated service stands. Choose an outward or downward route after modelling wheel and fastener access. Do not remove a support wheel from an unsupported robot.

Use accessible external cable trays with guards. Model connector bodies and minimum bend radii. Avoid sealed internal node conduits unless they provide a demonstrated advantage and allow harness replacement.

**Trade-off:** Battery servicing includes attachment removal. Measure the full sequence and include it in maintenance comparisons. If frequent battery exchange becomes a real workflow requirement, reopen the structure rather than claiming a 60-second hot swap.

### 4.4 Baseline and additive justification

Build a conventional control design in Fusion: the same service opening, footprint, load domain, attachment interface and wheel locations, using aluminium members and machined/fabricated junctions. A sensibly designed steel alternative may be included if time permits.

Compare finished assemblies, including fasteners, sleeves and machining allowances. Printed junctions remain justified only if they improve a useful outcome: lower assembled mass at equal functional stiffness, fewer alignment-sensitive parts, easier service access, or a geometry difficult to manufacture conventionally at acceptable cost.

A small node-only mass reduction cannot establish vehicle energy savings. If the printed design loses the comparison, retain additive work on the junction where it helps most and simplify the rest.

## 5. Module interface: locate first, support predictably, retain visibly

### 5.1 Station definition

Coordinates are millimetres in the O_I frame.

| Station | X | Y | Function |
|---|---:|---:|---|
| A | −250 | −200 | Primary round locator, primary Z pad, clamp |
| B | +250 | −200 | Diamond locator relieved along X, primary Z pad, clamp |
| C | −250 | +200 | Primary Z pad, clamp; lateral clearance |
| D | +250 | +200 | Retractable adjustable support, clamp; lateral clearance |

A constrains planar translation. B constrains lateral motion at its location and thus yaw while allowing spacing error along the A–B line. Three primary pads establish the initial seating plane. **The completed, four-supported assembly is not claimed to be an exact-constraint coupling.** It requires stiffness and load-sharing analysis after D and the clamps engage. Independent-constraint principles underpin the location scheme; this particular implementation remains a project proposal. [MIT constraint-design lecture](https://ocw.mit.edu/courses/2-75-precision-machine-design-fall-2001/962f560f763715a81e775af536b5e3f8_constraint_lecture_part_I.pdf)

### 5.2 Contact sequence and fourth support

Use cylindrical locating lands with entry chamfers and replaceable bushings. Chamfers provide entry guidance; they are not final seating tapers. Pin ends must not bottom before the primary pads contact. Keep adequate relief at non-locating stations and around clamp keepers.

D uses an accessible, lockable support screw with a replaceable swivel contact pad, initially retracted. Its intended role is to fill the fourth-point gap after the initial plane has been established, rather than force four inaccurate pads into one plane.

1. Keep the empty module captured by the handling fixture during lowering and initial location.
2. Bring A/B/C into verified contact without using clamps to drag a misaligned module into place.
3. Close the A/B/C clamps in the established sequence and adjustment range.
4. Advance D to contact using a controlled procedure, verify that A/B/C have not lifted, and secure D against backing out.
5. Close the D clamp. Check local seating and displacement again before removing the handling support.

The A/B/C triangle places the interface centre on a diagonal boundary. An offset empty-module CG can therefore make three-pad seating unstable. **The handling fixture must continue to prevent tipping until all support and retention steps are complete.** Do not conduct an unsupported gravity drop onto three pads.

Contact detection and screw adjustment torque must be established on the specimen; “finger tight” is insufficient as a released instruction. A feeler/contact indicator plus a displacement measurement provides a practical development check. If this process proves slow or operator-sensitive, use a supplier-qualified automatic work support or redesign the pad arrangement. Do not silently reinstate four rigid datums.

### 5.3 Clamps and wear components

Use four independently accessible manual draw clamps with captive keepers and positive secondary locks. Manual actuation removes the common shaft, wedge friction assumptions, four-corner synchronization and power-loss release dependency.

Selection must distinguish **holding capacity, actual clamping force, allowable load direction, fatigue duty and mounting strength**. They are not interchangeable ratings. No 5 kN clamp preload is prescribed. Derive the required retention and seating loads from the assembly model, select hardware, then measure achieved preload and scatter.

Seat compression into broad shoulders. Carry keeper uplift into backed structural flanges, not a few countersunk screws in a thin pocket. Check clamp bolts, keeper bending, pad bearing, insert retention and node prying together.

Use available hardened locating pins/bushings and replaceable wear pads with documented material and finish. Do not mandate an expensive A2 cartridge containing every interface function. A wear component replacement must include a datum inspection and requalification procedure.

### 5.4 What is gained and what remains

This revision removes active-release machinery and ambiguous wedge self-locking. It trades automatic exchange for an inspectable manual process, and gains a controlled means of addressing the fourth support. Remaining risks are clamp misadjustment, omission of a secondary lock, support-setting error, contamination, local stiffness and wear. Gate G3 tests these directly.

**Fallback:** If reliable quick exchange cannot be achieved, retain locating pins with captive bolted retention for the demonstrator and withdraw the tool-less claim. Interchangeability survives; measured changeover benefit may not.

## 6. Exchange handling completes the mechanism

The exchange equipment is part of the system boundary. A free-standing 40–50 kg conveyor must not depend on operators lifting and aligning it by hand.

**Selected concept:** A rated mobile lifting trolley with a purpose-designed capture cradle engaging accessible module lifting ledges outside the four mating stations. The lifting stroke exceeds the locator engagement and all retainers. Trolley legs, casters and cradle members must clear the AMR wheels and frame. Provide a second parking cradle for the outgoing module.

The handling trolley is preferably purchased/rented; the team designs and verifies the compatible cradle. A generic scissor table is not assumed to fit merely because it can lift the mass.

**Exchange sequence:**

1. Finish the task; remove cargo; stop and immobilize the base in the exchange zone.
2. Isolate attachment power, confirm stopped rollers, unplug the keyed connector and park the cable.
3. Engage and secure the trolley cradle. Prevent module motion before opening any clamp.
4. Release the clamps and retract D; raise the module clear without pulling sideways on the locators.
5. Secure the removed module on its parking support.
6. Bring in the next module; inspect/clean mating surfaces; perform §5.2 seating and retention.
7. Verify four retained stations, remove trolley support, connect utilities while isolated, then perform the restart checks.

Every intermediate state needs a stable support path. Include trolley overturning with an offset module, caster brakes, floor slope, pinch access and unintentional base motion. If the trolley cannot approach the underside or outboard ledges within the 800 × 600 layout, change the packaging before further optimization.

Time **stop-old-task to ready-for-new-task**, including handling, support adjustment, cleaning, connection and checks. Record latch-operation time only as a subcomponent. No three-minute promise is made before these measurements.

## 7. Part B: one useful, bounded conveyor

### 7.1 Physical task and geometry

The first use case is a single rigid-bottom tote transferred between the parked base and an aligned fixed station. Start with a **600 mm X × 400 mm Y tote envelope**, 50 kg maximum cargo target, and a bottom surface explicitly compatible with rollers. This is a task assumption, not proof that every tote of that external size is suitable.

| Feature | Initial geometry / decision |
|---|---|
| Roller count | Eight |
| Roller axes | X direction |
| Cargo transfer | ±Y direction |
| Roller diameter | 50 mm candidate |
| Roller pitch | 70 mm along Y |
| First-to-last centre span | 7 × 70 = 490 mm |
| Roller outside span along Y | 490 + 50 = 540 mm, before stops/guards |
| Usable roller length | 650 mm candidate, to accommodate the 600 mm tote dimension along X |
| Module envelope | Must fit within 800 × 600 mm including side frames, drive and guards; explicitly model any approved overhang |
| Transfer speed | Start at 0.20 m/s target |
| Acceleration ramp | Start at 1.0 s target |
| Drive | Selected geared motor with guarded timing-belt transmission, or rated MDR system after curve checks |
| Frame | Aluminium cross-members and side structures with original optimized structural end/connection brackets |

The 540 mm roller span leaves only 60 mm total in Y for end provisions. Resolve stop packaging and station gap in CAD; do not assume the remaining envelope is sufficient. Roller count and pitch may be revised together if the real station requires it.

Design Part B's brackets to integrate roller-bearing support, cross-member connection and restraint loads. Compare against a simple plate bracket. Print for geometry when useful; do not add decorative organic parts merely to label Part B “generative.”

### 7.2 Loads and actuation

At 50 kg, reaching 0.20 m/s in 1.0 s requires an ideal acceleration force of 10 N, 1 J of kinetic energy and 2 W instantaneous inertial power at the end of the ramp. These numbers exclude rolling resistance, belt loss, gearbox loss, bearing friction, starting torque and misalignment. They are **not a motor specification**.

Measure/estimate resistance and use:

`F_required = m_cargo × a_transfer + F_rolling + F_other`

`T_at_driven_roller = F_required × roller_radius`

`P_mechanical = F_required × conveyor_speed`

Select against starting and continuous torque, thermal duty, controller current and transmission ratings. Provide current limiting and jam detection. Hard-stop impact is a fault case governed by stopping distance/compliance, not the normal motor ramp.

Do not divide cargo weight by eight to size rollers. Determine the minimum actual supporting rollers for tote ribs, entry/exit and misalignment. Check shaft bending, bearing reactions and side-frame deflection at that distribution.

### 7.3 Cargo retention and station transfer

Fit side guides against X drift and positive end restraints at both Y ends. Restraints remain mechanically engaged during travel and power loss. Transfer may open only the station-facing restraint after the base is immobilized and the station is ready. The opposite restraint remains engaged. Loss of power midway through transfer must stop both conveyors and prevent base departure while cargo bridges the gap.

A passive station alignment guide or docking reference may improve repeatability. It must have its own load and approach limits; do not permit high-force autonomous impacts into a locating funnel.

Create an error budget at the tote support surface: base-to-station positioning, floor/suspension height, interface repeatability, module deflection, station deflection and tote geometry. Provisional development objectives are interface translational repeatability ≤0.5 mm and angular repeatability ≤0.1°; these are negotiable task targets, not supplier specifications. Over 600 mm, 0.1° contributes approximately 1.05 mm of displacement and must be included in the station budget.

Derive allowable height mismatch and physical gap from the actual tote bottom and supported transition. Until those numbers are established, a conveyor transfer rating is not released. Test partial transfer positions, not just fully centred cargo.

## 8. Correct load calculations before opening the solver

### 8.1 Free bodies and conventions

For top mass m, CG position r relative to O_I, base translational acceleration a and gravity vector g:

`F_equivalent_on_base = m × (g − a)`

`M_about_interface = r × F_equivalent_on_base + independently_applied_task_couple`

This quasi-static representation assumes the top body follows the prescribed acceleration. Add rotational inertia and moving-cargo effects when applicable. A remote force placed at the CG already creates its moment. Do not add that moment a second time.

For the complete vehicle, include all base masses and ground reactions. Internal clamp preload is not extra vehicle weight. Wheel contact loss does not mean loss of a module support pad.

### 8.2 Transparent 250 kg calculation examples

Assume g = 9.81 m/s², top CG height 0.30 m above O_I, and centred top load unless stated. The acceleration values are proposed analysis inputs, **not standard-mandated limits or authorized test speeds**.

| Case | Inputs | Total interface action, magnitudes |
|---|---|---|
| Static | 250 kg | Vertical weight = 2,452.5 N |
| Longitudinal operating case | 0.50 m/s² | Horizontal force = 125 N; pitch moment = 37.5 N·m, plus static weight |
| Lateral operating case | 0.50 m/s² | Lateral force = 125 N; roll moment = 37.5 N·m, plus static weight |
| Braking design case | 1.50 m/s² | Horizontal force = 375 N; pitch moment = 112.5 N·m, plus static weight |
| Braking sensitivity case | 2.50 m/s² | Horizontal force = 625 N; pitch moment = 187.5 N·m, plus static weight |
| Offset-weight case | 50 mm offset in X or Y | Additional corresponding moment = 122.625 N·m |
| Combined offset and braking | 50 mm X offset with adverse 1.50 m/s² braking | Pitch-moment magnitude can reach 235.125 N·m; vertical and horizontal forces remain as above |

Each is a whole-interface load. Never multiply it by four. Offset and acceleration signs must be enumerated to identify adverse combinations.

For ideal equal-stiffness four-support screening, vertical reaction magnitudes may be explored with `N/4 ± M_y/(2L) ± M_x/(2B)`, where L = 0.50 m and B = 0.40 m. This formula does **not** determine the actual A/B/C/D reactions because support setting, clamp preload and structural compliance differ. A negative screening reaction indicates an uplift/retention question, not automatic safe load sharing.

### 8.3 Required study cases

| ID | Case | Essential modelling detail / acceptance question |
|---|---|---|
| LC1 | Empty base; empty module; maximum declared top load | Does each configuration balance, and are local stresses/deflections acceptable? |
| LC2 | Top-load CG at domain corners plus braking in both X directions | Combined gravity/inertia; separation, clamp force and locator loading |
| LC3 | Cornering in both directions; braking while turning where possible | Combined vector acceleration, yaw inertia and tyre friction use |
| LC4 | Tote entry, centred state and exit | Moving CG and station support share; include partial cargo overhang |
| LC5 | One actual ground contact unloaded; declared uneven-floor displacement | Preserve interface contacts; model tyre/spring compliance and active contact set |
| LC6 | Conveyor stall and restrained-cargo stop fault | Bounded actuator torque or impact energy and compliance; no invented shock multiplier |
| LC7 | Clamp preload scatter, D mis-setting, debris, one incomplete latch | Sensitivity and fault detection; incomplete retention inhibits operation |
| LC8 | Trolley-supported exchange and battery/drive servicing | Intermediate support conditions and changed mass distribution |
| LC9 | Modal response and repeated duty | Actual assembly mass/supports; fatigue load spectrum after duty definition |

An analysis case may reveal an operating condition that must be excluded. If real braking can exceed the initial design value, restrict the system or redesign it; do not choose a gentler analysis simply to obtain a favourable plot.

## 9. Traction and stability are separate release gates

### 9.1 Wheel loading

A six-contact base is statically indeterminate without compliance. Obtain actual wheel, caster and drive-pod ratings; model spring rates, preloads, stops and tyre stiffness. Check empty, centred, offset, braking and floor-variation states.

For driven normal load N_d, the ideal longitudinal traction bound is `F_available ≤ μN_d`. Required force includes total vehicle inertia, rolling resistance, grade and caster scrub. Combined turning/braking consumes a shared friction budget; it is not valid to use the full longitudinal and lateral bounds simultaneously.

**Sensitivity example only:** At a hypothetical complete mass of 350 kg, 50% driven load and μ = 0.4, ideal driven traction is about 687 N. A 1.5 m/s² acceleration requires 525 N before other resistance, while 2.5 m/s² requires 875 N. This illustrates why extra motor wattage cannot fix insufficient normal load. None of these inputs is measured for AMRX.

If wheel-load requirements cannot be met, adjust battery placement and drive-pod suspension geometry, change the contact arrangement, or reduce the released motion envelope. Freeze no purchase until the candidate layout passes.

### 9.2 Stability

Compute the combined CG using the complete mass ledger. Use the polygon formed by actual active wheel contacts, not the interface rectangle. Evaluate gravity/inertia resultants against every tipping edge, including adverse load positions and transfer states.

For a simplified level-ground rigid body, tipping onset is approximately `a_tip = g × b / h`, where b is the CG distance to the relevant support edge and h its floor height. This is only a screening relation. Springs, wheel lift, slopes, impact and moving cargo require the assembly model.

Reduce interface height where packaging permits and retain low battery placement. If lightweighting requires ballast to regain stability, include that ballast in the proposed complete-base mass.

### 9.3 Braking and energy

Select drives using wheel radius, gearing, torque-speed curves, peak/continuous current, thermal duty and brake ratings. Establish normal stop, emergency-command stop and loss-of-power behaviour separately. Evaluate full-battery regeneration and controller overvoltage response.

`d_stop ≈ v × response_delay + v²/(2 × achieved_deceleration)` is an initial constant-deceleration estimate, not a protective-field certification. Verify achieved stopping behaviour in contained tests only after the relevant gates pass.

Battery capacity follows duty-cycle energy and permissible discharge, not a headline 60 Ah value. The voltage range comes from the actual cell count, BMS and charger. The stationary workability demonstrator can use a current-limited supply and avoid an unnecessary traction battery purchase.

## 10. Fusion, simulation and manufacturing workflow

### 10.1 Native project structure

| Assembly / record | Required contents |
|---|---|
| `00_Requirements_Parameters` | Coordinate frames, versioned parameter sheet, mass and load ledger |
| `01_PartA_Conventional_Baseline` | Fair control design with identical functional boundaries |
| `02_PartA_Hybrid` | Nodes, members, joints, drive brackets, wheel envelopes, service volumes |
| `03_Common_Interface` | A/B/C/D, locating fits, clamp/keeper drawings, tolerance stack |
| `04_PartB_Conveyor` | Eight rollers, drive, optimized brackets, restraints, tote envelope |
| `05_Passive_Carrier` | Independent attachment using the same interface specification |
| `06_Handling_Station` | Trolley cradle, parking support and representative transfer station |
| `07_Studies` | Global/local simulation, setup records, contacts, reactions and mesh checks |
| `08_Manufacturing` | Full-scale process concept and separately prepared demonstrator prints |

Use team-created Fusion geometry and history consistent with the confirmed originality rules. Represent purchased components faithfully with declared provenance; clarify whether supplier model imports are permitted before including them in the qualifying design.

### 10.2 Study sequence

1. Assemble a simple baseline and verify force/moment balance by hand.
2. Model complete-base stiffness and wheel/interface reactions before optimizing individual nodes.
3. Preserve mating lands, member interfaces, clamp backing and service-access features in the local design region.
4. Add actual battery-removal, caster-sweep, clamp-handle, tool, trolley and cable envelopes as obstacles.
5. Run load-case-driven generative studies with declared material/manufacturing assumptions.
6. Rebuild/finish the selected outcome as needed, then reanalyse the manufactured geometry in the full assembly.
7. Compare to the conventional baseline with identical loads, contacts and mass boundaries.

Fusion provides separate manufacturing-method constraints, including additive and milling options; this supports exploring alternatives but does not establish an outcome's production readiness or account entitlement. [Autodesk manufacturing-method documentation](https://help.autodesk.com/view/fusion360/ENU/?contextId=GD-SPECIFY-MFG-METHOD)

### 10.3 Numerical acceptance

Use **static yield FoS ≥2 as a provisional project screening target** for the full-scale metal structure under the declared peak load cases. This is not a universal standard requirement and does not cover fatigue, buckling, contact, joint slip or safety functions.

For decision-critical deflections and representative non-singular stresses, use at least three sensible mesh refinements and a provisional <5% change criterion between the final refinements. Inspect singular edges separately rather than allowing a non-convergent point stress to dictate a false result. Check force and moment reaction residuals against the applied actions; a provisional <1% imbalance target is a numerical sanity check, not model validation.

Use appropriate member/shell representations or adequate through-thickness discretization. Bound uncertain joints with flexible and stiff cases. Bonded contact is permitted only as a stated idealization; it cannot prove a bolted joint does not slip. Use contact/compliance models for supports and separate clamp preload from external load.

Functional acceptance comes from the transfer error budget and seating requirements. Modal frequencies must be compared with motor, roller and wheel excitation across operating speeds. Retire the arbitrary >35 Hz pass criterion.

If a required solver capability is unavailable, record the limitation and use justified conservative submodels or accessible laboratory evidence. Do not report nonlinear/contact/fatigue validation that was never performed.

### 10.4 Full-scale manufacturing concept

LPBF AlSi10Mg remains a candidate for selected complex nodes. Use the chosen supplier's machine/material/build-condition data, post-treatment route and inspection assumptions. EOS's aluminium material information illustrates why a generic alloy name is insufficient to select finished-part properties. [EOS aluminium materials](https://www.eos.info/metal-solutions/metal-materials/aluminium)

Before approving a node, obtain an orientation/support review covering heat flow, distortion, recoater clearance, powder removal, support access and build-plate separation. Then define machining datums, fixture lands and accessible cutters for pads, bores and mounting faces.

Show machining stock explicitly: extra material on an outside surface; smaller-than-finished holes where boring stock is required. Retire the ambiguous “oversize every bore by 1.2 mm.” Minimum walls, overhangs and drain holes follow the actual process rather than inherited universal constants.

Use a finite fatigue-life objective after duty definition. Evaluate stress range, mean stress, notches, surface condition and process defects. No infinite-life or zero-wear conclusion follows from a static stress plot.

### 10.5 Scaled physical demonstrator

Maintain a separate demonstrator configuration and load label. A nominal 1:2 scale is a starting option only after checking printer volume and purchased hardware. Screws, bearings, clamps and layer heights are selected for that model; they need not scale geometrically.

Use a polymer the available printer can reliably process. PLA/PETG can establish low-load geometry; PA-CF is optional when the printer and team can control it. Chopped fibre is not continuous reinforcement. Select orientation, walls and infill through slicing and representative joint trials, rather than defaulting every part to 100% infill.

The scaled model demonstrates assembly, exchange sequence, restricted-load retention and conveyor motion. It does not establish full-scale stiffness, impact response, fatigue life or 250 kg capability. Do not derive an industrial load rating by a geometric scale multiplier.

## 11. Minimum controls and fault behaviour

Use a small deterministic controller for the demonstrator. Selection of a module profile does not measure actual cargo or CG. Enforce a documented loading procedure and known demonstrator load; reject absent, unknown or inconsistent module identity.

| State | Permitted behaviour | Transition requirement |
|---|---|---|
| Absent / partly seated | No base travel or conveyor motion | Verified seating, support setting and retention |
| Retained, power isolated | Mechanical support established; safe utility connection | Connector latched, known module, inspection complete |
| Ready for travel | Cargo fully contained; restraints closed | Station clear and deliberate enable |
| Transfer ready | Base immobilized, station aligned | Correct receiving face, station ready, no incompatible command |
| Transferring | Only coordinated conveyor motion | End-state detection; cargo no longer bridging gap |
| Exchange | Base immobilized, cargo absent, power isolated, trolley engaged | Mechanical sequence completed |
| Fault / power restoration | Motion inhibited; module remains mechanically retained | Cause resolved and deliberate restart |

Check each clamp/keeper locally; a single lever-position switch cannot establish all four stations. Ordinary switches and GPIO may demonstrate logic in a supervised model but do not constitute a validated industrial safety system. Specify actual stop outputs and prevent automatic restart. Guards, cargo restraints and controlled test boundaries remain necessary independently of software.

Manual connectors need actual voltage/current, mating-life, keying, strain relief and fuse specifications. Connect/disconnect while isolated. Include inrush and converter limits for a future battery-powered version. Do not claim IP65 or certified STO from enclosure shape or a relay label.

## 12. Verification gates and stop conditions

**Current status of every gate: open.** Document review and calculations here prepare the work; they do not release hardware.

| Gate | Owner role | Deliverable and pass condition | Stop / revise if… |
|---|---|---|---|
| G0 — Requirements and access | Integration lead + faculty/SPOC | Official brief captured; scope clarified; required Fusion workflow and share-link access demonstrated | Eligibility, originality or essential software access remains unresolved |
| G1 — Configuration and packaging | Part A + Part B leads | One parameter sheet; full envelopes; no collision during clamp, trolley, battery and wheel motions | Nominal components fit only by omitting hardware or service access |
| G2 — Loads and ground support | Analysis lead + mechanical mentor | Independently checked equilibrium, mass/CG ledger, wheel-load/stability results | Traction or restoring margins fail under the declared envelope |
| G3 — Interface specimen | Interface lead | A/B/C/D section/tolerances; repeatable seating; retention and support-setting trials | D adjustment lifts primary pads, a clamp conceals mis-seating, or trolley support is inadequate |
| G4 — Structure and comparison | Analysis + CAD leads | Global/local studies, joint checks and same-boundary baseline comparison | Result depends on unrealistic supports or proposed complexity has no useful benefit |
| G5 — Manufacturing feasibility | Manufacturing lead | Sliced demonstrator parts, machine reservation, finishing plan and quotes for critical external work | Parts cannot be printed, finished or inspected in the real window |
| G6 — Stationary workability | Part B + controls leads | Restrained low-load exchange, powered tote transfer and fault checks | Cargo escapes, bridges unreliably, binds, or motion can start with incomplete retention |
| G7 — Optional low-speed mobility | Controls lead + competent test supervisor | Contained unloaded trials, then approved incremental loads; documented stop and retention behaviour | First meaningful test would be an uncontrolled full-load run |
| G8 — Capacity / endurance development | Faculty/industry engineering support | Full-scale hardware and fixtures; process-appropriate strength/endurance evidence | Team has only a scaled polymer model or an uncorrelated FEA plot |

### 12.1 First physical test campaign

Build the mating-interface specimen before buying the full robot. Start with geometry and hand-actuated motion, then progress to restrained forces using a documented fixture and agreed loads.

- Run 30 clean exchange cycles as an initial repeatability study; measure multiple fiducials sufficient to estimate translation and rotation, clamp sequence, D adjustment and operator variation.
- Introduce controlled misalignment and non-abrasive contamination only within the protected specimen protocol; document contact/debris size and whether the mechanism rejects incomplete seating.
- Deliberately leave one clamp unretained; verify motion inhibition. Test disconnected identity/seat inputs and power restoration.
- Apply independently bounded compression, shear and uplift to the representative metallic joint/interface specimen; inspect permanent set, slip and seating changes.
- Perform loaded conveyor entry/exit trials at restricted speed with rated restraint and a representative station before mobile trials.

These tests expose mechanisms; 30 exchanges are not an endurance qualification. Do not invent a 10,000-cycle life claim from them. The specimen's force limits must reflect its actual material and fixture, not the full-scale load table.

## 13. Execution plan for tomorrow and subsequent development

### 13.1 Before the updated university submission

The priority is a coherent and honest proposal supported by the work the team can actually complete. Do not fabricate results to fill an evidence gap.

| Order | Work | Completion evidence |
|---|---|---|
| 1 | Confirm the official brief, required link, originality rule and submission form | Team-held requirement checklist and organizer clarification where needed |
| 2 | Approve v2 scope and the single parameter table | Agreement that 250 kg means total top-load target and Part B cargo target is 50 kg |
| 3 | Create/update the original Fusion packaging model | Part A, conveyor, carrier, interface and service/handling envelopes visible |
| 4 | Produce an interface section and exchange sequence | Round/diamond location, A/B/C/D and trolley support are understandable |
| 5 | Recompute load cases and create the baseline study | Correct inputs and evidence status, even if the solve is still pending |
| 6 | Run an actual available Fusion study and print-preparation check if feasible | Real setup/result/slicer records; otherwise explicitly list them as next milestones |
| 7 | Remove unsupported submission claims | No achieved capacity, savings, lifetime, legal clearance or simulated result without evidence |
| 8 | Validate the actual submitted Fusion link and file contents | View access from an unauthenticated session and inclusion of both required parts |

If time is short, complete steps 1–5 and 7–8. A truthful “study planned” is stronger than an invented “validated.” This roadmap is not wording to copy into a submission governed by an AI-content prohibition.

### 13.2 Development after submission

The following are planning ranges, dependent on gate results and access; they are not SIH event rules.

| Stage | Planning range | Outcome |
|---|---|---|
| Configuration and bench geometry | First 2–3 working days | G0/G1; interface coupon CAD; actual printer/component information |
| Loads and interface experiment | Following 3–5 working days | G2/G3; identify whether manual four-support procedure is viable |
| Structural comparison and DfAM | Following 1–2 weeks, depending on Fusion and machining access | G4/G5; approved demonstrator design |
| Stationary demonstrator | After fabrication and component delivery | G6; exchange and transfer data |
| Optional mobility | Only after mechanical release | G7; restricted operating demonstration |
| Full-scale capacity and endurance | Separate programme with qualified facilities and supplier lead times | G8; evidence for any industrial performance claim |

### 13.3 Six-person responsibility split

1. **Integration and requirements:** Own parameters, source register, revision control and submission evidence.
2. **Part A CAD:** Own baseline/hybrid structure, packaging and service assembly.
3. **Interface and handling:** Own tolerance stack, clamps, fourth support and trolley cradle.
4. **Part B CAD:** Own conveyor, passive carrier and transfer station.
5. **Analysis and manufacturing:** Own free bodies, simulation setup, supplier data and slicing.
6. **Controls and verification:** Own deterministic state logic, data capture and test procedure.

Because the team is primarily CSE/IT, obtain a named mechanical faculty reviewer for joint sizing, ground support and loaded-test release. Student ownership of CAD and analysis remains essential; mentor review addresses a real competency gap rather than replacing the team's work.

## 14. Cost and value: establish a defensible comparison

No new price quotation is invented in this revision. The PPT's ₹5–6 lakh prototype estimate, ₹45–55 lakh commercial benchmark, fleet savings and gross margins are not retained as established results.

Request costs at three distinct boundaries:

| Boundary | Include |
|---|---|
| Chassis and base-side interface | All nodes/members/braces, joint hardware, supports, clamps, locators, finishing, inspection, assembly and rejected-part allowance |
| Complete demonstrator | Above plus scaled drive/control hardware if used, conveyor, handling fixture, station, guards and test equipment |
| Full-scale system concept | Full-size drives/brakes/battery/sensors, conveyor, exchange equipment, electrical integration, testing and service requirements |

For each line record quantity, revision, material/process, supplier/date, unit price, tax/freight, lead time and whether quoted or estimated. Break LPBF cost into build/support, post-treatment, removal, machining and inspection. A free university print still consumes time and should be identified as subsidized access.

Compare a bolted interface and v2 using the same module, operator, trolley and ready-to-operate definition. Compare structural mass and stiffness under identical loads. A complete robot's sales price cannot establish the savings from our chassis alone.

Existing MiR250 product information explicitly describes multiple top modules and applications, so generic “one base, multiple jobs” is not unique. It does not establish any particular competitor exchange time or that our manual mechanism is faster. [MiR250 manufacturer page](https://mobile-industrial-robots.com/products/robots/mir250)

For the target workflow, measure change frequency, task overlap and available base capacity. Annual time benefit can be estimated as `number_of_exchanges × measured_time_saved_per_exchange`, then reduced for added maintenance and recovery. One base cannot replace two simultaneous jobs. Proceed with the commercial exchange argument only where the observed workflow benefits.

**Evidence sought for differentiation:** A reproducible design that integrates module load transfer and service access, selective additive manufacture that improves a fair baseline, and a simpler exchange process whose complete time and repeatability are measured.

## 15. Audit-to-roadmap traceability: every finding receives a disposition

“Removed” below means the risky legacy requirement/claim is removed from v2. “Addressed” means a design response is defined. **Neither means the hardware has passed a test.** Gate references identify the evidence still required.

| Audit ID | v2 disposition and response | Closure dependency |
|---|---|---|
| F01 | Originality/AI-content boundary explicitly retained; team authors qualifying work (§2) | G0 |
| F02 | Native Part A/Part B project and public-link access check (§10, §13) | G0 |
| F03 | Scored mechanical/Fusion deliverables govern scope; unrelated features deferred (§2) | G0/G1 |
| F04 | One configuration, coordinate convention and mass ledger (§3) | G1 |
| F05 | 250 kg propagated as total top-load target; conveyor separately limited (§3, §8) | G2/G8 |
| F06 | Aluminium-specific geometry and studies replace CF-derived results (§4, §10) | G4 |
| F07 | Whole-interface loads resolved once; no fourfold duplication (§8) | G2 |
| F08 | Weight, inertia, preload and support reactions separated (§8) | G2 |
| F09 | O_G/O_I and all CG heights defined (§3, §8) | G1/G2 |
| F10 | Remote forces and equivalent moments are mutually exclusive representations (§8) | G2/G4 |
| F11 | Combined cases and module-specific domains replace six independent maxima (§8) | G2/G4 |
| F12 | Unsupported stiffness/sensor numerical claim removed (§1, §10) | New evidence before reuse |
| F13 | LiDAR floor strike removed as the asserted root industry problem (§2) | Sensor-specific study only if justified |
| F14 | Slower conveyor ramp and torque/resistance-based selection (§7) | G6 |
| F15 | Three initial pads plus controlled fourth support; no exact-constraint assembly claim (§5) | G3/G4 |
| F16 | Chamfer entry, cylindrical location and axial pads have separate contact roles (§5) | G3 |
| F17 | Independent clamps; individual adjustment, seating and force assessment (§5) | G3 |
| F18 | Custom wedge/friction-angle mechanism removed; positive secondary retention selected (§5) | G3 |
| F19 | Partial seating, exchange, faults and restart handled explicitly (§11) | G3/G6 |
| F20 | Uplift through backed keeper mounts; local retention path checked (§4–5) | G3/G4 |
| F21 | Replaceable wear parts, inspection and datum requalification; zero wear removed (§5) | G3/G8 |
| F22 | Approach/contact and contaminated-fit tests; precision tied to transfer budget (§5, §7) | G3/G6 |
| F23 | Captured lifting trolley and parking cradle included in system (§6) | G1/G3/G6 |
| F24 | Permanent base bracing around service opening; bare-base stiffness required (§4) | G4 |
| F25 | Central drive brackets and intervening side members included (§4) | G2/G4 |
| F26 | Positive rectangular joints, crush sleeves and restrained specimen tests (§4) | G3/G4 |
| F27 | Driven normal loads and traction assessed before motor selection (§9) | G2/G7 |
| F28 | Six-contact compliance/travel/sweep explicitly unresolved until model and test (§9) | G1/G2/G7 |
| F29 | Whole-vehicle active support polygon and combined CG used (§9) | G2/G7 |
| F30 | Unloaded, module-removed battery service with lifting support (§4) | G1/G2 |
| F31 | Curves, current, thermal limits and braking energy determine drives (§9) | G2/G7 |
| F32 | Flexure sensor bridge deferred; use simple rigid mounts pending need (§2) | Separate study if reintroduced |
| F33 | Eight rollers, 70 mm pitch and explicit outside span (§7) | G1 |
| F34 | Roller axes X and transfer ±Y fixed (§3, §7) | G1/G6 |
| F35 | Positive cargo restraints with transfer/power-loss sequence (§7, §11) | G6/G7 |
| F36 | Station, gap, floor/suspension and interface errors budgeted together (§7) | G6 |
| F37 | Minimum supporting rollers and tote-bottom geometry govern ratings (§7) | G4/G6 |
| F38 | Original load-bearing conveyor brackets and comparison included (§7, §10) | G4/G5 |
| F39 | Supplier-reviewed LPBF support/thermal plan; support-free claim removed (§10) | G5 |
| F40 | Supplier/process-specific material allowables (§10) | G4/G5 |
| F41 | Finite-duty fatigue assessment; static FoS not treated as life proof (§10) | G8 |
| F42 | Machining datums, fixture lands, stock convention and finishing quote (§10) | G5 |
| F43 | Thin-wall, insert, hole and joint local checks on finished geometry (§4, §10) | G4 |
| F44 | Separate polymer model configuration and test loads (§10) | G5/G6 |
| F45 | Scale demonstration explicitly separated from industrial capacity (§10) | G8 for full-scale rating |
| F46 | Printer/entitlement trial, actual slicing and lead-time gates (§10, §12) | G0/G5 |
| F47 | Blind-mate high-current block removed; isolated keyed connector selected (§11) | G6 |
| F48 | Actual pack voltage/BMS/current range required; capacity follows duty (§9) | G7 |
| F49 | Demonstrator stop logic separated from certified industrial safety functions (§11) | G6/G7; industrial validation later |
| F50 | Identity does not imply actual cargo/CG; unknown identity inhibits motion (§11) | G6 |
| F51 | Accessible guarded cable routes with actual connector envelopes (§4, §11) | G1/G6 |
| F52 | Minimal deterministic control sequence; no dependency on custom navigation (§11) | G6 |
| F53 | Restrained/static work precedes contained low-speed mobile tests (§12) | G3–G7 |
| F54 | No inherited FEA result; reproducible native study records required (§10) | G4 |
| F55 | Real support/contact states and stiffness sensitivity; bonding limitations stated (§10) | G4 |
| F56 | Mesh/reaction checks, functional deformation and actual excitation analysis (§10) | G4 |
| F57 | Old numbered bibliography not inherited; limited direct source register (§18) | G0; claim-by-claim evidence review |
| F58 | Absolute FTO/design-around/legal claims withdrawn (§1, §18) | Separate qualified review before commercialization |
| F59 | Existing modular products acknowledged; differentiation narrowed (§14) | Measured baseline comparison |
| F60 | Equal cost and mass boundaries, quotations and complete handling cost (§14) | G4/G5 |
| F61 | Task overlap, exchange frequency and utilization determine business relevance (§14) | Actual workflow data |
| F62 | Complete-base stability and ballast included in mass comparison (§9, §14) | G2/G4 |
| F63 | Interface precision allocated from station task requirements (§7) | G3/G6 |
| F64 | Fair conventional baseline can overturn printed-node selection (§4, §14) | G4 |
| F65 | Bounded interface plus independent passive-carrier concept; broader modules excluded (§2, §16) | G1/G4/G6 |

## 16. Interface release checklist for any additional module

The common grid is a starting point for compatibility. Release an additional attachment only when its record contains:

- Interface revision, mating dimensions, actual fit/tolerance inspection and keeper compatibility.
- Attachment tare, cargo limit, CG domain and moving-load states.
- Combined force/moment cases at O_I, with duration and duty assumptions.
- Frame/interface, wheel-load, stability and cargo-retention assessment.
- Physical clearance for travel, caster sweep, service, clamps and exchange equipment.
- Utility voltage/current, connector, control states and failure behaviour.
- Required transfer/operating precision and achieved measurement evidence.
- Handling points, empty-module exchange procedure and parking stability.

The passive carrier uses the same base locators, supports and clamps. Its mating structure must be independently dimensioned from this specification. A successful CAD mate proves geometric compatibility; physical exchange and load tests prove additional, separate properties. Towing modules, lifts and robot arms remain outside the first released family.

## 17. Conditions that must change the design

1. **Fourth-support setting is unreliable or slower than the benefit it creates:** Change support architecture or use captive bolted retention. Preserve honest interchangeability rather than promising fast exchange.
2. **Trolley cannot support the module throughout exchange:** Reposition lifting ledges, change cradle/envelope, or abandon the claimed exchange method before fabrication.
3. **Drive wheels unload or stability fails:** Change mass placement, suspension/contact geometry or operating domain. Increasing node thickness is not a solution to lost traction.
4. **Conventional baseline matches performance with materially less cost/effort:** Reduce printed scope to the justified junctions. The comparison must be allowed to falsify the preferred architecture.
5. **250 kg dominates effort and prevents a credible challenge deliverable:** Keep it only as an explicitly unvalidated future target, or lower it through a documented requirement change. No supplied requirement establishes it as mandatory.
6. **Station mismatch governs transfer failures:** Improve station alignment and cargo support before buying more precise interface hardware.
7. **Full-scale metal printing is unavailable:** Complete the original metal concept and its manufacturing analysis, then build the allowed scaled workability model. Do not describe it as a 250 kg physical prototype.
8. **No real workflow benefits from frequent changes:** Emphasize maintainable configurability and structural design; withdraw fleet-reduction economics.

**End-state sought:** An original, reviewable Fusion project; one practical functional attachment; an unchanged base accepting a second bounded attachment; a manufacturing plan backed by available processes; and measured workability evidence. Claims of industrial payload, speed, endurance or cost advantage follow the relevant evidence rather than preceding it.

## 18. Source register and limitations

### Supplied project documents

- **A:** `AMRX_AMR_Adversarial_Failure_Audit.md`, especially §§2–11, F01–F65. Source of audit IDs and the reported official requirements.
- **P:** `SIH26112_Final_Modular_AMR_SIH2026 (1).pptx`, slides 2–6 for architecture, materials, capacity and unsupported outcome claims.
- **R:** `modular-amr-technical-roadmap.md`, Parts 1–3 for inherited dimensions, mechanisms, calculations and conflicting design freezes.

### Direct primary-source checks, 11 September 2026

- [Autodesk — Specify manufacturing methods](https://help.autodesk.com/view/fusion360/ENU/?contextId=GD-SPECIFY-MFG-METHOD): Supports the existence of manufacturing-method constraints; not a guarantee of entitlement, successful solving or printability.
- [MiR — MiR250](https://mobile-industrial-robots.com/products/robots/mir250): Supports the existence of multiple applications/top modules on a common commercial base; not a quotation or quantified module-exchange benchmark.
- [MIT — Design of Constraints in Precision Systems](https://ocw.mit.edu/courses/2-75-precision-machine-design-fall-2001/962f560f763715a81e775af536b5e3f8_constraint_lecture_part_I.pdf): Supports independent-constraint and compliance principles; not a validation of the proposed adjustable support.
- [EOS — Aluminium materials](https://www.eos.info/metal-solutions/metal-materials/aluminium): Supports process/material-specific selection; no generic web strength has been adopted as an AMRX allowable.

The specific clamp catalogue route did not yield a usable primary datasheet in this review. No clamp rating or part number is therefore invented. No current official SIH page, full normative safety-standard text, complete patent claim review, supplier quotations, native CAD, solver outputs or physical test records were independently verified here. Such records remain explicit gate deliverables.

All v2 mechanism choices, provisional thresholds and operating assumptions are engineering proposals. The load examples are transparent first-principles calculations. This roadmap supersedes the old implementation plan without pretending to provide the physical evidence the old plan lacked.
