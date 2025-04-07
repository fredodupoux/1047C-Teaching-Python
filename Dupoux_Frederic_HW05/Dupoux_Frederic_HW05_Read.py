# HW005 b
# Author: Frederic Dupoux
# Date : 3/19/25

# Create the OIP, Pseudo code for a program that will produce a report of the records in a column format with headings, Inventory Value (Unit Price * Quantity) column with total, and a total number of records read. You need to create the master file with the following data and include it in your homework folder.

FILE_NAME: str = "FD_basketplus_product_list.txt"

# Main Function to Read File
def ReadFile():
    try:
        # Open file
        with open(FILE_NAME, "r") as file:
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
            print(f"{FILE_NAME} file has a total of {totalRecords} records.\n")            
    except FileNotFoundError:
        print("Error: The file does not exist.")

# Call ReadFile Function
# ReadFile()