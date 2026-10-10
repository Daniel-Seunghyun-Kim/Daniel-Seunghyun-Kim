# Al–Mo Direct Bonding Database v0.1

Status: 2026-08-27. Literature catalog and process-condition records are **separated**. One paper can generate many condition rows. Values not independently re-read from full text are tagged `Partial` or `Candidate`. Empty cells are `N/R`, never imputed.

## 0. Schema

### 0.1 Evidence_Class
- `D0`: same-metal direct interface (Al/Al or Mo/Mo) with no intentional interlayer at the bond plane.
- `D1`: same-metal system but Ti, Pd, AlN, Si amorphous layer, or other passivation/interlayer is present at or next to the bond plane.
- `S`: supporting surface chemistry, oxide, etch, or roughness paper. No bonding experiment.

### 0.2 Pretreatment_Category
`Dry` | `Wet` | `Mixed` | `None`

### 0.3 Bonding_Mode
`SAB` | `TCB` | `Diffusion` | `ADB` | `Plasma-direct` | `Pressure` | `None`

### 0.4 Problem_Code
`OX` reoxidation/native oxide · `RG` roughness/pitting · `RES` residue/contamination · `VD` void/particle · `HT` high thermal budget · `HP` high pressure/deformation · `RC` recrystallization/grain growth · `IL` interlayer/passivation residue · `TOP` topography/wafer bow · `CR` corrosion/overetch · `DATA` key metric unreported

### 0.5 Problem_Severity
`0` none observed · `1` controllable · `2` performance loss · `3` process limit/fail

### 0.6 Verification
`Verified` = full text or abstract with the cited number extracted in this build.
`Partial` = number taken from a secondary compilation and not re-read from full text.
`Candidate` = paper belongs in the catalog; quantitative row still incomplete.

---

## 1. Literature catalog (one row = one paper)

