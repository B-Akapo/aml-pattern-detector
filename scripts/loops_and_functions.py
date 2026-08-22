# a function to check transaction volume against threshold using for loop
# --------------------------------------------------
# Part 1: Use a function to check transactions
# --------------------------------------------------

def check_transaction(name, amount, threshold):
    if amount > threshold:
        print(f"{name}: {amount}, exceeds threshold")
    elif amount == threshold:
        print(f"{name}: {amount}, equals threshold")
    else:
        print(f"{name}: {amount}, is within threshold")

# Rewrite the three transactions using the function
check_transaction("Chidi Okafor", 15000, 10000)
check_transaction("Bunmi Akapo", 15000, 20000)
check_transaction("Austin Akapo", 20000, 20000)

# --------------------------------------------------
# Part 2: Use a for loop with 5 transaction amounts
# --------------------------------------------------

threshold = 20000

transactions = [15000, 8000, 20000, 5000, 30000]

for amount in transactions:
    if amount > threshold:
        print(f"{amount} exceeds threshold")
    elif amount == threshold:
        print(f"{amount} equals threshold")
    else:
        print(f"{amount} is within threshold")

# --------------------------------------------------
# Part 3: Combine tuples, a loop, and the function
# --------------------------------------------------

transactions = [
    ("Chidi", 15000),
    ("Bunmi", 8000),
    ("Austin", 20000),
    ("Ada", 5000),
    ("Emeka", 30000)
]

threshold = 20000

for name, amount in transactions:
    check_transaction(name, amount, threshold)