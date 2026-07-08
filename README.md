# Mapping Data-informed Urban Inequality Insights — Housing Equity

> 基于数据驱动的城市不平等洞察 —— 住房公平性制图研究

**研究尺度:** 伦敦全域(Borough 尺度)→ 南华克区(Southwark, LSOA 尺度,共 173 个 LSOA)

本项目把楼栋级 EPC 能效、房价、交通与医疗可及性等多源数据整合为多维**住房公平指数(Housing Equity Index, HEI)**,在此基础上分析其空间格局、集聚特征与人群差异,并探索人口调整型的住房公平测度。

---

## 研究框架

### 第一阶段:住房公平的量化与空间分析(RQ1–RQ4)

**RQ1 — 住房公平如何量化?**
*How can property-level EPC, house price and accessibility data be integrated into a multidimensional Housing Equity Index for Southwark?*
方法:EPC 聚合 → 房价聚合 → 交通与医疗变量合并 → 拥挤 proxy 构建 → 标准化 → HEI 构建;采用 **Bayesian Latent Index** 估计 HEI。

**RQ2 — Southwark 内部住房公平空间格局如何?**
*What is the spatial distribution of housing equity across Southwark LSOAs?*
方法:绘制 HEI map、HCI map、affordability map、EPC vulnerability map、overcrowding proxy map、transport / healthcare accessibility map。

**RQ3 — 住房公平低分区域是否存在空间集聚?**
*Are low housing equity areas spatially clustered within Southwark?*
方法:Global Moran's I、Local Moran's I / LISA、Low-Low 集聚区识别。

**RQ4 — Southwark 内部有哪些住房公平问题类型?**
*What types of housing equity challenges can be identified, and what policy interventions do they imply?*
方法:K-means / 层次聚类、cluster profile table、typology map、policy recommendation matrix;Geographically Weighted PCA(GWPCA);空间聚类 SKATER / REDCAP;未来风险方向:Multiscale Spatial Risk Index。

### 第二阶段(核心研究问题):人群差异下的住房不公

**核心问题:** 同一客观住房条件下,不同人群承受、感知住房不公的程度是否存在显著差异?

- **子问题 1(客观维度):** HEI 档位一致时,收入可负担性、职业、年龄、家庭结构、健康、通勤距离不同的片区,客观住房剥夺的承压强度是否不同?
- **子问题 2(主观维度):** 面对同类住房短板(拥挤、交通、医疗、高房价),不同人群的主观敏感度与不满程度是否分化?
- **子问题 3(空间维度):** 住房条件与人群特征的组合差异,是否形成特定的空间分异格局?

**研究假设(显著性水平 α = 0.05):**

- **H1(客观假设):** 同等 HEI 档位下,低收入、低 NSSEC 职业阶层、多子女、老年人群的客观住房剥夺承受度显著更高。
- **H2(感知假设):** 不同人群对住房短板的感知敏感度存在分化(青年敏感于交通,老年敏感于医疗,多子女敏感于拥挤,低收入敏感于房价)。
- **H3(空间假设):** "差住房 + 弱势人群"形成连片双重剥夺集聚区,"优住房 + 优势人群"形成连片优势区,空间耦合特征显著。

**核心研究方法:**

1. **聚类** — 划分多种人群主导型片区;在不同 HEI 层级下分层计算不同人群的敏感度。
2. **差异显著性检验** — 单因素方差分析(ANOVA)检验同一 HEI 档位下不同人群的客观承压与主观感知差异;卡方检验人口聚类与住房聚类的空间关联性。
3. **GIS 空间叠加分析** — 叠加 HEI 图层与人口聚类图层,识别空间耦合格局。
4. **贝叶斯模型优化** — 基于人群差异结果,构建人口调整型 HEI。

---

## 研究进度

**第一阶段(RQ1–RQ4)** 已通过 notebook 01–05 完成数据整合、空间分布、空间自相关与聚类分析。

**第二阶段(人群差异)** 进展:

1. **人群画像(Section 2)** — 用 Census 2021 的 9 个人口学比例变量(健康差比例、低职业阶层比例、有儿童家庭、老年独居、长距离通勤等)对 173 个 Southwark LSOA 做 K-means 聚类,分成 4 类人群主导型:**贫困型 / 老龄型 / 家庭型 / 专业型**。
2. **H1 验证(Section 3)** — 以 HEI 五档(Q1 最好 → Q5 最差)为分组,对每个人口学指标做单因素 ANOVA + Tukey 事后检验,回答:住房越差的片区,弱势人群比例是否显著更高?
3. **H2 验证(Section 4)** — 用 Spearman 相关矩阵检验"特定人群 ↔ 特定住房短板"的敏感度分化:老年独居片区是否集中暴露于医疗可及性差?多子女家庭片区是否集中暴露于拥挤?低职业阶层片区是否集中暴露于高房价?
4. **H3 + 调整型 HEI(Section 5–6)** — 卡方检验 HEI 档位与人群聚类的空间关联性,在地图上识别"双重剥夺区"(差住房 + 弱势人群)与"双重优势区";最后依据 H2 的敏感度权重构造人口调整型 HEI,与原始 Bayesian HEI 做对比。

---

## 项目结构

```
code/
├── 01_data_integration_southwark.ipynb        # 数据整合
├── 02_spatial_distribution_southwark.ipynb     # 空间分布
├── 03_spatial_autocorrelation_southwark.ipynb  # 空间自相关
├── 04_clustering_southwark.ipynb               # 聚类分析
├── 05_population_sensitivity_southwark.ipynb   # 人口敏感性分析
├── data/                                       # 数据(大文件需单独下载,见下)
├── figures/                                    # 输出图表
├── LSOA_Shapfile/                              # LSOA 地理边界
└── download_data.py                            # 数据集下载脚本
```

## 数据集下载

核心数据集 **EPC London Building Stock**(约 2.2GB)体积过大,未随仓库分发,
托管在 Hugging Face:
<https://huggingface.co/datasets/KevinLLLLuo/epc_london_building_stock>

clone 仓库后,运行以下命令下载数据:

```bash
pip install huggingface_hub
cd code
python download_data.py
```

数据会被下载到 `code/data/epc_london_building_stock.csv`。

## 环境依赖

```bash
pip install pandas geopandas numpy scikit-learn matplotlib seaborn esda libpysal huggingface_hub
```

## 使用方法

1. clone 本仓库
2. 按上面的说明下载数据集
3. 依次运行 `code/` 下编号 01–05 的 notebook

---

## Variable Reference Table