| DB_ID | Year | Short cite | Material | Pretreatment_Category | Bonding_Mode | Evidence_Class | Film_or_Bulk | DOI / source | Verification | BEOL_Relevance | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AL-D-01 | 1992 | Suga et al. | Al–Al | Dry | SAB | D0 | Bulk/film | 10.1016/0956-7151(92)90272-G | Partial | Low | RT Ar-FAB SAB; TEM atomic Al/Al |
| AL-D-02 | 1999 | Akatsu et al. | Al–Al | Dry | SAB | D0 | Bulk cube | 10.1023/A:1004661610307 | Partial | Low | RT, ~40 MPa, UHV; not wafer-scale |
| AL-D-03 | 2008 | Yun et al. | Al–Al | None | TCB | D0 | Film | 10.1109/MEMSYS.2008.4443780 | Partial | Mid | No active oxide removal; ~450 °C |
| AL-D-04 | 2009 | Çakmak et al. | Al–Al | None | TCB | D0 | Film | 10.1557/PROC-1222-DD04-02 | Partial | Mid | 400–550 °C, 60 kN, ~3.4 MPa |
| AL-D-05 | 2010 | Çakmak et al. | Al–Al | None | TCB | D0 | Film | 10.4071/2010DPC-THA34 | Candidate | Mid | Characterization follow-on |
| AL-D-06 | 2011 | Froemel et al. | Al–Al | None | TCB | D0 | Film | 10.1109/TRANSDUCERS.2011.5969495 | Candidate | Mid | Thin metal TCB |
| AL-D-07 | 2013 | Malik et al. | Al–Al | None | TCB | D0 | Film | 10.1109/TRANSDUCERS.2013.6626955 | Partial | Mid | 1 µm Al, Rq≈1.5 nm |
| AL-D-08 | 2014 | Malik et al. | Al–Al | None | TCB | D0 | Film | 10.1016/j.sna.2014.02.030 | Partial | Mid | MEMS sealing |
| AL-D-09 | 2015 | Malik et al. | Al–Al | None | TCB | D0 | Film | 10.1088/0960-1317/25/3/035025 | Verified | Mid | Abstract: 18–61 MPa; SiO2 underlayer effect |
| AL-D-10 | 2016 | Malik et al. | Al–Al | None | TCB | D0 | Film | 10.1063/1.4952709 | Partial | Mid | Interfacial TEM/EBSD |
| AL-D-11 | 2016 | Rebhan et al. | Al–Al | Dry | SAB/TCB | D0 | Film | 10.1149/07509.0015ECST | Verified | High | ComBond; 100 °C first wafer-level |
| AL-D-12 | 2018 | Hinterreiter et al. | Al–Al | Dry | SAB/TCB | D0 | Film | 10.1007/s00542-017-3520-8 | Verified | High | 150 °C, 1.9 MPa, oxide-free TEM |
| AL-D-12T | 2016 | Hinterreiter thesis | Al–Al | Dry | SAB/TCB | D0 | Film | JKU ePUB | Verified | High | Ex-situ plasma **fails** (roughen + extra oxide) |
| AL-D-13 | 2019 | Schulze et al. | Al–Al | Dry | SAB | D0 | Film | 10.1109/ECTC.2019.00040 | Partial | High | BEOL Al deposition + HV activation |
| AL-D-14 | 2019 | Wietstruck et al. | Al–Al | Dry | SAB | D0 | Film | 10.1109/ECTC.2019.00147 | Candidate | High | Sub-µm alignment |
| AL-D-15 | 2020 | Cheemalamarri et al. | Al–Al | Mixed | TCB | D1 | Film | 10.1088/2051-672X/abbb81 | Partial | High | Ultrathin Pd; not bare Al/Al |
| AL-D-16 | 2022 | Al Farisi et al. | Al–Al | None | TCB | D0 | Thick EP | 10.3390/mi13081221 | Partial | Low | Mechanical oxide fracture; local 250 MPa |
| AL-D-17 | 2022 | Hu et al. | Al–Al | Dry | Plasma-direct | D1 | Film | 10.1109/ECTC51906.2022.00060 | Partial | High | Ar/N2 → thin AlN-like layer |
| AL-D-18 | 2022 | Schulze et al. | Al–Al | Dry | SAB | D0 | Film | 10.1109/TCPMT.2022.3152348 | Partial | High | Ar plasma time × T × force |
| AL-D-19 | 2023 | Schulze et al. | Al–Al | Dry | SAB | D0 | Film | 10.1149/11201.0025ECST | Partial | High | No vacuum break; yield map |
| AL-D-20 | 2024 | Schulze et al. | Al–Al | Dry | SAB/TCB | D0 | Film | 10.1109/TCPMT.2024.3363236 | Partial | High | Collective D2W |
| AL-D-21 | 2024 | Braun et al. | Al–Al | None | TCB | D0 | Thick EP | 10.1109/ESTC60143.2024.10712092 | Candidate | Mid | Thick frames |
| AL-D-22 | 2024 | Diex et al. | Al–Al | Mixed | TCB | D1 | Film | 10.1109/SSI63222.2024.10740521 | Candidate | High | Passivated Al |
| AL-D-23 | 2024 | Cirulis et al. | Al–Al | Mixed | Hybrid | D1 | Film | 10.1109/ESTC60143.2024.10712121 | Candidate | High | Fine-pitch hybrid |
| AL-D-24 | 2025 | Hu et al. | Al–Al | Dry | Plasma-direct | D1 | Film | 10.1109/ICEPT67137.2025.11157112 | Partial | High | Plasma aging ~6 h |
| AL-D-25 | 2008 | Fan / Dragoi et al. | Al–Al | Dry | Plasma-direct | D0 | Film | 10.1016/j.mee.2008.01.036 | Candidate | High | O2-plasma assisted; ρc reported in secondary sources |
| AL-D-26 | 2022 | Li et al. | Al–Al | Dry | Diffusion | D0 | Foil/bulk | 10.1016/j.matchar.2022.111821 | Candidate | Low | Ar ion bombardment; not wafer-level |
| AL-W-01 | 2023 | Cheemalamarri et al. | Al–Al | Mixed | SAB/TCB | D1 | Film | N/R (ECTC/related) | Partial | High | NE14 solvent + Ar + Ti passivation |
| AL-W-02 | 2026 | Schulze et al. | Al–Al | Mixed | SAB | D0 | Film | 10.5162/iCCC2026/P43 | Verified | High | NH4F vs NH2OH after dry etch; C-SAM/AFM/XPS |
| AL-W-S1 | 2020 | Cheemalamarri Pd | Al–Al | Wet | TCB | S/D1 | Film | 10.1088/2051-672X/abbb81 | Partial | Mid | RCA/Piranha is pre-metallization, not bond-face |
| AL-W-S2 | patent | Hybrid Al metallization | Al–Al | Wet | Proposed | S | Film | Patent | Candidate | Mid | Nonaqueous NH4F/NH4HF2 |
| MO-D-H1 | 1960s | Historical gas-pressure Mo | Mo–Mo | None | Diffusion | D0 | Bulk | archival | Candidate | Low | ~1260–1427 °C |
| MO-D-01 | 1968 | Hashimoto & Tanuma | Mo–Mo | Wet/Mech | Diffusion | D0 | Bulk | 10.2207/qjjws1943.37.1345 | Partial | Low | Benzine + electropolish; HT |
| MO-D-02 | 1992 | Ohashi & Suga | Mo–Mo | Mech | Diffusion | D0 | Bulk SC | 10.2207/qjjws.10.53 | Partial | Low | Orientation-controlled |
| MO-D-03 | 2004 | Gnyusov et al. | Mo–Mo | None | Diffusion | D0 | Bulk | 10.1533/WINT.2004.3327 | Candidate | Low | Prior plastic deformation |
| MO-D-04 | 2008 | TZM + interlayers | Mo–Mo | None | Diffusion | D1 | Bulk alloy | 10.3139/146.101700 | Partial | Low | Ti/Ni/Mo/Ta IL |
| MO-D-05 | 2010 | Shimatsu & Uomoto | Mo–Mo | Dry | ADB | D0 | nm film | 10.1116/1.3437515 | Partial | High | Mo included among 14 metals; Mo-specific metrics N/R in open abstract |
| MO-D-06 | 2012 | Hao | Mo–Mo | None | Diffusion | D1 | Bulk | CNKI | Partial | Low | 5 µm Ti foil |
| MO-D-07 | 2017 | Denisov et al. | Mo–Mo | None | Diffusion | D1 | Bulk | 10.1080/09507116.2017.1295562 | Partial | Low | Mo/Ti/Mo HIP |
| MO-D-08 | 2019 | Al-Mashhadani | Mo–Mo | Mech | Diffusion | D0 | Bulk | TU Chemnitz diss. | Partial | Low | Surface + grain orientation DOE |
| MO-D-H2 | hist. | unsuccessful Mo–Mo | Mo–Mo | None | Diffusion | D0 | Bulk | secondary | Partial | Low | **Negative datapoint** |
| MO-D-H3 | hist. | Charles high-T Mo–Mo | Mo–Mo | None | Diffusion | D0 | Bulk | secondary | Partial | Low | 1650 °C success |
| MO-D-09 | 2024 | Duan et al. | Mo–Mo (in Si/Mo/Mo/Si) | Dry | SAB | D1 | nm film | 10.1007/s11665-023-XXXX / JMEP 2024 | Verified | High | Mo nano-interlayer; Mo/Mo diffusion after anneal. Not bare Mo wafer |
| MO-W-01 | 1968 | Hashimoto electropolish | Mo–Mo | Wet | Diffusion | D0 | Bulk | 10.2207/qjjws1943.37.1345 | Partial | Low | Wet is prep, bond is HT diffusion |
| MO-W-S1 | 2022 | Le et al. | Mo | Wet | None | S | Film | Wet Cleaning of Molybdenum for Nano Interconnects | Partial | High | HF / SC1 / formulated clean. **No bonding** |
| MO-W-S2 | 2023 | Pacco et al. | Mo | Wet | None | S | Film | 10.1116/6.0002404 | Partial | High | O3 oxidation + NH4OH dissolution. **No bonding** |
| MO-W-S3 | various | Mo electropolishing | Mo | Wet | None | S | Bulk | ASTM / literature | Candidate | Mid | Planarization candidate |
| MO-W-S4 | ASTM | B629 Mo preparation | Mo | Wet | None | S | Bulk | ASTM B629 | Candidate | Low | Standard, not wafer bond |
| MO-W-S5 | 2025 | isotropic Mo wet etch | Mo | Wet | None | S | Film | SciDirect 2025 | Candidate | Mid | H2O2 grain-dependent roughness risk |

