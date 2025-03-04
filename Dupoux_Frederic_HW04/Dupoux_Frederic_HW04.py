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
import modules as fd

# Print welcome message to user
print("\n\n*********** Welcome to the Picture Framing Shop V2! ***********\n")

# Initializing value to get in the loop
numberOfFrames: int = 0
framePrice: float = 0.00

#WHILE - number of frames is not -1 get in Main Loop
while (numberOfFrames != -1):
    # get number of frames from user
    numberOfFrames: int = fd.GetNumberOfFrames()
    #IF - number of frame is not -1 stay in the loop
    if numberOfFrames != -1:
        # get price of frames from user
        framePrice: float = fd.GetFramePrice()
        #IF - frame price is not -1 continue with sale
        if framePrice != -1:
            # call CalculateSales Function passing the two values collected
            fd.CalculateSales(numberOfFrames, framePrice)
        #ELSE
        else:
            # cancel sale without exiting program
            print("""
      *********** SALE CANCELLED *********** \n""")
            numberOfFrames = 0
        #ENDIF
    #ENDIF    
#ENDWHILE

# Call PrintTotalSales function when customer exits
fd.PrintTotalSales()