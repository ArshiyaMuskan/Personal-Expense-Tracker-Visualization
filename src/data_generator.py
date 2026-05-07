import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_expense_data():

    os.makedirs("data", exist_ok=True)

    categories = [
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Entertainment",
        "Health"
    ]

    payment_methods = [
        "Cash",
        "UPI",
        "Card"
    ]

    descriptions = [
        "Lunch",
        "Movie",
        "Groceries",
        "Bus Ticket",
        "Cab Ride",
        "Medicine",
        "Internet Bill",
        "Shoes"
    ]

    np.random.seed(42)

    start_date = datetime(2026, 1, 1)

    records = []

    for i in range(120):

        random_date = start_date + timedelta(
            days=np.random.randint(0, 90)
        )

        category = np.random.choice(categories)

        amount = np.random.randint(100, 3000)

        payment = np.random.choice(payment_methods)

        description = np.random.choice(descriptions)

        records.append([
            random_date.strftime("%Y-%m-%d"),
            category,
            amount,
            payment,
            description
        ])

    df = pd.DataFrame(records, columns=[
        "Date",
        "Category",
        "Amount",
        "Payment_Method",
        "Description"
    ])

    df.to_csv("data/expenses.csv", index=False)

    print("✅ Expense dataset created!")

    return df