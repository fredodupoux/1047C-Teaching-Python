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


# --- Business Rules Validation --- #
def ValidateBasketID(value: int) -> bool:
    return value < 0 or MIN_BASKET_ID <= value <= MAX_BASKET_ID
     
def ValidateUnitPrice(value: float) -> bool:
    return MIN_UNIT_PRICE <= value <= MAX_UNIT_PRICE

def ValidateQuantity(value: int) -> bool:
    return MIN_QUANTITY <= value <= MAX_QUANTITY

def ValidateDescription(description: str) -> bool:
    return len(description) != 0 and len(description) <= MAX_DESCRIPTION_LENGTH

# --- Numeric  Input Validation --- #
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
    inputPrompt = "Enter product description: "
    errorMessage = f"The product description can't be more than {MAX_DESCRIPTION_LENGTH} characters. Try again: "
    while True:
        description: str = input(inputPrompt)
        if ValidateDescription(description):
            return description
        else:
            print(errorMessage)


# --- Get Valid Basket ID --- #
def InputValidBasketID():
    inputPrompt = "Enter BasketID# or a negative to exit: "
    errorMessage = f"BasketID# must be between {MIN_BASKET_ID} and {MAX_BASKET_ID}. Try again: "
    return int((ValidateInput(inputPrompt, ValidateBasketID, errorMessage )))


# --- Get Valid Unit Price --- #
def InputValidUnitPrice():
    inputPrompt = "Enter Unit Price: "
    errorMessage = f"Unit Price must be between {MIN_UNIT_PRICE} and {MAX_UNIT_PRICE}. Try again: "
    return ValidateInput(inputPrompt, ValidateUnitPrice, errorMessage )

# --- Get Valid Unit Price --- #
def InputValidateQuantity():
    inputPrompt = "Enter Quantity: "
    errorMessage = f"Quantity must be between {MIN_QUANTITY} and {MAX_QUANTITY}. Try again: "
    return int(ValidateInput(inputPrompt, ValidateQuantity, errorMessage ))