| Variable Name | Description | Processing Method | Direction |
|---|---|---|---|
| **Identifiers** | | | |
| `lsoa11cd` | LSOA 2011 code | ONS boundary code | — |
| `lsoa21cd` | LSOA 2021 code (primary join key) | ONS boundary code | — |
| `lsoa21nm` | LSOA 2021 name | ONS boundary name | — |
| `n_properties` | Number of EPC-registered properties in LSOA | Count from EPC dataset | — |
| **Raw Input Variables** | | | |
| `avg_epc_score` | Average EPC energy efficiency score (0–100) | Mean of building-level EPC scores per LSOA | ↑ Higher = Better |
| `avg_epc_rating_num` | Average EPC rating (A=best → G=worst, mapped to numeric) | Mean of EPC band numeric mappings per LSOA | ↑ Higher = Better |
| `pct_epc_ABC` | % properties rated EPC A, B, or C | Count(A/B/C) / total properties | ↑ Higher = Better |
| `avg_floor_area` | Average floor area (m²) per property | Mean of floor area per LSOA | ↑ Higher = Better |
| `avg_rooms` | Average number of rooms per property | Mean of room count per LSOA | ↑ Higher = Better |
| `overcrowding_idx` | Overcrowding index: persons per room | Mean persons/rooms across properties | ↓ Lower = Better |
| `overcrowding_proxy` | Overcrowding proxy: 1 / (avg_floor_area × avg_rooms) | Inverse of space supply; inf → NaN → median impute | ↓ Lower = Better |
| `median_house_price` | Median residential transaction price (£) | Median of Land Registry prices 2015–2022 per LSOA | ↓ Lower = Better (affordability) |
| `transport_ptai` | Public Transport Accessibility Index (PTAI) | TfL PTAI score averaged per LSOA | ↑ Higher = Better |
| `ptal_grade` | PTAI letter grade (1a–6b) | Categorical derived from PTAI score | — (ordinal) |
| `ptai_high` | Binary: PTAI ≥ 20 (high accessibility) | Indicator variable | ↑ Higher = Better |
| `ptai_low` | Binary: PTAI < 5 (low accessibility) | Indicator variable | ↓ Lower = Better |
| `hospital` | Hospital accessibility score | Composite of distance/count to nearest hospitals | ↑ Higher = Better |
| `GP` | GP surgery accessibility score | Composite of distance/count to nearest GPs | ↑ Higher = Better |
| `pharmacy` | Pharmacy accessibility score | Composite of distance/count to nearest pharmacies | ↑ Higher = Better |
| `hospital_rnk` | Hospital accessibility rank within Southwark | Rank 1 = best access | ↑ Higher = Better |
| `hospital_pct` | Hospital accessibility percentile (0–1) | Rank / N | ↑ Higher = Better |
| `domain_h` | AHAH healthcare domain score | From ONS AHAH index, healthcare dimension | ↑ Higher = Better |
| `ahah` | Access to Healthy Assets and Hazards (AHAH) composite | ONS AHAH composite index | ↑ Higher = Better |
| **HEI Pipeline — Direction-Aligned Variables** (`_al` suffix) | | | |
| `avg_epc_rating_num_al` | EPC rating, direction-aligned & MinMax scaled | inf/NaN → median → winsorise → Z-score → keep direction → MinMax [0,1] | ↑ Higher = Better |
| `overcrowding_proxy_al` | Overcrowding proxy, direction-aligned & MinMax scaled | Same pipeline → **invert** (1 − x) → MinMax [0,1] | ↑ Higher = Better |
| `median_house_price_al` | House price, direction-aligned & MinMax scaled | Same pipeline → **invert** (1 − x) → MinMax [0,1] | ↑ Higher = Better |
| `transport_ptai_al` | PTAI, direction-aligned & MinMax scaled | Same pipeline → keep direction → MinMax [0,1] | ↑ Higher = Better |
| `hospital_al` | Hospital access, direction-aligned & MinMax scaled | Same pipeline → keep direction → MinMax [0,1] | ↑ Higher = Better |
| **Composite Indices** | | | |
| `HEI_bayes` | Housing Equity Index — Bayesian Latent Factor (primary) | Gibbs sampler K=1, conjugate priors on 5 `_al` vars; output [0,1] | ↓ Lower = Better (0 = most equitable) |
| `HEI_bayes_uncert` | HEI posterior uncertainty (95% CI width) | `HEI_bayes_hi − HEI_bayes_lo` from Gibbs samples | ↓ Lower = Better |
| `HEI_bayes_lo` | HEI Bayesian 2.5th percentile | Lower bound of posterior credible interval | — (diagnostic) |
| `HEI_bayes_hi` | HEI Bayesian 97.5th percentile | Upper bound of posterior credible interval | — (diagnostic) |
| `HEI_equal` | Housing Equity Index — Equal weights | Simple mean of 5 `_al` variables | ↓ Lower = Better |
| `HEI_pca` | Housing Equity Index — PCA weights | First principal component of 5 `_al` variables | ↓ Lower = Better |
| `HEI_quintile` | HEI quintile classification (1–5) | `HEI_bayes` cut into 5 equal groups | Q1 = Best equity; Q5 = Worst |

---

## Key Results

The figures below represent the most analytically significant outputs across all six research stages. All files are in `code/figures/`.

---

### Stage 1 — Context & Motivation

**`intro_london_price_trends.png`**
Borough-level median house price trajectories for Greater London (2001–2017). Demonstrates Southwark's sustained above-average price growth and motivates the choice of study area as a site of acute affordability pressure within the inner city.

**`intro_southwark_location_hei.png`**
Dual-panel figure: (left) Southwark's geographic position within Greater London; (right) the Bayesian Housing Equity Index choropleth at LSOA level. Provides spatial context and serves as the visual anchor for the entire study.

