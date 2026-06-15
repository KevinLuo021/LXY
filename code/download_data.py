"""
下载本项目所需的大数据集(EPC London Building Stock）。

数据集托管在 Hugging Face,不随 Git 仓库分发。
首次使用前运行本脚本即可把数据下载到 code/data/ 下。

用法:
    pip install huggingface_hub
    python download_data.py
"""

from pathlib import Path
from huggingface_hub import hf_hub_download

REPO_ID = "KevinLLLLuo/epc_london_building_stock"
FILENAME = "epc_london_building_stock.csv"
DEST_DIR = Path(__file__).parent / "data"


def main():
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    print(f"正在从 Hugging Face 下载 {FILENAME} ...")
    path = hf_hub_download(
        repo_id=REPO_ID,
        filename=FILENAME,
        repo_type="dataset",
        local_dir=str(DEST_DIR),
    )
    print(f"完成。数据已保存到: {path}")


if __name__ == "__main__":
    main()
