# Final Exa comparison and recommendation correction — 2026-10-02

## Scope and evidence level

Four focused Exa searches requested five hits each. This is not 20 unique full-text studies, an exhaustive prior-art search, a patentability opinion, or a guarantee of novelty. Four primary URLs were fetched through Exa; existing local full texts were also used. Raw search/fetch output: `EXA_FINAL_RAW_20261002.json`. No new measured or calculated material property was generated.

| Reference | Checked contribution | Limitation | Adoption / recommendation consequence |
|---|---|---|---|
| Christopher Perez et al., **High Thermal Conductivity of Submicrometer Aluminum Nitride Thin Films Sputter-Deposited at Low Temperature**, ACS Nano 17, 21240–21250 (2023), DOI [10.1021/acsnano.3c05485](https://doi.org/10.1021/acsnano.3c05485) | Local full text: low-temperature reactive sputtering, structure, TDTR and defect/transport interpretation | DC growth and substrate/stage conditions differ from our RF Si(100) route. Figure 3 is not a gas-only controlled pair | Adopt structure–transport evidence chain; generic low-temperature growth is insufficient. Process-history pilot must independently reproduce an effect beyond uncertainty |
| Tarmo Nieminen, Tomi Koskinen, Vladimir Kornienko, Glenn Ross, Mervi Paulasto-Kröckel, **Thermal Boundary Conductance of Direct Bonded Aluminum Nitride to Silicon Interfaces**, ACS Applied Electronic Materials 6, 2413–2419 (2024), DOI [10.1021/acsaelm.4c00068](https://pmc.ncbi.nlm.nih.gov/articles/PMC11044587/) | Full text: separately designed deposited/bonded AlN–Si interface specimens, TDTR and interface characterization | AlN–Si bonding is not our Al–Al joining route. 300°C bonding followed by 600°C/24 h is not a 150°C total-budget recipe | Adopt target-interface sensitivity and process-history accounting; constrain nuisance interfaces before reporting G |
| Patrick E. Hopkins, Leslie M. Phinney, Justin R. Serrano, Thomas E. Beechem, **Effects of surface roughness and oxide layer on the thermal boundary conductance at aluminum/silicon interfaces**, Physical Review B 82, 085307 (2010), DOI [10.1103/PhysRevB.82.085307](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.82.085307) | Publisher abstract and figure captions: Al/Si surface roughness/oxide treatment affects TDTR boundary conductance | Does not validate our complete specimen or establish that every TDTR experiment needs bonding | Record Al/Si oxide, roughness and preparation; use reference specimens and sensitivity analysis for additional interface terms |
| Sarabjot Singh et al., **Predictive Simulations and Experimental Study of AlN Bonding for Better Thermal Dissipation in BSPDN**, IITC (2025), [IBM primary abstract](https://research.ibm.com/publications/predictive-simulations-and-experimental-study-of-aln-bonding-for-better-thermal-dissipation-in-bspdn) | Institutional abstract: geometry/power/film-thickness modeling and AlN integration test vehicles | Full-paper geometry, Cu connectivity and detailed controls not checked; DOI remains VERIFY_REQUIRED | A generic AlN-versus-oxide FEM comparison is not enough. Adopt realistic boundary conditions; use our measured film/interface inputs for predictions |
| Yun-long Qiu, Wen-jie Hu, Chang-ju Wu, Wei-fang Chen, **Heat transfer performance and scale effect of hot spots in embedded microchannel cooling system**, Journal of Zhejiang University (Engineering Science) 55(4), 665–674 (2021), DOI [10.3785/j.issn.1008-973X.2021.04.008](https://www.zjujournals.com/eng/EN/10.3785/j.issn.1008-973X.2021.04.008) | Primary abstract and Fig. 11 caption: hotspot size and location relative to embedded channels; Si–Si direct-bond test chip | Not a full replication or operating-lifetime audit. Received 2020, published 2021 | **Downgrade hotspot displacement as standalone novelty.** Build/reproduce a validated reference first; independent paper differentiation is still unproven |
| Hinterreiter et al., **Surface pretreated low-temperature aluminum–aluminum wafer bonding**, Microsystem Technologies, online 2017 / issue 2018, DOI [10.1007/s00542-017-3520-8](https://doi.org/10.1007/s00542-017-3520-8) | Prior local audit and Exa publisher result: pretreated Al-alloy wafer bonding at 150°C | Proprietary surface treatment, Al alloy, vacuum/pressure and later anneals; not a pure-Al ordinary-plasma recipe. Full author list/volume/pages: VERIFY_REQUIRED | Treat as enabling-process precedent, not a transferable recipe or independent novelty by itself |

## User correction: the purpose of Al–Al bonding

**USER_SPECIFIED / PROPOSED**, not a completed fabrication result: the intended AlN/Si TBC specimen needs single-crystal Si(100) above Al. Ordinary Si deposition is not an accepted route to that required wafer-quality crystalline layer. The proposed Al–Al joining route uses crystalline Si wafers instead. This replaces the earlier shorthand “operator requires a bonded specimen.” It does not establish a universal need for Al–Al bonding in TDTR.

Final stack order, residual Si thickness, wafer transfer/thinning method, transducer location, optical access, process order and accepted thermal budget are **UNKNOWN**. The diagram is a material/process-role diagram, not a qualified fabrication cross-section.

Target AlN/Si conductance G must be identifiable apart from film κ and any Al/Si or Al–Al contributions. For the same interface, area-normalized TBR R″ = 1/G; they are reciprocal descriptions, not two independent measurements. If individual terms cannot be separated, report effective stack resistance with its assumptions and uncertainty.

## Decision

Start with the existing RF AlN process-history pilot and the c-Si(100)-preserving thermal specimen design **conditional on measurement access**. Existing sample/log/XRD/calculation assets make this the shorter testable route, not an assured paper. Match final thickness and thermal history, independently repeat depositions, and accept a measured effect only beyond uncertainty. Expand to composition/cross-section/TEM and held-out model prediction only when justified. If the effect vanishes, retain process-control data; do not force a standalone novelty claim.

Backside microchannels remain an independent platform, but the current hotspot-location task is baseline reproduction/validation. Fabrication intake, sealing, pumping and measurements must be accepted before spending on integrated-device work. No new research topic was added by this correction.

## Evidence still required

- Accepted AlN/Si measurement stack and sensitivity/covariance analysis; reference specimens for nuisance interfaces.
- Actual accessible Al–Al preparation and bonding recipe, full thermal budget and wafer thinning route.
- Independent AlN run data, real thickness/roughness/composition, thermal uncertainties; no conductivity or TBC outcome exists in this update.
- DFT/BTE convergence and file provenance audit before quantitative reuse.
- IBM full paper, closest process-history prior art, and microchannel comparison details before standalone novelty claims.
- DRIE, bonding, flow-loop intake/quotes and leak/thermal validation before actual device integration.
- Patent claims/family/legal-status comparison and inventive-step evaluation before any patentability claim.
