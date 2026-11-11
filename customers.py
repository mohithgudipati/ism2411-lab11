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