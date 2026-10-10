# Molecular-modeling viewers — on-box verification (2026-08-31)

| Program | Shortcut (.lnk) | Real exe path | Type | Notes |
|---|---|---|---|---|
| **Materials Studio 2024** | `C:\ProgramData\...\Programs\BIOVIA\Materials Studio 2024.lnk` | install dir `C:\Program Files (x86)\BIOVIA\Materials Studio 24.1` (`bin/` = 46 `.exe`) | Full molecular modeling | lnk→program version 24.1 (lnk raw bytes `...al 200...`). |
| **VESTA** | on-box | `C:\Users\effec\Downloads\VESTA-win64\VESTA-win64\VESTA.exe` (57.9 MB, real exe) | Crystal structure viewer (CIF/POSCAR) | Use for instant orientation visualization. |

## Workflow (no hallucination gate)

```
generate_aln_orientations.py  (72/500-atom AlN qe/md seeds, a=3.112/c=4.982/u=0.382)
        ↓ load the bundle files
Materials Studio 24.1 (Viewer64)  <-- open the .xyz/POSCAR/CIF, inspect geometry
   or  VESTA  <-- quick crystal/orientation check
        ↓ verify (physical correctness)
run QE pw.x / LAMMPS NEMD  <-- gate on real pseudopotentials
```

## GATE (why not execute yet)
- **QE `pw.x` → no-op wrapper**: QED_7-4/run_pw_x.py finds nothing on box.
- **N/Al PAW `.UPF` → 0 files** on box → vc-relax/imaginary-mode checks blocked.
- **XRD raw .csv** exists (0629/0709) → orientation registry / fraction table OK.
