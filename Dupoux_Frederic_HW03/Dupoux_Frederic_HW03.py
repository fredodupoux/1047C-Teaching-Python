# HW003
# Author: Frederic Dupoux
# Date : 2/24/25

# This program lets a user input the number and price of 8x10 frames a client will buy 
# and output the cost of the frames, the discount amount, sales tax and total cost of the frames
# It will cumulate all the sales until the user quits, and will output the total amount
# of customers, total cost of frames, discount sales tax and grand total due.

# Define Sales Tax 7.5%
SALES_TAX_RATE: float = 0.075
# Define price Ranges
PRICE_RANGE_MIN: float = 16.95
PRICE_RANGE_MAX: float = 25.95
# Define Frame Range
MIN_FRAME: int = 1
MAX_FRAME: int = 75
# Define Discount Brackets
DISCOUNT_5: int = 5
DISCOUNT_10: int = 10
DISCOUNT_15: int = 15
# Define Discount Value
DISCOUNT_5_VALUE: float = 0.05
DISCOUNT_10_VALUE: float = 0.10
DISCOUNT_15_VALUE: float = 0.15



# Initialize Totals
totalNumberOfCustomer: int = 0
totalNumberOfFrames: int = 0
totalCostOfFrames: float = 0.0
totalDiscount: float = 0.0
totalSalesTax: float = 0.0
totalAmountDue: float = 0.0

# Print welcome message to user
print("\n\n*********** Welcome to the Picture Framing Shop! ***********\n")

# Initializing values before getting in the loop
discountRate: float = 0.00 
validFramePrice: bool = False 
numberOfFrames: int = 0

# Main Loop
while numberOfFrames != -1:
    try:
        # Input number of frames
        numberOfFrames: int = int(
            input("Enter -1 to end sales or the number of frames being purchased: "))
        # Validate Sentinel values
        if numberOfFrames != -1:          
            # Validate range of frames
            if numberOfFrames not in range(MIN_FRAME, MAX_FRAME+1):
                print(f"Please enter a number in the range of {MIN_FRAME} to {MAX_FRAME} frames.")
            # Determine Discount Rate based on Number of Frames
            else: 
                if numberOfFrames > DISCOUNT_15:
                    discountRate: float = DISCOUNT_15_VALUE
                elif numberOfFrames > DISCOUNT_10:
                    discountRate: float = DISCOUNT_10_VALUE
                elif numberOfFrames > DISCOUNT_5:
                    discountRate: float = DISCOUNT_5_VALUE
                else :
                    discountRate: float = 0

                # Prime Value to get in next Loop
                validFramePrice: bool = True

            # frame price loop
            while validFramePrice:
                try:
                    # Input Price of Frame
                    framePrice: float = float(input("Enter the price for the frames: "))
                    # Validate frame price range
                    if framePrice < PRICE_RANGE_MIN or framePrice > PRICE_RANGE_MAX:
                        print(f"Enter a valid price ranging from {PRICE_RANGE_MIN} to {PRICE_RANGE_MAX}")
                    else :
                        #Calculate sales 
                        costOfFrames: float = framePrice * numberOfFrames
                        discountAmount: float = costOfFrames * discountRate
                        netAmount: float = costOfFrames - discountAmount
                        salesTax: float = netAmount * SALES_TAX_RATE
                        amountDue: float = netAmount + salesTax

                        # Print and Display formatted output
                        print("\n")
                        print(f"Order details for {numberOfFrames} frames priced at ${framePrice:.2f}\n")
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

                        #Accumulte Totals
                        totalNumberOfCustomer += 1
                        totalNumberOfFrames += numberOfFrames
                        totalCostOfFrames += costOfFrames
                        totalDiscount += discountAmount
                        totalSalesTax += salesTax
                        totalAmountDue += amountDue
                        # Exit current loop
                        validFramePrice = False
                except:
                    #Stay in the price loop and print non numeric error message
                    print("Please input only numeric values for the price of frames.")       
    except:
        #Print non numeric error message
        print("Please input only numeric values for the number of frames.")

# Back to main. If customer Close Sales
if totalNumberOfCustomer <= 0:
    print("""
      *********** BYE ***********

      """)
else: 
    print("""
      *********** CLOSING SALES ***********
                    *********

      """)
    # Print Final Total Accumulators
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
