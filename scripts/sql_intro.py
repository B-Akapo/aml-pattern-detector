import sqlite3
# sqlite3 is a lightweight database engine built into Python — no server,
#  no install.

# Create an in-memory database (exists only while the script runs — fine for practice)
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create a table — like defining spreadsheet column headers, but for a real database
cursor.execute("""
    CREATE TABLE transactions (
        customer TEXT,
        amount INTEGER,
        currency TEXT,
        country TEXT
    )
""")

# Insert rows — same data you've already used
transactions = [
    ("Chidi Okafor", 15000, "USD", "NG"),
    ("Bunmi Akapo", 8000, "USD", "NG"),
    ("Austin Akapo", 20000, "USD", "UK"),
    ("Gabriel Akapo", 6000, "USD", "CHN"),
    ("Bologi Stephen", 25000, "USD", "CHN"),
]
cursor.executemany("INSERT INTO transactions VALUES (?, ?, ?, ?)", transactions)

# SELECT * = "give me every column"; FROM transactions = "from this table"
cursor.execute("SELECT * FROM transactions")
print(cursor.fetchall())  # fetchall() pulls all matching rows back as a list

print()

# WHERE filters rows — this is the SQL equivalent of your df[df["amount"] > 10000] line
cursor.execute("SELECT customer, amount FROM transactions WHERE amount > 10000")
print(cursor.fetchall())

print()

# GROUP BY + aggregate functions — total amount per country
cursor.execute("""
    SELECT country, SUM(amount) as total_amount
    FROM transactions
    GROUP BY country
""")
print(cursor.fetchall())

# Average transaction amount per currency
cursor.execute("""
    SELECT currency, AVG(amount) as average_amount
    FROM transactions
    GROUP BY currency
""")
print(cursor.fetchall())

# COUNT(*) — number of transactions per country
cursor.execute("""
    SELECT country, COUNT(*) as transaction_count
    FROM transactions
    GROUP BY country
""")
print(cursor.fetchall())

# Total amount per country, only for transactions over 5000
cursor.execute("""
    SELECT country, SUM(amount) as total_amount
    FROM transactions
    WHERE amount > 5000
    GROUP BY country
""")
print(cursor.fetchall())

conn.close()