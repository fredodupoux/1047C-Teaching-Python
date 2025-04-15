# import configuration file with business constants
from Dupoux_Frederic_HW06_config import (
    MIN_SALES_PERSON_ID,
    MAX_SALES_PERSON_ID,
    MAX_SALES_AMOUNT,
    MIN_SALES_AMOUNT
)


# --- Business Rules Validation --- #
def validUserID(value: int) -> bool:
    return value == -1 or MIN_SALES_PERSON_ID <= value <= MAX_SALES_PERSON_ID
     
def validSalesValue(value: int) -> bool:
    return value == -1 or MIN_SALES_AMOUNT <= value <= MAX_SALES_AMOUNT

# --- Numeric  Input Validation --- #
def validateInput(inputPrompt: str, validateFunction, errorMessage: str) -> float:
    while True:
        try:
            value = float(input(inputPrompt))
            if validateFunction(value):
                return value
            else:
                print(errorMessage)
        except:
            print('Input only numeric values. Please try again!')

# --- Get Valid User ID --- #
def inputValidUserID() -> int:
    inputPrompt = 'Enter Sales Person ID# or -1 to exit: '
    errorMessage = f'Sales Person ID# must be between {MIN_SALES_PERSON_ID} and {MAX_SALES_PERSON_ID}.'
    return int((validateInput(inputPrompt, validUserID, errorMessage )))

# --- Get Valid Daily Sale --- #
def inputDailySale(salesPersonID) -> float:
    inputPrompt = f'Enter daily sale amount for Sales Person #{salesPersonID}: '
    errorMessage = f'Sales amount must be between {MIN_SALES_AMOUNT} and {MAX_SALES_AMOUNT}.'
    return float((validateInput(inputPrompt, validSalesValue, errorMessage )))

# --- Sort List From Low To High --- #
def sortSalesList(salesList) -> []:
    # handle empty list
    if not salesList:
        return salesList
    
    doneSorting: bool = False
    while not doneSorting:
        # initialize index and flag 
        index: int = 0
        swapped: bool = False
        while index < len(salesList) -1:
            if salesList[index] > salesList[index + 1]:
                holdSale = salesList[index + 1]
                # swap values
                salesList[index + 1] = salesList[index]
                salesList[index] = holdSale
                swapped = True
            #increment counter 
            index += 1
        # if no swaps are made list is sorted
        if not swapped:
            doneSorting = True
            
    return salesList

#  --- Get Maximum Value --- #
def getListMaximum(salesList) -> float:
    # handle empty list
    if not salesList:
        return salesList
    # initialize index of highest value
    highValueIndex = 0
    # Iterate through the list from the second element   
    for index in range (1,len(salesList)):
        if salesList[index] > salesList[highValueIndex]:           
            # update lowest value index
            highValueIndex = index

    return salesList[highValueIndex]


#  --- Get Minimum Value --- #
def getListMinimum(salesList) -> float:
    # handle empty list
    if not salesList:
        return salesList
    # initialize index of lowest value
    lowValueIndex = 0
    # Iterate through the list from the second element   
    for index in range (1,len(salesList)):
        if salesList[index] < salesList[lowValueIndex]:
            # update lowest value index
            lowValueIndex = index

    return salesList[lowValueIndex]