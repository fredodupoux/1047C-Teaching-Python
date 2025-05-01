### Functions

#### Input Number of Frames

| **Passed Value** | **Return Value** |
|------------------|------------------|
|                  | Number of Frames |

**OUTPUT**
- Error Message

**INPUT**
- Number of Frames

**PROCESS**
- Validate

**Pseudo Code**

```plaintext
Number of Frames: int = 0
valid Number of Frames: bool = False

WHILE not valid Number of Frames:
    TRY
        Number of Frames = Input number of frames
        Set valid number of frames = True
        IF number of Frames is not -1:
            IF number of frames is not in range (MIN_FRAME, MAX_FRAME + 1)
                Print invalid range message
                Set valid number of frames = False
            ENDIF
        ENDIF
    EXCEPTION:
        Print nonnumeric error message
ENDWHILE

Return number of frames
```

#### Input Frame Price

| **Passed Value** | **Return Value** |
|------------------|------------------|
|                  | Price            |

**OUTPUT**
- Error Message

**INPUT**
- Frame Price

**PROCESS**
- Validate

**Pseudo Code**

```plaintext
Frame Price float = 0.00
Valid Frame Price bool = False

WHILE not valid frame price:
    TRY:
        frame price: float = Input Price of Frame
        Set valid Frame Price to True
        IF frame Price is not -1:
            IF frame Price is not in range PRICE_RANGE_MIN to PRICE_RANGE_MAX:
                Print invalid range message
                Set valid Frame Price to False
            ENDIF
        ENDIF
    EXCEPTION:
        Print nonnumeric error message
ENDWHILE

Return Frame Price
```

#### Get Discount Rate

| **Passed Value** | **Return Value** |
|------------------|------------------|
| Number of Frames| Discount rate    |

**OUTPUT**
-

**INPUT**
-

**PROCESS**
- Determine discount rate based on number of frames.

**Pseudo Code**

```plaintext
IF number of frames > DISCOUNT_15:
    return DISCOUNT_15_VALUE
ELIF number of frames > DISCOUNT_10:
    return DISCOUNT_10_VALUE
ELIF number of frames > DISCOUNT_5:
    return DISCOUNT_5_VALUE
ELSE:
    return 0.00
```

#### Calculate Sales

| **Passed Value** | **Return Value** |
|------------------|------------------|
| Number of Frames, Frame Price, Sales Tax Rate | |

**OUTPUT**
- Current Cost of Frames
- Current Discount Amount
- Current Net Amount
- Current Sales Tax
- Current Amount Due

**INPUT**
-

**PROCESS**
- Determine discount rate based on number of frames.

**Pseudo Code**

```plaintext
Calculate Cost of Frames
Call Discount Rate = GetDiscountRate()
Calculate discount amount
Calculate net amount
Calculate Sales Tax
Calculate Amount Due
Call SetTotals()
Print Order details
Print Cost of Frames
IF - Discount > 0
    Print Discount
    Print Net Amount
ENDIF
Print Sales Tax and
Print Total Amount Due
```

#### Set Totals

| **Passed Value** | **Return Value** |
|------------------|------------------|
| Number of Frames, cost of Frames, discount Amount, Sales Tax, amount Due | |

**OUTPUT**
-

**INPUT**
-

**PROCESS**
- Update Accumulators

**Pseudo Code**

```plaintext
Access Accumulators from global variables
define global total Number of Customer
define global total Number of Frames
define global total Cost of Frames
define global total Discount
define global total Sales Tax
define global total Amount Due
Update Accumulators
Update total Number of Customer += 1
Update total Number of Frames += number of Frames
Update total Cost of Frames += cost of Frames
Update total Discount += discount Amount
Update total Sales Tax += sales Tax
Update total Amount Due += amount Due
```

#### Get Totals

| **Passed Value** | **Return Value** |
|------------------|------------------|
|                  | total Number of Customer, total Number of Frames, total Cost of Frames, total Discount, total Sales Tax, total Amount Due |

**OUTPUT**
-

**INPUT**
-

**PROCESS**
- Get Accumulators

**Pseudo Code**

```plaintext
Access Accumulators from global variables
define global total Number of Customer
define global total Number of Frames
define global total Cost of Frames
define global total Discount
define global total Sales Tax
define global total Amount Due
return Accumulators
total Number of Customer,
total Number of Frames,
total Cost of Frames,
total Discount,
total Sales Tax,
total Amount Due
```

#### Print Total Sales

**OUTPUT**
- total Number of Customer, total Number of Frames, total Cost of Frames, total Discount, total Sales Tax, total Amount Due

**INPUT**
-

**PROCESS**
- Get Accumulators value and display to user

**Pseudo Code**

```plaintext
Call GetTotals()
IF total Number of customers <= 0:
    Print Goodbye message
ELSE:
    print closing sales message
    Print Final Total Accumulators
    print sale summary
    Print Total number of customers
    Print Total number of frames
    Print Total Cost of frames
    IF total Discount > 0
        Print Total Discount
    ENDIF
    Print Sales Tax
    Print Total Amount Due
```

### Main Program

| **Member Name** | **Program Name** | **Date** | **Grade** |
|-----------------|------------------|----------|-----------|
|                 | Practice_04             | 3/4/25   |           |

**OUTPUT**
- Current Cost of Frames
- Current Discount Amount
- Current Net Amount
- Current Sales Tax
- Current Amount Due
- Total number of customers processed
- Total number of 8x10 picture frames sold
- Total cost of 8x10 picture frames sold
- Total amount of discounts
- Total of sales tax
- Total of amount due

**INPUT**
- Number of Frames
- Price of frames

**PROCESS**
- Validate Nonnumeric inputs
- Validate Number of Frames from (0 to 75]
- Validate Price of Frames from (16.95 to 25.95)
- Calculate Cost of Frames (Number of Frames * Price of Frames)
- Determine Discount Rate based on Number of Frames
- Calculate Discount Amount (Cost of Frames * Discount Rate)
- Calculate Net Amount (Cost of Frames – Discount Amount)
- Calculate Sales Tax (Net Amount * Sales Rate)
- Calculate Amount Due (Net Amount + Sales Tax)
- Accumulate Number of Customers
- Accumulate Number of Frames
- Accumulate Total cost of 8x10 picture frames sold
- Accumulate Total amount of discounts
- Accumulate Total of sales tax
- Accumulate Total of amount due

**Pseudo Code – Main**

```plaintext
Import modules to access functions
define Constants and Global Variables
Define Sales Tax 7.5%
Define price Ranges - PRICE_RANGE_MIN - PRICE_RANGE_MAX
Define Frame Range - MIN_FRAME - MAX_FRAME
Define Discount Brackets - DISCOUNT_5 - DISCOUNT_10 - DISCOUNT_15
Define Discount Values - DISCOUNT_5_VALUE - DISCOUNT_10_VALUE - DISCOUNT_15_VALUE
Initialize Total Number of Customer = 0
Initialize Total Number of Frames = 0
Initialize Total Cost of Frames = 0
Initialize Total Discount = 0
Initialize Total Sales Tax = 0
Initialize Total Amount Due = 0
Print welcome message to user
Initializing value to get in the loop
Number of Frames = 0
frame Price = 0.00
WHILE - number of frames is not -1
    Call number of Frames = Input NumberofFrames()
    IF - number of frames is not -1
        Call frame Price = InputFramePrice()
        IF - frame price is not -1
            Call CalculateSales()
        ELSE
            Cancel sale without exiting program and print cancelled sales message
            Set number of Frames = 0
        ENDIF
    ENDIF
ENDWHILE
Call PrintTotalSales()
```

---