import pandas as pd
import json
from pathlib import Path

df = pd.read_csv("data/supplier_performance_data.csv")

metadata = []

for _, row in df.iterrows():


    metadata.append({
    "supplier_id": row["Supplier_ID"],
    "region": row["Region"],
    "tier": row["Supplier_Tier"],
    "risk_level": row["Risk_Level"],
    "category": row["Product_Category"]
})


Path("generated").mkdir(exist_ok=True)

with open("generated/supplier_summary.json","w") as f:
    json.dump(metadata,f,indent=4)

print("Metadata created")
