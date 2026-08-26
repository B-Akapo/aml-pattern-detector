import pandas as pd
# "import" brings in the pandas library. "as pd" gives it a short nickname
# so we type pd.something() instead of pandas.something() every time.

transactions = [
    {"customer": "Chidi Okafor", "amount": 15000, "currency": "USD", "country":"NG"},
    {"customer": "Bunmi Akapo", "amount": 8000, "currency": "USD", "country":"NG"},
    {"customer": "Austin Akapo", "amount": 20000, "currency": "USD", "country":"UK"},
    {"customer": "Gabriel Akapo", "amount": 6000, "currency": "USD", "country":"CHN"},
    {"customer": "Bologi Stephen", "amount": 25000, "currency": "USD", "country":"CHN"},
]

df = pd.DataFrame(transactions)
# Converts our list of dictionaries into a DataFrame — pandas's spreadsheet-like table.
# "df" is a very common short name for "DataFrame" in Python code.

print(df)
# Displays the whole table.

print()

print(df[df["country"] == "NG"])
# Confirms the "country" that are "NG"

print()

print(df["amount"].sum())
#prints total transaction volume

print(df["amount"].mean())
#prints the mean of all the transactions

print()

flagged = df[df["amount"] > 10000]
# Filters the table to only rows where amount > 10000.
# This is the pandas equivalent of a WHERE clause in SQL.

print(flagged)