**Inventory (this build)**
- Literature rows: 47
- Al D0 bonding papers: 22
- Al D1: 6
- Al wet/mixed bonding: 2 (AL-W-01, AL-W-02)
- Mo D0 bonding: 8 (mostly bulk HT)
- Mo wafer-level D0 with quantitative interface metrics: **0 fully Verified**
- Mo wet **bonding** papers: 1 historical (MO-W-01, HT bulk)
- Mo wet **surface** papers: 5 supporting
- Wafer-level Mo–Mo + wet oxide strip + quantitative bond: **0**

---

## 2. Process-condition records (one row = one experimental cell)

Field order matches the v0.1 schema. Only cells with a reported outcome or a clearly stated experimental setting are listed. Do not collapse T×P×t sweeps.

### 2.1 Al–Al Dry / None / Vacuum

| Rec_ID | DB_ID | Pretreatment_Category | Evidence_Class | Film_thickness_nm | Surface_Rq_nm | Plasma_Gas | Air_Break | Bond_T_C | Bond_Force_kN | Bond_Pressure_MPa | Bond_Time_min | Bond_Ambient | Post_Anneal | Bond_Strength_MPa | Bond_Yield_pct | Void_Fraction_pct | Interface_Result | Problem_Code | Problem_Severity | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AL-D-02-a | AL-D-02 | Dry | D0 | bulk cube | N/R | Ar-FAB | No | 25 | N/R | 40 | N/R | UHV | none | N/R (atomic contact) | N/R | N/R | TEM atomic Al/Al | HP,DATA | 2,1 | Partial |
| AL-D-03-a | AL-D-03 | None | D0 | ~2000 | N/R | none | Yes | 450 | 9/14/18 | N/R | N/R | N/R | none | R<1 Ω (electrical) | hermetic He leak ~1e-12 | N/R | oxide broken by T+P | HT,OX | 3,2 | Partial |
| AL-D-04-a | AL-D-04 | None | D0 | ~500 | N/R | none | Yes | 400 | 60 | 3.4 | N/R | N/R | none | adhesion low vs 500 °C | N/R | N/R | native oxide remains | HT,OX | 3,2 | Partial |
| AL-D-04-b | AL-D-04 | None | D0 | ~500 | N/R | none | Yes | 500–550 | 60 | 3.4 | N/R | N/R | none | adhesion ≈8–10 J/m2 | N/R | N/R | TCB success | HT,OX | 3,2 | Partial |
| AL-D-07-a | AL-D-07 | None | D0 | ~1000 | 1.5 | none | Yes | 400 | 18 or 36 | 34.3 or 68.6 | 60 | <1e-3 mbar | none | incomplete | N/R | high | oxide barrier | HT,HP,OX | 3,2,2 | Partial |
| AL-D-07-b | AL-D-07 | None | D0 | ~1000 | 1.5 | none | Yes | ≥450 | 18 or 36 | 34.3 or 68.6 | 60 | <1e-3 mbar | none | 20–50 | N/R | N/R | TCB | HT,HP,OX | 3,2,2 | Partial |
| AL-D-09-a | AL-D-09 | None | D0 | N/R | N/R | none | Yes | 400 | 60 | N/R | 15 | N/R | none | significantly lower | N/R | N/R | 15 min insufficient | HT,VD,DATA | 3,2,1 | Verified |
| AL-D-09-b | AL-D-09 | None | D0 | N/R | N/R | none | Yes | 400 | 60 | N/R | 30 | N/R | none | similar to 60 min | N/R | N/R | SiO2 underlayer helps vs Al/Si | HT | 3 | Verified |
| AL-D-09-c | AL-D-09 | None | D0 | N/R | N/R | none | Yes | 400 | 60 | N/R | 60 | N/R | none | in 18–61 range | N/R | N/R | cohesive Si fracture rises with T,F | HT | 3 | Verified |
| AL-D-09-d | AL-D-09 | None | D0 | N/R | N/R | none | Yes | 300–550 | 36 or 60 | N/R | 15/30/60 | N/R | none | mean 18–61 | N/R | N/R | strength ↑ with T and force | HT,HP,DATA | 3,2,2 | Verified |
| AL-D-10-a | AL-D-10 | None | D0 | N/R | N/R | none | Yes | 400 | 36 | N/R | 60 | N/R | none | N/R | voids | high | incomplete | VD,OX,HP | 2,2,2 | Partial |
| AL-D-10-b | AL-D-10 | None | D0 | N/R | N/R | none | Yes | 400 | 60 | N/R | 60 | N/R | none | N/R | 100 dicing | low | success | HT,HP | 3,2 | Partial |
| AL-D-10-c | AL-D-10 | None | D0 | N/R | N/R | none | Yes | 550 | 36 | N/R | 60 | N/R | none | N/R | 96 dicing | N/R | grain rotation | HT,RC | 3,2 | Partial |
| AL-D-11-a | AL-D-11 | Dry | D0 | N/R | N/R | Ar (ComBond) | No | 100 | 60 | N/R | N/R | HV cluster | none | tensile ≈23 | patterned ~100 | low | oxide-free atomic contact | DATA | 1 | Partial |
| AL-D-11-b | AL-D-11 | Dry | D0 | N/R | N/R | Ar (ComBond) | No | 150 | 60 | N/R | N/R | HV cluster | none | tensile ≈37 | blank bonded | low | oxide-free | DATA | 1 | Partial |
| AL-D-12-fail | AL-D-12 | None | D0 | 300 | 1.2 | none | Yes | 550 | 60 | 1.9 | N/R | N/R | none | fail | unbonded | high | native oxide 3–4 nm intact; Ti droplets | OX,HT,HP | 3,3,3 | Verified |
| AL-D-12-a | AL-D-12 | Dry | D0 | 300 | 1.2 | Ar sputter (proprietary) | No | 150 | 60 | 1.9 | 90 | HV cluster | none | ALPS > SWD (DCB crack 5–10% shorter) | C-SAM mostly bonded | particle voids | TEM: no amorphous oxide; EDX no O pile-up | VD | 1 | Verified |
| AL-D-12-b | AL-D-12 | Dry | D0 | 300 | 1.2 | Ar sputter | No | 150 | 60 | 1.9 | 90 | HV | 250 °C / 1 h | N/R | small voids shrink | ↓ | void closure by Al self-diffusion | VD | 1 | Verified |
| AL-D-12-c | AL-D-12 | Dry | D0 | 300 | 1.2 | Ar sputter | No | 150 | 60 | 1.9 | 90 | HV | 350 °C / 1 h | N/R | weak-bond area ~×0.5 vs as-bonded | ↓ | particle voids remain | VD | 1 | Verified |
| AL-D-12T-pl | AL-D-12T | Dry | D0 | 300 | ↑ after plasma | ex-situ plasma | Yes | N/A | N/A | N/A | N/A | air | none | not bonded in this path | N/A | N/A | XPS: extra oxidation + AFM roughening | OX,RG | 3,3 | Verified |
| AL-D-13-a | AL-D-13 | Dry | D0 | N/R | <2 | HV activation | No | 300–500 | 60 | N/R | 60 | HV | none | 20×20 µm <50 mΩ | N/R | N/R | RG and OX sensitive | RG,OX,HT | 2,2,2 | Partial |
| AL-D-16-a | AL-D-16 | None | D0 | ~8000 EP | grooved | none | Yes | 150 | N/R | local 250 | 40 | vacuum | none | fail | N/R | N/R | oxide not fractured | HP,OX | 3,3 | Partial |
| AL-D-16-b | AL-D-16 | None | D0 | ~8000 EP | grooved | none | Yes | 250 | N/R | local 250 | 40 | vacuum | none | 11–16 | N/R | N/R | mechanical oxide rupture | HP | 3 | Partial |
| AL-D-17-a | AL-D-17 | Dry | D1 | N/R | N/R | Ar/N2 ~10 s | Yes? | RT contact + 300 anneal | 0.05 kN (50 N) | ~0.2 MPa (2000 mbar) | N/R | N/R | 300 °C | ≈32 | N/R | N/R | AlN-like activated layer | IL | 1–2 | Partial |
| AL-D-18-a | AL-D-18 | Dry | D0 | N/R | N/R | Ar 2.5–5 min | No? | 250 | 20–40 | N/R | N/R | N/R | none | N/R | >85 | N/R | mΩ contacts | RES,RG,TOP | 2 | Partial |
| AL-D-19-a | AL-D-19 | Dry | D0 | N/R | N/R | Ar 5 min | No | 300 | 60 | N/R | 60 | HV | none | N/R | >95 | N/R | optimum of reported sweep | TOP,RG | 1–2 | Partial |
| AL-D-20-a | AL-D-20 | Dry | D0 | N/R | N/R | Ar ComBond | No | 300 | N/R | 52–60 | 60 | HV | none | >90 | >90 | N/R | D2W topography limited | HP,TOP | 2,2 | Partial |
| AL-D-24-a | AL-D-24 | Dry | D1 | N/R | N/R | Ar/N2 | Yes (aging) | 300 anneal | N/R | N/R | N/R | ambient delay | 300 °C | N/R | usable ≤6 h | N/R | activated-state lifetime | OX | 1–2 | Partial |

