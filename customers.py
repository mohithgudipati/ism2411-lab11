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
customer["phone"] = "555-123-4567"      # add a new field
print("After adding phone:", customer)

customer["tier"] = "platinum"           # update a field
print("After updating tier:", customer)

del customer["email"]                   # delete a field
print("After deleting email:", customer)