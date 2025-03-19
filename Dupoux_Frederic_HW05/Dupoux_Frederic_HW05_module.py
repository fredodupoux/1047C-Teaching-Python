# *_module.py
#import configuration file with business constants
from Dupoux_Frederic_HW05_config import (
    MIN_BASKET_ID,
    MAX_BASKET_ID,
    MIN_UNIT_PRICE,
    MAX_UNIT_PRICE,
    MIN_QUANTITY,
    MAX_QUANTITY,
    MAX_DESCRIPTION_LENGTH
)


# --- Validation Functions --- #
def ValidateBasketID(value: int) -> bool:
    return MIN_BASKET_ID <= value <= MAX_BASKET_ID

def ValidateUnitPrice(value: float) -> bool:
    return MIN_UNIT_PRICE <= value <= MAX_UNIT_PRICE

def ValidateQuantity(value: int) -> bool:
    return value in range(MIN_QUANTITY,MAX_QUANTITY)

def ValidateDescription(description: str) -> bool:
    return len(description) != 0 and len(description) < MAX_DESCRIPTION_LENGTH

# --- Get Valid Numeric Input --- #
def ValidateInput(inputPrompt: str, validateFunction, errorMessage: str) -> float:
    while True:
        try:
            value = float(input(inputPrompt))
            if validateFunction(value):
                return value
            else:
                print(errorMessage)
        except:
            print("Input only numeric values. Please try again!")

# --- Get Valid Description --- #
def InputProductDescription():
    inputPrompt = "Enter product description (less than 25 characters): "
    errorMessage = "The product description must be less than 25 characters. Please try again."
    while True:
        description: str = input(inputPrompt)
        if ValidateDescription(description):
            return description
        else:
            print(errorMessage)


# --- Get Valid Basket ID --- #
def InputValidBasketID():
    inputPrompt = "Enter Basket ID (1000-9999) or a negative to exit: "
    errorMessage = "Basket ID must be between 1000 and 9999."
    return int(ValidateInput(inputPrompt, ValidateBasketID, errorMessage ))


# --- Get Valid Unit Price --- #
def InputValidUnitPrice():
    inputPrompt = "Enter Unit Price (5.95-75.95): "
    errorMessage = "Unit Price must be between 5.95 and 75.95."
    return ValidateInput(inputPrompt, ValidateUnitPrice, errorMessage )

# --- Get Valid Unit Price --- #
def InputValidateQuantity():
    inputPrompt = "Enter Quantity (0-999): "
    errorMessage = "Quantity must be between 0 and 999."
    return int(ValidateInput(inputPrompt, ValidateQuantity, errorMessage ))
