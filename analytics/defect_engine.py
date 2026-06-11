import pandas as pd


def highest_average_defect_category(
    csv_file: str,
) -> pd.DataFrame:

    df = pd.read_csv(csv_file)

    category_defects = (
        df.groupby("Product_Category")[
            "Defect_Rate_Pct"
        ]
        .mean()
        .reset_index()
    )

    category_defects = category_defects.sort_values(
        by="Defect_Rate_Pct",
        ascending=False,
    )

    return category_defects.head(1)


if __name__ == "__main__":
    result = highest_average_defect_category(
        "data/supplier_performance_data.csv"
    )

    print(result)