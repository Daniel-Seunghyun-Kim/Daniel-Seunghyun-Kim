# Al target nitridation and process history proposal

2026-10-02. Status: **PROPOSED, conditional supporting research; standalone novelty UNKNOWN**. No solver was run and no growth sequence was generated. Existing thermal-transport calculations remain unchanged.

## Recommendation

Include a separate four-slide proposal because target history can help interpret existing short/long pre-sputtering experiments. Keep the AlN/Si thermal-resistance measurement chain as the main research priority. Begin with a calibrated time-dependent nitridation/erosion model; add local atomistic calculations only when a particular reaction or impact question cannot be resolved by the simpler model.

Working question: under matched final deposition conditions, does the initial target state produce a reproducible transient that predicts an independent film response after thickness, substrate heating, oxygen and chamber conditioning are controlled?

This is a proposed test, not an established gap. Generic short/long poisoning, texture changes and MD/ML surface simulations already have close prior art.

## Correct the physical assumptions

- Al is fcc; Al(111) denotes an oriented surface. A strong diffraction peak alone does not make a full commercial target a single crystal. Use manufacturer information and appropriate XRD/EBSD to qualify an idealized local facet model.
- AlN(002), usually expressed as wurtzite (0002), is a diffraction-plane label. Surface cut (0001), c-axis [0001] and diffraction (0002) must not be interchanged. N uptake or an Al–N XPS signal does not establish an oriented crystalline AlN layer.
- Nitridation, implantation, Ar-induced erosion, mixing, oxide removal and heating compete. Do not prescribe a perfect AlN(0002) layer and present its appearance as a predicted outcome.
- The target and deposited film are different surfaces. A target-state result does not by itself establish substrate-film texture or conductivity.
- Target diameter/thickness/racetrack belong in macroscopic geometry and spatial flux models. An atomistic Al(111) patch represents local surface chemistry; an entire engineering target is not a sensible initial all-atom model.
- RF power and gas flow alone do not specify ion/radical fluxes, energy/angle distributions or surface temperature. Ordinary neutral-flow CFD cannot independently supply chemical growth and crystal orientation.

**First protocol check:** distinguish existing Ar-only pre-cleaning/de-poisoning from N2/Ar conditioning. The proposed mixed-plasma model does not establish the gas ambient of prior short/long pre-sputtering runs. A shorter pre-sputter is not automatically less target nitridation. Record shutter state and initial target condition as well.

## Useful hierarchy

| Stage | Inputs and method | Defensible output | Main limitation |
|---|---|---|---|
| Minimum transient model | Time-dependent gas balance and target coverage/erosion; actual RF/pressure/flow/rate/temperature logs | Conditional trends and validated process transients | Unknown rates and initial conditions may be non-identifiable; original steady-state Berg equations alone do not prove time evolution |
| Local DFT/NEB | Qualified Al facets, termination/oxide assumptions and selected N reactions | Reaction/adsorption/diffusion energetics | Not a direct RF-power-to-growth-time model |
| Reactive MD / collision model | Validated Al–N interactions, Ar impacts and short-range response; species energies and angles | Dose-dependent N incorporation, erosion, damage and local structure | Pure Al EAM is insufficient for Al–N chemistry; accelerated incident flux can alter relaxation |
| Time bridging | Independently calibrated flux and validated kinetic/accelerated method | Conditional time mapping | Dose is the time integral of flux; MD steps cannot simply be relabeled as experimental minutes |
| Film and thermal comparison | Matched thickness, independent depositions, temperature/oxygen checks, XRD/composition and measured thermal response | Whether process history predicts an independent film/thermal result | Correlation alone cannot prove target-state causality |

## Advantages and disadvantages

**Advantages:** directly connected to current pre-sputtering comparisons; useful for conditioning/repeatability even without a standalone paper; a small transient model can be tested before expensive atomistic training or plasma simulation; preserves a physical role for existing computational skills without confusing target chemistry with thermal BTE.

**Disadvantages:** close prior art; difficult access to the eroding target surface; interrupted analysis and air exposure can change the surface; uncertain plasma boundary conditions; strong scale/time mismatch; substantial potential-validation cost. A witness coupon samples arriving material and cannot substitute for target-surface crystallography.

