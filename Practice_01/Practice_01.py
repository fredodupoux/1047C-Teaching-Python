# Practice_01
# Author: Frederic Dupoux
# Date : 1/8/25
# Modified: 1/27/25

#
print(" Welcome, this program will calculate a workers gross pay!")
print("It will also calculate workers over time pay.")

# Input Workers Name
workersName: str = (input("Enter worker's name: "))

# Input Hours Worked
hoursWorked: float = float(input("Enter hours worked: "))

# Input Hourly Rate
hourlyRate: float = float(input("Enter your hourly pay rate: "))

# Calculate Gross Pay (Hours Worked * Pay Rate)
grossPay: float = hoursWorked * hourlyRate

# Round Gross Pay
# roundedGrossPay = round(grossPay, 2)

# Display Workers Name and Gross Pay with a formatted output.
print(f"{workersName},'s gross pay is: $,{grossPay:,.2f}")
