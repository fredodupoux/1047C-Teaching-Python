# *module.py
#import configuration file with business constants
from Dupoux_Frederic_HWX04_config import (
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

# Initialize Global Variables to keep track of totals
#  Total Number Of Customer
totalNumberOfCustomer: int = 0
#  Total Number Of Frames
totalNumberOfFrames: int = 0
#  Total Cost Of Frames
totalCostOfFrames: float = 0.00
#  Total Discount
totalDiscount: float = 0.00
#  Total Sales Tax
totalSalesTax: float = 0.00
#  Total Amount Due
totalAmountDue: float = 0.00

def InputNumberOfFrames():
    numberOfFrames: int = 0
    validNumberOfFrames: bool = False
    # WHILE
    while not validNumberOfFrames:
        try:
            # Input number of frames
            numberOfFrames: int = int(
                input(
                    "Enter -1 to close sales or \nenter the number of frames being purchased: "
                )
            )
            validNumberOfFrames = True
            if numberOfFrames != -1:
                # Validate range of frames
                if numberOfFrames not in range(MIN_FRAME, MAX_FRAME + 1):
                    print(
                        f"Please enter a number in the range of {MIN_FRAME} to {MAX_FRAME} frames."
                    )
                    validNumberOfFrames = False
        except:
            # Stay in the price loop and print non numeric error message
            print("Input only numeric values. Please try again!")
    # ENDWHILE
    return numberOfFrames


def InputFramePrice():
    framePrice: float = 0.00
    validFramePrice: bool = False
    while not validFramePrice:
        try:
            # Input Price of Frame
            framePrice: float = float(
                input(
                    "\nEnter -1 to cancel this sale or \nenter the price for the frames being purchased: "
                )
            )
            validFramePrice = True
            if framePrice != -1:
                # Validate frame price range
                if framePrice < PRICE_RANGE_MIN or framePrice > PRICE_RANGE_MAX:
                    print(
                        f"Enter a valid price ranging from {PRICE_RANGE_MIN} to {PRICE_RANGE_MAX}"
                    )
                    validFramePrice = False
        except:
            # Stay in the price loop and print non numeric error message
            print("Please input only numeric values for the price of frames.")
    # ENDWHILE
    return framePrice


def GetDiscountRate(numberOfFrames: int):
    if numberOfFrames > DISCOUNT_15:
        return DISCOUNT_15_VALUE
    elif numberOfFrames > DISCOUNT_10:
        return DISCOUNT_10_VALUE
    elif numberOfFrames > DISCOUNT_5:
        return DISCOUNT_5_VALUE
    else:
        return 0.00


def CalculateSales(
    numberOfFrames: int, framePrice: float, salesTaxRate: float = SALES_TAX_RATE
):
    # Calculate sales
    costOfFrames: float = framePrice * numberOfFrames
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


def GetTotals():
    # Access Totals from global variables
    global totalNumberOfCustomer
    global totalNumberOfFrames
    global totalCostOfFrames
    global totalDiscount
    global totalSalesTax
    global totalAmountDue

    return (
        totalNumberOfCustomer,
        totalNumberOfFrames,
        totalCostOfFrames,
        totalDiscount,
        totalSalesTax,
        totalAmountDue
    )


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


def PrintTotalSales():
    (
        totalNumberOfCustomer,
        totalNumberOfFrames,
        totalCostOfFrames,
        totalDiscount,
        totalSalesTax,
        totalAmountDue
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
