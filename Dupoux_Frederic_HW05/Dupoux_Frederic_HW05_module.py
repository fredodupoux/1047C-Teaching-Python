# *_module.py
#import configuration file with business constants
from Dupoux_Frederic_HW05_config import (
    SALES_TAX_RATE,
    MIN_FRAME,
    MAX_FRAME,
    DISCOUNT_5,
    DISCOUNT_10,
    DISCOUNT_15,
    DISCOUNT_5_VALUE,
    DISCOUNT_10_VALUE,
    DISCOUNT_15_VALUE,
    PRICE_RANGE_MAX,
    PRICE_RANGE_MIN,
    SENTINEL_VALUE
)

# Initialize Global Accumulators
totalNumberOfCustomer: int = 0
totalNumberOfFrames: int = 0
totalCostOfFrames: float = 0.00
totalDiscount: float = 0.00
totalSalesTax: float = 0.00
totalAmountDue: float = 0.00

# --- Get Valid Input ---
# def getValidInput()
    

# --- Input Number Of Frames with validation ---
def InputNumberOfFrames():
    # value priming
    numberOfFrames: int = 0
    validNumberOfFrames: bool = False

    while not validNumberOfFrames:
        try:
            # Prompt Input number of frames
            numberOfFrames: int = int(
                input(
                    "Enter -1 to close sales or \nenter the number of frames being purchased: "
                )
            )
            # Set value to true
            validNumberOfFrames = True
            # check input for sentinel
            if numberOfFrames != SENTINEL_VALUE:
                # validate range of frames
                if numberOfFrames not in range(MIN_FRAME, MAX_FRAME + 1):
                    print(
                        f"Please enter a number in the range of {MIN_FRAME} to {MAX_FRAME} frames."
                    )
                    # Set value to false if incorrect
                    validNumberOfFrames = False
        except ValueError:
            # catch errors and print nonnumeric error message
            print("Input only numeric values. Please try again!")
    return numberOfFrames

# --- Input Frame Price with validation ---
def InputFramePrice():
    # value priming
    framePrice: float = 0.00
    validFramePrice: bool = False

    while not validFramePrice:
        try:
            # Prompt Input Price of Frame
            framePrice: float = float(
                input(
                    "\nEnter -1 to cancel this sale or \nenter the price for the frames being purchased: "
                )
            )
            # Set value to true            
            validFramePrice = True
            # check sentinel value
            if framePrice != SENTINEL_VALUE:
                # validate frame price range
                if framePrice < PRICE_RANGE_MIN or framePrice > PRICE_RANGE_MAX:
                    print(
                        f"Enter a valid price ranging from {PRICE_RANGE_MIN} to {PRICE_RANGE_MAX}"
                    )
                    # Set value to false if incorrect
                    validFramePrice = False
        except ValueError:
            # catch errors and print nonnumeric error message
            print("Please input only numeric values for the price of frames.")
    return framePrice

# --- Get Discount Rate based on number of frames ---
def GetDiscountRate(numberOfFrames: int):
    if numberOfFrames > DISCOUNT_15:
        return DISCOUNT_15_VALUE
    elif numberOfFrames > DISCOUNT_10:
        return DISCOUNT_10_VALUE
    elif numberOfFrames > DISCOUNT_5:
        return DISCOUNT_5_VALUE
    else:
        return 0.00

# --- CalculateSales based on number of frames, frame price and tax rates ---
def CalculateSales(
    numberOfFrames: int, framePrice: float, salesTaxRate: float = SALES_TAX_RATE
):
    # Calculate sales
    costOfFrames: float = framePrice * numberOfFrames
    # Call GetDiscountRate Function
    discountRate: float = GetDiscountRate(numberOfFrames)
    discountAmount: float = costOfFrames * discountRate
    netAmount: float = costOfFrames - discountAmount
    salesTax: float = netAmount * salesTaxRate
    amountDue: float = netAmount + salesTax
    
    # Call SetTotals Function
    SetTotals(numberOfFrames, costOfFrames, discountAmount, salesTax, amountDue)

    # Print and Display formatted output
    print("\n")
    print(f"Order details for {numberOfFrames} frames priced at ${framePrice:.2f}\n")
    print(f"Cost of frames:             ${costOfFrames:>10,.2f}")
    # Display discount and net amount only if discount is applied
    if discountRate > 0:
        print(
            f"Discount: {int(discountRate * 100):<2}%               ${discountAmount:>10,.2f}"
        )
        print(f"Net Amount:                 ${netAmount:>10,.2f}")
    # Display Sales Tax and Total Amount Due
    print(f"Sales Tax:                  ${salesTax:>10,.2f}")
    print("----------------------------------------")
    print(f"Total due:                  ${amountDue:>10,.2f}")
    print("\n")

# --- GetTotals from Accumulators ---
def GetTotals():
    # Access Totals from global variables
    global totalNumberOfCustomer
    global totalNumberOfFrames
    global totalCostOfFrames
    global totalDiscount
    global totalSalesTax
    global totalAmountDue
    # Return Accumulators
    return (
        totalNumberOfCustomer,
        totalNumberOfFrames,
        totalCostOfFrames,
        totalDiscount,
        totalSalesTax,
        totalAmountDue
    )

# --- Set Totals ---
def SetTotals(numberOfFrames, costOfFrames, discountAmount, salesTax, amountDue):
    # Access totals from global variables
    global totalNumberOfCustomer
    global totalNumberOfFrames
    global totalCostOfFrames
    global totalDiscount
    global totalSalesTax
    global totalAmountDue

    # Update totals global variables
    totalNumberOfCustomer += 1
    totalNumberOfFrames += numberOfFrames
    totalCostOfFrames += costOfFrames
    totalDiscount += discountAmount
    totalSalesTax += salesTax
    totalAmountDue += amountDue

# --- PrintTotalSales ---
def PrintTotalSales():
    # Set local variables to Accumulators by Calling GetTotals function
    (totalNumberOfCustomer, totalNumberOfFrames, totalCostOfFrames, totalDiscount, totalSalesTax, totalAmountDue
    ) = GetTotals()

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
        print("\n\n\n")
