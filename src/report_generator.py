import pandas as pd
import os

os.makedirs("outputs", exist_ok=True)

os.makedirs("reports", exist_ok=True)

def generate_report(
    total_spending,
    average_daily_spending,
    highest_category
):

    report_df = pd.DataFrame({
        "Metric": [
            "Total Spending",
            "Average Daily Spending",
            "Highest Spending Category"
        ],
        "Value": [
            total_spending,
            round(average_daily_spending, 2),
            highest_category
        ]
    })

    report_df.to_csv(
        "outputs/final_report.csv",
        index=False
    )

    with open(
        "reports/expense_report.txt",
        "w"
    ) as file:

        file.write(
            "PERSONAL EXPENSE TRACKER REPORT\n"
        )

        file.write("=" * 40 + "\n\n")

        file.write(
            f"Total Spending: ₹{total_spending}\n"
        )

        file.write(
            f"Average Daily Spending: ₹{average_daily_spending:.2f}\n"
        )

        file.write(
            f"Highest Spending Category: {highest_category}\n"
        )

    print("✅ Reports generated successfully!")