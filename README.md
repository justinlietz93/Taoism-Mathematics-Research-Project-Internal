# Phase Calculus and Taoism Modern Mathematics Research

A collection of research artifacts exploring Phase Calculus and connections to Taoist texts and related mathematics. This repository bundles publications, reproducible research artifacts (TeX sources, notebooks, validation scripts), datasets, and supporting code used across the project's subprojects.

## Top Level Directories

 - [`Active-Study`/](/Active-Study/)
    - The live research, notes, and experiments in progress as part of this teams progress in determining what connection, if any, that Phase Calculus has to the math described in ancient Chinese and how modern science uses it to solve otherwise unwieldy or unsolvable problems.
 - [`CITATIONS/`](/CITATIONS/)
 - [`code/`](/code/)
    - Research software, simulations, datasets, and notebooks that support the project's publications. Notable items include `iching-wilhelm-dataset-master`, the Fortran `MFE_pub-main` code, and helper scripts such as `yinyang_transform.py`.
 - [`Modular-Forms/`](CITATIONS/External-Research.md) Collection of modular-forms resources and lecture materials (PDFs and notes), e.g., `MFLecture1.pdf` and `Zagier123ModularForms.pdf`.
 - [`Phase-Calculus/`](/Phase-Calculus/)
    - The main research collection — many subprojects and papers (CF000, CF00, CF13, CF19, Farey_Remainder_Recursion_and_Orthogonality, Loop_Generated_Projection_in_TDAHE, Monodromy_as_Memory, Unified_Quintic, etc.). Each subproject typically contains TeX sources, PDFs, notebooks, provenance manifests, and validation artifacts for reproducible research and publication.
 - [`Prospect-Leads/`](CITATIONS/External-Research.md) Miscellaneous leads and collected PDFs/datasets intended for future study and follow-up research.
 - [`Tao-Research/`](CITATIONS/External-Research.md) Local copies and scanned PDFs relating to Taoist texts, Yi Jing/I Ching translations, and related historical and technical materials used in the project.

---

## Directory layout

<details>
<summary>Expand directory tree (click to toggle)</summary>

