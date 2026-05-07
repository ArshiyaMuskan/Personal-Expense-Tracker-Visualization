import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("images", exist_ok=True)

sns.set(style="whitegrid")


def category_chart(category_data):

    plt.figure(figsize=(10, 5))

    category_data.plot(kind="bar")

    plt.title("Category-wise Spending")

    plt.xlabel("Category")

    plt.ylabel("Amount")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "images/category_spending.png"
    )

    plt.close()

    print("✅ Category chart saved!")


def monthly_chart(monthly_data):

    plt.figure(figsize=(10, 5))

    monthly_data.plot(marker="o")

    plt.title("Monthly Spending Trend")

    plt.xlabel("Month")

    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig(
        "images/monthly_spending.png"
    )

    plt.close()

    print("✅ Monthly chart saved!")


def payment_chart(payment_data):

    plt.figure(figsize=(7, 7))

    payment_data.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Payment Method Distribution")

    plt.ylabel("")

    plt.tight_layout()

    plt.savefig(
        "images/payment_methods.png"
    )

    plt.close()

    print("✅ Payment chart saved!")


def daily_spending_chart(daily_data):

    plt.figure(figsize=(12, 5))

    daily_data.plot()

    plt.title("Daily Spending Trend")

    plt.xlabel("Date")

    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig(
        "images/daily_spending.png"
    )

    plt.close()

    print("✅ Daily spending chart saved!")