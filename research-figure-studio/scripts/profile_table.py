"""Emit a bounded JSON profile for CSV/XLSX scientific figure inputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def read_table(path: Path, sheet: str | int | None) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix in {".csv", ".txt", ".tsv"}:
        sep = "\t" if suffix in {".tsv", ".txt"} else ","
        return pd.read_csv(path, sep=sep)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path, sheet_name=sheet if sheet is not None else 0)
    raise ValueError(f"Unsupported input type: {suffix}")


def profile(df: pd.DataFrame) -> dict:
    fields = []
    for name in df.columns:
        s = df[name]
        item = {
            "name": str(name),
            "dtype": str(s.dtype),
            "missing": int(s.isna().sum()),
            "non_null": int(s.notna().sum()),
            "unique_non_null": int(s.nunique(dropna=True)),
        }
        if pd.api.types.is_numeric_dtype(s):
            a = pd.to_numeric(s, errors="coerce").to_numpy(dtype=float)
            finite = a[np.isfinite(a)]
            item["nonfinite"] = int(np.isfinite(a).size - finite.size)
            if finite.size:
                q = np.quantile(finite, [0, 0.25, 0.5, 0.75, 1])
                item["numeric"] = {
                    "min": float(q[0]),
                    "q1": float(q[1]),
                    "median": float(q[2]),
                    "q3": float(q[3]),
                    "max": float(q[4]),
                }
        else:
            counts = s.dropna().astype(str).value_counts().head(8)
            item["top_values"] = [{"value": k, "count": int(v)} for k, v in counts.items()]
        fields.append(item)
    return {
        "rows": int(len(df)),
        "columns": int(df.shape[1]),
        "duplicate_rows": int(df.duplicated().sum()),
        "fields": fields,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--sheet")
    args = parser.parse_args()
    result = profile(read_table(args.input, args.sheet))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
