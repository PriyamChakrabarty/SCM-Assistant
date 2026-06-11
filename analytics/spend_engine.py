import pandas as pd


def calculate_regional_spend(csv_file: str) -> pd.DataFrame:
    df = pd.read_csv(csv_file)

    regional_spend = (
        df.groupby("Region")["PO_Value"]
        .sum()
        .reset_index()
    )

    regional_spend = regional_spend.sort_values(
        by="PO_Value",
        ascending=False,
    )

    return regional_spend.reset_index(drop=True)


if __name__ == "__main__":
    result = calculate_regional_spend(
        "data/supplier_performance_data.csv"
    )

    print(result)