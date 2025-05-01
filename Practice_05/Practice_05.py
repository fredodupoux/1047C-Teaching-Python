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
import Practice_05_Create as create
import Practice_05_List as read

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
            create.CreateFile()
        if menu == 2:
            # Call the function to read and display the file
            read.ReadFile()
        if menu == 0:
            exit()
    print("Bye!")

# Call the main function.
if __name__ == '__main__':
    main()