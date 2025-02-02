# Author: Frederic Dupoux
# Date : 1/14/2025
# Miami Dade College - COP 1047C

#  This program lets a user enter the number of 8x10
#  frames being purchased, it calculates and displays 
#  the price of the frames, the sales tax amount and 
#  the total amount due.

# creating constants for known values
FRAME_PRICE: float = 19.95 # price of one frame
TAX_RATE: float = 0.075 # 7.5%

# Input number of frames being purchased.
numberOfFrames: int = int(input("\nEnter the number of frames being purchased: "))

# Compute cost of frames being purchased
costOfFrames: float = FRAME_PRICE * numberOfFrames

# Compute sales tax
salesTax: float = (costOfFrames * TAX_RATE)

# Compute Total Amount Due
amountDue: float = costOfFrames + salesTax

# Display formatted cost of frames, sales tax and total amount due
print("\n")
print(f"Order details for {numberOfFrames} frames.\n")
print(f"Subtotal          ${costOfFrames:,.2f}")
print(f"Sales Tax         ${salesTax:,.2f}")
print("----------------------------")
print(f"Total due         ${amountDue:,.2f}")
print("\n")