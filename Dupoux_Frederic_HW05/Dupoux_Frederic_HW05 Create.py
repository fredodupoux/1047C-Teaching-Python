# HW005 a
# Author: Frederic Dupoux
# Date : 3/19/25

# Create the OIP, Pseudo code for two programs that will allow the user of Basket Plus to create (program 1) and list (program2) a sequential file in Basket ID order.
# Following is the structure of each record:

# Basket ID 9999 (must be four digits, 1000-9999)
# Product Description x(25)
# Unit Price 99.99 (5.95-75.95)
# Quantity 999 (0-999)

# The create program should validate all data and provide a total of records created. In the creation program, a negative value for the Basket ID indicates the end of the creation process.

# Import modules to access functions
import Dupoux_Frederic_HW05_module as bp
totalRecords: int = 0

# Main Function to Create File
def CreateFile():
    global totalRecords
    with open("Basketplus_product_list.txt", "w") as new_file:
        basketID: int = bp.InputValidBasketID()
        while basketID > 0:
            productDescription: str = bp.InputProductDescription()
            unitPrice: float = bp.InputValidUnitPrice()
            quantity: int = bp.InputValidateQuantity()
            # write to file
            new_file.write(str(basketID) + "\n")
            new_file.write(productDescription + "\n")
            new_file.write(str(unitPrice) + "\n")
            new_file.write(str(quantity) + "\n")
            # Increment Totals
            totalRecords += 1
            # Continue with loop
            previousID: int = basketID
            basketID: int = bp.InputValidBasketID()
            while basketID <= previousID and basketID >= 0:
                print(f"Invalid ID. BasketID# must be greater then {previousID}.")
                basketID: int = bp.InputValidBasketID()

    print(f"Total Records Saved: {totalRecords}")

# Call Create Function
CreateFile()