---

### Stage 2 — Housing Equity Index (RQ1–RQ2)

**`map_HEI_bayes_southwark.png`**
Primary output of the project. Choropleth map of the Bayesian Latent Factor HEI across all 173 Southwark LSOAs (0 = best equity, 1 = worst). Reveals a clear north–south spatial gradient, with riverside and central LSOAs recording the highest deprivation scores.

**`bayes_hei_diagnostics.png`**
Model validation panel for the Gibbs-sampler Bayesian latent factor. Shows posterior distributions, convergence trace, and comparison of Bayesian HEI against equal-weight and PCA alternatives, confirming model stability and construct validity.

---

### Stage 3 — Spatial Structure (RQ3–RQ4)

**`gwpca_local_loadings.png`**
Geographically Weighted PCA local factor loadings across Southwark LSOAs. Reveals that the relative contribution of each HEI dimension (EPC, overcrowding, price, transport, healthcare) varies significantly across space — evidence that a single global weighting scheme misrepresents local deprivation drivers.

**`gwpca_dominant_score.png`**
Maps the dominant deprivation dimension per LSOA derived from GWPCA. Identifies distinct sub-zones driven by price unaffordability (north), transport deficit (south-east), and EPC underperformance (inner areas).

**`spatial_clustering_comparison.png`**
Three-panel comparison of K-Means, SKATER (spatially constrained), and REDCAP cluster solutions. Demonstrates that imposing spatial contiguity produces more geographically coherent, policy-relevant typologies than unconstrained partitioning.

---

### Stage 4 — Population Sensitivity (RQ5)

**`pop_cluster_profiles.png`**
Z-scored heatmap and parallel coordinates showing the demographic signature of each K-Means population cluster (Deprived / Elderly / Family / Professional). Confirms that Census 2021 indicators cleanly differentiate four structurally distinct community types across Southwark.

**`h1_anova_boxplots.png`**
Box plots of nine demographic vulnerability indicators stratified by HEI quintile (Q1 best → Q5 worst). ANOVA results annotated per panel. Supports Hypothesis H1: LSOAs with the worst housing equity systematically concentrate higher proportions of low-income, low-NSSEC, and deprived households.

**`h2_sensitivity_heatmap.png`**
Full Spearman ρ matrix: nine demographic variables × six HEI components. Insignificant cells (α = 0.05) crossed out. The structured pattern of correlations supports Hypothesis H2 — different population groups are differentially sensitive to specific housing deprivation dimensions (e.g., elderly populations cluster in areas with poor healthcare access).

**`h3_double_deprivation_map.png`**
Three-panel spatial overlay (Bayesian HEI | Population-type cluster | Zone classification). Identifies Double Deprivation zones (Q4–Q5 HEI + Deprived population) and Double Advantage zones. Bivariate Moran's I confirms statistically significant spatial co-clustering of housing and population disadvantage (Hypothesis H3).

**`hei_adjusted_map.png`**
Side-by-side comparison of the standard Bayesian HEI and the demographically-adjusted HEI (weights recalibrated by Spearman sensitivity scores). Rank-change panel highlights LSOAs where accounting for population composition substantially re-orders the deprivation ranking.

---

### Stage 5 — Spatial Overlay Analysis (RQ6)

**`overlay_vulnerability_surface.png`**
Scatter plot positioning all 173 LSOAs in a two-dimensional vulnerability space: housing equity deprivation (x-axis) × composite population vulnerability score (y-axis). Quadrant lines at medians divide the space into four interpretable risk zones; points coloured by joint typology.

**`overlay_policy_matrix.png`**
5 × 4 policy intervention matrix (housing type A–E × population type). Cell colour encodes priority tier (green = low, red = critical). Provides a directly actionable, evidence-based framework linking analytical typologies to targeted policy responses.

**`overlay_priority_map.png`**
Dual-panel map: (left) continuous composite intervention priority score per LSOA, combining housing deprivation rank and population vulnerability rank; (right) joint typology classification. The highest-priority LSOAs (dark red) require immediate multi-dimensional intervention addressing both physical housing conditions and socioeconomic vulnerability.
