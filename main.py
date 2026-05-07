from src.data_generator import generate_expense_data
from src.database import create_database
from src.data_loader import load_data, clean_data
from src.analysis import *
from src.visualization import *
from src.report_generator import generate_report

# ====================================================
# GENERATE DATA
# ====================================================

generate_expense_data()

# ====================================================
# DATABASE
# ====================================================

conn = create_database()

# ====================================================
# LOAD DATA
# ====================================================

df = load_data()

df = clean_data(df)

# ====================================================
# ANALYSIS
# ====================================================

category_data = category_analysis(df)

monthly_data = monthly_analysis(df)

payment_data = payment_analysis(df)

daily_data = daily_spending_analysis(df)

total = total_spending(df)

average = average_daily_spending(daily_data)

highest_category, highest_amount = highest_spending_category(
    category_data
)

# ====================================================
# VISUALIZATION
# ====================================================

category_chart(category_data)

monthly_chart(monthly_data)

payment_chart(payment_data)

daily_spending_chart(daily_data)

# ====================================================
# REPORT
# ====================================================

generate_report(
    total,
    average,
    highest_category
)

# ====================================================
# FINAL OUTPUT
# ====================================================

print("\n========== FINAL SUMMARY ==========")

print(f"Total Spending: ₹{total}")

print(f"Average Daily Spending: ₹{average:.2f}")

print(
    f"Highest Spending Category: {highest_category}"
)

print("===================================")

conn.close()