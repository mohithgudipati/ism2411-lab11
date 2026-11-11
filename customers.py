#ISM2411 Lab 11

#REFLECTION

#1. I use brackets when the key needs to be inputed, like when placing a customers tier. If the bracket is missing then the error will tell me that something is wrong. If the key does not exist I would use .get(), for example if there is no email or phone number so thr program does not crash. My rule of thumb would be to use brackets iff they exist and use .get() if they do not.
#2. This reminded me of adding up totals with a function in categroires on Excel. This python method works way better because you can take huge datasets and have it run effectively and quicker. I can also use the same code on different data so that is helpful.




#EXERCISE 1

print("=== Exercise 1: One customer ===")
customer = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.75,
}
print("name:", customer["name"])
print("email:", customer["email"])
print("tier:", customer["tier"])
print("ytd_spend:", customer["ytd_spend"])
print(customer)

#EXERCISE 2

print("\n=== Exercise 2: Update and add ===")
customer["phone"] = "555-123-4567"  # add a new field
print("After adding phone:", customer)

customer["tier"] = "platinum"  # update a field
print("After updating tier:", customer)

del customer["email"]# delete a field
print("After deleting email:", customer)

#EXERCISE 3

print("\n=== Exercise 3: Safe lookup ===")
email = customer.get("email", "no email on file")
print("Using .get():", email)

try:
    email = customer["email"]
    print(email)
except KeyError:
    print("Using brackets: KeyError - 'email' key does not exist")

#EXERCISE 4

print("\n=== Exercise 4: Iterate ===")
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterating without .items():
for item in customer:
    print(item)
#The difference is looping over the dictionary without the .items() will only give back the keys. Using .items() gives me both the key and value. Without this i would need to input customer(item) into the code to get a value back.

#EXERCISE 5

print("\n=== Exercise 5: Lookup table ===")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final price on ${purchase}: ${final_price:.2f}")

#EXERCISE 6

print("\n=== Exercise 6: List of dicts ===")
customer1 = {"name": "Alice Johnson", "email": "alice@example.com",
             "tier": "platinum", "ytd_spend": 5200.00}
customer2 = {"name": "Ben Carter", "email": "ben@example.com",
             "tier": "silver", "ytd_spend": 840.50}
customer3 = {"name": "Priya Patel", "email": "priya@example.com",
             "tier": "gold", "ytd_spend": 2300.25}
customer4 = {"name": "Dan Lee", "email": "dan@example.com",
             "tier": "bronze", "ytd_spend": 150.00}

customers = [customer1, customer2, customer3, customer4]

purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} | {c['tier']} | discount on ${purchase}: ${discount_amount:.2f}")

#EXERCISE 7

print("\n=== Exercise 7: Nested catalog ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} (only {info['stock']} left)")

#EXERCISE 8

print("\n=== Exercise 8: Sales by region ===")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")