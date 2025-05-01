# HW005 b
# Author: Frederic Dupoux
# Date : 4/21/25

# Create the OIP, Pseudo code for a program that will produce a report of the records in a column format with headings, Inventory Value (Unit Price * Quantity) column with total, and a total number of records read. You need to create the master file with the following data and include it in your homework folder.

FILE_NAME: str = 'FD_BasketPlus_Inventory.csv'

# Main Function to Read File
def ReadFile():
    try:
        # Open file
        with open(FILE_NAME, 'r') as file:
            # Read first Basket ID to prime loop
            csvRecord: int = file.readline()
            # Print Business Header
            print(f'\n\n\t{'*********** BASKET PLUS INVENTORY REPORT ***********':>57}\n')
            # Print Headers
            print(f'+{('-' * 79)}+')
            print(f'|{'Basket':^10}| {'Product':^27} | {'Unit':^10} | {'Inventory':^9} | {'Inventory':^12}|')
            print(f'|{'ID':^10}| {'Description':^27} | {'Price':^10} | {'Quantity':^9} | {'Value':^12}|')
            print(f'+{('-' * 79)}+')
            # Initialize Total Records
            totalRecords: int = 0
            # Initialize Total Inventory Value
            totalInventoryValue: float = 0
            # Do while Basket ID is not empty
            while csvRecord != '':
                # Strip end of Line
                csvRecord = csvRecord.rstrip('\n')
                # Split into Data List
                recordData = csvRecord.split(',')
                # Assign Basket ID
                basketID: int = int(recordData[0])
                # Assign Product Description
                productDescription = recordData[1]
                # Assign Unit Price
                unitPrice: float = float(recordData[2])
                # Assign Quantity
                quantity = int(recordData[3])

                # Compute Inventory Value
                inventoryValue: float = unitPrice * quantity 
                # Print Record (Basket ID, Description, Price, Quantity)
                print(f'|{basketID:^10}| {productDescription:<27} | {float(unitPrice):^10,.2f} |   {quantity:>4}    | ${inventoryValue:>10,.2f} |')
                # Increment Total Records
                totalRecords += 1
                # Sum Total Inventory Value
                totalInventoryValue += inventoryValue
                # Read next Basket ID
                csvRecord: int = file.readline()
            # End while
            # Display Total Records
            emptySpace: str = ''
            print(f'+{('-' * 79)}+')
            print(f'| Inventory File has {totalRecords} records.{emptySpace:9} |  Total Inventory Value:  ${totalInventoryValue:>10,.2f} |')
            print(f'+{('-' * 79)}+\n')
    except FileNotFoundError:
        print('Error: The file does not exist.')

# Call ReadFile Function
ReadFile()