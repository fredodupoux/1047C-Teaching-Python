## Daily Sales Summary

| **Member Name** | **Program Name** | **Date** | **Grade** |
|-----------------|------------------|----------|-----------|
| Main            | Practice_06 – Daily Sales Summary | 4/15/25 |           |

### OUTPUT
- Input Error Messages
- Sales Summary

### INPUT
- Sales Person ID
- Daily Sales Value

### PROCESS
- Call InputValidUserID (10 – 99)
- Call InputDailySale (0 – 10,000)
- Call SortSalesList (dailySalesList)
- Print Sorted Sales List with Loop
- Accumulate Total Sales
- Average Total Sales
- Get Minimum Sales in List
- Get Maximum Sales in List

### Pseudo Code – Main

```plaintext
Print Welcome Message
call inputValidUserID() to prompt user for salesPersonID
WHILE salesPersonID != -1:
    initialize dailySalesList[]
    call inputDailySale() to Prompt User for dailySale Amount
    WHILE dailySale != -1:
        Prompt User for dailySale Amount
        Add sale to dailySalesList
    END WHILE
    call sortSalesList() to sort list
    Print Sales Summary for Employee if list is not empty
    IF sortedSalesList is not empty:
        print no records for Sales Person
    ELSE:
        initialize index and totalSales value.
        WHILE index < len(sortedSalesList):
            print sortedSalesList[index]
            cumulate total sales
            increment index
        END WHILE
        compute average sales
        print summary of daily sales
        call getListMinimum and print minimum value
        call getListMinimum and print maximum value
    END IF
    call inputValidUserID() to prompt user for salesPersonID
END WHILE
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

| **Function Name**             | **Passed Value** | **Return Value** |
|------------------------------|------------------|------------------|
| Validate User ID             | Value            | Bool             |
| Validate Daily Sale Value    | Value            | Bool             |

#### Pseudo Code

```plaintext
IF Value == -1
    Return TRUE
END IF
IF Value in Range (10 – 99)
    Return TRUE
END IF

IF Value == -1
    Return TRUE
END IF
IF Value in Range (0 - 10,000)
    Return TRUE
END IF
```

### Get User Input

| **Function Name**             | **Passed Value** | **Return Value** |
|------------------------------|------------------|------------------|
| Input Valid User ID         |                  | value            |
| Input Daily Sale Value       |                  | value            |

#### Pseudo Code

```plaintext
Define Input Prompt
Define Error Message
Return int(Validate Input(input prompt, valid user ID (), error message))

Define Input Prompt
Define Error Message
Return float(ValidateInput(input prompt, Daily Sale Value(), error message))
```

### Sorting List

| **Function Name** | **Passed Value** | **Return Value** |
|------------------|------------------|------------------|
| Sort Sales List  | Sales List       | List             |

#### Pseudo Code

```plaintext
IF salesList is empty
    return salesList
END IF
Prime flag to get in loop
WHILE not doneSorting:
    initialize index and swapped flag
    WHILE index < len(salesList) -1:
        IF index 0 > index 1:
            hold value index 1
            swap values index 1 = index 0
            replace value of index 0 with held value of index 1
            set swap flag to true
        END IF
        increment index
        IF swapped flag == false :
            set doneSorting to True
        END IF
    END WHILE
return salesList
```

### Get Maximum Value in List

| **Function Name** | **Passed Value** | **Return Value** |
|------------------|------------------|------------------|
| Get Maximum value | Sales List       | float            |

#### Pseudo Code

```plaintext
if salesList empty:
    return salesList
initialize highValueIndex to index 0
FORLOOP Iterate through the list from the second element
    IF salesList[index] > salesList[highValueIndex]:
        update lowest value index
    ENDIF
return [highValueIndex]
```

### Get Minimum Value in List

| **Function Name** | **Passed Value** | **Return Value** |
|------------------|------------------|------------------|
| Get Minimum value | Sales List       | float            |

#### Pseudo Code

```plaintext
if salesList empty:
    return salesList
initialize lowValueIndex to index 0
FORLOOP Iterate through the list from the second element
    IF salesList[index] < salesList[lowValueIndex]:
        update lowest value index
    ENDIF
return [lowValueIndex]
```

---