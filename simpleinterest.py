#Collecting Loan amount
def simple_interest(loan_amount,interest,years):
    result=(loan_amount*years*interest/100)
    return result

loan_amount=float(input("Enter the Loan Amount:"))
interest=float(input("Enter the rate of interest (Per Annum):"))
years=float(input("Enter Loan tenure (No.of.years):"))

simple_interest(loan_amount,interest,years)

si=simple_interest(loan_amount,interest,years)

print(f"The interest is {si}")