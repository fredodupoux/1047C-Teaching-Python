## CREATE FILE - OIP

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
  - Create Records and write to file
  - Increment Counter

### Pseudo Code – Create File

```plaintext
Import modules to access functions
Define Constants and Global Variables for business rules
Initialize Counter for Total Records
Open file
Call InputValidBasketID
WHILE BasketID > 0
    Call InputProductDescription
    Call InputUnitPrice
    Call InputQuantity
    Create Record
    Write record to file
    Increment Total Records
    Call InputValidBasketID
    WHILE BasketID < PreviousID and BasketID >= 0
        Print Invalid ID must be > Previous ID
        Call InputValidBasketID
Close file gracefully
Print Total Records
```

---

## LIST FILE - OIP

### OUTPUT
- Headers
- List records
- Error message if no file

### INPUT
- (None)

### PROCESS
- Open file
- Initialize Total Records
- Read Lines to print
- Increment Total Records
- Print Total Records

### Pseudo Code – LIST File

```plaintext
Open file
Read first CSV Record
Print Headers
Initialize Total Records
Do while CSV Record is not empty
    Strip end of Line
    Split into Data List
    Assign Basket ID with index
    Assign Product Description with index
    Assign Unit Price with index
    Assign Quantity with index
    Compute Inventory Value
    Print Record (Basket ID, Description, Price, Quantity, Inventory Value)
    Increment Total Records
    Read next CSV Record
End while
Display Total Inventory Value
Display total records in file
```

---

## MODULES

### Input Validation

| **Function Name**       | **Passed Value**                  | **Return Value** |
|-------------------------|-----------------------------------|------------------|
| Validate Input          | Input Prompt, Validate Function, Error Message | Value           |
| Input Validation        | Value                             |                  |

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
|-------------------------|------------------|------------------|
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
|---------------------------------|------------------|------------------|
| Input Product Description       |                  | Description      |
| Input Valid Basket ID          |                  | value            |
| Input Valid Unit Price         |                  | value            |
| Input Valid Quantity           |                  | value            |

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