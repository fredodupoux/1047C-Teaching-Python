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
import Dupoux_Frederic_HW05_module as fd
from Dupoux_Frederic_HW05_config import (
    SENTINEL_VALUE
)
# Print welcome message to user
print("\n\n*********** Welcome to the Picture Framing Shop V2! ***********\n")

# Initializing value to get in the loop
numberOfFrames: int = 0
framePrice: float = 0.00

#WHILE - number of frames is not -1 get in Main Loop
while (numberOfFrames != SENTINEL_VALUE):
    # Input number of frames from user
    numberOfFrames: int = fd.InputNumberOfFrames()
    #IF - number of frame is not -1 stay in the loop
    if numberOfFrames != SENTINEL_VALUE:
        # Input price of frames from user
        framePrice: float = fd.InputFramePrice()
        #IF - frame price is not -1 continue with sale
        if framePrice != SENTINEL_VALUE:
            # call CalculateSales Function passing the two values collected
            fd.CalculateSales(numberOfFrames, framePrice)
        #ELSE
        else:
            # cancel sale without exiting program
            numberOfFrames = 0
            print("""
      *********** SALE CANCELLED *********** \n""")
        #ENDIF
    #ENDIF    
#ENDWHILE
# Call PrintTotalSales function when customer exits
fd.PrintTotalSales()