# A single transaction record, represented with variables
customer_name = "Chidi Okafor"
transaction_amount = 15000
transaction_currency = "USD"
threshold = 10000

if transaction_amount > threshold:
    print(customer_name, "exceeded the reporting threshold")
else:
    print(customer_name, "is within normal limits")

#f-strings: embedding variables directly inside a text message
print(f"{customer_name} sent {transaction_amount} {transaction_currency}\n")

#Excercise 1
customer_name_2 = "Bunmi Akapo"
transaction_amount_2 = 15000
transaction_currency = "USD"
threshold = 20000

if transaction_amount_2 > threshold:
    print(customer_name_2, "exceeded the reporting threshold")
else:
    print(customer_name_2, "is within normal limits")

print(f"{customer_name_2} sent {transaction_amount_2} {transaction_currency}\n")

#Excercise 2
customer_name_3 = "Austin Akapo"
transaction_amount_3 = 20000
transaction_currency = "USD"
threshold = 20000

if transaction_amount_3 > threshold:
    print(customer_name_3, "exceeded the reporting threshold")
elif transaction_amount_3 == threshold:
    print(customer_name_3, "exactly at threshold")
else:
    print(customer_name_3, "is within normal limits")

print(f"{customer_name_3} sent {transaction_amount_3} {transaction_currency}")