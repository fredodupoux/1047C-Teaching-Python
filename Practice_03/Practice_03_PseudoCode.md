| **Member Name** | **Program Name** | **Date** | **Grade** |
|-----------------|------------------|----------|-----------|
| Frederic Dupoux | Practice_03             | 2/11/25  | -6        |

### OUTPUT
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

### INPUT
- Number of Frames
- Price of frames

### PROCESS
- Validate Number of Frames (> 0 and <= 75)
- Validate Price of Frames (>= 16.95 and <= 25.95)
- Calculate Cost Of Frames (Number of Frames * Price of Frames)
- Determine Discount Rate based on Number of Frames
- Calculate Discount Amount (Cost Of Frames * Discount Rate)
- Calculate Net Amount (Cost of Frames – Discount Amount)
- Calculate Sales Tax (Net Amount * Sales Rate)
- Calculate Amount Due (Net Amount + Sales Tax)
- Accumulate Number Of Customers
- Accumulate Number Of Frames
- Accumulate Total cost of 8x10 picture frames sold
- Accumulate Total amount of discounts
- Accumulate Total of sales tax
- Accumulate Total of amount due

### Pseudo Code

```plaintext
Define Sales Tax 7.5%
Define price Ranges - PRICE_RANGE_MIN - PRICE_RANGE_MAX
Define Frame Range - MIN_FRAME - MAX_FRAME
Define Discount Brackets - DISCOUNT_5 - DISCOUNT_10 - DISCOUNT_15
Define Discount Values - DISCOUNT_5_VALUE - DISCOUNT_10_VALUE - DISCOUNT_15_VALUE

Initialize Total Number Of Customer = 0
Initialize Total Number Of Frames = 0
Initialize Total Cost Of Frames = 0
Initialize Total Discount = 0
Initialize Total Sales Tax = 0
Initialize Total Amount Due = 0

Print welcome message to user
Initializing numberOfFrames, discountRate and validFramePrice before getting in the loop

WHILE Number of Frames != -1
    TRY
        PROMPT: Input number of frames
        IF - Validate Sentinel value -1
        IF - numberOfFrames not in range(MIN_FRAME, MAX_FRAME+1)
            Print range error message to user
        ELSE
            Determine Discount Rate based on Number of Frames
            IF - Number Of Frames > 15: Discount = 15%
            ELIF - Number Of Frames > 10: Discount = 10%
            ELIF - Number Of Frames > 5: Discount = 5%
            ELSE - Discount = 0
            ENDIF
            Prime validFramePrice to get in next Loop
        ENDIF

        WHILE frame price is valid
            TRY
                PROMPT: Input Price of Frame
                IF - framePrice < PRICE_RANGE_MIN or framePrice > PRICE_RANGE_MAX:
                    Print range error message
                ELSE
                    Calculate Cost Of Frames (Number of Frames * Price of Frames)
                    Calculate discount amount
                    Calculate net amount
                    Calculate Sales Tax
                    Calculate Amount Due
                    Print and Display formatted output
                    Display discount and net amount only if discount is applied
                    IF - Discount > 0
                        Print Discount & Net Amount
                    ENDIF
                    Display Sales Tax and Total Amount Due
                    Accumulate Totals
                    !validFramePrice to Exit current loop
                ENDIF
            EXCEPTION:
            ENDWHILE
        ENDIF
    EXCEPTION:
ENDWHILE

IF customer Close Sales
    Print Goodbye message
ELSE
    quit and print Closing sales details
    Print Final Total Accumulators
    Display formatted output
    IF - Discount > 0
        Print Total Discount
    ENDIF
    Display Sales Tax and Total Amount Due
ENDIF
```

---
