# Practice_05
# Author: Frederic Dupoux
# Date : 3/19/25

# Create the OIP, Pseudo code for a program that will allow the user of Basket Plus to create a sequential file in Basket ID order. Following is the structure of each record:

# Basket ID 9999 (must be four digits, 1000-9999)
# Product Description x(25)
# Unit Price 99.99 (5.95-75.95)
# Quantity 999 (0-999)

# The program should validate all data input and provide a total of records created. A negative value for the Basket ID indicates the end of the creation process.


# Import modules to access functions
import Practice_05_module as bp

FILE_NAME: str = 'FD_basketplus_product_list.txt'


# Main Function to Create File
def CreateFile():
    # set total records to 0
    totalRecords: int = 0
    with open(FILE_NAME, 'w') as new_file:
    # with open(FILE_NAME, 'a') as new_file:
        # Input BasketID
        basketID: int = bp.InputValidBasketID()
        while basketID > 0:
            # Input Product Description
            productDescription: str = bp.InputProductDescription()
            # Input Unit Price
            unitPrice: float = bp.InputValidUnitPrice()
            # Input Quantity
            quantity: int = bp.InputValidateQuantity()
            # write ID
            new_file.write(str(basketID) + '\n')
            # write description
            new_file.write(productDescription + '\n')
            # write price
            new_file.write(str(unitPrice) + '\n')
            # write quantity
            new_file.write(str(quantity) + '\n')

            # Increment total records
            totalRecords += 1
            print('\nRecord Saved\n')
            # set previousID
            previousID: int = basketID
            # input BasketID to continue or exit loop
            basketID: int = bp.InputValidBasketID()
            # validate sequential basketID
            while basketID <= previousID and basketID >= 0:
                print(f'Invalid ID. BasketID# must be greater then {previousID}.')
                # input BasketID to continue or exit loop
                basketID: int = bp.InputValidBasketID()

    print(f'Total Records Saved: {totalRecords}')

# Call Create Function
CreateFile()