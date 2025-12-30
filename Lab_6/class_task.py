#E-commerce Checkout System
# You are developing a checkout system for an e-commerce platform. The system needs to calculate the total price of items in a shopping cart, applying discounts and taxes. How would you design a function that takes a list of item prices, a discount rate, and a tax rate, and returns the final total?

# Objective: Create a function to calculate the total price of items in a shopping cart, including discounts and taxes.

# Instructions:
# Define a function named calculate_total that accepts three parameters: prices (a list of item prices), discount_rate (a percentage discount), and tax_rate (a percentage tax).
# Calculate the subtotal by summing the prices.
# Apply the discount to the subtotal.
# Calculate the tax on the discounted total.
# Return the final total rounded to two decimal places.

def calculate_total(prices,discount_rate,tax_rate):
    sub_total=sum(prices)
    discounted_total=sub_total*(1-discount_rate/100)
    final_total=discounted_total*(1+tax_rate/100)
    return final_total

cart=[100,50,25]
print("Total is",calculate_total(cart,discount_rate=10,tax_rate=5))