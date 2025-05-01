# HW02
# Author: Frederic Dupoux
# Date : 1/27/25

# This program allows a user to input 
# the quantity of 8x10 frames he wants to purchase.
# It calculates and display the cost of the frames, 
# amount of discount based on the quantity being purchased, 
# net amount, the sales tax, and amount due.

# Define Known constants
FRAME_COST : float = 19.95
SALES_TAX_RATE : float = 0.075

# Get number of frames being purchased from user input
numberOfFrames : int = int(input("\nEnter the number of frames being purchased: "))

# Set discount rate based on number of frames
if 1 <= numberOfFrames <= 5:
    discountRate : float = 0.00
elif 6 <= numberOfFrames <= 10:
        discountRate : float = 0.05
elif 11 <= numberOfFrames <= 15:
        discountRate : float = 0.10
elif numberOfFrames > 15:
        discountRate : float = 0.15
else:
    print("Invalid number of frames entered.")
    exit()

# Calculate cost of frames
costOfFrames : float = FRAME_COST * numberOfFrames

# Calculate discount amount
discountAmount : float = costOfFrames * discountRate

# Calculate net amount
netAmount : float = costOfFrames - discountAmount

# Calculate Sales Tax
salesTax : float = netAmount * SALES_TAX_RATE

# Calculate Amount Due
amountDue : float = netAmount + salesTax

# Display formatted output
print("\n")
print(f"Order details for {numberOfFrames} frames.\n")
print(f"Cost of frames:             ${costOfFrames:>10,.2f}")

# Display discount and net amount only if discount is applied
if numberOfFrames > 5:
    print(f"Discount: {int(discountRate*100):<2}%               ${discountAmount:>10,.2f}")
    print(f"Net Amount:                 ${netAmount:>10,.2f}")

# Display Sales Tax and Total Amount Due
print(f"Sales Tax:                  ${salesTax:>10,.2f}")
print("----------------------------------------")
print(f"Total due:                  ${amountDue:>10,.2f}")
print("\n")