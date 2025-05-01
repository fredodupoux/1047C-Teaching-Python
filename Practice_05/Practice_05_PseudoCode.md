## CREATE FILE - OIP

| **Member Name** | **Program Name** | **Date** | **Grade** |
|-----------------|------------------|----------|-----------|
| CREATE FILE     | Practice_05 CREATE      | 3/18/25  |           |

### OUTPUT
- Save to text file
- Error Messages
- Total of Records saved

### INPUT
- Basket ID
- Product description
- Unit Price
- Quantity

### PROCESS
- Initialize Accumulator Total Records
- Open text file to output to
- Loop while BasketID is not negative
  - Call InputValidBasketID (1000 – 9999)
  - Call InputProductDescription (< 25 characters)
  - Call InputUnitPrice (5.95 – 75.95)
  - Call InputQuantity (0 – 999)
  - Write fields to file
  - Increment Counter

### Pseudo Code – Create File

```plaintext
Import modules to access functions
Define Constants and Global Variables for business rules
Initialize Counter for Total Records
Open file
Call InputValidBasketID
WHILE ID > 0
    Call InputProductDescription
    Call InputUnitPrice
    Call InputQuantity
    Write fields to file
    Increment Total Records
    Call InputValidBasketID
    WHILE BasketID < PreviousID and BasketID >= 0
        Print Invalid ID must be > Previous ID
        Call InputValidBasketID
Close file gracefully
Print Total Records
```

---

## LIST FILE

| **Member Name** | **Program Name** | **Date** | **Grade** |
|-----------------|------------------|----------|-----------|
| LIST FILE       | Practice_05 LIST        |          |           |

### OUTPUT
- Headers
- List records
- Error message if no file

### INPUT
- (None)

### PROCESS
- Open file
- Initialize Total Records
- Strip data to print
- Increment Total Records
- Print Total Records

### Pseudo Code – LIST File

```plaintext
Open file
Read first Basket ID
Print Headers
Initialize Total Records
Do while Basket ID is not empty
    Prepare Basket ID to print
    Read Product Description
    Prepare Product Description to print
    Read Unit Price
    Prepare Unit Price to print
    Read Quantity
    Prepare Quantity to print
    Print Record (Basket ID, Description, Price, Quantity)
    Increment Total Records
    Read next Basket ID
End while
Display Total Records
```

---

## MODULES

### Input Validation

| **Function Name** | **Passed Value**                  | **Return Value** |
|-------------------|-----------------------------------|------------------|
| Validate Input    | Input Prompt, Validate Function, Error Message | Value           |

#### Pseudo Code

```plaintext
WHILE True:
    TRY
        Input Value
        IF call Validate Function(Value) = True
            Return Value
        ELSE print error message
    EXCEPTION:
        Print Nonnumeric error
```

### Business Rules

| **Function Name**       | **Passed Value** | **Return Value** |
|------------------------|------------------|------------------|
| Validate Basket ID     | Value            | Bool             |
| Validate Unit Price    | Value            | Bool             |
| Validate Quantity      | Value            | Bool             |
| Validate Description   | Description      | Bool             |

#### Pseudo Code

```plaintext
IF Value < 0
    Return TRUE
IF Value in Range (1000 – 9999)
    Return TRUE

IF Value in Range (5.95 – 75.95)
    Return TRUE

IF Value in Range (0 – 999)
    Return TRUE

IF len(Description) != 0 and len(Description) < 25
    Return TRUE
```

### Get User Input

| **Function Name**               | **Passed Value** | **Return Value** |
|--------------------------------|------------------|------------------|
| Input Product Description      |                  | Description      |
| Input Valid Basket ID         |                  | value            |
| Input Valid Unit Price        |                  | value            |
| Input Valid Quantity          |                  | value            |

#### Pseudo Code

```plaintext
While True:
    Input description
    IF Validate Description(description)
        Return description
    ELSE
        Print error message

Input Prompt
Error Message
Return int(Validate Input())

Input Prompt
Error Message
Return float(ValidateInput())

Input Prompt
Error Message
Return int(Validate Input())
```

---