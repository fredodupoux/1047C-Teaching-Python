#HW00C
# Author: Frederic Dupoux
# Date : 1/20/25

# Write a program to calculate the final
# cost of an object after a discount.
# Allow the user to enter the cost of the
# item and the discount rate. Display
# the original cost, amount of discount,
# and the final cost.


# Get Item's Original cost
originalCost: float = float(input("Enter the item's price: $"))
# Get Discount Rate
discountRate: float = float(input("Enter the discount rate: %"))
# Calculate Discount Amount
discountAmount: float = originalCost * discountRate / 100
# Calculate Final Cost
finalCost: float = originalCost - discountAmount
# Display Original Cost, Discount Amount and Final Cost.
print("\n")
print("Item's Cost Details")
print("-------------------")
print(f"Original Cost:      ${originalCost:.2f}")
print(f"Discount Amount:    ${discountAmount:.2f}")
print(f"Final Cost:         ${finalCost:.2f}")
print("\n")