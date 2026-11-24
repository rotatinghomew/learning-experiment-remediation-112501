"""读取合成资料并执行最小的输入契约校验。"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

REQUIRED_FILES = ("source_info.json", "events.json", "entities.json", "observations.json")


def load_bundle(root: str | Path) -> dict[str, Any]:
    """读取资料包，保留缺失值和原始顺序。"""
    base = Path(root)
    bundle: dict[str, Any] = {}
    for name in REQUIRED_FILES:
        path = base / name
        if not path.is_file():
            raise FileNotFoundError(path)
        with path.open(encoding="utf-8") as handle:
            bundle[name] = json.load(handle)
    if bundle["source_info.json"].get("source_kind") != "synthetic":
        raise ValueError("资料包必须标明为 synthetic")
    return bundle
