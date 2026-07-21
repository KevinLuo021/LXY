# Housing Equity Analysis in Inner-City London
### A Spatiotemporal and Population-Differentiated Study of 173 LSOAs in Southwark

> **MSc Dissertation** · King's College London · Urban Informatics · 2024/25  
> Supervisor: Dr Yijing Li

---

## Overview

This project develops an integrated, data-driven framework for mapping and explaining housing inequality at the neighbourhood scale in the London Borough of Southwark. Starting from five heterogeneous data sources — EPC energy efficiency records, Land Registry transaction prices, TfL transport accessibility scores, NHS healthcare access, and Census 2021 demographics — it constructs a **Bayesian Latent Factor Housing Equity Index (HEI)** for all 173 Lower Super Output Areas (LSOAs), then analyses its spatial structure, dimensional drivers, and population-differentiated effects.

**Key findings:**
- HEI ranges from 0.015 to 0.968 across 173 contiguous LSOAs, with a statistically significant north–south gradient (25 High-High and 24 Low-Low LISA clusters at *p* < 0.05)
- GWPCA reveals spatially non-stationary dimensional drivers: hospital access dominates in 46 LSOAs, EPC efficiency in 42, overcrowding in 36, price in 30, transport in 19
- All three population-heterogeneity hypotheses (H1–H3) are empirically confirmed; the demographically adjusted HEI re-ranks 139 of 173 LSOAs
- 37 Double Disadvantage zones identified; top-10 priority LSOAs scored 0.815–0.980

---

## Repository Structure

```
├── 00_introduction_southwark.ipynb         # Study area context & motivation
├── 01_data_integration_southwark.ipynb     # Multi-source data pipeline & HEI construction
├── 02_spatial_distribution_southwark.ipynb # Spatial distribution mapping (RQ1–RQ2)
├── 03_spatial_autocorrelation_southwark.ipynb  # Moran's I & LISA clustering (RQ3)
├── 04_clustering_southwark.ipynb           # K-Means, SKATER, REDCAP, GWPCA (RQ4)
├── 05_population_sensitivity_southwark.ipynb   # H1–H3 hypothesis testing
├── 06_overlay_analysis_southwark.ipynb     # Dual-deprivation overlay & priority scoring
├── data/                                   # Processed datasets (see download instructions)
├── figures/                                # All output figures
├── LSOA_Shapfile/                          # ONS LSOA 2021 boundary shapefiles
└── download_data.py                        # EPC dataset download script
```

---

## Data Sources

| Dataset | Source | Licence |
|---|---|---|
| Energy Performance Certificates (EPC) | MHCLG | OGL v3.0 |
| Land Registry Price Paid Data | HM Land Registry | OGL v3.0 |
| Public Transport Accessibility Index (PTAI) | Transport for London | OGL v3.0 |
| Healthcare facility locations | NHS Digital | OGL v3.0 |
| Census 2021 LSOA statistics | ONS | OGL v3.0 |
| LSOA 2021 boundary shapefiles | ONS Geoportal | OGL v3.0 |

The EPC dataset (~2.2 GB) is hosted on Hugging Face and must be downloaded separately:

```bash
pip install huggingface_hub
python download_data.py
# Downloads to: data/epc_london_building_stock.csv
```

---

## Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/KevinLuo021/LXY.git
cd LXY

# 2. Install dependencies
pip install pandas geopandas numpy scikit-learn matplotlib seaborn \
            esda libpysal pysal mgwr scipy statsmodels huggingface_hub

# 3. Download the EPC dataset
python download_data.py

# 4. Run notebooks in order
jupyter notebook
```

Run notebooks `00` → `06` in sequence. Each notebook is self-contained and saves outputs to `figures/` and `data/`.

---

## Methods Summary

| Stage | Method | Output |
|---|---|---|
| Data pipeline | Winsorisation → Z-score → Min-Max → direction alignment | 5 normalised `_al` variables |
| Index construction | Bayesian latent factor (Gibbs sampler, *K*=1, conjugate priors) | `HEI_bayes` per LSOA |
| Spatial autocorrelation | Global Moran's *I*, Local LISA | HH/LL cluster maps |
| Housing typology | K-Means (*k*=4), SKATER, REDCAP (ARI validation) | 4-class housing zones |
| Dimensional decomposition | GWPCA (adaptive bisquare kernel, LOO-CV bandwidth) | Local loadings per LSOA |
| Population clustering | K-Means on Census 2021 demographics | 4-class population types |
| Hypothesis testing | ANOVA + Tukey HSD (H1), Spearman ρ + Kruskal-Wallis (H2), χ² + Cramér's V + Bivariate Moran's I (H3) | H1–H3 all supported |
| Adjusted HEI | Sensitivity-weighted composite | Re-ranks 139/173 LSOAs |
| Priority scoring | *P*ᵢ = (rank(HEI) + rank(VUL)) / 2*n* | Priority map & top-10 list |

---

## Key Output Figures

| Figure | Description |
|---|---|
| `map_HEI_bayes_southwark.png` | Bayesian HEI choropleth — north–south gradient across 173 LSOAs |
| `bayes_hei_diagnostics.png` | Gibbs sampler convergence & benchmark comparison (equal-weight, PCA) |
| `gwpca_local_loadings.png` | Spatially varying dimensional loadings from GWPCA |
| `gwpca_dominant_score.png` | Dominant deprivation driver per LSOA |
| `spatial_clustering_comparison.png` | K-Means vs SKATER vs REDCAP cluster solutions |
| `h1_anova_boxplots.png` | ANOVA results: demographic vulnerability by HEI quintile |
| `h2_sensitivity_heatmap.png` | Spearman ρ matrix: population groups × HEI dimensions |
| `h3_double_deprivation_map.png` | Dual deprivation spatial overlay (H3) |
| `hei_adjusted_map.png` | Standard vs demographically adjusted HEI comparison |
| `overlay_priority_map.png` | Joint typology & composite priority score map |
| `overlay_policy_matrix.png` | Policy intervention matrix (housing type × population type) |

---

## Variable Reference

| Variable | Description | Direction |
|---|---|---|
| `avg_epc_rating_num_al` | EPC energy efficiency, normalised | ↑ Higher = Better |
| `overcrowding_proxy_al` | Overcrowding proxy (inverted), normalised | ↑ Higher = Better |
| `median_house_price_al` | House price affordability (inverted), normalised | ↑ Higher = Better |
| `transport_ptai_al` | PTAI transport accessibility, normalised | ↑ Higher = Better |
| `hospital_al` | Healthcare access score, normalised | ↑ Higher = Better |
| `HEI_bayes` | Bayesian Latent Factor HEI (primary index) | ↓ Lower = More Deprived |
| `HEI_bayes_uncert` | Posterior uncertainty (95% CI width) | — |
| `HEI_equal` | Equal-weight benchmark composite | ↓ Lower = More Deprived |
| `HEI_pca` | PCA-weight benchmark composite | ↓ Lower = More Deprived |
| `HEI_adj` | Demographically adjusted HEI | ↓ Lower = More Deprived |

---

## Licence

Code: MIT License. Data: subject to original provider licences (all OGL v3.0).
