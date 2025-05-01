# Practice_06
# Author: Frederic Dupoux
# Date : 4/14/25

# Create a Python program that will allow the user to process an unknown of sales for individual salespersons using a List. 

# Allow the user to enter the salesperson's ID (2 digits, from 10-99) then the daily sales amount (0-10,000) for an unknown number of days. 

# Using the validation routines developed previously, validate the input fields. 
# When all the sales for a salesperson have been entered, then print the list of sales, determine and print the highest, lowest and the average amount of sales (MIN and MAX functions cannot be used). 
# Entering a negative number for sales should indicate the end of sales for that salesperson. Entering a negative number for salesperson's ID should stop the program.

# Extra Credit: Sort the salesperson's sales in order from highest to lowest and print the sorted list. You cannot use the Sort function. (10 pts)

# Import modules to access functions
import Practice_06_module as fd

# Print Welcome Message
print('\n***  Compute Employee\'s Daily Sales Summary ***\n')

# call inputValidUserID() to prompt user for salesPersonID
salesPersonID: int = fd.inputValidUserID()
# get in the loop
while salesPersonID != -1:
    # initialize dailySalesList[]
    dailySalesList = []
    # call inputDailySale() to Prompt User for dailySale Amount
    dailySale = fd.inputDailySale(salesPersonID)
    # get in loop
    while dailySale != -1:
        # add sale to list
        dailySalesList += [dailySale]
        # call inputDailySale() to Prompt User for dailySale Amount
        dailySale = fd.inputDailySale(salesPersonID)

    # store a copy of dailySalesList in a variable
    sortedSalesList = dailySalesList.copy()
    #  call sortSalesList() to sort list
    fd.sortSalesList(sortedSalesList)

    # Print Sales Summary for Employee if list is not empty
    if not dailySalesList:
        print(f'\nThere are no records for Sales Person #{salesPersonID}')

    else:

        print(f'\nSales summary for Sales Person #{salesPersonID}')
        print('-----------------------------------')
        # initialize index and totalSales value.
        index: int = 0
        totalSales: float = 0
        # Print list with a while loop
        while index < len(dailySalesList):
            sales = dailySalesList[index]
            print(f'Day {index + 1}:                 ${sales:10,.2f}')
            totalSales += sales
            # increment index
            index += 1

        # compute average sales
        averageSales = totalSales / len(dailySalesList)
        # print summary of daily sales
        print('-----------------------------------')
        print(f'Total:                 ${totalSales:10,.2f}')
        print()
        print(f'Average sales:         ${averageSales:10,.2f}')
        # get minimum value
        print(f'Lowest sales :         ${fd.getListMinimum(dailySalesList):10,.2f}')
        # get maximum value
        print(f'Highest sales:         ${fd.getListMaximum(dailySalesList):10,.2f}')
    
    # call inputValidUserID() to prompt user for salesPersonID
    print()
    salesPersonID: int = fd.inputValidUserID()

# exit
print('\n--- Program terminated. Good bye. ---\n')