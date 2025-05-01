# *_module.py
#import configuration file with business constants
from Practice_04_config import (
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
    PRICE_RANGE_MIN
)

# Initialize Global Accumulators
totalNumberOfCustomer: int = 0
totalNumberOfFrames: int = 0
totalCostOfFrames: float = 0.00
totalDiscount: float = 0.00
totalSalesTax: float = 0.00
totalAmountDue: float = 0.00

# --- Get Valid Input Universal --- #
def GetValidInput(inputPrompt: str, validateFunction, errorMessage: str) -> float:
    while True:
        try:
            value = float(input(inputPrompt))
            if validateFunction(value):
                return value
            else:
                print(errorMessage)
        except:
            print("Input only numeric values. Please try again.")

# --- Validate Frame Count --- #
def ValidateFrameCount (value: float) -> bool:
    if value == -1:
        return True
    if value in range(MIN_FRAME, MAX_FRAME + 1):
        return True

# --- Validate Frame Price --- #
def ValidateFramePrice(value: float) -> bool:
    if value == -1:
        return True
    if value >= PRICE_RANGE_MIN and value <= PRICE_RANGE_MAX:
        return True
    
# --- Input Number Of Frames --- #
def InputNumberOfFrames():
    inputPrompt = "Enter -1 to close sales or \nenter the number of frames being purchased: "
    errorMessage = f"Please enter a number in the range of {MIN_FRAME} to {MAX_FRAME} frames."
    return int(GetValidInput(inputPrompt, ValidateFrameCount, errorMessage))

# --- Input Frame Price --- #
def InputFramePrice():
    inputPrompt = "\nEnter -1 to cancel this sale or \nenter the price for the frames being purchased: "
    errorMessage = f"Enter a valid price ranging from {PRICE_RANGE_MIN} to {PRICE_RANGE_MAX}"
    return GetValidInput(inputPrompt, ValidateFramePrice, errorMessage)

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
