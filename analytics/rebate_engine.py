import pandas as pd


def find_rebate_eligible_suppliers(csv_file: str) -> pd.DataFrame:
    """
    Policy §4.2

    Tier-1
    OTD >= 93
    Defect < 0.5
    Sustainability >= 85
    """

    df = pd.read_csv(csv_file)

    eligible = df[
        (df["Contract_Tier"] == "Tier-1")
        & (df["OTD_Rate_Pct"] >= 93)
        & (df["Defect_Rate_Pct"] < 0.5)
        & (df["Sustainability_Score"] >= 85)
    ]

    return (
        eligible[
            [
                "Supplier_ID",
                "Supplier_Name",
                "OTD_Rate_Pct",
                "Defect_Rate_Pct",
                "Sustainability_Score",
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )


if __name__ == "__main__":
    result = find_rebate_eligible_suppliers(
        "data/supplier_performance_data.csv"
    )

    print(result)