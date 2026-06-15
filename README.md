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
