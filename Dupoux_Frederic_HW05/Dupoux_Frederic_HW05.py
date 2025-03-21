# HW005
# Author: Frederic Dupoux
# Date : 3/17/25

# Create the OIP, Pseudo code for two programs that will allow the user of Basket Plus to create (program 1) and list (program2) a sequential file in Basket ID order.
# Following is the structure of each record:

# Basket ID 9999 (must be four digits, 1000-9999)
# Product Description x(25)
# Unit Price 99.99 (5.95-75.95)
# Quantity 999 (0-999)

# The create program should validate all data and provide a total of records created. In the creation program, a negative value for the Basket ID indicates the end of the creation process.

# The list program should produce a report of the records in a column format with headings, Inventory Value (Unit Price * Quantity) column with total, and a total number of records read. You need to create the master file with the following data and include it in your homework folder.

# Import modules to access functions
import Dupoux_Frederic_HW05_module as bp
totalRecords: int = 0


# Main Function to Create File
def CreateFile():
    global totalRecords
    with open("basketplus_product_data.txt", "w") as new_file:
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

# Main Function to Read File
def ReadFile():
    try:
        # Open file
        with open("basketplus_product_data.txt", "r") as file:
            # Read first Basket ID to prime loop
            basketID: int = file.readline()
            # Print Headers
            print(f"\n{"Basket ID":^10} | {"Product Description":^27} | {"Unit Price":^10} | {"Quantity":^9} | {"Value":^12}")
            print("---------------------------------------------------------------------------------")
            # Initialize Total Records
            totalRecords: int = 0
            # Do while Basket ID is not empty
            while basketID != "":
                # 	Prepare Basket ID to print
                basketID = basketID.rstrip("\n")
                # Read Product Description
                productDescription = file.readline()
                # Prepare Product Description to print
                productDescription = productDescription.rstrip("\n")
                # Read Unit Price
                unitPrice = file.readline()
                # Prepare Unit Price to print
                unitPrice = unitPrice.rstrip("\n")
                # Read Quantity
                quantity = file.readline()
                # Prepare Quantity to print
                quantity = quantity.rstrip("\n")
                # Compute Inventory Value
                inventoryValue: float = float(unitPrice) * float(quantity) 
                # Print Record (Basket ID, Description, Price, Quantity)
                print(f"{basketID:^10} | {productDescription:<27} | {float(unitPrice):^10,.2f} | {quantity:^9} | ${inventoryValue:>11,.2f}")
                # Increment Total Records
                totalRecords += 1
                # Read next Basket ID
                basketID: int = file.readline()
            # End while
            # Display Total Records
            print("---------------------------------------------------------------------------------\n")
            print(f"basketplus_product_data.txt file has {totalRecords} records.\n")            
    except FileNotFoundError:
        print("Error: The file does not exist.")


def main():
    # Print welcome message to user
    print("\n\n*********** Welcome to Basket Plus! ***********\n")
    menu: int = 9
    while menu != 0:
        menu = int(input(
    '''1. Enter 1 to Create a file,
2. Enter 2 to read your file, 
0. Enter 0 to exit: '''
            ))
        if menu == 1:
            # Call the function to create the file
            CreateFile()
        if menu == 2:
            # Call the function to read and display the file
            ReadFile()
        if menu == 0:
            exit()
    print("Bye!")

# Call the main function.
if __name__ == '__main__':
    main()