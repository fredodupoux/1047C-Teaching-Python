# HW004
# Author: Frederic Dupoux
# Date : 3/3/25

# This program lets a user input 
# the number and price of 8x10 frames a client will buy 
# and output the cost of the frames, 
# the discount amount, sales tax and total cost.
# It will cumulate all the sales until the user quits
# And it will output the total amount of customers, 
# total cost of frames, discount sales tax and grand total due.
# All using functions store in a module.

# Import modules to access functions
import Practice_04_module as fd
from Practice_04_config import (
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