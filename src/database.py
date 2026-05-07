import sqlite3

def create_database():

    conn = sqlite3.connect("data/expenses.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        payment_method TEXT,
        description TEXT
    )
    """)

    conn.commit()

    print("✅ Database created!")

    return conn