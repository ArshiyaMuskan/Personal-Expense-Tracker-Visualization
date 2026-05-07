def category_analysis(df):

    result = df.groupby("Category")["Amount"].sum()

    return result


def monthly_analysis(df):

    result = df.groupby("Month")["Amount"].sum()

    return result


def payment_analysis(df):

    result = df.groupby(
        "Payment_Method"
    )["Amount"].sum()

    return result


def daily_spending_analysis(df):

    result = df.groupby("Date")["Amount"].sum()

    return result


def total_spending(df):

    return df["Amount"].sum()


def average_daily_spending(daily_spending):

    return daily_spending.mean()


def highest_spending_category(category_data):

    category = category_data.idxmax()

    amount = category_data.max()

    return category, amount