Deposition metadata (Hinterreiter, verified): 200 mm Si / 20 nm Ti / 300 nm Al-0.5Cu. SWD: 215 °C, Ar 3.3×10⁻³ mbar. ALPS: 30 °C, Ar 5.33×10⁻⁵ mbar. Native Al2O3 3–4 nm. ComBond Al2O3 sputter rate up to 15 nm min⁻¹ on ALD test films.

### 2.2 Al–Al Wet / Mixed

| Rec_ID | DB_ID | Cleaning_Chemistry | Pretreat_T_C | Pretreat_Time | Subsequent_Dry | Bond_T_C | Bond_Force_kN | Result | Surface_after_wet | Problem_Code | Problem_Severity | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AL-W-01-a | AL-W-01 | NE14 solvent, post dry-etch | N/R | N/R | Ar 30 s + Ti 2–4 nm | blanket ≤300; patterned ≤350 | patterned ≥1 MPa | fine-pitch continuity | delay → Cl pits | CR,RES,IL | 3,2,2 | Partial |
| AL-W-02A | AL-W-02 | none (post dry-etch only) | — | — | Ar ~3.5 min | 300 | 60 | many weak-bonded areas | etch residue | RES | 3 | Verified |
| AL-W-02B | AL-W-02 | NH4F + ethylene glycol (NOE) | 35 | 2 min 20 s | Ar same | 300 | 60 | unbonded area ↓ vs 02A | Ra≈5.1 nm, Rz≈45.8 nm; F, pits | RG,CR | 2,2 | Partial |
| AL-W-02C | AL-W-02 | NH2OH + IPA (ACT935) | 80 | 20 min | Ar same | 300 | 60 | **best C-SAM** | Ra≈4.6 nm, Rz≈34.2 nm | RG | 1 | Verified (best clean); AFM numbers Partial |
| AL-W-02D | AL-W-02 | ACT935 | 80 | 40 min | Ar same | 300 | 60 | worse than 20 min | edge ring; Rz≈51.6 nm | RG,CR | 2 | Partial |

