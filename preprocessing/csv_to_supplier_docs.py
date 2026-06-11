from pathlib import Path
import pandas as pd

INPUT_FILE = "data/supplier_performance_data.csv"
OUTPUT_FILE = "generated/supplier_docs.txt"


def safe_value(row, column_name):
    return str(row[column_name]) if column_name in row.index else "N/A"


def main():
    Path("generated").mkdir(exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    documents = []

    for _, row in df.iterrows():
        document = f"""
Supplier ID: {safe_value(row, 'Supplier_ID')}
Supplier Name: {safe_value(row, 'Supplier_Name')}
Region: {safe_value(row, 'Region')}
Country: {safe_value(row, 'Country')}
Tier: {safe_value(row, 'Supplier_Tier')}
Product Category: {safe_value(row, 'Product_Category')}
OTD Rate Percent: {safe_value(row, 'OTD_Rate_Pct')}
Defect Rate Percent: {safe_value(row, 'Defect_Rate_Pct')}
Compliance Score: {safe_value(row, 'Compliance_Score')}
Risk Level: {safe_value(row, 'Risk_Level')}
Lead Time Days: {safe_value(row, 'Lead_Time_Days')}
Sustainability Score: {safe_value(row, 'Sustainability_Score')}
Active Disruption: {safe_value(row, 'Active_Disruption')}
Alternate Supplier: {safe_value(row, 'Alt_Supplier_ID')}
Total PO Value: {safe_value(row, 'PO_Value')}
"""

        documents.append(document.strip())
        documents.append("\n" + ("-" * 80) + "\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(documents))

    print(f"Generated: {OUTPUT_FILE}")
    print(f"Documents created: {len(df)}")


if __name__ == "__main__":
    main()