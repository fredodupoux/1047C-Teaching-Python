# HW003
# Author: Frederic Dupoux
# Date : 2/15/25

# This program lets a user input the number and price of 8x10 frames a client will buy 
# and output the cost of the frames, the discount amount, sales tax and total cost of the frames
# It will cumulate all the sales until the user quits, and will output the total amount
# of customers, total cost of frames, discount sales tax and grand total due.

# Define Sales Tax 75%
SALES_TAX_RATE: float = 0.075
# Define price Ranges
PRICE_RANGE_MIN: float = 16.95
PRICE_RANGE_MAX: float = 25.95
# Define Frame Range
MIN_FRAME: int = 1
MAX_FRAME: int = 75
# Initialize Total Number Of Customer = 0
totalNumberOfCustomer: int = 0
# Initialize Total Number Of Frames = 0
totalNumberOfFrames: int = 0
# Initialize Total Cost Of Frames = 0
totalCostOfFrames: float = 0.0
# Initialize Total Discount = 0
totalDiscount: float = 0.0
# Initialize Total Sales Tax = 0
totalSalesTax: float = 0.0
# Initialize Total Amount Due = 0
totalAmountDue: float = 0.0

# Print welcome message to user
print("\n\n*********** Welcome to the Picture Framing Shop! ***********\n")

# prime value to get in the loop
validNumberOfFrames: bool = True

# WHILE Number of Frames is NOT valid
while validNumberOfFrames:
    #TRY
    try:
        #PROMPT: Input Number Of Frames: Sentinel value <= 0
        numberOfFrames: int = int(input("Enter the number of frames being purchased or -1 to quit: "))
        #IF - Check for Sentinel value
        if numberOfFrames <= 0:
            validNumberOfFrames = False # exit the loop and quit
        #ELSE
        else:
            #IF - Validate Range    
            if numberOfFrames not in range(MIN_FRAME, MAX_FRAME + 1):
                print(f"Please enter a number in the range of {MIN_FRAME} to {MAX_FRAME} frames: ")
            #ELSE    
            else:
                #Determine Discount Rate based on Number of Frames
                #IF
                if 1 <= numberOfFrames <= 5:
                    discountRate : float = 0.00
                elif 6 <= numberOfFrames <= 10:
                    discountRate : float = 0.05
                elif 11 <= numberOfFrames <= 15:
                    discountRate : float = 0.10
                #ELSE
                else :
                    discountRate : float = 0.15
                #Exit the loop.
                validNumberOfFrames = False
            #ENDIF
        #ENDIF  
    #EXCEPTION
    except:
        #Stay in the loop and print non numeric error message
        print("Please input only numeric values.")
#END WHILE

#WHILE Number of Frames > 0
while numberOfFrames > 0:
    #TRY
    try:
        # Set value to get in the loop
        validFramePrice: bool = True
        #WHILE frame price is NOT valid
        while validFramePrice:
            #TRY
            try:
                #PROMPT: Input Price of Frame
                framePrice: float = float(input("Enter the price for the frames: "))
                #IF - Validate frame price range
                if framePrice < PRICE_RANGE_MIN or framePrice > PRICE_RANGE_MAX:
                    print(f"Enter a valid price ranging from {PRICE_RANGE_MIN} to {PRICE_RANGE_MAX}")
                #ELSE
                else :
                    #Calculate Cost Of Frames (Number of Frames * Price of Frames)
                    costOfFrames: float = framePrice * numberOfFrames
                    # Calculate discount amount
                    discountAmount : float = costOfFrames * discountRate
                    # Calculate net amount
                    netAmount : float = costOfFrames - discountAmount
                    # Calculate Sales Tax
                    salesTax : float = netAmount * SALES_TAX_RATE
                    # Calculate Amount Due
                    amountDue : float = netAmount + salesTax
                    # Print and Display formatted output
                    print("\n")
                    print(f"Order details for {numberOfFrames} frames priced at ${framePrice}\n")
                    print(f"Cost of frames:             ${costOfFrames:>10,.2f}")
                    # Display discount and net amount only if discount is applied
                    if numberOfFrames > 5:
                        print(f"Discount: {int(discountRate*100):<2}%               ${discountAmount:>10,.2f}")
                        print(f"Net Amount:                 ${netAmount:>10,.2f}")
                    # Display Sales Tax and Total Amount Due
                    print(f"Sales Tax:                  ${salesTax:>10,.2f}")
                    print("----------------------------------------")
                    print(f"Total due:                  ${amountDue:>10,.2f}")
                    print("\n")
                    # Exit Frame Price loop
                    validFramePrice = False
                #ENDIF
            #Catch Exceptions:
            except:
                #Stay in the price loop and print non numeric error message
                print("Please input only numeric values.")
        #ENDWHILE 

        #Accumulte Totals
        totalNumberOfCustomer += 1
        totalNumberOfFrames += numberOfFrames
        totalCostOfFrames += costOfFrames
        totalDiscount += discountAmount
        totalSalesTax += salesTax
        totalAmountDue += amountDue

        # prime value to get in the loop
        validNumberOfFrames = True
        # WHILE: number of frames is not valid
        while validNumberOfFrames:
            #TRY
            try:
                #PROMPT: Input Number Of Frames any number less then zero closes the program
                numberOfFrames = int(input("Enter -1 to end sales or the number of frames being purchased: "))
                #IF - check Sentinel value
                if numberOfFrames <= 0:
                    # exit loop
                    validNumberOfFrames = False
                #ELSE 
                else:
                    #IF - Validate range of frames
                    if numberOfFrames in range(MIN_FRAME, MAX_FRAME+1):
                        #reset valid number of frames to exit loop
                        validNumberOfFrames = False
                        #Determine Discount Rate based on Number of Frames
                        # IF
                        if 1 <= numberOfFrames <= 5:
                            discountRate : float = 0.00
                        elif 6 <= numberOfFrames <= 10:
                            discountRate : float = 0.05
                        elif 11 <= numberOfFrames <= 15:
                            discountRate : float = 0.10
                        # ELSE
                        else :
                            discountRate : float = 0.15
                        #ENDIF
                    #ELSE - Input valid range.
                    else: 
                        print(f"Enter a number between {MIN_FRAME} and {MAX_FRAME} frames.")
                    #ENDIF
            #Catch Exception
            except:
                #Print non numeric error message
                print("Please input only numeric values.")
        #END WHILE
    #Catch Exception
    except:
        #Print non numeric error message
        print("Please input only numeric values.")
#END WHILE

#IF customer Close Sales
if totalNumberOfCustomer > 0:
    print("""
      *********** CLOSING SALES ***********
                    *********

      """)
    # Print Final Total Accumulators
    # Display formatted output
    print("SALE SUMMARY")
    print("--------------------------------------------")
    print(f"Total number of customers:       {totalNumberOfCustomer:>10}")
    print(f"Total number of frames:          {totalNumberOfFrames:>10}")
    print("--------------------------------------------")
    print(f"Total Cost of frames:           ${totalCostOfFrames:>10,.2f}")
    # Display discount and net amount only if discount is applied
    if totalDiscount > 0:
        print(f"Total Discount:                 ${totalDiscount:>10,.2f}")
    # Display Sales Tax and Total Amount Due
    print(f"Total Sales Tax:                ${totalSalesTax:>10,.2f}")
    print("--------------------------------------------")
    print(f"GRAND TOTAL DUE:                ${totalAmountDue:>10,.2f}")
    print("\n")
#ELSE quit and no print
else: 
    print("""
      *********** BYE ***********

      """)
#ENDIF