Bond-quality model (do not reduce to Ra only):

`Bond quality = f(residue removal, Rq, Rz, pitting, F/Cl, reoxidation, air-break)`

AL-W-02: 20 min NH2OH is best because it removes etch residue without destroying Al topography. 40 min over-cleans. Lowest Ra is **not** the best bond.

### 2.3 Mo–Mo Dry / Diffusion / ADB

| Rec_ID | DB_ID | Evidence_Class | Film_or_Bulk | Surface | Bond_T_C | Bond_Pressure_MPa | Bond_Time_min | Bond_Ambient | Result | Problem_Code | Problem_Severity | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MO-D-H1-a | MO-D-H1 | D0 | Bulk | various finish | 1260–1427 | 68.9 | 180 | gas pressure | self-bond | HT,RC | 3,3 | Candidate |
| MO-D-01-a | MO-D-01 | D0 | Bulk 1 mm | emery + benzine; some EP | ~900 | deformation 5–10% | N/R | N/R | local bonding starts | HT | 3 | Partial |
| MO-D-01-b | MO-D-01 | D0 | Bulk | same | ~1100 | 5–10% def. | N/R | N/R | strength rises sharply | HT | 3 | Partial |
| MO-D-01-c | MO-D-01 | D0 | Bulk | same | 1250 | 5–10% def. | 5 | N/R | grains cross interface | RC | 3 | Partial |
| MO-D-01-d | MO-D-01 | D0 | Bulk | same | >1200 | N/R | N/R | N/R | recrystallization embrittlement | RC | 3 | Partial |
| MO-D-02-a | MO-D-02 | D0 | SC (025)/(121) | #600 polish | 1400–1800 | 10 → 1.3 | 15 | vacuum | base-metal strength if twist ≲10° | HT | 3 | Partial |
| MO-D-05-a | MO-D-05 | D0 | nm film | sputter, vacuum contact | 25 | contact | N/R | vacuum | 14-metal RT ADB survey | DATA | 2 | Partial |
| MO-D-06-a | MO-D-06 | D1 | Bulk | Ti 5 µm foil | 1000 | 10 | 60 | vacuum | 100% interface bonding rate | IL | 2 | Partial |
| MO-D-H2-a | MO-D-H2 | D0 | Bulk | N/R | 1200 | 40 | 20 | N/R | **FAIL** | HT,DATA | 3,1 | Partial |
| MO-D-H3-a | MO-D-H3 | D0 | Bulk | N/R | 1650 | 0.03447 | 60 | ~0.13 Pa | original interface disappears | HT | 3 | Partial |
| MO-D-09-a | MO-D-09 | D1 | Mo 9.88 nm | Ar SAB, RT | 25 + anneal 100 | N/R | N/R | vacuum anneal | voids present | VD | 2 | Verified |
| MO-D-09-b | MO-D-09 | D1 | Mo 9.88 nm | Ar SAB, RT | 25 + anneal 300 | N/R | N/R | vacuum | void area → 0; strength 6.57 MPa | none at 300 °C | 0 | Verified |
| MO-D-09-c | MO-D-09 | D1 | Mo 9.88 nm | Ar SAB, RT | 25 + anneal 500 | N/R | N/R | vacuum | void still 0; partial crystallization | RC | 1 | Verified |

