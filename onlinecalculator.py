print("Welcome to the Online Store Discount Calculator!")

# Ask user for purchase amount
amount = float(input("Enter total purchase amount: "))

# Determine discount
if amount > 5000:
    discount = 0.25
elif 3000 < amount <= 5000:
    discount = 0.15
elif 1000 < amount <= 3000:
    discount = 0.05
else:
    discount = 0.0

# Calculate values
discount_amount = amount * discount
final_price = amount - discount_amount

# Display results
print(f"Discount applied: {discount * 100}%")
print(f"Amount saved: KES {discount_amount:.2f}")
print(f"Final amount to pay: KES {final_price:.2f}")
