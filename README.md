# 伦敦 Southwark 住房不平等分析 (Housing Equity Analysis – Southwark)

基于数据驱动的城市住房不平等分析项目,涵盖数据整合、空间分布、空间自相关、聚类与人口敏感性分析。

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