MO-D-09 stack (verified): amorphous Si 2.54 nm / Mo 9.88 nm / amorphous Si 3.79 nm. This is **Si–Si SAB with Mo nano-interlayer**, not a Mo-wafer D0 experiment. Keep as D1. Useful because MD and TEM show Mo/Mo atomic diffusion during 300–500 °C anneal.

MO-D-H2 vs MO-D-H3: 1200 °C / 40 MPa / 20 min fails, while 1650 °C / 34.5 kPa / 60 min succeeds. Pressure-up models are insufficient; homologous temperature and recrystallization kinetics dominate bulk Mo.

### 2.4 Mo wet / supporting chemistry (no wafer-level Mo–Mo bond)

| Rec_ID | DB_ID | Cleaning_Chemistry | Pretreat_T_C | Pretreat_Time | Surface reaction | Rq outcome | Bonding experiment? | Problem_Code | Problem_Severity | Evaluation for later bond | Verification |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MO-W-01-a | MO-W-01 | benzine after emery | RT | N/R | organics off | N/R | Yes, but HT diffusion | OX | 2 | oxide not stripped | Partial |
| MO-W-01-b | MO-W-01 | electropolish | N/R | N/R | planarize | N/R | Yes, 1100 °C; no clear strength gain vs other polish | DATA | 1 | not a low-T enabler | Partial |
| MO-W-S1-a | MO-W-S1 | 0.05% HF ~1 min | RT | ~1 | Mo compatible | N/R | No | OX | 2 | weak MoOx removal | Partial |
| MO-W-S1-b | MO-W-S1 | SC1 (NH4OH/H2O2) | N/R | N/R | high Mo etch | roughness risk | No | RG,CR | 3 | unsuitable as-is | Partial |
| MO-W-S1-c | MO-W-S1 | FOTOPUR R-2403 semi-aqueous alkaline | N/R | N/R | residue + Mo oxide ↓ | N/R | No | OX | 1 | **promising**; needs vacuum transfer | Partial |
| MO-W-S2-a | MO-W-S2 | O3 ox <~230 °C + wet dissolution | <230 | N/R | amorphous MoO3 selective strip | can smooth | No | none if controlled | 1 | **promising** | Partial |
| MO-W-S2-b | MO-W-S2 | O3 ≥250 °C + dilute NH4OH | ≥250 | N/R | crystalline MoO3 residual | roughness ↑ | No | RG,OX | 2–3 | avoid | Partial |
| MO-W-S2-c | MO-W-S2 | conc. NH4OH 70 °C | 70 | N/R | crystalline MoO3 can dissolve | N/R | No | CR | 1 | window needs DOE | Partial |
| MO-W-S2-d | MO-W-S2 | O3 290 °C + optimized hot NH4OH | 290 / 70 | N/R | oxide strip + smoothen | Rq ≈ 0.38 nm reported in secondary cites | No | DATA | 1 | **best supporting claim**; not bonded | Partial |
| MO-W-S5-a | MO-W-S5 | aqueous H2O2 | RT | N/R | ox+dissolve, grain-dependent | anisotropic roughening | No | RG | 3 | not for bonding face | Candidate |

