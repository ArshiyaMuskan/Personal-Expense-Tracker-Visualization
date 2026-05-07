import pandas as pd

def load_data():

    df = pd.read_csv("data/expenses.csv")

    print("✅ Data loaded successfully!")

    return df


def clean_data(df):

    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = df["Date"].dt.strftime("%Y-%m")

    print("✅ Data cleaned successfully!")

    return df