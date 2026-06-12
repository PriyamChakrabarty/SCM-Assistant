import pandas as pd


def active_disruption_suppliers(csv_file: str) -> pd.DataFrame:
    """
    Policy §9
    """

    df = pd.read_csv(csv_file)

    disrupted = df[
        df["Active_Disruptions"].notna()
    ]

    return (
        disrupted[
            [
                "Supplier_ID",
                "Supplier_Name",
                "Risk_Level",
                "Active_Disruptions",
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )


if __name__ == "__main__":
    result = active_disruption_suppliers(
        "data/supplier_performance_data.csv"
    )

    print(result)