**Correct research gap (do not write “Mo wet is unsuitable”):**

Wet chemistries that remove MoOx while recovering Rq ≲ 0.5 nm **exist** (formulated cleans; controlled O3 + NH4OH). What does **not** exist is a wafer-level D0 dataset:

`Wet oxide removal → Rq/Rz/XPS → no air-break or timed transfer → Mo/Mo bond → C-SAM/TEM/ρc/TBR`

---

## 3. Problem-occurrence table (ML/DOE ready)

| Material | Condition | Outcome | Cause | Code | Severity |
|---|---|---|---|---|---|
| Al | native oxide kept, T=400 °C, moderate P | incomplete | Al2O3 diffusion barrier | OX | 3 |
| Al | conventional TCB ≥450–550 °C | bond improves | plasticity + diffusion | HT | 3 |
| Al | 1.9 MPa, no oxide removal, even 550 °C | fail (Hinterreiter) | oxide intact | OX | 3 |
| Al | ComBond oxide removal + 150 °C / 1.9 MPa | success | metallic contact, no air-break | VD | 1 |
| Al | ex-situ plasma then air | worse surface | extra oxide + roughen | OX,RG | 3 |
| Al | high local pressure / grooves | bond at 250 °C | mechanical oxide fracture | HP | 3 |
| Al | no post-etch wet clean | weak SAB | polymer/halogen residue | RES | 3 |
| Al | delayed Cl-etch clean | pits | Cl corrosion | CR | 3 |
| Al | ACT935 20 min then Ar SAB | best mixed route | residue off, Rz controlled | RG | 1 |
| Al | ACT935 40 min | worse bond | over-clean, Rz/edge | RG | 2 |
| Al | Ar/N2 plasma | low-T bond via AlN-like skin | residual IL | IL | 1–2 |
| Al | plasma-activated, air delay >6 h | aging | reoxidation/adsorbate | OX | 2 |
| Mo | bulk T below diffusion threshold | nonbond | low diffusivity | HT | 3 |
| Mo | bulk >1200 °C long dwell | embrittlement | recrystallization | RC | 3 |
| Mo | 1200 °C / 40 MPa / 20 min | fail | kinetics not met | HT | 3 |
| Mo | 1650 °C / 34.5 kPa / 60 min | success | T dominates P | HT | 3 |
| Mo | grain misorientation | strength drop | interface crystallography | RC | 2–3 |
| Mo | SC1/H2O2 | roughen | oxidation-dissolution | RG,CR | 3 |
| Mo | 0.05% HF | oxide remains | weak MoOx etch | OX | 2 |
| Mo | semi-aqueous formulated clean | oxide/residue ↓ | controlled dissolution | OX | 1 |
| Mo | O3 + hot NH4OH optimized | smooth + strip | selective MoO3 dissolution | OX | 1 |
| Mo | wet then air | reoxidation | MoOx regrowth | OX | 2–3 |
| Mo | Shimatsu ADB including Mo | RT contact claimed | Mo-specific TEM/strength N/R | DATA | 2 |
| Mo | Si/Mo/Mo/Si SAB + 300 °C anneal | void-free, 6.57 MPa | nano-Mo, not bulk | IL | 1 |

