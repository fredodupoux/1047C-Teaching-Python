| **Member Name** | **Program Name** | **Date** | **Grade** |
|-----------------|------------------|----------|-----------|
| Frederic Dupoux | Practice_02             | 2/1/25   |           |

### OUTPUT
- Cost of Frames
- Amount of discount
- Net amount
- Sales tax
- Amount due

### INPUT
- Number of frames being purchased

### PROCESS
- Set discount rate based on quantity of frames being purchased:
  - If \(1 \leq \text{number of frames} \leq 5\), set discount rate to 0%
  - If \(6 \leq \text{number of frames} \leq 10\), set discount rate to 5%
  - If \(11 \leq \text{number of frames} \leq 15\), set discount rate to 10%
  - If \(\text{number of frames} > 15\), set discount rate to 15%
- Calculate Cost of Frames (Number of Frames \(*\) Frame Cost)
- Calculate Amount of Discount (Cost of Frames \(*\) Discount Rate)
- Calculate Net Amount (Cost of Frames - Amount of Discount)
- Calculate Sales Tax (Net Amount \(*\) Sales Tax Rate)
- Calculate Amount Due (Net Amount + Sales Tax)
- Display formatted output rounded to two digits.

### Pseudo Code

```plaintext
# Define Known constants FRAME_COST, SALES_TAX_RATE

# Input number of frames being purchased from user input

# Set discount rate based on number of frames
# If 1 ≤ number of frames ≤ 5 : set discount rate to 0%
# Elif 6 ≤ number of frames ≤ 10 : set discount rate to 5%
# Elif 11 ≤ number of frames ≤15 : set discount rate to 10%
# Elif number of frames > 15 : set discount rate to 15%
# Else: Invalid Number, exit.

# Calculate cost of Frames
# Calculate discount amount
# Calculate net amount
# Calculate Sales Tax
# Calculate Amount Due

# Display formatted output
```

---