```markdown
Phase-Calculus&Taoism-Math/
├── code/
│   ├── iching-wilhelm-dataset-master/
│   │   ├── create_data.ipynb
│   │   ├── data
│   │   ├── iching_wheel.jpg
│   │   ├── LICENSE
│   │   └── README.md
│   ├── MFE_pub-main/
│   │   ├── idlcodes
│   │   ├── LICENSE
│   │   ├── main.F
│   │   ├── ModBoundary.F
│   │   ├── ModBval.F
│   │   ├── ModConductivity.F
│   │   ├── ModControl.F
│   │   ├── ModDel.F
│   │   ├── ModField.F
│   │   ├── ModGetQtys.F
│   │   ├── ModGrid.F
│   │   ├── ModInitialization.F
│   │   ├── ModInterp.F
│   │   ├── ModIO.F
│   │   ├── ModIteration_sts.F
│   │   ├── ModPhysics.F
│   │   ├── ModRHS.F
│   │   ├── ModRHS_oldemf.F
│   │   ├── ModSundry.F
│   │   ├── ModWork.F
│   │   ├── postcpp
│   │   ├── probs
│   │   ├── python
│   │   └── README.txt
│   ├── pencil-code-master.zip
│   └── yinyang_transform.py
├── Germinal-Theory.germ
├── Modular-Forms/
│   ├── MFLecture1.pdf
│   └── Zagier123ModularForms.pdf
├── Phase-Calculus/
│   ├── CF000_Primitive_Distinguishability
│   │   ├── arxiv.sty
│   │   ├── CF000_Primitive_Distinguishability.pdf
│   │   ├── CFN000_Primitive_Origin.ipynb
│   │   ├── docs
│   │   ├── lean
│   │   ├── main.tex
│   │   ├── orcid.pdf
│   │   ├── outputs
│   │   ├── README_publication_update.md
│   │   └── scripts
│   ├── CF00_Induced_Geometry
│   │   ├── arxiv.sty
│   │   ├── CF00_Induced_Geometry.pdf
│   │   ├── CFN00_Induced_Geometry.ipynb
│   │   ├── docs
│   │   ├── lean
│   │   ├── main.tex
│   │   ├── notebooks
│   │   ├── orcid.pdf
│   │   ├── PROVENANCE_manifest.json
│   │   ├── README.md
│   │   ├── sympy
│   │   ├── template_PROVENANCE_manifest.json
│   │   └── verification
│   ├── CF13_Pi_Transcendence_Chirality_and_NN_Obstruction
│   │   ├── arxiv.sty
│   │   ├── CFN13_Pi_Transcendence_Chirality_NN.ipynb
│   │   ├── docs
│   │   ├── lean4
│   │   ├── main.pdf
│   │   ├── main.tex
│   │   ├── notebooks
│   │   ├── orcid.pdf
│   │   ├── PROVENANCE_manifest.json
│   │   ├── README_PUBLICATION_UPDATE.md
│   │   ├── reports
│   │   └── scripts
│   ├── CF19_The_Full_Lifted_Object
│   │   ├── arxiv.sty
│   │   ├── CF19_The_Full_Lifted_Object.pdf
│   │   ├── code
│   │   ├── data
│   │   ├── figures
│   │   ├── formal
│   │   ├── main.tex
│   │   ├── notebooks
│   │   ├── notes
│   │   ├── orcid.pdf
│   │   ├── packages
│   │   ├── PROVENANCE_manifest.json
│   │   ├── README.md
│   │   ├── RELEASE_CHANGES.md
│   │   └── validation
│   ├── Domesticating_Chaos
│   │   ├── arxiv.sty
│   │   ├── certificates
│   │   ├── Domesticating_Chaos_Projection_Loss_Accounting_in_Phase_Calculus.pdf
│   │   ├── figures
│   │   ├── figures_jpg
│   │   ├── lean
│   │   ├── main.tex
│   │   ├── notebooks
│   │   ├── outputs
│   │   ├── PROVENANCE_manifest.json
│   │   ├── pyproject.toml
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── scripts
│   │   ├── SHA256SUMS.txt
│   │   ├── src
│   │   └── tests
│   ├── Farey_Remainder_Recursion_and_Orthogonality
│   │   ├── arxiv.sty
│   │   ├── Farey_Remainder_Recursion_and_Orthogonality.pdf
│   │   ├── main.tex
│   │   ├── orcid.pdf
│   │   └── references.bib
│   ├── Loop_Generated_Projection_in_TDAHE
│   │   ├── arxiv.sty
│   │   ├── data
│   │   ├── FIGURE_CAPTIONS.md
│   │   ├── figures
│   │   ├── lean
│   │   ├── MANIFEST_SHA256.csv
│   │   ├── notebooks
│   │   ├── PHASE_CALCULUS_TDAHE_FIGURE_NOTE.md
│   │   ├── README.md
│   │   ├── reports
│   │   ├── scripts
│   │   ├── SOURCE_CROSSWALK.md
│   │   ├── TDAHE_Phase_Calculus_with_Experimental_Consequences.pdf
│   │   └── TDAHE_Phase_Calculus_with_Experimental_Consequences.tex
│   ├── Monodromy_as_Memory
│   │   ├── arxiv.sty
│   │   ├── certificate_cli_double_cover.json
│   │   ├── certificate_cli_quintic.json
│   │   ├── certificate.json
│   │   ├── claim_ledger.json
│   │   ├── cli_double_report.txt
│   │   ├── cli_quintic_report.txt
│   │   ├── closure_certificate.json
│   │   ├── data
│   │   ├── docs
│   │   ├── inline_verification_report.txt
│   │   ├── latexmk_report.txt
│   │   ├── lean
│   │   ├── main.aux
│   │   ├── main.log
│   │   ├── main.out
│   │   ├── main.tex
│   │   ├── Monodromy_as_Memory.pdf
│   │   ├── notebooks
│   │   ├── orcid.pdf
│   │   ├── packages
│   │   ├── pdflatex_report.txt
│   │   ├── PROVENANCE_manifest.json
│   │   ├── pyproject.toml
│   │   ├── pytest_report.txt
│   │   ├── README.md
│   │   ├── references.bib
│   │   ├── scripts
│   │   ├── SHA256SUMS.txt
│   │   ├── src
│   │   ├── sympy_report.txt
│   │   └── tests
│   ├── Non_Commutative_Phase_Geometry
│   │   ├── fix_commutator_residual_figure.py
│   │   ├── fixed_fig02_commutator_residuals.pdf
│   │   ├── fixed_fig02_commutator_residuals.png
│   │   ├── fixed_fig02_commutator_residuals.svg
│   │   └── nc_phase_geometry_package_v0_3_ALL_FIGURES
│   ├── Operational_Utility_and_Multiscale_Invariance_of_Phase_Calculus
│   │   ├── abstract.txt
│   │   ├── arxiv.sty
│   │   ├── extension_closure.tex
│   │   ├── figures
│   │   ├── lean4
│   │   ├── LICENSE.md
│   │   ├── main.tex
│   │   ├── notebooks
│   │   ├── Operational_Utility_and_Multiscale_Invariance_of_Phase_Calculus.pdf
│   │   ├── orcid.pdf
│   │   ├── ou_v5_4_PROVENANCE_manifest_20260419100033.json
│   │   ├── packages
│   │   ├── phase_calculus_demonstration_paper_v5_4_cfn_standard_release.tex
│   │   ├── pi_spigot_lock_section_full.tex
│   │   ├── pi_spigot_lock_section.tex
│   │   ├── README.md
│   │   ├── references.bib
│   │   ├── requirements.txt
│   │   ├── results
│   │   ├── review_notes.txt
│   │   ├── summary.json
│   │   ├── supplemental
│   │   ├── technical_info.txt
│   │   └── unification_theorem.tex
│   ├── Phase_Calculus_as_Universal_Exact_Grammar_for_Branching_Structures
│   │   ├── arxiv.sty
│   │   ├── certificate_bring_quintic_roots.json
│   │   ├── certificate_log_countable.json
│   │   ├── certificate_quintic_s5.json
│   │   ├── claim_ledger.json
│   │   ├── closure_certificate.json
│   │   ├── data
│   │   ├── figures
│   │   ├── lean
│   │   ├── main.pdf
│   │   ├── main.tex
│   │   ├── notebooks
│   │   ├── patches
│   │   ├── Phase_Calculus_as_Universal_Exact_Grammar_for_Branching_Structures.pdf
│   │   ├── PROVENANCE_manifest.json
│   │   ├── pyproject.toml
│   │   ├── README.md
│   │   ├── references.bib
│   │   ├── reports
│   │   ├── scripts
│   │   ├── SHA256SUMS.txt
│   │   ├── src
│   │   ├── sympy_audit_ledger.json
│   │   └── tests
│   ├── Phase_Calculus_Complete_Formalisation
│   │   ├── packages
│   │   ├── PCVDMFullDynamicsRegressor
│   │   ├── Phase_Calculus_Complete_Formalisation.pdf
│   │   ├── Phase_Calculus_Complete_Formalisation.tex
│   │   ├── PROVENANCE_manifest.json
│   │   ├── README.md
│   │   ├── updates_to_make.csv
│   │   └── verification_report.md
│   ├── Quotient_Descent
│   │   ├── arxiv.sty
│   │   ├── claim_registry.csv
│   │   ├── lakefile.toml
│   │   ├── lean-toolchain
│   │   ├── Main.lean
│   │   ├── Operation_Descent_in_Phase_Calculus.pdf
│   │   ├── Origin_and_Dependency_Chain_v1_5.tex
│   │   ├── PCEML
│   │   ├── PCEML.lean
│   │   ├── PC_EML_v1_5_validation_executed.ipynb
│   │   ├── PC_EML_v1_5_validation.ipynb
│   │   ├── pc_vdm_lifted_descent_solver
│   │   ├── Primitive_Operation_Descent_v1_5.tex
│   │   ├── Primitive_Origin_and_Dependency_Chain.pdf
│   │   ├── PROVENANCE_manifest_20260424132901.json
│   │   ├── Quotient_Descent_and_EML_Operator_v1_5.tex
│   │   ├── Quotient_Descent.pdf
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── SHA256SUMS
│   │   ├── supporting_evidence
│   │   ├── sympy_pc_eml_v1_5_validation.py
│   │   ├── table_of_contents.txt
│   │   ├── THEOREM_INVENTORY.csv
│   │   ├── validation
│   │   └── xi_eml_reframe_patch
│   ├── Retained_State_Phase_Calculus
│   │   ├── arxiv.sty
│   │   ├── main.html
│   │   ├── main.tex
│   │   ├── Makefile
│   │   ├── orcid.pdf
│   │   ├── pdf_text.txt
│   │   ├── README.md
│   │   ├── references.bib
│   │   ├── retained_state_phase_calculus_v6.pdf
│   │   ├── SHA256SUMS.txt
│   │   └── supplement
│   ├── The_Transcendental_Wall
│   │   ├── certificates
│   │   ├── claim_ledger.json
│   │   ├── closure_certificate.json
│   │   ├── data
│   │   ├── figures
│   │   ├── lean
│   │   ├── main.tex
│   │   ├── notebooks
│   │   ├── pyproject.toml
│   │   ├── README.md
│   │   ├── references.bib
│   │   ├── reports
│   │   ├── scripts
│   │   ├── SHA256SUMS.txt
│   │   ├── src
│   │   ├── tests
│   │   └── Transcendental_Wall_Inverse_Word_Certifier.pdf
│   └── Unified_Quintic
│       ├── arxiv.sty
│       ├── CLOSURE_CERTIFICATE.md
│       ├── FIGURE_QA_CHECKLIST.md
│       ├── figures
│       ├── main.tex
│       ├── README.md
│       ├── results
│       ├── tools
│       ├── Unified_Quintic.pdf
│       ├── Unified_Quintic_PROVENANCE_manifest_20260424071110.json
│       └── validation
├── Prospect-Leads/
│   ├── Axis-Free-overset-grid.pdf
│   ├── Dataset-of-Ancient-Chinese-Math.pdf
│   ├── icpr2011_Logic-and-Philosophy-Today.pdf
│   ├── Leibniz-Binary-Shao-Yongs-YiJing.pdf
│   ├── Liu_2022_ApJ_940_62.pdf
│   ├── philosophies-10-00111.pdf
│   └── Physics_of_Buddhism_The_physics_and_math.pdf
└── Tao-Research/
    ├── 01-1-4-2024 (1).pdf
    ├── 0403123v1.pdf
    ├── 1003.1633v1.pdf
    ├── 1648-16.pdf
    ├── 1705.0203v1.pdf
    ├── 1_ The Shape of Understanding - by Vincent John.pdf
    ├── 2508.08210v2.pdf
    ├── 2606.18009v1.pdf
    ├── 5d56507fb71b0.pdf
    ├── 5e0429a28f229.pdf
    ├── 9911050v1.pdf
    ├── 9911051v1.pdf
    ├── ChinaandUniversals.pdf
    ├── Geochem Geophys Geosyst - 2004 - Kageyama - Yin‐Yang grid   An overset grid in spherical geometry.pdf
    ├── Geochem Geophys Geosyst - 2014 - Yoshida - A Fortran visualization program for spherical data on a Yin‐Yang grid.pdf
    ├── Jin-Yuan Mathematics and Quanzhen Taoism.pdf
    ├── Koulaouzidis_2018.pdf
    ├── Luo_2025_ApJS_280_48.pdf
    ├── Mathematics _ Definition, History, & Importance _ Britannica.pdf
    ├── mwre-mwr-d-12-00108.1.pdf
    ├── Tao Te Ching.pdf
    ├── The Tao of Math.pdf
    ├── windwalker-iching.pdf
    ├── Yin-Yang_grid_and_geodynamo_simulation.pdf
    └── Unearthing-the-Ancient-Yi_Chinese.pdf

111 directories, 223 files
```

</details>

## Citations

A consolidated list of source materials and DOI links is available in [CITATIONS/](/CITATIONS/). Many of the original source PDFs and datasets are excluded from version control for licensing reasons; keep these files tracked so others can locate the referenced materials via DOI.