---

## 4. Process-window sketch (do not treat as fitted model)

Al, oxide **kept**:
- T ≳ 450 °C and P typically tens of MPa on frames; full-area 1.9 MPa is not enough.
- Homologous T at 450 °C ≈ 0.78 Tm(Al). Plasticity breaks Al2O3.

Al, in-situ dry oxide **removed**, no air-break:
- T window 100–300 °C; P can drop to ~2 MPa on 200 mm full area.
- New limiters: Rq, particles, pad topography, activation recipe, vacuum integrity.

Al, wet:
- Wet is a **residue/Rz controller**, not a proven standalone oxide-strip-to-bond path.
- Over-clean (time) is as bad as under-clean.

Mo bulk:
- Practical diffusion bonding ≳ 1100–1650 °C. BEOL-incompatible.
- Recrystallization above ~1200 °C is a hard ceiling for ductility.

Mo thin film:
- RT SAB/ADB is physically plausible (high surface energy, nanocrystalline) but **D0 wafer metrics are missing**.
- Best quantitative proxy: Duan D1, 300 °C post-anneal, void → 0.

Mo wet:
- Chemistry window exists. Bonding window does not.

---

## 5. DOE v0.1 for sputtered Mo films (same lot)

Fixed: sputtered Mo on Si or AlN, target Rq < 0.5 nm if CMP available; record as-deposited Rq/Rz/XPS. Thermal budget 250 / 300 / 350 °C to stay near CMOS/BEOL and AlN/AlScN process limits.

| Group | Wet | Dry | Air_Break | Question |
|---|---|---|---|---|
| M0 | none | none | Yes | baseline native MoOx |
| M1 | none | Ar SAB | No | dry-only SAB |
| M2 | 0.05% HF | none | timed | HF-only oxide strip |
| M3 | formulated Mo oxide clean | none | timed | wet-only feasibility |
| M4 | 0.05% HF | Ar | No | wet+dry synergy |
| M5 | semi-aqueous residue/oxide clean | Ar | No | hybrid candidate |
| M6 | controlled O3 + hot NH4OH | Ar | No | sub-nm smooth + SAB |

Responses (not binary bond/fail):

`Rq, Rz, O/Mo XPS, t_MoOx, f_void (C-SAM), Gc or τ, ρc (TLM/4PP), TBR (TDTR if available)`

Negative and Partial rows stay in the DB. Do not drop MO-D-H2 or Shimatsu DATA flags.

---

## 6. Expansion log (next 30–50 papers → 100+ records)

Priority full-text pulls:
1. Malik 2015/2016 tables: explode every T×F×t×underlayer cell that was actually run.
2. Schulze 2018–2024 IHP series: Ar time × T × kN yield maps.
3. Rebhan 2016 full ECS paper: 100 °C pull-test raw values.
4. Fan/Dragoi 2008: confirm ρc = 2.6×10⁻⁸ Ω·cm² and plasma gas.
5. Shimatsu 2010: extract Mo row from the 14-metal table if it exists.
6. Al-Mashhadani 2019 dissertation tables.
7. Le 2022 and Pacco 2023: numeric etch rates, XPS O 1s, Rq before/after.
8. Do **not** recode Si/Mo/Au or Mo interlayer Si–Si as D0.

Stop rule: if a paper has no Al/Al or Mo/Mo bond plane and no quantitative Mo/Al surface metric usable as a regressor, keep it out of process-condition DB.