No local instrument access, analysis quote or model runtime was newly validated. Obtain instrument-owner agreement before interrupted target removal/analysis. Do not promise an XPS/TEM result or a cost from an equipment list.

## Evidence and kill tests

1. Record available gas/pressure/RF response, deposition rate and substrate temperature through the transient; retain independent runs rather than many points from one run.
2. Establish target starting state and allowed surface-analysis route. A facet-specific claim remains a model assumption until texture is supported.
3. Fit only an identifiable minimum model. Predict a withheld history or conditioning cycle and compare its uncertainty with a simpler model.
4. Link matched-thickness films to composition/structure and real thermal measurements. Control substrate heating and oxygen before attributing differences to poisoning.
5. If the effect disappears under these controls, is explained by existing models or cannot be independently predicted, retain supporting process-control data and stop the standalone mechanistic claim.
6. Keep a prescribed growth animation labeled illustrative. Do not call it computed time evolution.

## Direct prior art checked

- **Muhammad Arif, Markus Sauer, Annette Foelske-Schmitz, Christoph Eisenmenger-Sittner (2017).** Characterization of aluminum and titanium nitride films prepared by reactive sputtering under different poisoning conditions of target. *Journal of Vacuum Science & Technology A* **35(6), 061507**. DOI [10.1116/1.4993082](https://doi.org/10.1116/1.4993082). [Author-hosted full PDF](https://static.ifp.tuwien.ac.at/homepages/Personen/duenne_schichten/pdf/J_Vac_Sci_Technol_A_35_6_2017.pdf). Abstract, experiment and Fig.5 checked: deposited-film composition/texture and substrate temperature differ with target history. It is not target-crystal imaging or proof for the current RF tool. Figure provenance: `agent_control/EXA_ARIF2017_FIGURE.md`.
- **Tobias Gergs, Thomas Mussenbrock, Jan Trieschmann (2023).** Physics-separating artificial neural networks for predicting sputtering and thin film deposition of AlN in Ar/N2 discharges on experimental timescales. *Journal of Physics D: Applied Physics* **56, 194001**. DOI [10.1088/1361-6463/acc07e](https://doi.org/10.1088/1361-6463/acc07e). [Primary author manuscript record](https://arxiv.org/abs/2301.03524). Abstract and DOI linkage checked: reactive MD, time-stamped force-bias Monte Carlo and ANN connect plasma–surface evolution to a specific reference case. Detailed model transferability and training-set reuse remain VERIFY_REQUIRED; no model was installed or run here.
- **S. Berg, E. Särhammar, T. Nyberg (2014).** Upgrading the “Berg-model” for reactive sputtering processes. *Thin Solid Films* **565, 186–192**. DOI [10.1016/j.tsf.2014.02.063](https://doi.org/10.1016/j.tsf.2014.02.063). Publisher abstract/excerpts checked: sputtering, implantation and knock-in extensions. General modeling precedent, not an RF-AlN transient calibration for our tool.

## Main slide 7 source verification

**Yun-long Qiu, Wen-jie Hu, Chang-ju Wu, Wei-fang Chen.** Heat transfer performance and scale effect of hot spots in embedded microchannel cooling system. *Journal of Zhejiang University (Engineering Science)* **55(4), 665–674 (2021)**. DOI [10.3785/j.issn.1008-973X.2021.04.008](https://www.zjujournals.com/eng/EN/10.3785/j.issn.1008-973X.2021.04.008).

The slide uses **Figure 11**, not Figure 7. The x-axis S1–S7 denotes SHS locations; the y-axis is temperature rise in K. The legend denotes chip1/chip2. Caption conditions: background heat flux 50 W/cm², SHS heat flux 870 W/cm². These are literature conditions, not our experiment. Received September2020; published May2021. The 2020 Sensors paper (DOI10.3390/s20195533) is a distinct reference and must not be substituted for this figure.

Publication record, primary abstract and Fig.11 caption rechecked on 2026-10-02. This confirms the source and prior hotspot-location work, not an independent replication of every result.
