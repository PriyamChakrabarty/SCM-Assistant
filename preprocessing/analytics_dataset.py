from pathlib import Path
import json
import pandas as pd

INPUT_FILE = "data/supplier_performance_data.csv"
OUTPUT_FILE = "generated/analytics_cache.json"


def main():
    Path("generated").mkdir(exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    analytics = {
        "total_rows": int(len(df)),
        "unique_suppliers": int(df["Supplier_ID"].nunique())
        if "Supplier_ID" in df.columns
        else 0,
        "total_spend": float(df["PO_Value"].sum())
        if "PO_Value" in df.columns
        else 0,
        "regions": sorted(df["Region"].dropna().unique().tolist())
        if "Region" in df.columns
        else [],
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(analytics, file, indent=4)

    print(f"Generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()