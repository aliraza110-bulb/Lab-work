item_price = "19.90", "50.98", "47.00"

discount_rate = 0.10
subtotal = 0.0

for price in item_price:
    price_in_no = float(price)
    print("Price in numbers:", price_in_no)
    subtotal += price_in_no

print("Subtotal:", f"{subtotal:.2f}")

discount_amount = discount_rate * subtotal
print("Discount amount:", f"{discount_amount:.2f}")

final_amount = subtotal - discount_amount
print("Final amount:", f"{final_amount:.2f}")
