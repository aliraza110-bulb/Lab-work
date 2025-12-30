# Task #2
# Scenario:
# A delivery company wants to optimize its shipping cost calculations.
# They charge customers based on package weight and distance using the following formula:   

# Shipping Cost=Base Cost+(Weight×Weight Rate)+(Distance×Distance Rate)
# Where:
# Base Cost = $50
# Weight Rate = $10 per kg
# Distance Rate = $5 per km
# You’re Task:
# Write a Python function calculate_shipping_cost(weight, distance) that takes:
# weight (kg) of the package
# distance (km) the package will be shipped
# Returns the total shipping cost based on the formula.
# The company offers a discount:
# If the total shipping cost is above $500, apply a 15% discount.
# If the cost is between $300 and $500, apply a 10% discount.
# Otherwise, no discount.
# Implement another function apply_discount(cost) that:
# Takes the total cost as input.
# Applies the correct discount.
# Returns the final discounted cost.
# Write a Python program that:
# Asks the user to input weight and distance.
# Calls calculate_shipping_cost() to compute the initial cost.
# Calls apply_discount() to adjust the cost if applicable.
# Displays the final amount the customer must pay.
# Task Description:
# Develop a Python program that calculates shipping costs based on package weight and distance.

Base_Cost = 50
Weight_Rate = 10
Distance_Rate = 5

def calculate_shipping_cost(weight,distance):
    Shipping_Cost=Base_Cost+(weight*Weight_Rate)+(distance*Distance_Rate)
    return Shipping_Cost

def apply_discount(cost):
    if cost > 500:
        return cost *0.85
    elif 300>= cost <=500:
        return cost *0.90
    else :
        return cost
    
weight=float(input("Enter The weight :"))
distance=float(input("Enter the distance :"))

initial_cost=calculate_shipping_cost(weight,distance)
final_cost=apply_discount(initial_cost)

print(f"The final cost is :{final_cost:.2f}")