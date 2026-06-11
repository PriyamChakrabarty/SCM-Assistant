import pandas as pd


def get_swl_suppliers(csv_file: str) -> pd.DataFrame:
    """
    Policy §3.4

    Compliance Score < 60
    """

    df = pd.read_csv(csv_file)

    swl = df[df["Compliance_Score"] < 60]

    return (
        swl[
            [
                "Supplier_ID",
                "Supplier_Name",
                "Compliance_Score",
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )


if __name__ == "__main__":
    result = get_swl_suppliers(
        "data/supplier_performance_data.csv"
    )

    print(result)