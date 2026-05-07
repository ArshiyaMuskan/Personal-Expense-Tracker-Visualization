import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.analysis import (
    category_analysis,
    monthly_analysis,
    payment_analysis,
    daily_spending_analysis,
    total_spending,
    average_daily_spending,
    highest_spending_category
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================

st.title("💰 Personal Expense Tracker Dashboard")

st.markdown(
    "Track, analyze, and visualize your expenses using Python and Streamlit."
)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_expense_data():

    df = pd.read_csv("data/expenses.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = df["Date"].dt.strftime("%Y-%m")

    return df

df = load_expense_data()

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("📌 Filters")

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Select Payment Method",
    options=df["Payment_Method"].unique(),
    default=df["Payment_Method"].unique()
)

filtered_df = df[
    (df["Category"].isin(category_filter)) &
    (df["Payment_Method"].isin(payment_filter))
]

# =========================================================
# METRICS
# =========================================================

category_data = category_analysis(filtered_df)

monthly_data = monthly_analysis(filtered_df)

payment_data = payment_analysis(filtered_df)

daily_data = daily_spending_analysis(filtered_df)

total = total_spending(filtered_df)

average = average_daily_spending(daily_data)

highest_category, highest_amount = highest_spending_category(
    category_data
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "💵 Total Spending",
    f"₹{total:,.2f}"
)

col2.metric(
    "📊 Average Daily Spending",
    f"₹{average:,.2f}"
)

col3.metric(
    "🔥 Highest Spending Category",
    highest_category
)

# =========================================================
# CATEGORY-WISE BAR CHART
# =========================================================

st.subheader("📌 Category-wise Spending")

fig1, ax1 = plt.subplots(figsize=(8, 4))

category_data.plot(
    kind="bar",
    ax=ax1
)

ax1.set_xlabel("Category")

ax1.set_ylabel("Amount")

ax1.set_title("Category-wise Spending")

plt.xticks(rotation=45)

st.pyplot(fig1)

# =========================================================
# MONTHLY TREND CHART
# =========================================================

st.subheader("📈 Monthly Spending Trend")

fig2, ax2 = plt.subplots(figsize=(8, 4))

monthly_data.plot(
    marker="o",
    ax=ax2
)

ax2.set_xlabel("Month")

ax2.set_ylabel("Amount")

ax2.set_title("Monthly Spending")

st.pyplot(fig2)

# =========================================================
# PAYMENT METHOD PIE CHART
# =========================================================

st.subheader("💳 Payment Method Distribution")

fig3, ax3 = plt.subplots(figsize=(6, 6))

payment_data.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax3
)

ax3.set_ylabel("")

st.pyplot(fig3)

# =========================================================
# DAILY SPENDING TREND
# =========================================================

st.subheader("📅 Daily Spending Trend")

fig4, ax4 = plt.subplots(figsize=(10, 4))

daily_data.plot(ax=ax4)

ax4.set_xlabel("Date")

ax4.set_ylabel("Amount")

ax4.set_title("Daily Spending")

st.pyplot(fig4)

# =========================================================
# DATASET PREVIEW
# =========================================================

st.subheader("🗂 Expense Dataset Preview")

st.dataframe(filtered_df)

# =========================================================
# DOWNLOAD REPORT
# =========================================================

st.subheader("⬇ Download Expense Report")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="expense_report.csv",
    mime="text/csv"
)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    "Built with ❤️ using Python, Pandas, Matplotlib, and Streamlit"
)